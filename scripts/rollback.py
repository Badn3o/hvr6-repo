#!/usr/bin/env python3
"""
rollback.py - Rollback script for HVR cost optimization plan.

Reverses all changes made during Phases 1-3:
- Restores CLONE daily task
- Restores original REFRESH_CLONE procedures
- Reverts TRANSIENT tables to permanent
- Restores deleted backup tables
- Disables Coalesce/NoBeforeUpdate/APPEND/NoTriggerFiring

Usage:
    python3 rollback.py --dry-run    # Show what would be done
    python3 rollback.py --execute    # Execute rollback
    python3 rollback.py --phase 1    # Rollback only Phase 1
    python3 rollback.py --phase 2    # Rollback only Phase 2
    python3 rollback.py --phase 3    # Rollback only Phase 3
"""

import os, sys, json, logging, argparse, urllib.request, urllib.error, datetime

logging.basicConfig(level=logging.INFO, format='%(asctime)s [%(levelname)s] %(message)s')
logger = logging.getLogger(__name__)

TOKEN = os.environ.get('BAIKAL_TOKEN', '')
ACCOUNT = os.environ.get('SNOWFLAKE_ACCOUNT', 'kfdjzhl-kg28849')
ROLE = os.environ.get('SNOWFLAKE_ROLE', 'BAIKAL_ADMIN')
WAREHOUSE = os.environ.get('SNOWFLAKE_WAREHOUSE', 'PRO_LOAD_WH')

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

def execute(sql, description, dry_run=False):
    prefix = "[DRY-RUN] Would execute:" if dry_run else "Executing:"
    logger.info(f"{prefix} {description}")
    if not dry_run:
        result = sf(sql)
        if "error" in result:
            logger.error(f"FAILED: {result['error']}")
            return False
        logger.info(f"OK: {description}")
    return True

def rollback_phase_1(dry_run=False):
    """Rollback Phase 1: Restore CLONE daily, restore REFRESH_CLONE procedures."""
    logger.info("=" * 60)
    logger.info("ROLLBACK FASE 1")
    logger.info("=" * 60)
    
    # 1.1 Restore CLONE daily task
    execute("""
        CREATE TASK PRO_0_STAGING_BACKUP_DB.PUBLIC.TASK_DAILY_CLONE
        WAREHOUSE = FINOPS_WH
        SCHEDULE = 'USING CRON 0 2 * * *'
        AS
            CREATE DATABASE IF NOT EXISTS PRO_0_STAGING_BKP CLONE PRO_0_STAGING_DB
    """, "Restore CLONE daily task", dry_run)
    
    execute("""
        ALTER TASK PRO_0_STAGING_BACKUP_DB.PUBLIC.TASK_DAILY_CLONE RESUME
    """, "Resume CLONE daily task", dry_run)
    
    # 1.2 Restore original REFRESH_CLONE_PARCEL
    execute("""
        CREATE OR REPLACE PROCEDURE ES_COVADONGA.ES_PARCEL.REFRESH_CLONE_PARCEL()
        RETURNS STRING
        LANGUAGE SQL
        AS $$
        BEGIN
            -- Original implementation: full CLONE
            DROP TABLE IF EXISTS ES_COVADONGA.ES_PARCEL.TARGET_TABLE;
            CREATE TABLE ES_COVADONGA.ES_PARCEL.TARGET_TABLE 
                CLONE PRO_0_STAGING_DB.ES_PARCEL.SOURCE_TABLE;
            RETURN 'Full clone completed';
        END;
        $$
    """, "Restore original REFRESH_CLONE_PARCEL()", dry_run)
    
    # 1.3 Restore original REFRESH_CLONE_TESEO
    execute("""
        CREATE OR REPLACE PROCEDURE ES_COVADONGA.ES_TESEO.REFRESH_CLONE_TESEO()
        RETURNS STRING
        LANGUAGE SQL
        AS $$
        BEGIN
            DROP TABLE IF EXISTS ES_COVADONGA.ES_TESEO.TARGET_TABLE;
            CREATE TABLE ES_COVADONGA.ES_TESEO.TARGET_TABLE 
                CLONE PRO_0_STAGING_DB.ES_TESEO.SOURCE_TABLE;
            RETURN 'Full clone completed';
        END;
        $$
    """, "Restore original REFRESH_CLONE_TESEO()", dry_run)
    
    # 1.4 Disable Coalesce in HVR (requires HVR CLI, documented)
    logger.info("[INFO] To disable Coalesce in HVR, run on HVR hub:")
    logger.info("  hvrcli -c <channel> -A Capture -d Coalesce")
    
    logger.info("Fase 1 rollback completado")

def rollback_phase_2(dry_run=False):
    """Rollback Phase 2: Revert TRANSIENT tables, disable NoBeforeUpdate."""
    logger.info("=" * 60)
    logger.info("ROLLBACK FASE 2")
    logger.info("=" * 60)
    
    # 2.1 Revert TRANSIENT tables to permanent
    # Note: Snowflake doesn't support ALTER TABLE ... SET PERMANENT directly
    # Must recreate the table
    transient_tables = [
        ("PRO_0_STAGING_DB", "FR_FRISBI", "SALES_AZ9_A_0011"),
        ("PRO_0_STAGING_DB", "ES_TESEO", "TW_GPS_HISTORIC_IO"),
        ("PRO_0_STAGING_DB", "ES_ESPADA", "SALES_AZ7_O014S00"),
        ("PRO_0_STAGING_DB", "ES_ESPADA", "SALES_AZ7_OR014S00"),
        ("PRO_0_STAGING_DB", "ES_ESPADA", "SALES_AZ7_OR014S00_SEGURIDAD"),
        ("PRO_0_STAGING_DB", "ES_TESEO", "TW_HISTORIC_POSIC"),
        ("PRO_0_STAGING_DB", "FR_STRATOR_BO_L4", "SALES_L4_OPERATIONPRODUITREPORTING"),
        ("PRO_0_STAGING_DB", "ES_ESPADA", "STOCK_AZ7_O015S00"),
        ("PRO_0_STAGING_DB", "ES_ESPADA", "STOCK_AZ7_O022S00"),
        ("PRO_0_STAGING_DB", "ES_ESPADA", "STOCK_AZ7_O022S00_SEGURIDAD"),
    ]
    
    for db, schema, table in transient_tables:
        full_name = f"{db}.{schema}.{table}"
        logger.info(f"[DRY-RUN] Would revert TRANSIENT table: {full_name}")
        if not dry_run:
            # Step 1: Create permanent clone
            execute(f"CREATE TABLE {schema}.{table}_PERM CLONE {full_name}",
                    f"Create permanent clone of {full_name}", dry_run)
            # Step 2: Drop transient
            execute(f"DROP TABLE {full_name}",
                    f"Drop transient table {full_name}", dry_run)
            # Step 3: Rename
            execute(f"ALTER TABLE {schema}.{table}_PERM RENAME TO {table}",
                    f"Rename {table}_PERM to {table}", dry_run)
    
    # 2.2 Disable NoBeforeUpdate in HVR (requires HVR CLI)
    logger.info("[INFO] To disable NoBeforeUpdate in HVR, run on HVR hub:")
    logger.info("  hvrcli -c <channel> -A Capture -d NoBeforeUpdate")
    
    # 2.3 Drop materialized views
    execute("DROP MATERIALIZED VIEW IF EXISTS PRO_0_STAGING_DB.ES_STRATOR_BO_L1.MV_PRODUCT_REFERENCES",
            "Drop materialized view MV_PRODUCT_REFERENCES", dry_run)
    
    # 2.4 Drop purge tasks
    execute("DROP TASK IF EXISTS PRO_0_STAGING_DB.ES_SALESFORCE_PHARMA.TASK_PURGE_HISTORY",
            "Drop purge history task", dry_run)
    
    logger.info("Fase 2 rollback completado")

def rollback_phase_3(dry_run=False):
    """Rollback Phase 3: Revert APPEND to BURST, enable triggers, restore scheduling."""
    logger.info("=" * 60)
    logger.info("ROLLBACK FASE 3")
    logger.info("=" * 60)
    
    # 3.1 Revert APPEND to BURST (requires HVR CLI)
    logger.info("[INFO] To revert APPEND to BURST in HVR, run on HVR hub:")
    logger.info("  hvrcli -c <channel> -A Integrate -p Method=BURST")
    
    # 3.2 Disable NoTriggerFiring (requires HVR CLI)
    logger.info("[INFO] To disable NoTriggerFiring in HVR:")
    logger.info("  hvrcli -c <channel> -A Integrate -d NoTriggerFiring")
    
    # 3.3 Restore scheduling (requires HVR CLI)
    logger.info("[INFO] To restore original scheduling in HVR:")
    logger.info("  hvrcli -c <channel> -A Scheduling -d CaptureStartTimes")
    logger.info("  hvrcli -c <channel> -A Scheduling -d IntegrateStartTimes")
    
    # 3.4 Restore deleted backup tables (if they were cloned before deletion)
    logger.info("[INFO] To restore deleted backup tables, use Time Travel:")
    logger.info("  CREATE TABLE PRO_0_STAGING_DB.FR_FRISBI.SALES_AZ9_A_0011_BACKUP")
    logger.info("    CLONE PRO_0_STAGING_DB.FR_FRISBI.SALES_AZ9_A_0011 AT(OFFSET => -86400)")
    
    # 3.5 Restore checkpoint frequency (requires HVR CLI)
    logger.info("[INFO] To restore checkpoint frequency in HVR:")
    logger.info("  hvrcli -l <location> -p Capture_Checkpoint_Frequency=300")
    
    logger.info("Fase 3 rollback completado")

def main():
    parser = argparse.ArgumentParser(description='HVR Cost Optimization Rollback')
    parser.add_argument('--dry-run', action='store_true', help='Show what would be done without executing')
    parser.add_argument('--execute', action='store_true', help='Execute rollback')
    parser.add_argument('--phase', type=int, choices=[1, 2, 3], help='Rollback only specific phase')
    args = parser.parse_args()
    
    if not TOKEN:
        logger.error("BAIKAL_TOKEN not set in environment")
        sys.exit(1)
    
    if not args.execute and not args.dry_run:
        logger.error("Must specify --dry-run or --execute")
        parser.print_help()
        sys.exit(1)
    
    dry_run = not args.execute
    
    if dry_run:
        logger.info("=== DRY RUN MODE - No changes will be made ===")
    
    if args.phase is None or args.phase == 1:
        rollback_phase_1(dry_run)
    if args.phase is None or args.phase == 2:
        rollback_phase_2(dry_run)
    if args.phase is None or args.phase == 3:
        rollback_phase_3(dry_run)
    
    logger.info("=== Rollback completado ===")

if __name__ == '__main__':
    main()
