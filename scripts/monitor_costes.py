#!/usr/bin/env python3
"""
monitor_costes.py — Monitor de costes Snowflake para HVR → Snowflake
=====================================================================
Conecta a Snowflake vía REST API (BAIKAL_TOKEN), consulta el consumo de
créditos por warehouse (WAREHOUSE_METERING_HISTORY), compara semana actual
vs semana anterior y genera alertas si el consumo supera un umbral.

Uso:
    python3 monitor_costes.py [--umbral-pct 20] [--output /ruta/metricas.json]

Variables de entorno requeridas:
    BAIKAL_TOKEN          Token de autenticación Snowflake
    SNOWFLAKE_ACCOUNT     Identificador de cuenta Snowflake (p.ej. xy12345)
    SNOWFLAKE_WAREHOUSE   Warehouse para ejecutar las queries (p.ej. PRO_BI_WH)

Opcionales:
    SNOWFLAKE_ROLE        Role a usar (por defecto ACCOUNTADMIN)
    SNOWFLAKE_DATABASE    Database por defecto
"""

import argparse
import json
import logging
import os
import sys
import time
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

import urllib.request
import urllib.error

# ---------------------------------------------------------------------------
# Logging
# ---------------------------------------------------------------------------
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)
logger = logging.getLogger("monitor_costes")

# ---------------------------------------------------------------------------
# Constantes
# ---------------------------------------------------------------------------
SNOWFLAKE_API_BASE = "https://{account}.snowflakecomputing.com/api/v2/statements"
QUERY_TIMEOUT_SECONDS = 300
QUERY_POLL_INTERVAL = 5

# Warehouses monitorizados (los identificados en el plan de optimización)
WAREHOUSES_MONITORED = [
    "PRO_LOAD_WH",
    "PRO_TRANSFORM_WH",
    "PRO_TRANSFORM_COMPLEX_WH",
    "DEV_TRANSFORM_WH",
    "PRO_BI_WH",
    "PRO_INTERNAL_BI_WH",
    "STREAMLIT_APPS_WH",
    "DEV_LOAD_WH",
    "BAIKAL_DP_WH",
]

# Query de metering: créditos por warehouse, desglosados por semana
QUERY_METERING = """
SELECT
    warehouse_name,
    DATE_TRUNC('week', start_time) AS week,
    SUM(credits_used)          AS total_credits,
    SUM(credits_used_compute)  AS compute_credits,
    SUM(credits_used_cloud_services) AS cloud_credits,
    COUNT(*)                   AS query_count
FROM SNOWFLAKE.ACCOUNT_USAGE.WAREHOUSE_METERING_HISTORY
WHERE start_time >= DATEADD(day, -14, CURRENT_DATE())
  AND warehouse_name IN ({placeholders})
GROUP BY warehouse_name, DATE_TRUNC('week', start_time)
ORDER BY week DESC, total_credits DESC;
"""

# Query de queries costosas (top 20 última semana)
QUERY_EXPENSIVE = """
SELECT
    query_id,
    warehouse_name,
    database_name,
    ROUND(execution_time / 1000, 1) AS exec_seconds,
    query_text
FROM SNOWFLAKE.ACCOUNT_USAGE.QUERY_HISTORY
WHERE start_time >= DATEADD(day, -7, CURRENT_DATE())
  AND (database_name LIKE '%PRO_0_STAGING%'
       OR database_name LIKE '%ES_COVADONGA%')
  AND execution_time / 1000 > 60
ORDER BY execution_time DESC
LIMIT 20;
"""

# Query de storage por base de datos
QUERY_STORAGE = """
SELECT
    database_name,
    SUM(active_bytes)   / POWER(1024, 3) AS active_gb,
    SUM(time_travel_bytes) / POWER(1024, 3) AS time_travel_gb,
    SUM(fail_safe_bytes)   / POWER(1024, 3) AS fail_safe_gb
FROM SNOWFLAKE.ACCOUNT_USAGE.TABLE_STORAGE_METRICS
WHERE database_name IN ('PRO_0_STAGING_DB', 'ES_COVADONGA')
GROUP BY database_name;
"""


# ---------------------------------------------------------------------------
# Helpers REST API Snowflake
# ---------------------------------------------------------------------------

def _get_env() -> Dict[str, str]:
    """Valida y devuelve las variables de entorno necesarias."""
    token = os.environ.get("BAIKAL_TOKEN", "").strip()
    account = os.environ.get("SNOWFLAKE_ACCOUNT", "").strip()
    warehouse = os.environ.get("SNOWFLAKE_WAREHOUSE", "").strip()

    missing = []
    if not token:
        missing.append("BAIKAL_TOKEN")
    if not account:
        missing.append("SNOWFLAKE_ACCOUNT")
    if not warehouse:
        missing.append("SNOWFLAKE_WAREHOUSE")

    if missing:
        logger.error("Faltan variables de entorno: %s", ", ".join(missing))
        sys.exit(1)

    return {
        "token": token,
        "account": account,
        "warehouse": warehouse,
        "role": os.environ.get("SNOWFLAKE_ROLE", "ACCOUNTADMIN"),
        "database": os.environ.get("SNOWFLAKE_DATABASE", ""),
    }


def _build_headers(token: str) -> Dict[str, str]:
    return {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json",
        "Accept": "application/json",
        "X-Snowflake-Authorization-Token-Type": "KEYPAIR_JWT",
    }


def _build_statement_url(account: str) -> str:
    return SNOWFLAKE_API_BASE.format(account=account)


def _submit_query(url: str, headers: Dict[str, str], sql: str,
                  warehouse: str, role: str, database: str = "") -> str:
    """Envía una query y devuelve el statementHandle."""
    payload: Dict[str, Any] = {
        "statement": sql.strip(),
        "warehouse": warehouse,
        "role": role,
        "timeout": QUERY_TIMEOUT_SECONDS,
        "parameters": {
            "MULTI_STATEMENT_COUNT": 0,
        },
    }
    if database:
        payload["database"] = database

    body = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(url, data=body, headers=headers, method="POST")

    try:
        with urllib.request.urlopen(req) as resp:
            data = json.loads(resp.read().decode("utf-8"))
    except urllib.error.HTTPError as exc:
        body_err = exc.read().decode("utf-8", errors="replace")
        logger.error("HTTP %d al enviar query: %s", exc.code, body_err)
        raise

    # Snowflake devuelve un array o un objeto con statementHandle
    if isinstance(data, list):
        handle = data[0].get("statementHandle", "")
    elif isinstance(data, dict):
        handle = data.get("statementHandle", "")
        # Comprobar errores
        if "code" in data and data.get("code") != "090106":
            msg = data.get("message", "Error desconocido")
            logger.error("Error Snowflake: [%s] %s", data.get("code"), msg)
            raise RuntimeError(f"Snowflake error: [{data.get('code')}] {msg}")
    else:
        raise RuntimeError(f"Respuesta inesperada: {type(data)}")

    if not handle:
        raise RuntimeError("No se obtuvo statementHandle de Snowflake")

    logger.info("Query enviada — handle=%s…", handle[:16])
    return handle


def _poll_result(url: str, headers: Dict[str, str], handle: str) -> List[Dict[str, Any]]:
    """Poll hasta que la query termine y devuelve las filas como dicts."""
    poll_url = f"{url}/{handle}"
    deadline = time.monotonic() + QUERY_TIMEOUT_SECONDS

    while time.monotonic() < deadline:
        req = urllib.request.Request(poll_url, headers=headers, method="GET")
        try:
            with urllib.request.urlopen(req) as resp:
                data = json.loads(resp.read().decode("utf-8"))
        except urllib.error.HTTPError as exc:
            body_err = exc.read().decode("utf-8", errors="replace")
            logger.error("HTTP %d en poll: %s", exc.code, body_err)
            raise

        # Determinar estado
        if isinstance(data, dict):
            status_info = data.get("status", {})
            if isinstance(status_info, dict):
                state = status_info.get("state", "")
            else:
                state = str(status_info)

            if state in ("SUCCESS", "SUCCEEDED"):
                return _parse_rows(data)
            elif state in ("FAILED", "FAILED_WITH_ERROR", "ABORTED"):
                msg = data.get("message", "Query falló")
                raise RuntimeError(f"Query falló: {msg}")
            # RUNNING / QUEUED → seguir esperando
            logger.debug("Query en estado %s, reintentando…", state)

        time.sleep(QUERY_POLL_INTERVAL)

    raise TimeoutError(f"Query {handle[:16]}… no completó en {QUERY_TIMEOUT_SECONDS}s")


def _parse_rows(data: Any) -> List[Dict[str, Any]]:
    """Extrae filas de la respuesta Snowflake."""
    if isinstance(data, list):
        return data  # ya son dicts

    if not isinstance(data, dict):
        return []

    # Formato estándar: data["data"] = lista de listas, data["resultSetMetadata"]["columns"]
    columns_info = data.get("resultSetMetadata", {}).get("columnInfo", [])
    columns_info += data.get("resultSetMetadata", {}).get("columns", [])
    col_names = [c.get("name", f"col_{i}") for i, c in enumerate(columns_info)]

    raw_rows = data.get("data", [])
    rows = []
    for raw in raw_rows:
        if isinstance(raw, list):
            rows.append(dict(zip(col_names, raw)))
        elif isinstance(raw, dict):
            rows.append(raw)

    return rows


def execute_query(env: Dict[str, str], sql: str) -> List[Dict[str, Any]]:
    """Ejecuta una query completa (submit + poll) y devuelve filas."""
    url = _build_statement_url(env["account"])
    headers = _build_headers(env["token"])
    handle = _submit_query(
        url, headers, sql,
        warehouse=env["warehouse"],
        role=env["role"],
        database=env.get("database", ""),
    )
    return _poll_result(url, headers, handle)


# ---------------------------------------------------------------------------
# Lógica de análisis
# ---------------------------------------------------------------------------

def _split_weeks(rows: List[Dict[str, Any]]) -> Tuple[List[Dict], List[Dict]]:
    """Separa filas en semana actual y semana anterior según campo 'week'."""
    current_week: List[Dict] = []
    previous_week: List[Dict] = []

    for row in rows:
        week_val = row.get("week", row.get("WEEK", ""))
        if isinstance(week_val, str):
            # Formato ISO: 2026-06-16
            try:
                week_date = datetime.strptime(week_val[:10], "%Y-%m-%d").date()
            except ValueError:
                current_week.append(row)
                continue
        else:
            current_week.append(row)
            continue

        # Semana actual = la más reciente en los datos
        if not current_week and not previous_week:
            ref_date = week_date
        else:
            ref_date = max(
                ref_date if 'ref_date' in dir() else week_date,
                week_date,
            )

        # Si la semana coincide con la referencia → actual
        if week_date >= ref_date - timedelta(days=6):
            current_week.append(row)
        else:
            previous_week.append(row)

    return current_week, previous_week


def _aggregate_by_warehouse(rows: List[Dict]) -> Dict[str, Dict[str, float]]:
    """Agrega créditos por warehouse."""
    agg: Dict[str, Dict[str, float]] = {}
    for row in rows:
        wh = row.get("warehouse_name", row.get("WAREHOUSE_NAME", "UNKNOWN"))
        if wh not in agg:
            agg[wh] = {"total_credits": 0.0, "compute_credits": 0.0,
                       "cloud_credits": 0.0, "query_count": 0}
        agg[wh]["total_credits"] += float(row.get("total_credits", row.get("TOTAL_CREDITS", 0)) or 0)
        agg[wh]["compute_credits"] += float(row.get("compute_credits", row.get("COMPUTE_CREDITS", 0)) or 0)
        agg[wh]["cloud_credits"] += float(row.get("cloud_credits", row.get("CLOUD_CREDITS", 0)) or 0)
        agg[wh]["query_count"] += int(row.get("query_count", row.get("QUERY_COUNT", 0)) or 0)
    return agg


def compare_weeks(current: Dict[str, Dict], previous: Dict[str, Dict],
                  umbral_pct: float) -> List[Dict[str, Any]]:
    """Compara semana actual vs anterior y genera alertas."""
    alerts = []
    all_warehouses = set(list(current.keys()) + list(previous.keys()))

    for wh in sorted(all_warehouses):
        cur = current.get(wh, {}).get("total_credits", 0)
        prev = previous.get(wh, {}).get("total_credits", 0)

        if prev > 0:
            pct_change = ((cur - prev) / prev) * 100
        elif cur > 0:
            pct_change = 100.0
        else:
            pct_change = 0.0

        alert = {
            "warehouse": wh,
            "current_week_credits": round(cur, 2),
            "previous_week_credits": round(prev, 2),
            "pct_change": round(pct_change, 1),
            "alert": abs(pct_change) > umbral_pct,
            "direction": "up" if pct_change > 0 else "down",
        }

        if alert["alert"]:
            alerts.append(alert)
            logger.warning(
                "⚠ ALERTA %s: %.1f%% cambio (%.1f → %.1f créditos)",
                wh, pct_change, prev, cur,
            )
        else:
            logger.info(
                "  %s: %.1f%% cambio (%.1f → %.1f créditos) — OK",
                wh, pct_change, prev, cur,
            )

    return alerts


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(
        description="Monitor de costes Snowflake para HVR → Snowflake",
    )
    parser.add_argument(
        "--umbral-pct", type=float, default=20.0,
        help="Umbral de cambio porcentual para alerta (default: 20%%)",
    )
    parser.add_argument(
        "--output", type=str, default="metricas_costes.json",
        help="Ruta del fichero JSON de salida (default: metricas_costes.json)",
    )
    parser.add_argument(
        "--verbose", action="store_true",
        help="Activar logging DEBUG",
    )
    args = parser.parse_args()

    if args.verbose:
        logging.getLogger().setLevel(logging.DEBUG)

    logger.info("=" * 60)
    logger.info("Monitor de Costes Snowflake — HVR → Snowflake")
    logger.info("=" * 60)

    # 1. Configuración
    env = _get_env()
    logger.info("Cuenta: %s | Warehouse: %s | Role: %s",
                env["account"], env["warehouse"], env["role"])

    # 2. Query de metering
    logger.info("Consultando WAREHOUSE_METERING_HISTORY (últimas 2 semanas)…")
    placeholders = ", ".join(f"'{w}'" for w in WAREHOUSES_MONITORED)
    sql_metering = QUERY_METERING.format(placeholders=placeholders)

    try:
        metering_rows = execute_query(env, sql_metering)
    except Exception as exc:
        logger.error("Error en query de metering: %s", exc)
        sys.exit(2)

    logger.info("Filas obtenidas: %d", len(metering_rows))

    # 3. Separar semanas y agregar
    current_rows, previous_rows = _split_weeks(metering_rows)
    current_agg = _aggregate_by_warehouse(current_rows)
    previous_agg = _aggregate_by_warehouse(previous_rows)

    # 4. Comparar y alertar
    logger.info("Comparando semana actual vs anterior (umbral: %.0f%%)…", args.umbral_pct)
    alerts = compare_weeks(current_agg, previous_agg, args.umbral_pct)

    # 5. Queries costosas
    logger.info("Consultando queries costosas…")
    expensive_rows: List[Dict] = []
    try:
        expensive_rows = execute_query(env, QUERY_EXPENSIVE)
    except Exception as exc:
        logger.warning("No se pudieron obtener queries costosas: %s", exc)

    # 6. Storage
    logger.info("Consultando storage por base de datos…")
    storage_rows: List[Dict] = []
    try:
        storage_rows = execute_query(env, QUERY_STORAGE)
    except Exception as exc:
        logger.warning("No se pudo obtener storage: %s", exc)

    # 7. Construir métricas
    now = datetime.now(timezone.utc).isoformat()
    metricas = {
        "timestamp": now,
        "account": env["account"],
        "umbral_pct": args.umbral_pct,
        "warehouses_monitored": WAREHOUSES_MONITORED,
        "current_week": current_agg,
        "previous_week": previous_agg,
        "alerts": alerts,
        "alert_count": len(alerts),
        "expensive_queries": expensive_rows[:10],
        "storage_by_database": storage_rows,
        "summary": {
            "total_current_credits": round(
                sum(v["total_credits"] for v in current_agg.values()), 2
            ),
            "total_previous_credits": round(
                sum(v["total_credits"] for v in previous_agg.values()), 2
            ),
        },
    }

    # Calcular cambio total
    cur_total = metricas["summary"]["total_current_credits"]
    prev_total = metricas["summary"]["total_previous_credits"]
    if prev_total > 0:
        metricas["summary"]["total_pct_change"] = round(
            ((cur_total - prev_total) / prev_total) * 100, 1
        )
    else:
        metricas["summary"]["total_pct_change"] = 0.0

    # 8. Guardar JSON
    output_path = Path(args.output)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(metricas, f, indent=2, ensure_ascii=False, default=str)
    logger.info("Métricas guardadas en: %s", output_path.resolve())

    # 9. Resumen en consola
    print("\n" + "=" * 60)
    print("RESUMEN DE COSTES")
    print("=" * 60)
    print(f"  Semana actual : {cur_total:>10.1f} créditos")
    print(f"  Semana previa : {prev_total:>10.1f} créditos")
    print(f"  Cambio        : {metricas['summary']['total_pct_change']:>+9.1f}%")
    print(f"  Alertas       : {len(alerts)}")
    if alerts:
        print("\n  ⚠  ALERTAS ACTIVAS:")
        for a in alerts:
            print(f"    • {a['warehouse']}: {a['pct_change']:+.1f}% "
                  f"({a['previous_week_credits']:.0f} → {a['current_week_credits']:.0f})")
    print("=" * 60)

    # Código de salida: 1 si hay alertas, 0 si todo OK
    sys.exit(1 if alerts else 0)


if __name__ == "__main__":
    main()
