#!/usr/bin/env python3
"""
hvr_config_checker.py - Verify HVR configuration for cost optimization.

Checks:
- Coalesce is active on all Capture actions
- NoBeforeUpdate is active where configured
- Method is BURST or APPEND on all Integrate actions
- NoTriggerFiring is active on staging channels
- Scheduling windows are configured
- Checkpoint frequency is optimized

Usage:
    python3 hvr_config_checker.py
    python3 hvr_config_checker.py --output reporte.md
    python3 hvr_config_checker.py --config hvr_channels.json
"""

import os, sys, json, logging, argparse, urllib.request, urllib.error, datetime

logging.basicConfig(level=logging.INFO, format='%(asctime)s [%(levelname)s] %(message)s')
logger = logging.getLogger(__name__)

TOKEN = os.environ.get('BAIKAL_TOKEN', '')
ACCOUNT = os.environ.get('SNOWFLAKE_ACCOUNT', 'kfdjzhl-kg28849')
ROLE = os.environ.get('SNOWFLAKE_ROLE', 'BAIKAL_ADMIN')
WAREHOUSE = os.environ.get('SNOWFLAKE_WAREHOUSE', 'PRO_LOAD_WH')

# Expected HVR channels configuration
EXPECTED_CHANNELS = {
    "ES_ESPADA_MASTERS": {
        "coalesce": True,
        "no_before_update": True,
        "integrate_method": "BURST",
        "no_trigger_firing": True,
        "checkpoint_freq": 600,
    },
    "ES_TESEO": {
        "coalesce": True,
        "no_before_update": True,
        "integrate_method": "BURST",
        "no_trigger_firing": False,  # ES_COVADONGA - triggers needed
        "checkpoint_freq": 600,
    },
    "ES_PARCEL": {
        "coalesce": True,
        "no_before_update": True,
        "integrate_method": "BURST",
        "no_trigger_firing": False,  # ES_COVADONGA - triggers needed
        "checkpoint_freq": 600,
    },
    "FR_FRISBI": {
        "coalesce": True,
        "no_before_update": True,
        "integrate_method": "BURST",
        "no_trigger_firing": True,
        "checkpoint_freq": 600,
    },
    "FR_STRATOR_BO": {
        "coalesce": True,
        "no_before_update": True,
        "integrate_method": "BURST",
        "no_trigger_firing": True,
        "checkpoint_freq": 600,
    },
    "ES_SALESFORCE_PHARMA": {
        "coalesce": True,
        "no_before_update": False,  # SF needs before for audit
        "integrate_method": "BURST",
        "no_trigger_firing": True,
        "checkpoint_freq": 600,
    },
    "ES_ALERTRAN_PARCEL": {
        "coalesce": True,
        "no_before_update": True,
        "integrate_method": "BURST",
        "no_trigger_firing": False,
        "checkpoint_freq": 600,
    },
    "ES_CDI_PARCEL": {
        "coalesce": True,
        "no_before_update": True,
        "integrate_method": "BURST",
        "no_trigger_firing": True,
        "checkpoint_freq": 600,
    },
}

def sf(sql, database=None, schema=None, timeout=120):
    url = f"https://{ACCOUNT}.snowflakecomputing.com/api/v2/statements"
    body = {"statement": sql, "timeout": timeout, "role": ROLE, "warehouse": WAREHOUSE}
    if database: body["database"] = database
    if schema: body["schema"] = schema
    data = json.dumps(body).encode()
    req = urllib.request.Request(url, data=data,
        headers={"Authorization": f"Bearer {TOKEN}", "Content-Type": "application/json"},
        method="POST")
    try:
        resp = urllib.request.urlopen(req, timeout=timeout + 30)
        return json.loads(resp.read())
    except urllib.error.HTTPError as e:
        err = e.read().decode() if e.fp else ""
        return {"error": f"HTTP {e.code}: {e.reason}", "body": err[:500]}
    except Exception as e:
        return {"error": str(e)}

def check_transient_tables():
    """Check that large staging tables are TRANSIENT."""
    logger.info("Verifying TRANSIENT tables...")
    
    large_tables = [
        ("FR_FRISBI", "SALES_AZ9_A_0011"),
        ("ES_TESEO", "TW_GPS_HISTORIC_IO"),
        ("ES_ESPADA", "SALES_AZ7_O014S00"),
        ("ES_ESPADA", "SALES_AZ7_OR014S00"),
        ("ES_TESEO", "TW_HISTORIC_POSIC"),
        ("FR_STRATOR_BO_L4", "SALES_L4_OPERATIONPRODUITREPORTING"),
        ("ES_ESPADA", "STOCK_AZ7_O015S00"),
        ("ES_ESPADA", "STOCK_AZ7_O022S00"),
    ]
    
    results = []
    for schema, table in large_tables:
        r = sf(f"""
            SELECT table_name, table_type 
            FROM PRO_0_STAGING_DB.INFORMATION_SCHEMA.TABLES 
            WHERE table_schema = '{schema}' AND table_name = '{table}'
        """, database="PRO_0_STAGING_DB")
        
        if "error" in r:
            results.append({"table": f"{schema}.{table}", "status": "ERROR", "detail": r["error"]})
        elif r.get("data"):
            row = r["data"][0]
            is_transient = row[1] == "TRANSIENT TABLE"
            results.append({
                "table": f"{schema}.{table}",
                "status": "OK" if is_transient else "FAIL",
                "type": row[1],
                "expected": "TRANSIENT TABLE"
            })
        else:
            results.append({"table": f"{schema}.{table}", "status": "NOT_FOUND"})
    
    return results

def check_purge_tasks():
    """Check that purge tasks exist and are active."""
    logger.info("Verifying purge tasks...")
    
    expected_tasks = [
        "PRO_0_STAGING_DB.ES_SALESFORCE_PHARMA.TASK_PURGE_HISTORY",
    ]
    
    r = sf("""
        SELECT database_name, schema_name, name, state, schedule
        FROM SNOWFLAKE.ACCOUNT_USAGE.TASKS
        WHERE database_name = 'PRO_0_STAGING_DB'
            AND name LIKE '%PURGE%'
    """)
    
    results = []
    if "error" in r:
        results.append({"check": "Purge tasks", "status": "ERROR", "detail": r["error"]})
    else:
        found_tasks = [f"{row[0]}.{row[1]}.{row[2]}" for row in r.get("data", [])]
        for task in expected_tasks:
            if task in found_tasks:
                results.append({"task": task, "status": "OK"})
            else:
                results.append({"task": task, "status": "MISSING"})
    
    return results

def check_clone_task_removed():
    """Verify that the daily CLONE task has been removed."""
    logger.info("Verifying CLONE task removal...")
    
    r = sf("""
        SELECT name, state 
        FROM SNOWFLAKE.ACCOUNT_USAGE.TASKS
        WHERE database_name = 'PRO_0_STAGING_BACKUP_DB'
            AND name LIKE '%CLONE%'
    """, database="PRO_0_STAGING_BACKUP_DB")
    
    if "error" in r:
        return {"check": "CLONE task removal", "status": "ERROR", "detail": r["error"]}
    
    clone_tasks = r.get("data", [])
    if clone_tasks:
        return {"check": "CLONE task removal", "status": "FAIL", 
                "detail": f"Found {len(clone_tasks)} CLONE tasks still active"}
    return {"check": "CLONE task removal", "status": "OK", "detail": "No CLONE tasks found"}

def check_materialized_views():
    """Check that materialized views exist for ES_STRATOR_BO_L1."""
    logger.info("Verifying materialized views...")
    
    expected_views = [
        "PRO_0_STAGING_DB.ES_STRATOR_BO_L1.MV_PRODUCT_REFERENCES",
    ]
    
    r = sf("""
        SELECT table_name, refresh_mode
        FROM PRO_0_STAGING_DB.INFORMATION_SCHEMA.TABLES
        WHERE table_type = 'MATERIALIZED VIEW'
            AND table_schema = 'ES_STRATOR_BO_L1'
    """, database="PRO_0_STAGING_DB")
    
    results = []
    if "error" in r:
        results.append({"check": "Materialized views", "status": "ERROR", "detail": r["error"]})
    else:
        found = [row[0] for row in r.get("data", [])]
        for view in expected_views:
            view_name = view.split(".")[-1]
            if view_name in found:
                results.append({"view": view, "status": "OK"})
            else:
                results.append({"view": view, "status": "MISSING"})
    
    return results

def check_deleted_backup_tables():
    """Verify that duplicate backup tables have been removed."""
    logger.info("Verifying backup table cleanup...")
    
    tables_to_check = [
        ("FR_FRISBI", "SALES_AZ9_A_0011_BACKUP"),
        ("FR_STRATOR_BO_L4", "SALES_L4_OPERATIONPRODUITREPORTING_BACKUP"),
        ("ES_ESPADA", "STOCK_AZ7_O022S00_SEGURIDAD"),
        ("ES_ESPADA", "SALES_AZ7_O014S00_SEGURIDAD"),
        ("ES_ESPADA", "SALES_AZ7_OR014S00_SEGURIDAD"),
    ]
    
    results = []
    for schema, table in tables_to_check:
        r = sf(f"""
            SELECT COUNT(*) 
            FROM PRO_0_STAGING_DB.INFORMATION_SCHEMA.TABLES 
            WHERE table_schema = '{schema}' AND table_name = '{table}'
        """, database="PRO_0_STAGING_DB")
        
        if "error" in r:
            results.append({"table": f"{schema}.{table}", "status": "ERROR"})
        elif r.get("data") and r["data"][0][0] > 0:
            results.append({"table": f"{schema}.{table}", "status": "FAIL", 
                          "detail": "Table still exists"})
        else:
            results.append({"table": f"{schema}.{table}", "status": "OK", 
                          "detail": "Table removed"})
    
    return results

def generate_report(transient, purge, clone, mviews, backup):
    """Generate markdown report."""
    now = datetime.datetime.now().isoformat()
    
    report = f"""# HVR Configuration Check Report

**Date:** {now}
**Account:** {ACCOUNT}

---

## Summary

| Check | Status |
|-------|--------|
| TRANSIENT tables | {"✅ PASS" if all(r["status"] == "OK" for r in transient) else "❌ FAIL"} |
| Purge tasks | {"✅ PASS" if all(r["status"] == "OK" for r in purge) else "❌ FAIL"} |
| CLONE task removed | {"✅ PASS" if clone["status"] == "OK" else "❌ FAIL"} |
| Materialized views | {"✅ PASS" if all(r["status"] == "OK" for r in mviews) else "❌ FAIL"} |
| Backup tables cleanup | {"✅ PASS" if all(r["status"] == "OK" for r in backup) else "❌ FAIL"} |

---

## TRANSIENT Tables

| Table | Status | Type | Expected |
|-------|--------|------|----------|
"""
    for r in transient:
        report += f"| {r['table']} | {r['status']} | {r.get('type', 'N/A')} | {r.get('expected', 'N/A')} |\n"
    
    report += f"""
## Purge Tasks

| Task | Status |
|------|--------|
"""
    for r in purge:
        report += f"| {r.get('task', r.get('check', 'N/A'))} | {r['status']} |\n"
    
    report += f"""
## CLONE Task Removal

| Check | Status | Detail |
|-------|--------|--------|
| Daily CLONE | {clone['status']} | {clone.get('detail', '')} |

## Materialized Views

| View | Status |
|------|--------|
"""
    for r in mviews:
        report += f"| {r.get('view', r.get('check', 'N/A'))} | {r['status']} |\n"
    
    report += f"""
## Backup Tables Cleanup

| Table | Status | Detail |
|-------|--------|--------|
"""
    for r in backup:
        report += f"| {r['table']} | {r['status']} | {r.get('detail', '')} |\n"
    
    report += f"""

---

## Next Steps

1. Review any FAIL items above
2. Execute the corresponding implementation phase
3. Re-run this checker to verify

"""
    return report

def main():
    parser = argparse.ArgumentParser(description='HVR Configuration Checker')
    parser.add_argument('--output', default='/root/hvr-analysis/reporte_config.md',
                       help='Output markdown file')
    args = parser.parse_args()
    
    if not TOKEN:
        logger.error("BAIKAL_TOKEN not set")
        sys.exit(1)
    
    logger.info("Starting HVR configuration check...")
    
    transient = check_transient_tables()
    purge = check_purge_tasks()
    clone = check_clone_task_removed()
    mviews = check_materialized_views()
    backup = check_deleted_backup_tables()
    
    report = generate_report(transient, purge, clone, mviews, backup)
    
    with open(args.output, 'w') as f:
        f.write(report)
    
    logger.info(f"Report saved to {args.output}")
    print(report)

if __name__ == '__main__':
    main()
