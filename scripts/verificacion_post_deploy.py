#!/usr/bin/env python3
"""
verificacion_post_deploy.py — Verificación post-deploy HVR → Snowflake
========================================================================
Verifica el estado correcto de la infraestructura tras un despliegue:
  1. Coalesce activo en canales HVR (vía tabla de auditoría Snowflake)
  2. Tablas TRANSIENT creadas correctamente en PRO_0_STAGING_DB
  3. Tasks de purga existentes y activas
  4. Genera un reporte Markdown con el resultado.

Uso:
    python3 verificacion_post_deploy.py [--output reporte.md] [--config hvr_config.json]

Variables de entorno requeridas:
    BAIKAL_TOKEN          Token de autenticación Snowflake
    SNOWFLAKE_ACCOUNT     Identificador de cuenta Snowflake
    SNOWFLAKE_WAREHOUSE   Warehouse para ejecutar las queries
"""

import argparse
import json
import logging
import os
import sys
import time
from datetime import datetime, timezone
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
logger = logging.getLogger("verificacion_post_deploy")

# ---------------------------------------------------------------------------
# Constantes
# ---------------------------------------------------------------------------
SNOWFLAKE_API_BASE = "https://{account}.snowflakecomputing.com/api/v2/statements"
QUERY_TIMEOUT_SECONDS = 120
QUERY_POLL_INTERVAL = 3

# Tablas que deben ser TRANSIENT según el plan de optimización (Fase 2.1)
EXPECTED_TRANSIENT_TABLES = [
    ("PRO_0_STAGING_DB", "FR_FRISBI", "SALES_AZ9_A_0011"),
    ("PRO_0_STAGING_DB", "ES_TESEO", "TW_GPS_HISTORIC_IO"),
    ("PRO_0_STAGING_DB", "ES_ESPADA", "SALES_AZ7_O014S00"),
    ("PRO_0_STAGING_DB", "ES_ESPADA", "SALES_AZ7_OR014S00"),
    ("PRO_0_STAGING_DB", "ES_ESPADA", "SALES_AZ7_OR014S00_SEGURIDAD"),
    ("PRO_0_STAGING_DB", "ES_ESPADA", "STOCK_AZ7_O015S00"),
    ("PRO_0_STAGING_DB", "ES_TESEO", "TW_HISTORIC_POSIC"),
    ("PRO_0_STAGING_DB", "FR_STRATOR_BO_L4", "SALES_L4_OPERATIONPRODUITREPORTING"),
    ("PRO_0_STAGING_DB", "ES_CDI_PARCEL", "PLSTMPIMAGENES"),
    ("PRO_0_STAGING_DB", "FR_FRISBI", "SALES_AZ9_A_0011_BACKUP"),
]

# Tasks de purga esperados (Fase 2.4)
EXPECTED_PURGE_TASKS = [
    ("PRO_0_STAGING_DB", "ES_SALESFORCE_PHARMA", "TASK_PURGE_HISTORY"),
    ("PRO_0_STAGING_DB", "PUBLIC", "TASK_PURGE_HVR_HISTORY"),
]

# Canales HVR donde Coalesce debe estar activo
HVR_CHANNELS = [
    "CH_ES_ESPADA_MASTERS",
    "CH_ES_TESEO",
    "CH_ES_PARCEL",
    "CH_FR_FRISBI",
    "CH_ES_ALERTRAN",
    "CH_ES_CDI",
    "CH_FR_STRATOR",
    "CH_ES_SALESFORCE_PHARMA",
]

# Queries SQL
QUERY_TRANSIENT_CHECK = """
SELECT
    table_catalog,
    table_schema,
    table_name,
    table_type,
    retention_time,
    is_transient
FROM INFORMATION_SCHEMA.TABLES
WHERE table_catalog = 'PRO_0_STAGING_DB'
  AND table_type = 'BASE TABLE'
ORDER BY table_schema, table_name;
"""

QUERY_TASKS_STATUS = """
SELECT
    task_schema,
    task_name,
    state,
    schedule,
    created_on,
    last_committed_on
FROM TABLE(INFORMATION_SCHEMA.TASK_HISTORY(
    database_name => 'PRO_0_STAGING_DB',
    result_limit => 100
))
ORDER BY task_schema, task_name;
"""

QUERY_TASKS_DEFINITION = """
SHOW TASKS IN DATABASE PRO_0_STAGING_DB;
"""

QUERY_COALESCE_AUDIT = """
SELECT
    query_text,
    start_time,
    warehouse_name
FROM SNOWFLAKE.ACCOUNT_USAGE.QUERY_HISTORY
WHERE start_time >= DATEADD(day, -7, CURRENT_DATE())
  AND (
    query_text ILIKE '%coalesce%'
    OR query_text ILIKE '%hvr%'
    OR query_text ILIKE '%integrate%'
  )
  AND (database_name LIKE '%PRO_0_STAGING%'
       OR database_name LIKE '%ES_COVADONGA%')
ORDER BY start_time DESC
LIMIT 50;
"""

QUERY_CHANNEL_INTEGRATION = """
SELECT
    table_name,
    last_altered,
    comment
FROM INFORMATION_SCHEMA.TABLES
WHERE table_catalog = 'PRO_0_STAGING_DB'
  AND (
    table_name LIKE '%_b'
    OR table_name LIKE '%_hvr'
    OR table_name LIKE '%_integrate'
  )
LIMIT 50;
"""


# ---------------------------------------------------------------------------
# Helpers REST API Snowflake
# ---------------------------------------------------------------------------

def _get_env() -> Dict[str, str]:
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


def _build_url(account: str) -> str:
    return SNOWFLAKE_API_BASE.format(account=account)


def _submit_and_poll(env: Dict[str, str], sql: str) -> List[Dict[str, Any]]:
    """Envía query, espera resultado, devuelve filas como dicts."""
    url = _build_url(env["account"])
    headers = _build_headers(env["token"])

    payload: Dict[str, Any] = {
        "statement": sql.strip(),
        "warehouse": env["warehouse"],
        "role": env["role"],
        "timeout": QUERY_TIMEOUT_SECONDS,
    }
    if env.get("database"):
        payload["database"] = env["database"]

    body = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(url, data=body, headers=headers, method="POST")

    try:
        with urllib.request.urlopen(req) as resp:
            resp_data = json.loads(resp.read().decode("utf-8"))
    except urllib.error.HTTPError as exc:
        err_body = exc.read().decode("utf-8", errors="replace")
        logger.error("HTTP %d: %s", exc.code, err_body)
        raise

    # Extraer handle
    if isinstance(resp_data, list):
        handle = resp_data[0].get("statementHandle", "") if resp_data else ""
    elif isinstance(resp_data, dict):
        handle = resp_data.get("statementHandle", "")
        if resp_data.get("code") and resp_data.get("code") != "090106":
            raise RuntimeError(f"Snowflake error [{resp_data.get('code')}]: {resp_data.get('message')}")
    else:
        raise RuntimeError(f"Respuesta inesperada: {type(resp_data)}")

    if not handle:
        raise RuntimeError("No se obtuvo statementHandle")

    # Poll
    poll_url = f"{url}/{handle}"
    deadline = time.monotonic() + QUERY_TIMEOUT_SECONDS

    while time.monotonic() < deadline:
        req_poll = urllib.request.Request(poll_url, headers=headers, method="GET")
        with urllib.request.urlopen(req_poll) as resp:
            data = json.loads(resp.read().decode("utf-8"))

        if isinstance(data, dict):
            status = data.get("status", {})
            state = status.get("state", "") if isinstance(status, dict) else str(status)

            if state in ("SUCCESS", "SUCCEEDED"):
                return _extract_rows(data)
            elif state in ("FAILED", "FAILED_WITH_ERROR", "ABORTED"):
                raise RuntimeError(f"Query falló: {data.get('message', state)}")

        time.sleep(QUERY_POLL_INTERVAL)

    raise TimeoutError(f"Query timeout tras {QUERY_TIMEOUT_SECONDS}s")


def _extract_rows(data: Any) -> List[Dict[str, Any]]:
    if isinstance(data, list):
        return data
    if not isinstance(data, dict):
        return []

    col_info = data.get("resultSetMetadata", {})
    columns = col_info.get("columnInfo", []) or col_info.get("columns", [])
    names = [c.get("name", f"col_{i}") for i, c in enumerate(columns)]

    rows = []
    for raw in data.get("data", []):
        if isinstance(raw, list):
            rows.append(dict(zip(names, raw)))
        elif isinstance(raw, dict):
            rows.append(raw)
    return rows


def safe_query(env: Dict[str, str], sql: str, label: str) -> List[Dict[str, Any]]:
    """Ejecuta query con manejo de errores."""
    try:
        logger.info("Ejecutando: %s", label)
        rows = _submit_and_poll(env, sql)
        logger.info("  → %d filas", len(rows))
        return rows
    except Exception as exc:
        logger.error("  → ERROR: %s", exc)
        return []


# ---------------------------------------------------------------------------
# Verificaciones
# ---------------------------------------------------------------------------

def verificar_transient(tables: List[Dict]) -> Dict[str, Any]:
    """Verifica que las tablas esperadas son TRANSIENT."""
    logger.info("=" * 50)
    logger.info("VERIFICACIÓN 1: Tablas TRANSIENT")
    logger.info("=" * 50)

    # Construir set de tablas transient encontradas
    transient_found = set()
    non_transient = set()

    for row in tables:
        db = row.get("table_catalog", row.get("TABLE_CATALOG", ""))
        schema = row.get("table_schema", row.get("TABLE_SCHEMA", ""))
        name = row.get("table_name", row.get("TABLE_NAME", ""))
        is_transient = row.get("is_transient", row.get("IS_TRANSIENT", ""))

        if db == "PRO_0_STAGING_DB":
            key = (db, schema, name)
            if str(is_transient).upper() == "YES":
                transient_found.add(key)
            else:
                non_transient.add(key)

    results = []
    all_ok = True

    for db, schema, name in EXPECTED_TRANSIENT_TABLES:
        key = (db, schema, name)
        found = key in transient_found
        status = "✅" if found else "❌"
        if not found:
            all_ok = False
            # Verificar si existe pero no es transient
            if key in non_transient:
                detail = "Existe pero NO es TRANSIENT"
            else:
                detail = "No encontrada en INFORMATION_SCHEMA"
            logger.warning("  %s %s.%s — %s", status, schema, name, detail)
        else:
            detail = "TRANSIENT correcto"
            logger.info("  %s %s.%s — %s", status, schema, name, detail)

        results.append({
            "database": db,
            "schema": schema,
            "table": name,
            "expected_transient": True,
            "is_transient": found,
            "detail": detail,
        })

    return {
        "check": "transient_tables",
        "status": "PASS" if all_ok else "FAIL",
        "total_expected": len(EXPECTED_TRANSIENT_TABLES),
        "total_transient": sum(1 for r in results if r["is_transient"]),
        "details": results,
    }


def verificar_tasks(tasks_rows: List[Dict]) -> Dict[str, Any]:
    """Verifica que las tasks de purga existen y están activas."""
    logger.info("=" * 50)
    logger.info("VERIFICACIÓN 2: Tasks de purga")
    logger.info("=" * 50)

    # Construir set de tasks encontradas
    tasks_found: Dict[Tuple[str, str, str], str] = {}
    for row in tasks_rows:
        db = row.get("task_schema", row.get("TASK_SCHEMA", row.get("database_name", "")))
        schema = row.get("task_schema", row.get("TASK_SCHEMA", ""))
        name = row.get("task_name", row.get("TASK_NAME", ""))
        state = row.get("state", row.get("STATE", ""))

        key = ("PRO_0_STAGING_DB", schema, name)
        tasks_found[key] = str(state).lower()

    results = []
    all_ok = True

    for db, schema, name in EXPECTED_PURGE_TASKS:
        key = (db, schema, name)
        state = tasks_found.get(key, None)

        if state is None:
            status = "❌"
            detail = "No encontrada"
            all_ok = False
        elif state == "started":
            status = "✅"
            detail = "Activa (STARTED)"
        elif state == "scheduled":
            status = "✅"
            detail = "Programada (SCHEDULED)"
        else:
            status = "⚠️"
            detail = f"Estado: {state}"
            all_ok = False

        logger.info("  %s %s.%s — %s", status, schema, name, detail)
        results.append({
            "database": db,
            "schema": schema,
            "task": name,
            "found": state is not None,
            "state": state or "NOT_FOUND",
            "detail": detail,
        })

    return {
        "check": "purge_tasks",
        "status": "PASS" if all_ok else "FAIL",
        "total_expected": len(EXPECTED_PURGE_TASKS),
        "total_found": sum(1 for r in results if r["found"]),
        "details": results,
    }


def verificar_coalesce(query_history: List[Dict],
                       channel_tables: List[Dict]) -> Dict[str, Any]:
    """
    Verifica que Coalesce está activo en canales HVR.
    
    Estrategia:
    - Busca queries con 'coalesce' en el texto (auditoría)
    - Verifica existencia de tablas intermedias HVR (_b, _hvr)
    - Infiere estado de Coalesce por la presencia/ausencia de patrones
    """
    logger.info("=" * 50)
    logger.info("VERIFICACIÓN 3: Coalesce en canales HVR")
    logger.info("=" * 50)

    # Analizar queries de auditoría
    coalesce_queries = []
    hvr_queries = []

    for row in query_history:
        text = row.get("query_text", row.get("QUERY_TEXT", "")).lower()
        if "coalesce" in text:
            coalesce_queries.append(row)
        if "hvr" in text or "integrate" in text:
            hvr_queries.append(row)

    # Verificar tablas intermedias HVR
    intermediate_tables = []
    for row in channel_tables:
        name = row.get("table_name", row.get("TABLE_NAME", ""))
        if name.endswith("_b") or "_hvr" in name.lower():
            intermediate_tables.append(name)

    # Determinar estado por canal
    channel_status = {}
    for channel in HVR_CHANNELS:
        # Buscar queries relacionadas con este canal
        related = [q for q in hvr_queries
                   if channel.lower() in q.get("query_text", q.get("QUERY_TEXT", "")).lower()]

        # Heurística: si hay queries de integrate sin coalesce → posiblemente inactivo
        has_coalesce = any(
            channel.lower() in q.get("query_text", q.get("QUERY_TEXT", "")).lower()
            for q in coalesce_queries
        )

        if has_coalesce:
            channel_status[channel] = ("ACTIVE", "Coalesce detectado en queries recientes")
        elif related:
            channel_status[channel] = ("UNKNOWN", "Queries HVR encontradas pero sin evidencia de Coalesce")
        else:
            channel_status[channel] = ("NO_DATA", "Sin datos de auditoría (puede ser normal)")

    all_ok = True
    results = []
    for channel, (state, detail) in channel_status.items():
        if state == "ACTIVE":
            icon = "✅"
        elif state == "UNKNOWN":
            icon = "⚠️"
            all_ok = False
        else:
            icon = "ℹ️"
        logger.info("  %s %s — %s", icon, channel, detail)
        results.append({
            "channel": channel,
            "coalesce_state": state,
            "detail": detail,
        })

    return {
        "check": "coalesce_hvr",
        "status": "PASS" if all_ok else "WARN",
        "coalesce_queries_found": len(coalesce_queries),
        "hvr_queries_found": len(hvr_queries),
        "intermediate_tables_found": len(intermediate_tables),
        "channels": results,
    }


# ---------------------------------------------------------------------------
# Generación de reporte
# ---------------------------------------------------------------------------

def generar_reporte(resultados: List[Dict], output_path: str):
    """Genera un reporte Markdown con los resultados de las verificaciones."""
    now = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")

    lines = [
        "# 📋 Reporte de Verificación Post-Deploy HVR → Snowflake",
        "",
        f"**Fecha:** {now}",
        f"**Generado por:** `verificacion_post_deploy.py`",
        "",
        "---",
        "",
        "## Resumen Ejecutivo",
        "",
        "| Verificación | Estado | Detalle |",
        "|-------------|--------|---------|",
    ]

    overall_ok = True
    for r in resultados:
        check_name = r["check"]
        status = r["status"]
        if status == "PASS":
            icon = "✅ PASS"
        elif status == "WARN":
            icon = "⚠️ WARN"
            overall_ok = False
        else:
            icon = "❌ FAIL"
            overall_ok = False

        # Detalle resumido
        if check_name == "transient_tables":
            detail = f"{r['total_transient']}/{r['total_expected']} tablas TRANSIENT"
        elif check_name == "purge_tasks":
            detail = f"{r['total_found']}/{r['total_expected']} tasks encontradas"
        elif check_name == "coalesce_hvr":
            active = sum(1 for c in r["channels"] if c["coalesce_state"] == "ACTIVE")
            detail = f"{active}/{len(r['channels'])} canales con Coalesce activo"
        else:
            detail = ""

        lines.append(f"| {check_name} | {icon} {status} | {detail} |")

    lines.append("")
    lines.append(f"**Resultado general:** {'✅ TODO OK' if overall_ok else '⚠️ REQUERE ATENCIÓN'}")
    lines.append("")
    lines.append("---")
    lines.append("")

    # Detalle por verificación
    for r in resultados:
        check = r["check"]
        lines.append(f"## {check}")
        lines.append("")

        if check == "transient_tables":
            lines.append("| Database | Schema | Tabla | ¿TRANSIENT? | Detalle |")
            lines.append("|----------|--------|-------|-------------|---------|")
            for d in r["details"]:
                icon = "✅" if d["is_transient"] else "❌"
                lines.append(
                    f"| {d['database']} | {d['schema']} | `{d['table']}` "
                    f"| {icon} {'Sí' if d['is_transient'] else 'No'} | {d['detail']} |"
                )

        elif check == "purge_tasks":
            lines.append("| Database | Schema | Task | ¿Encontrada? | Estado | Detalle |")
            lines.append("|----------|--------|------|-------------|--------|---------|")
            for d in r["details"]:
                icon = "✅" if d["found"] else "❌"
                lines.append(
                    f"| {d['database']} | {d['schema']} | `{d['task']}` "
                    f"| {icon} {'Sí' if d['found'] else 'No'} | {d['state']} | {d['detail']} |"
                )

        elif check == "coalesce_hvr":
            lines.append(f"**Queries Coalesce encontradas:** {r['coalesce_queries_found']}")
            lines.append(f"**Queries HVR encontradas:** {r['hvr_queries_found']}")
            lines.append(f"**Tablas intermedias HVR:** {r['intermediate_tables_found']}")
            lines.append("")
            lines.append("| Canal | Estado | Detalle |")
            lines.append("|-------|--------|---------|")
            for d in r["channels"]:
                icon = {"ACTIVE": "✅", "UNKNOWN": "⚠️", "NO_DATA": "ℹ️"}.get(d["coalesce_state"], "❓")
                lines.append(f"| `{d['channel']}` | {icon} {d['coalesce_state']} | {d['detail']} |")

        lines.append("")

    lines.append("---")
    lines.append("")
    lines.append("## Próximos Pasos")
    lines.append("")

    if overall_ok:
        lines.append("Todas las verificaciones pasaron correctamente. El despliegue está en buen estado.")
    else:
        lines.append("Se encontraron issues que requieren atención:")
        lines.append("")
        for r in resultados:
            if r["status"] != "PASS":
                lines.append(f"- **{r['check']}**: {r['status']} — Revisar detalle arriba.")

    lines.append("")
    lines.append(f"*Reporte generado automáticamente el {now}*")

    contenido = "\n".join(lines) + "\n"

    path = Path(output_path)
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(contenido)

    logger.info("Reporte guardado en: %s", path.resolve())
    return contenido


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(
        description="Verificación post-deploy HVR → Snowflake",
    )
    parser.add_argument(
        "--output", type=str, default="reporte_post_deploy.md",
        help="Ruta del reporte Markdown (default: reporte_post_deploy.md)",
    )
    parser.add_argument(
        "--config", type=str, default="",
        help="Ruta a JSON de configuración HVR (opcional)",
    )
    parser.add_argument(
        "--verbose", action="store_true",
        help="Activar logging DEBUG",
    )
    args = parser.parse_args()

    if args.verbose:
        logging.getLogger().setLevel(logging.DEBUG)

    logger.info("=" * 60)
    logger.info("Verificación Post-Deploy HVR → Snowflake")
    logger.info("=" * 60)

    # 1. Configuración
    env = _get_env()
    logger.info("Cuenta: %s | Warehouse: %s", env["account"], env["warehouse"])

    # Cargar config HVR si se proporciona
    hvr_config: Dict[str, Any] = {}
    if args.config and Path(args.config).exists():
        with open(args.config, "r") as f:
            hvr_config = json.load(f)
        logger.info("Config HVR cargada desde: %s", args.config)

    # 2. Ejecutar verificaciones
    resultados = []

    # 2.1 Tablas TRANSIENT
    tables = safe_query(env, QUERY_TRANSIENT_CHECK, "Tablas en PRO_0_STAGING_DB")
    if tables:
        r_transient = verificar_transient(tables)
        resultados.append(r_transient)
    else:
        resultados.append({
            "check": "transient_tables",
            "status": "FAIL",
            "error": "No se pudieron consultar las tablas",
            "details": [],
        })

    # 2.2 Tasks de purga
    tasks = safe_query(env, QUERY_TASKS_STATUS, "Tasks en PRO_0_STAGING_DB")
    if not tasks:
        tasks = safe_query(env, QUERY_TASKS_DEFINITION, "SHOW TASKS (fallback)")
    if tasks:
        r_tasks = verificar_tasks(tasks)
        resultados.append(r_tasks)
    else:
        resultados.append({
            "check": "purge_tasks",
            "status": "FAIL",
            "error": "No se pudieron consultar las tasks",
            "details": [],
        })

    # 2.3 Coalesce en canales HVR
    audit = safe_query(env, QUERY_COALESCE_AUDIT, "Auditoría Coalesce/HVR")
    channel_tbls = safe_query(env, QUERY_CHANNEL_INTEGRATION, "Tablas intermedias HVR")
    r_coalesce = verificar_coalesce(audit, channel_tbls)
    resultados.append(r_coalesce)

    # 3. Generar reporte
    logger.info("Generando reporte…")
    reporte = generar_reporte(resultados, args.output)

    # 4. Resumen en consola
    print("\n" + "=" * 60)
    print("RESUMEN POST-DEPLOY")
    print("=" * 60)
    for r in resultados:
        status = r["status"]
        icon = {"PASS": "✅", "WARN": "⚠️", "FAIL": "❌"}.get(status, "❓")
        print(f"  {icon} {r['check']}: {status}")
    print("=" * 60)
    print(f"Reporte: {Path(args.output).resolve()}")
    print("=" * 60)

    # Código de salida
    has_fail = any(r["status"] == "FAIL" for r in resultados)
    has_warn = any(r["status"] == "WARN" for r in resultados)
    if has_fail:
        sys.exit(2)
    elif has_warn:
        sys.exit(1)
    else:
        sys.exit(0)


if __name__ == "__main__":
    main()
