# IMPLEMENTACION FASE 1 - Optimizacion HVR 6.2
# Reduccion de costes: objetivo -40% (5.305 -> ~3.183 creditos/mes)
# Fecha: 2026-06-20
# Autor: Arquitectura de Datos

---

## INDICE

1. [Resumen Ejecutivo](#resumen)
2. [Accion 1.1 - Eliminar CLONE diario de PRO_0_STAGING_DB](#accion-11)
3. [Accion 1.2 - Optimizar REFRESH_CLONE_PARCEL y REFRESH_CLONE_TESEO](#accion-12)
4. [Accion 1.3 - Reducir frecuencia COPY INTO ES_ESPADA_MASTERS](#accion-13)
5. [Accion 1.4 - Aplicar Coalesce en Capture todos los canales](#accion-14)
6. [Plan de Ejecucion y Dependencias](#plan)
7. [Metricas de Seguimiento](#metricas)

---

## RESUMEN EJECUTIVO

La Fase 1 agrupa 4 acciones de optimizacion de bajo riesgo y alto impacto
sobre el pipeline HVR 6.2 que replica datos hacia Snowflake (PRO_0_STAGING_DB
y ES_COVADONGA). Se estima una reduccion de costes del 25-30% del total
necesario para alcanzar el objetivo del -40%.

| Accion | Ahorro estimado | Riesgo | Tiempo |
|--------|----------------|--------|--------|
| 1.1 - Eliminar CLONE diario | ~1.200 creditos/mes | Medio | 2-3 dias |
| 1.2 - Optimizar REFRESH_CLONE | ~800 creditos/mes | Alto | 5-7 dias |
| 1.3 - Reducir COPY INTO | ~200 creditos/mes | Bajo | 1 dia |
| 1.4 - Coalesce en Capture | ~100 creditos/mes | Bajo | 1 dia |
| **TOTAL FASE 1** | **~2.300 creditos/mes** | | **9-12 dias** |

---

## ACCION 1.1 - ELIMINAR CLONE DIARIO DE PRO_0_STAGING_DB

### 1.1.1 Descripcion Tecnica

El task SP_DAILY_BACKUP ejecuta diariamente un CREATE DATABASE CLONE de
PRO_0_STAGING_DB en FINOPS_WH. Esta operacion consume ~680 segundos por
ejecucion y genera un coste elevado de warehouse por la copia completa del
esquema.

**Problema:** El CLONE completo diario es innecesario porque Snowflake ya
mantiene Time Travel (1 dia por defecto en STANDARD, configurable hasta 90
dias en ENTERPRISE). Los datos clonados pueden recuperarse via Time Travel
sin necesidad de una copia completa diaria.

**Solucion:** Reemplazar el CLONE diario por:
1. Extender el periodo de Time Travel de PRO_0_STAGING_DB a 7 dias
2. Implementar un backup incremental via CREATE TABLE ... CLONE solo de
   tablas modificadas (detectadas via CHANGES() stream)
3. Mantener un snapshot semanal (domingo) en lugar de diario

### 1.1.2 Pasos de Implementacion

**PASO 1: Verificar configuracion actual de Time Travel**

```sql
-- Conectarse como ACCOUNTADMIN o SECURITYADMIN
USE ROLE ACCOUNTADMIN;

-- Verificar el periodo de Time Travel actual
SHOW DATABASES LIKE 'PRO_0_STAGING_DB';

-- Consultar el parametro
SELECT NAME, RETENTION_TIME_IN_DAYS
FROM SNOWFLAKE.ACCOUNT_USAGE.DATABASES
WHERE NAME = 'PRO_0_STAGING_DB'
  AND DELETED IS NULL;
```

**PASO 2: Extender Time Travel a 7 dias**

```sql
-- Extender retencion a 7 dias (maximo para STANDARD)
ALTER DATABASE PRO_0_STAGING_DB SET DATA_RETENTION_TIME_IN_DAYS = 7;

-- Verificar cambio
SELECT NAME, RETENTION_TIME_IN_DAYS
FROM SNOWFLAKE.ACCOUNT_USAGE.DATABASES
WHERE NAME = 'PRO_0_STAGING_DB';
```

**PASO 3: Crear Stream para detectar tablas modificadas**

```sql
-- Crear stream sobre la base de datos para tracking de cambios
USE DATABASE PRO_0_STAGING_DB;
USE SCHEMA HVR;

-- Stream a nivel de base de datos para capturar DML
CREATE STREAM IF NOT EXISTS PRO_0_STAGING_DB.HVR.STREAM_TABLE_CHANGES
  ON DATABASE PRO_0_STAGING_DB
  APPEND_ONLY = FALSE;

-- Alternativa: streams por tabla critica
CREATE STREAM IF NOT EXISTS PRO_0_STAGING_DB.HVR.STREAM_PARCEL_CHANGES
  ON TABLE PRO_0_STAGING_DB.HVR.PARCEL
  APPEND_ONLY = FALSE;

CREATE STREAM IF NOT EXISTS PRO_0_STAGING_DB.HVR.STREAM_TESEO_CHANGES
  ON TABLE PRO_0_STAGING_DB.HVR.TESEO
  APPEND_ONLY = FALSE;
```

**PASO 4: Crear Stored Procedure de backup incremental**

```sql
CREATE OR REPLACE PROCEDURE PRO_0_STAGING_DB.HVR.SP_INCREMENTAL_BACKUP(
    TARGET_DB STRING,
    SOURCE_DB STRING
)
RETURNS STRING
LANGUAGE SQL
EXECUTE AS CALLER
AS
$$
DECLARE
    tables_changed ARRAY;
    tbl STRING;
    clone_count INTEGER DEFAULT 0;
    ts STRING;
BEGIN
    -- Obtener tablas con cambios en las ultimas 24h usando el stream
    SELECT ARRAY_AGG(DISTINCT TABLE_NAME) INTO :tables_changed
    FROM TABLE(INFORMATION_SCHEMA.STREAM_DATA(
        'PRO_0_STAGING_DB.HVR.STREAM_TABLE_CHANGES',
        'LAST_24_HOURS'
    ))
    WHERE METADATA$ACTION IN ('INSERT', 'UPDATE', 'DELETE');

    -- Si no hay cambios, no hacer nada
    IF (ARRAY_SIZE(:tables_changed) = 0) THEN
        RETURN 'No changes detected. Backup skipped.';
    END IF;

    -- Timestamp para naming
    ts := TO_CHAR(CURRENT_TIMESTAMP(), 'YYYYMMDD_HH24MISS');

    -- Iterar sobre tablas cambiadas y crear clones incrementales
    FOR i IN 0 TO ARRAY_SIZE(:tables_changed) - 1 DO
        tbl := tables_changed[i];
        EXECUTE IMMEDIATE
            'CREATE TABLE IF NOT EXISTS ' || :TARGET_DB || '.HVR_BACKUP.' ||
            :tbl || '_' || :ts || ' CLONE ' || :SOURCE_DB || '.HVR.' || :tbl;
        clone_count := clone_count + 1;
    END FOR;

    RETURN 'Backup completed: ' || :clone_count || ' tables cloned.';
END;
$$;
```

**PASO 5: Reemplazar el task SP_DAILY_BACKUP**

```sql
-- Primero, desactivar el task actual
ALTER TASK PRO_0_STAGING_DB.HVR.SP_DAILY_BACKUP SUSPEND;

-- Verificar que esta suspendida
SHOW TASKS LIKE 'SP_DAILY_BACKUP';

-- Eliminar el task antiguo
DROP TASK IF EXISTS PRO_0_STAGING_DB.HVR.SP_DAILY_BACKUP;

-- Crear nuevo task incremental (semanal en lugar de diario)
CREATE OR REPLACE TASK PRO_0_STAGING_DB.HVR.SP_WEEKLY_BACKUP
  WAREHOUSE = FINOPS_WH
  SCHEDULE = 'USING CRON 0 2 * * 0 UTC'  -- Domingo a las 02:00 UTC
  COMMENT = 'Backup semanal incremental de PRO_0_STAGING_DB via Time Travel + Streams'
AS
  CALL PRO_0_STAGING_DB.HVR.SP_INCREMENTAL_BACKUP(
    'PRO_0_BACKUP_DB',
    'PRO_0_STAGING_DB'
  );

-- Crear task diario ligero (solo verifica cambios, no clona)
CREATE OR REPLACE TASK PRO_0_STAGING_DB.HVR.SP_DAILY_CHECK_CHANGES
  WAREHOUSE = FINOPS_WH
  SCHEDULE = 'USING CRON 0 3 * * * UTC'  -- Diario a las 03:00 UTC
  COMMENT = 'Verificacion diaria de cambios para backup incremental'
AS
  -- Solo registra cambios, no ejecuta clone
  INSERT INTO PRO_0_STAGING_DB.HVR.BACKUP_CHANGE_LOG
  SELECT
    CURRENT_TIMESTAMP() AS CHECK_TIME,
    TABLE_NAME,
    COUNT(*) AS CHANGE_COUNT
  FROM TABLE(INFORMATION_SCHEMA.STREAM_DATA(
    'PRO_0_STAGING_DB.HVR.STREAM_TABLE_CHANGES',
    'LAST_24_HOURS'
  ))
  GROUP BY TABLE_NAME;

-- Activar el nuevo task semanal
ALTER TASK PRO_0_STAGING_DB.HVR.SP_WEEKLY_BACKUP RESUME;
ALTER TASK PRO_0_STAGING_DB.HVR.SP_DAILY_CHECK_CHANGES RESUME;
```

**PASO 6: Crear tabla de auditoria de cambios**

```sql
CREATE TABLE IF NOT EXISTS PRO_0_STAGING_DB.HVR.BACKUP_CHANGE_LOG (
    CHECK_TIME   TIMESTAMP_NTZ,
    TABLE_NAME   STRING,
    CHANGE_COUNT INTEGER,
    BACKUP_EXECUTED BOOLEAN DEFAULT FALSE,
    BACKUP_TIME  TIMESTAMP_NTZ
);

-- Crear tabla de configuracion de backup
CREATE TABLE IF NOT EXISTS PRO_0_STAGING_DB.HVR.BACKUP_CONFIG (
    CONFIG_KEY   STRING PRIMARY KEY,
    CONFIG_VALUE STRING,
    UPDATED_AT   TIMESTAMP_NTZ DEFAULT CURRENT_TIMESTAMP()
);

INSERT INTO PRO_0_STAGING_DB.HVR.BACKUP_CONFIG VALUES
  ('BACKUP_MODE', 'INCREMENTAL', CURRENT_TIMESTAMP()),
  ('BACKUP_FREQUENCY', 'WEEKLY', CURRENT_TIMESTAMP()),
  ('TIME_TRAVEL_DAYS', '7', CURRENT_TIMESTAMP()),
  ('LAST_FULL_BACKUP', CURRENT_TIMESTAMP()::STRING, CURRENT_TIMESTAMP());
```

### 1.1.3 Verificacion Post-Implementacion

```sql
-- Ver 1: Confirmar que el task antiguo esta eliminado
SHOW TASKS LIKE '%BACKUP%' IN DATABASE PRO_0_STAGING_DB;
-- Resultado esperado: solo SP_WEEKLY_BACKUP y SP_DAILY_CHECK_CHANGES

-- Ver 2: Confirmar Time Travel extendido
SELECT NAME, RETENTION_TIME_IN_DAYS
FROM SNOWFLAKE.ACCOUNT_USAGE.DATABASES
WHERE NAME = 'PRO_0_STAGING_DB';
-- Resultado esperado: RETENTION_TIME_IN_DAYS = 7

-- Ver 3: Verificar que los streams existen y estan activos
SHOW STREAMS IN SCHEMA PRO_0_STAGING_DB.HVR;
-- Resultado esperado: STREAM_TABLE_CHANGES, STREAM_PARCEL_CHANGES, etc.

-- Ver 4: Verificar que el nuevo task se ejecuta correctamente
SELECT NAME, STATE, SCHEDULE, LAST_FUTURE_SCHEDULED_TIME
FROM TABLE(INFORMATION_SCHEMA.TASK_HISTORY())
WHERE NAME IN ('SP_WEEKLY_BACKUP', 'SP_DAILY_CHECK_CHANGES')
ORDER BY NAME;
-- Resultado esperado: STATE = 'SCHEDULED', proxima ejecucion correcta

-- Ver 5: Simular recuperacion via Time Travel (prueba de concepto)
-- Verificar que podemos acceder a datos de hace 7 dias
SELECT COUNT(*) AS ROWS_YESTERDAY
FROM PRO_0_STAGING_DB.HVR.PARCEL AT(OFFSET => -86400);  -- hace 24h

-- Ver 6: Monitorizar uso de warehouse post-cambio
SELECT
  WAREHOUSE_NAME,
  SUM(CREDITS_USED) AS TOTAL_CREDITS,
  SUM(CREDITS_USED_COMPUTE) AS COMPUTE_CREDITS,
  SUM(CREDITS_USED_CLOUD_SERVICES) AS CLOUD_CREDITS
FROM SNOWFLAKE.ACCOUNT_USAGE.WAREHOUSE_METERING_HISTORY
WHERE WAREHOUSE_NAME = 'FINOPS_WH'
  AND START_TIME >= DATEADD(DAY, -7, CURRENT_TIMESTAMP())
GROUP BY WAREHOUSE_NAME;
-- Resultado esperado: reduccion significativa vs semana anterior

-- Ver 7: Verificar tabla de auditoria
SELECT * FROM PRO_0_STAGING_DB.HVR.BACKUP_CHANGE_LOG
ORDER BY CHECK_TIME DESC LIMIT 10;
```

### 1.1.4 Riesgos

| # | Riesgo | Probabilidad | Impacto | Mitigacion |
|---|--------|-------------|---------|------------|
| R1 | Time Travel de 7 dias puede no ser suficiente para recuperacion de desastres | Bajo | Alto | Mantener backup semanal completo en PRO_0_BACKUP_DB; documentar proceso de recuperacion |
| R2 | Streams pueden perder datos si hay DDL changes (ALTER TABLE) | Medio | Medio | Anadir trigger de DDL para re-crear streams; monitorizar con INFORMATION_SCHEMA.STREAMS |
| R3 | El nuevo task incremental no detecta cambios en tablas sin stream | Medio | Alto | Crear streams para TODAS las tablas HVR, no solo las principales; script de validacion |
| R4 | Incremento de storage por Time Travel extendido (7 dias) | Bajo | Bajo | Monitorizar storage con DATABASE_STORAGE_USAGE_HISTORY; el coste de storage es ~10x menor que warehouse |
| R5 | Dependencias downstream que esperan el CLONE diario | Medio | Alto | Inventariar todos los consumidores del CLONE; notificar con 2 semanas de antelacion |

### 1.1.5 Rollback Procedure

```sql
-- ROLLBACK COMPLETO - Ejecutar si la solucion incremental falla

-- Paso 1: Detener nuevos tasks
ALTER TASK PRO_0_STAGING_DB.HVR.SP_WEEKLY_BACKUP SUSPEND;
ALTER TASK PRO_0_STAGING_DB.HVR.SP_DAILY_CHECK_CHANGES SUSPEND;

-- Paso 2: Restaurar el task original de CLONE diario
CREATE OR REPLACE TASK PRO_0_STAGING_DB.HVR.SP_DAILY_BACKUP
  WAREHOUSE = FINOPS_WH
  SCHEDULE = 'USING CRON 0 2 * * * UTC'
  COMMENT = 'Backup diario completo de PRO_0_STAGING_DB (RESTAURADO)'
AS
  CREATE OR REPLACE DATABASE PRO_0_BACKUP_DB CLONE PRO_0_STAGING_DB;

-- Paso 3: Activar el task restaurado
ALTER TASK PRO_0_STAGING_DB.HVR.SP_DAILY_BACKUP RESUME;

-- Paso 4: Verificar que el CLONE funciona
SELECT COUNT(*) FROM PRO_0_BACKUP_DB.HVR.PARCEL;
SELECT COUNT(*) FROM PRO_0_STAGING_DB.HVR.PARCEL;
-- Ambos deben tener el mismo count

-- Paso 5: Eliminar los objetos creados
DROP TASK IF EXISTS PRO_0_STAGING_DB.HVR.SP_WEEKLY_BACKUP;
DROP TASK IF EXISTS PRO_0_STAGING_DB.HVR.SP_DAILY_CHECK_CHANGES;
DROP PROCEDURE IF EXISTS PRO_0_STAGING_DB.HVR.SP_INCREMENTAL_BACKUP(STRING, STRING);
DROP TABLE IF EXISTS PRO_0_STAGING_DB.HVR.BACKUP_CHANGE_LOG;
DROP TABLE IF EXISTS PRO_0_STAGING_DB.HVR.BACKUP_CONFIG;

-- Paso 6: Revertir Time Travel (opcional, no afecta coste significativamente)
-- ALTER DATABASE PRO_0_STAGING_DB SET DATA_RETENTION_TIME_IN_DAYS = 1;

-- NOTA: Los streams NO se eliminan en rollback porque no afectan coste.
-- Pueden eliminarse manualmente si se desea:
-- DROP STREAM IF EXISTS PRO_0_STAGING_DB.HVR.STREAM_TABLE_CHANGES;
```

### 1.1.6 Tiempo Estimado

| Subtarea | Tiempo |
|----------|--------|
| Analisis de dependencias y consumidores | 4h |
| Extension de Time Travel | 1h |
| Creacion de Streams | 2h |
| Desarrollo Stored Procedure backup incremental | 4h |
| Testing en entorno de desarrollo | 4h |
| Despliegue en produccion | 2h |
| Monitorizacion post-despliegue (3 dias) | 6h |
| **TOTAL** | **23h (~3 dias)** |

---

## ACCION 1.2 - OPTIMIZAR REFRESH_CLONE_PARCEL Y REFRESH_CLONE_TESEO

### 1.2.1 Descripcion Tecnica

Los stored procedures REFRESH_CLONE_PARCEL() y REFRESH_CLONE_TESEO() ejecutan
operaciones de clone completo de tablas de 160GB+ que consumen entre 683 y
887 segundos cada una. Estas operaciones son el mayor consumidor individual
de creditos en el pipeline HVR.

**Problema:** El clone completo de tablas de 160GB+ es extremadamente costoso
porque copia todos los micro-partitions, incluso aquellos que no han cambiado
desde la ultima ejecucion.

**Solucion:** Reemplazar el clone completo por MERGE incremental usando
Snowflake Streams y Change Data Capture (CDC):
1. Crear streams sobre las tablas origen para capturar cambios
2. Reemplazar el stored procedure de clone por un MERGE que solo aplica
   cambios (INSERT, UPDATE, DELETE) detectados en el stream
3. Mantener la estructura de la tabla destino intacta

### 1.2.2 Pasos de Implementacion

**PASO 1: Analizar estructura actual de las tablas**

```sql
-- Obtener DDL de las tablas origen y destino
SELECT GET_DDL('TABLE', 'ES_COVADONGA.HVR.PARCEL');
SELECT GET_DDL('TABLE', 'ES_COVADONGA.HVR.TESEO');

-- Obtener columnas y tipos
SELECT COLUMN_NAME, DATA_TYPE, IS_NULLABLE, COMMENT
FROM INFORMATION_SCHEMA.COLUMNS
WHERE TABLE_SCHEMA = 'HVR'
  AND TABLE_NAME IN ('PARCEL', 'TESEO')
ORDER BY TABLE_NAME, ORDINAL_POSITION;

-- Obtener claves primarias (necesarias para MERGE)
SHOW PRIMARY KEYS IN TABLE ES_COVADONGA.HVR.PARCEL;
SHOW PRIMARY KEYS IN TABLE ES_COVADONGA.HVR.TESEO;
```

**PASO 2: Crear Streams sobre las tablas origen**

```sql
-- Streams para capturar cambios en las tablas origen
USE DATABASE ES_COVADONGA;
USE SCHEMA HVR;

CREATE STREAM IF NOT EXISTS STREAM_PARCEL
  ON TABLE ES_COVADONGA.HVR.PARCEL
  APPEND_ONLY = FALSE
  SHOW_INITIAL_ROWS = TRUE
  COMMENT = 'Stream CDC para tabla PARCEL - reemplaza REFRESH_CLONE_PARCEL';

CREATE STREAM IF NOT EXISTS STREAM_TESEO
  ON TABLE ES_COVADONGA.HVR.TESEO
  APPEND_ONLY = FALSE
  SHOW_INITIAL_ROWS = TRUE
  COMMENT = 'Stream CDC para tabla TESEO - reemplaza REFRESH_CLONE_TESEO';

-- Verificar streams creados
SHOW STREAMS IN SCHEMA ES_COVADONGA.HVR;
```

**PASO 3: Crear Stored Procedure MERGE incremental para PARCEL**

```sql
CREATE OR REPLACE PROCEDURE ES_COVADONGA.HVR.SP_MERGE_PARCEL()
RETURNS STRING
LANGUAGE SQL
EXECUTE AS CALLER
COMMENT = 'MERGE incremental de PARCEL usando STREAM - reemplaza REFRESH_CLONE_PARCEL'
AS
$$
DECLARE
    rows_inserted INTEGER DEFAULT 0;
    rows_updated INTEGER DEFAULT 0;
    rows_deleted INTEGER DEFAULT 0;
    has_changes BOOLEAN DEFAULT FALSE;
BEGIN
    -- Verificar si hay cambios en el stream
    SELECT COUNT(*) > 0 INTO :has_changes
    FROM ES_COVADONGA.HVR.STREAM_PARCEL
    WHERE METADATA$ACTION IN ('INSERT', 'UPDATE', 'DELETE');

    IF (NOT :has_changes) THEN
        RETURN 'No changes in PARCEL stream. Skipping.';
    END IF;

    -- MERGE: Aplicar cambios de INSERT y UPDATE
    -- Asumiendo que la clave primaria es PARCEL_ID
    MERGE INTO ES_COVADONGA.HVR.PARCEL_TARGET AS tgt
    USING (
        SELECT *
        FROM ES_COVADONGA.HVR.STREAM_PARCEL
        WHERE METADATA$ACTION IN ('INSERT', 'UPDATE')
    ) AS src
    ON tgt.PARCEL_ID = src.PARCEL_ID
    WHEN MATCHED AND METADATA$ACTION = 'UPDATE' THEN
        UPDATE SET
            tgt.FIELD1 = src.FIELD1,
            tgt.FIELD2 = src.FIELD2,
            tgt.FIELD3 = src.FIELD3,
            -- Listar TODAS las columnas excepto la PK
            tgt.LAST_MODIFIED = CURRENT_TIMESTAMP()
    WHEN NOT MATCHED AND METADATA$ACTION = 'INSERT' THEN
        INSERT (PARCEL_ID, FIELD1, FIELD2, FIELD3, LAST_MODIFIED)
        VALUES (src.PARCEL_ID, src.FIELD1, src.FIELD2, src.FIELD3, CURRENT_TIMESTAMP());

    GET DIAGNOSTICS rows_inserted := ROW_COUNT;

    -- Procesar DELETEs
    DELETE FROM ES_COVADONGA.HVR.PARCEL_TARGET
    WHERE PARCEL_ID IN (
        SELECT PARCEL_ID
        FROM ES_COVADONGA.HVR.STREAM_PARCEL
        WHERE METADATA$ACTION = 'DELETE'
    );

    GET DIAGNOSTICS rows_deleted := ROW_COUNT;

    -- Vaciar el stream (marcar cambios como consumidos)
    -- Nota: Snowflake lo hace automaticamente al leer con MERGE

    RETURN 'PARCEL merge completed. Inserted/Updated: ' ||
           :rows_inserted || ', Deleted: ' || :rows_deleted;
END;
$$;
```

**PASO 4: Crear Stored Procedure MERGE incremental para TESEO**

```sql
CREATE OR REPLACE PROCEDURE ES_COVADONGA.HVR.SP_MERGE_TESEO()
RETURNS STRING
LANGUAGE SQL
EXECUTE AS CALLER
COMMENT = 'MERGE incremental de TESEO usando STREAM - reemplaza REFRESH_CLONE_TESEO'
AS
$$
DECLARE
    rows_affected INTEGER DEFAULT 0;
    has_changes BOOLEAN DEFAULT FALSE;
BEGIN
    -- Verificar cambios
    SELECT COUNT(*) > 0 INTO :has_changes
    FROM ES_COVADONGA.HVR.STREAM_TESEO
    WHERE METADATA$ACTION IN ('INSERT', 'UPDATE', 'DELETE');

    IF (NOT :has_changes) THEN
        RETURN 'No changes in TESEO stream. Skipping.';
    END IF;

    -- MERGE para TESEO (misma logica, ajustar columnas segun DDL real)
    MERGE INTO ES_COVADONGA.HVR.TESEO_TARGET AS tgt
    USING (
        SELECT *
        FROM ES_COVADONGA.HVR.STREAM_TESEO
        WHERE METADATA$ACTION IN ('INSERT', 'UPDATE')
    ) AS src
    ON tgt.TESEO_ID = src.TESEO_ID
    WHEN MATCHED AND METADATA$ACTION = 'UPDATE' THEN
        UPDATE SET
            tgt.FIELD1 = src.FIELD1,
            tgt.FIELD2 = src.FIELD2,
            tgt.LAST_MODIFIED = CURRENT_TIMESTAMP()
    WHEN NOT MATCHED AND METADATA$ACTION = 'INSERT' THEN
        INSERT (TESEO_ID, FIELD1, FIELD2, LAST_MODIFIED)
        VALUES (src.TESEO_ID, src.FIELD1, src.FIELD2, CURRENT_TIMESTAMP());

    GET DIAGNOSTICS rows_affected := ROW_COUNT;

    -- Procesar DELETEs
    DELETE FROM ES_COVADONGA.HVR.TESEO_TARGET
    WHERE TESEO_ID IN (
        SELECT TESEO_ID
        FROM ES_COVADONGA.HVR.STREAM_TESEO
        WHERE METADATA$ACTION = 'DELETE'
    );

    RETURN 'TESEO merge completed. Rows affected: ' || :rows_affected;
END;
$$;
```

**PASO 5: Reemplazar los tasks que llaman a los procedimientos antiguos**

```sql
-- Desactivar tasks antiguos
ALTER TASK ES_COVADONGA.HVR.REFRESH_CLONE_PARCEL_TASK SUSPEND;
ALTER TASK ES_COVADONGA.HVR.REFRESH_CLONE_TESEO_TASK SUSPEND;

-- Verificar suspension
SHOW TASKS LIKE 'REFRESH_CLONE%' IN DATABASE ES_COVADONGA;

-- Eliminar tasks antiguos
DROP TASK IF EXISTS ES_COVADONGA.HVR.REFRESH_CLONE_PARCEL_TASK;
DROP TASK IF EXISTS ES_COVADONGA.HVR.REFRESH_CLONE_TESEO_TASK;

-- Crear nuevos tasks con MERGE incremental
CREATE OR REPLACE TASK ES_COVADONGA.HVR.MERGE_PARCEL_TASK
  WAREHOUSE = HVR_WH
  SCHEDULE = 'USING CRON 0 */2 * * * UTC'  -- Cada 2 horas
  COMMENT = 'MERGE incremental de PARCEL - optimizado vs CLONE completo'
AS
  CALL ES_COVADONGA.HVR.SP_MERGE_PARCEL();

CREATE OR REPLACE TASK ES_COVADONGA.HVR.MERGE_TESEO_TASK
  WAREHOUSE = HVR_WH
  SCHEDULE = 'USING CRON 0 */2 * * * UTC'  -- Cada 2 horas
  COMMENT = 'MERGE incremental de TESEO - optimizado vs CLONE completo'
AS
  CALL ES_COVADONGA.HVR.SP_MERGE_TESEO();

-- Activar nuevos tasks
ALTER TASK ES_COVADONGA.HVR.MERGE_PARCEL_TASK RESUME;
ALTER TASK ES_COVADONGA.HVR.MERGE_TESEO_TASK RESUME;
```

**PASO 6: Inicializar las tablas destino (sincronizacion inicial)**

```sql
-- La primera vez, las tablas destino deben estar sincronizadas.
-- Opcion A: Si las tablas destino ya existen con datos, verificar consistencia
SELECT
  (SELECT COUNT(*) FROM ES_COVADONGA.HVR.PARCEL) AS SOURCE_COUNT,
  (SELECT COUNT(*) FROM ES_COVADONGA.HVR.PARCEL_TARGET) AS TARGET_COUNT;

-- Opcion B: Si hay discrepancia, hacer una sincronizacion inicial unica
-- (esto se ejecuta una sola vez, fuera del task programado)
CREATE OR REPLACE TABLE ES_COVADONGA.HVR.PARCEL_TARGET AS
SELECT *, CURRENT_TIMESTAMP() AS LAST_MODIFIED
FROM ES_COVADONGA.HVR.PARCEL;

CREATE OR REPLACE TABLE ES_COVADONGA.HVR.TESEO_TARGET AS
SELECT *, CURRENT_TIMESTAMP() AS LAST_MODIFIED
FROM ES_COVADONGA.HVR.TESEO;

-- NOTA IMPORTANTE: Despues de la sincronizacion inicial, los streams
-- solo capturaran cambios NUEVOS. Los datos existentes ya estan en destino.
```

### 1.2.3 Verificacion Post-Implementacion

```sql
-- Ver 1: Confirmar que los streams tienen datos
SELECT TABLE_NAME, COUNT(*) AS CHANGE_COUNT
FROM (
    SELECT 'PARCEL' AS TABLE_NAME, METADATA$ACTION
    FROM ES_COVADONGA.HVR.STREAM_PARCEL
    UNION ALL
    SELECT 'TESEO' AS TABLE_NAME, METADATA$ACTION
    FROM ES_COVADONGA.HVR.STREAM_TESEO
)
GROUP BY TABLE_NAME;

-- Ver 2: Ejecutar MERGE manualmente y verificar resultados
CALL ES_COVADONGA.HVR.SP_MERGE_PARCEL();
CALL ES_COVADONGA.HVR.SP_MERGE_TESEO();

-- Ver 3: Comparar conteos entre origen y destino
SELECT
  'PARCEL' AS TABLE_NAME,
  (SELECT COUNT(*) FROM ES_COVADONGA.HVR.PARCEL) AS SOURCE_ROWS,
  (SELECT COUNT(*) FROM ES_COVADONGA.HVR.PARCEL_TARGET) AS TARGET_ROWS;

SELECT
  'TESEO' AS TABLE_NAME,
  (SELECT COUNT(*) FROM ES_COVADONGA.HVR.TESEO) AS SOURCE_ROWS,
  (SELECT COUNT(*) FROM ES_COVADONGA.HVR.TESEO_TARGET) AS TARGET_ROWS;

-- Ver 4: Verificar que los nuevos tasks se ejecutan correctamente
SELECT
  NAME,
  STATE,
  SCHEDULE,
  LAST_FUTURE_SCHEDULED_TIME,
  LAST_SUCCEEDED_TIME,
  LAST_ERROR_MESSAGE
FROM TABLE(INFORMATION_SCHEMA.TASK_HISTORY())
WHERE NAME IN ('MERGE_PARCEL_TASK', 'MERGE_TESEO_TASK')
ORDER BY NAME;

-- Ver 5: Medir tiempo de ejecucion (debe ser < 100s vs 683-887s anterior)
SELECT
  NAME,
  TOTAL_ELAPSED_TIME / 1000.0 AS EXEC_SECONDS,
  BYTES_SCANNED,
  ROWS_PRODUCED
FROM TABLE(INFORMATION_SCHEMA.TASK_HISTORY())
WHERE NAME IN ('MERGE_PARCEL_TASK', 'MERGE_TESEO_TASK')
ORDER BY NAME DESC LIMIT 10;

-- Ver 6: Verificar que no hay drift entre origen y destino
-- (comparar checksums de filas clave)
SELECT COUNT(*) AS MISMATCH_COUNT FROM (
    SELECT PARCEL_ID, FIELD1, FIELD2 FROM ES_COVADONGA.HVR.PARCEL
    MINUS
    SELECT PARCEL_ID, FIELD1, FIELD2 FROM ES_COVADONGA.HVR.PARCEL_TARGET
);

-- Ver 7: Monitorizar creditos consumidos post-optimizacion
SELECT
  WAREHOUSE_NAME,
  DATE_TRUNC('DAY', START_TIME) AS DAY,
  SUM(CREDITS_USED) AS DAILY_CREDITS
FROM SNOWFLAKE.ACCOUNT_USAGE.WAREHOUSE_METERING_HISTORY
WHERE WAREHOUSE_NAME = 'HVR_WH'
  AND START_TIME >= DATEADD(DAY, -14, CURRENT_TIMESTAMP())
GROUP BY 1, 2
ORDER BY 2;
```

### 1.2.4 Riesgos

| # | Riesgo | Probabilidad | Impacto | Mitigacion |
|---|--------|-------------|---------|------------|
| R1 | La sincronizacion inicial puede tardar horas en tablas de 160GB+ | Alto | Medio | Ejecutar en ventana de mantenimiento; usar warehouse dedicado mas grande solo para inicializacion |
| R2 | MERGE puede ser mas lento que CLONE si hay muchos cambios (>50% filas) | Medio | Alto | Implementar umbral: si cambios >50%, hacer CLONE completo en su lugar; monitorizar ratio de cambios |
| R3 | Puede haber perdida de datos si el stream se consume incorrectamente | Bajo | Alto | Implementar tabla de auditoria de cambios; validacion de conteos post-ejecucion |
| R4 | DDL changes (ALTER TABLE origen) pueden romper el MERGE | Medio | Alto | Anadir deteccion de DDL en el procedure; script de re-sincronizacion automatica |
| R5 | El MERGE consume mas warehouse que lo esperado si no hay filtro de particiones | Medio | Medio | Usar clustering keys en las tablas destino; limitar el scan del stream a cambios recientes |
| R6 | Race condition si HVR escribe mientras el MERGE se ejecuta | Bajo | Alto | Coordinar ventanas de ejecucion con HVR; usar LOCK tables si es necesario |

### 1.2.5 Rollback Procedure

```sql
-- ROLLBACK COMPLETO - Restaurar REFRESH_CLONE original

-- Paso 1: Detener nuevos tasks
ALTER TASK ES_COVADONGA.HVR.MERGE_PARCEL_TASK SUSPEND;
ALTER TASK ES_COVADONGA.HVR.MERGE_TESEO_TASK SUSPEND;

-- Paso 2: Eliminar nuevos tasks
DROP TASK IF EXISTS ES_COVADONGA.HVR.MERGE_PARCEL_TASK;
DROP TASK IF EXISTS ES_COVADONGA.HVR.MERGE_TESEO_TASK;

-- Paso 3: Restaurar tasks originales de CLONE
CREATE OR REPLACE TASK ES_COVADONGA.HVR.REFRESH_CLONE_PARCEL_TASK
  WAREHOUSE = HVR_WH
  SCHEDULE = 'USING CRON 0 */2 * * * UTC'
  COMMENT = 'CLONE completo de PARCEL (RESTAURADO)'
AS
  CALL ES_COVADONGA.HVR.REFRESH_CLONE_PARCEL();

CREATE OR REPLACE TASK ES_COVADONGA.HVR.REFRESH_CLONE_TESEO_TASK
  WAREHOUSE = HVR_WH
  SCHEDULE = 'USING CRON 0 */2 * * * UTC'
  COMMENT = 'CLONE completo de TESEO (RESTAURADO)'
AS
  CALL ES_COVADONGA.HVR.REFRESH_CLONE_TESEO();

-- Paso 4: Activar tasks restaurados
ALTER TASK ES_COVADONGA.HVR.REFRESH_CLONE_PARCEL_TASK RESUME;
ALTER TASK ES_COVADONGA.HVR.REFRESH_CLONE_TESEO_TASK RESUME;

-- Paso 5: Verificar que el CLONE funciona
SELECT COUNT(*) FROM ES_COVADONGA.HVR.PARCEL_TARGET;
SELECT COUNT(*) FROM ES_COVADONGA.HVR.TESEO_TARGET;

-- Paso 6: Limpiar objetos creados (opcional, no afecta funcionalidad)
DROP PROCEDURE IF EXISTS ES_COVADONGA.HVR.SP_MERGE_PARCEL();
DROP PROCEDURE IF EXISTS ES_COVADONGA.HVR.SP_MERGE_TESEO();
-- NO eliminar streams: no afectan coste y pueden ser utiles despues

-- NOTA: Las tablas TARGET creadas por el MERGE pueden eliminarse
-- o mantenerse como backup. No afectan al funcionamiento del CLONE.
```

### 1.2.6 Tiempo Estimado

| Subtarea | Tiempo |
|----------|--------|
| Analisis DDL y claves primarias de tablas | 4h |
| Creacion de Streams | 2h |
| Desarrollo Stored Procedures MERGE | 8h |
| Testing de MERGE con datos reales | 8h |
| Sincronizacion inicial (160GB+) | 4-8h |
| Despliegue en produccion | 4h |
| Monitorizacion post-despliegue (5 dias) | 10h |
| **TOTAL** | **40-44h (~5-6 dias)** |

---

## ACCION 1.3 - REDUCIR FRECUENCIA COPY INTO ES_ESPADA_MASTERS

### 1.3.1 Descripcion Tecnica

Las operaciones COPY INTO sobre ES_ESPADA_MASTERS consumen 200-257 segundos
cada una. El problema principal es que el FileFormat de HVR genera archivos
pequenos que provocan multiples operaciones COPY INTO cuando una sola masiva
seria mas eficiente.

**Problema:** El HVR FileFormat con MaxFileSize pequeno y
BurstCommitFrequency alta genera muchos archivos pequenos en el stage, lo que
provoca multiples COPY INTO y overhead de cloud services.

**Solucion:**
1. Aumentar MaxFileSize del FileFormat de HVR (de ~64MB a 256-512MB)
2. Reducir BurstCommitFrequency para agrupar commits
3. Usar compresion ZSTD en lugar de GZIP (mejor ratio, mismo speed)
4. Consolidar multiples COPY INTO en uno solo usando patrones de archivo

### 1.3.2 Pasos de Implementacion

**PASO 1: Verificar configuracion actual del FileFormat**

```sql
-- Ver el FileFormat usado por HVR
SHOW FILE FORMATS IN SCHEMA ES_COVADONGA.HVR;

-- Obtener DDL del FileFormat
SELECT GET_DDL('FILE_FORMAT', 'ES_COVADONGA.HVR.HVR_FILE_FORMAT');

-- Ver stages usados
SHOW STAGES IN SCHEMA ES_COVADONGA.HVR;

-- Ver propiedades del stage
SELECT * FROM INFORMATION_SCHEMA.STAGES
WHERE STAGE_SCHEMA = 'HVR'
  AND STAGE_NAME LIKE '%ESPADA%';
```

**PASO 2: Crear nuevo FileFormat optimizado**

```sql
-- Crear FileFormat optimizado para HVR
CREATE OR REPLACE FILE FORMAT ES_COVADONGA.HVR.HVR_FILE_FORMAT_OPTIMIZED
  TYPE = PARQUET
  COMPRESSION = ZSTD
  BINARY_AS_TEXT = FALSE
  TRIM_SPACE = FALSE
  ERROR_ON_COLUMN_COUNT_MISMATCH = TRUE
  -- Propiedades clave para optimizacion:
  MAX_FILE_SIZE = 512000000    -- 512MB (vs ~64MB actual)
  -- Nota: MAX_FILE_SIZE es para COPY INTO externo; para interno se usa
  -- el parametro del stage
  COMMENT = 'FileFormat HVR optimizado - ZSTD + 512MB max file size';

-- Alternativo: si el formato es CSV
CREATE OR REPLACE FILE FORMAT ES_COVADONGA.HVR.HVR_CSV_OPTIMIZED
  TYPE = CSV
  COMPRESSION = ZSTD
  FIELD_DELIMITER = ','
  SKIP_HEADER = 1
  TRIM_SPACE = FALSE
  ERROR_ON_COLUMN_COUNT_MISMATCH = TRUE
  EMPTY_FIELD_AS_NULL = TRUE
  COMMENT = 'CSV optimizado para HVR - ZSTD';
```

**PASO 3: Configurar Stage optimizado**

```sql
-- Crear stage optimizado con FileFormat nuevo
CREATE OR REPLACE STAGE ES_COVADONGA.HVR.HVR_ESPADA_STAGE
  FILE_FORMAT = ES_COVADONGA.HVR.HVR_FILE_FORMAT_OPTIMIZED
  URL = 's3://bucket-hvr-data/espada/'  -- ajustar URL real
  CREDENTIALS = (AWS_KEY_ID = '...' AWS_SECRET_KEY = '...')
  -- O usar Storage Integration:
  -- STORAGE_INTEGRATION = HVR_STORAGE_INT
  COMMENT = 'Stage optimizado para ES_ESPADA_MASTERS - ZSTD + 512MB'
  ENABLED = TRUE;

-- Verificar stage
SELECT * FROM @ES_COVADONGA.HVR.HVR_ESPADA_STAGE;
```

**PASO 4: Optimizar COPY INTO con consolidacion de archivos**

```sql
-- COPY INTO optimizado: usar patron para consolidar archivos
-- En lugar de multiples COPY INTO pequenos, usar uno solo con patron

-- COPY INTO consolidado
COPY INTO ES_COVADONGA.HVR.ZCDS_6_MAT_MD_V
FROM (
    SELECT
        $1:COL1::STRING AS COL1,
        $1:COL2::NUMBER AS COL2,
        $1:COL3::TIMESTAMP_NTZ AS COL3,
        -- Mapear todas las columnas necesarias
        METADATA$FILENAME AS SOURCE_FILE,
        METADATA$FILE_ROW_NUMBER AS SOURCE_ROW
    FROM @ES_COVADONGA.HVR.HVR_ESPADA_STAGE
    -- Patron para seleccionar solo archivos relevantes
    (PATTERN => '.*espada_masters_.*\\.parquet')
)
FILE_FORMAT = ES_COVADONGA.HVR.HVR_FILE_FORMAT_OPTIMIZED
MATCH_BY_COLUMN_NAME = CASE_INSENSITIVE
PURGE = FALSE
FORCE = FALSE
ON_ERROR = 'CONTINUE';

-- Alternativa: Si se necesita control mas fino, usar stored procedure
CREATE OR REPLACE PROCEDURE ES_COVADONGA.HVR.SP_COPY_ESPADA_MASTERS()
RETURNS STRING
LANGUAGE SQL
EXECUTE AS CALLER
AS
$$
DECLARE
    files_copied INTEGER DEFAULT 0;
    pattern STRING DEFAULT '.*ZCDS_6_MAT_MD.*\\.parquet';
BEGIN
    -- Un unico COPY INTO con patron para consolidar
    COPY INTO ES_COVADONGA.HVR.ZCDS_6_MAT_MD_V
    FROM @ES_COVADONGA.HVR.HVR_ESPADA_STAGE
    (PATTERN => :pattern)
    FILE_FORMAT = ES_COVADONGA.HVR.HVR_FILE_FORMAT_OPTIMIZED
    MATCH_BY_COLUMN_NAME = CASE_INSENSITIVE
    ON_ERROR = 'CONTINUE';

    -- Registrar resultados
    GET DIAGNOSTICS files_copied := ROW_COUNT;

    RETURN 'COPY INTO completed. Rows: ' || :files_copied;
END;
$$;
```

**PASO 5: Configurar parametros de BurstCommitFrequency en HVR**

```
# Configuracion en HVR Hub (interfaz web o API)
# Estos parametros se configuran en el HVR Channel, no en Snowflake

# En HVR Hub UI:
# 1. Ir a Channel > ES_ESPADA_MASTERS
# 2. FileFormat > Properties:
#    - MaxFileSize: 512 (MB)
#    - BurstCommitFrequency: 300 (segundos) -- subir de ~30s a 300s
#    - CompressionAlgorithm: ZSTD
#    - CompressionLevel: 3 (balance speed/ratio)
# 3. Guardar y reiniciar el channel

# Alternativa via HVR API (si esta disponible):
# PUT /api/v1/channels/ES_ESPADA_MASTERS/fileformat
# {
#   "maxFileSize": 512,
#   "burstCommitFrequency": 300,
#   "compressionAlgorithm": "ZSTD",
#   "compressionLevel": 3
# }
```

**PASO 6: Actualizar el task de COPY INTO**

```sql
-- Si hay un task programado para COPY INTO, actualizarlo
ALTER TASK ES_COVADONGA.HVR.COPY_ESPADA_MASTERS_TASK SUSPEND;

DROP TASK IF EXISTS ES_COVADONGA.HVR.COPY_ESPADA_MASTERS_TASK;

CREATE OR REPLACE TASK ES_COVADONGA.HVR.COPY_ESPADA_MASTERS_TASK
  WAREHOUSE = HVR_WH
  SCHEDULE = 'USING CRON 0 */4 * * * UTC'  -- Cada 4 horas (vs cada hora)
  COMMENT = 'COPY INTO optimizado de ES_ESPADA_MASTERS - ZSTD + 512MB + consolidado'
AS
  CALL ES_COVADONGA.HVR.SP_COPY_ESPADA_MASTERS();

ALTER TASK ES_COVADONGA.HVR.COPY_ESPADA_MASTERS_TASK RESUME;
```

### 1.3.3 Verificacion Post-Implementacion

```sql
-- Ver 1: Confirmar que el nuevo FileFormat existe y tiene propiedades correctas
SELECT
  NAME,
  FORMAT_TYPE,
  COMPRESSION,
  RECORD_DELIMITER,
  FIELD_DELIMITER
FROM INFORMATION_SCHEMA.FILE_FORMATS
WHERE FILE_FORMAT_SCHEMA = 'HVR'
  AND NAME LIKE '%OPTIMIZED%';

-- Ver 2: Verificar que el COPY INTO funciona con el nuevo formato
COPY INTO ES_COVADONGA.HVR.ZCDS_6_MAT_MD_V_TEST
FROM @ES_COVADONGA.HVR.HVR_ESPADA_STAGE
(PATTERN => '.*test.*\\.parquet')
FILE_FORMAT = ES_COVADONGA.HVR.HVR_FILE_FORMAT_OPTIMIZED
MATCH_BY_COLUMN_NAME = CASE_INSENSITIVE;

-- Ver 3: Medir tiempo de COPY INTO (objetivo: <100s vs 200-257s)
SELECT
  NAME,
  TOTAL_ELAPSED_TIME / 1000.0 AS EXEC_SECONDS,
  BYTES_SCANNED / 1048576.0 AS MB_SCANNED,
  ROWS_COPIED
FROM TABLE(INFORMATION_SCHEMA.COPY_HISTORY(
  TABLE_NAME => 'ES_COVADONGA.HVR.ZCDS_6_MAT_MD_V',
  START_TIME => DATEADD(HOUR, -24, CURRENT_TIMESTAMP())
))
ORDER BY EXEC_SECONDS DESC LIMIT 10;

-- Ver 4: Verificar tamano de archivos en el stage
SELECT
  NAME,
  SIZE / 1048576.0 AS SIZE_MB,
  LAST_MODIFIED
FROM TABLE(INFORMATION_SCHEMA.STAGE_FILE_LIST(
  '@ES_COVADONGA.HVR.HVR_ESPADA_STAGE'
))
ORDER BY SIZE_MB DESC LIMIT 20;
-- Resultado esperado: archivos mas grandes (256-512MB vs ~64MB)

-- Ver 5: Monitorizar creditos de cloud services (objetivo: reduccion)
SELECT
  WAREHOUSE_NAME,
  SUM(CREDITS_USED_CLOUD_SERVICES) AS CLOUD_CREDITS,
  SUM(CREDITS_USED_COMPUTE) AS COMPUTE_CREDITS
FROM SNOWFLAKE.ACCOUNT_USAGE.WAREHOUSE_METERING_HISTORY
WHERE WAREHOUSE_NAME = 'HVR_WH'
  AND START_TIME >= DATEADD(DAY, -7, CURRENT_TIMESTAMP())
GROUP BY WAREHOUSE_NAME;

-- Ver 6: Verificar que los datos son correctos (no corruption)
SELECT COUNT(*) FROM ES_COVADONGA.HVR.ZCDS_6_MAT_MD_V
WHERE SOURCE_FILE IS NOT NULL;
```

### 1.3.4 Riesgos

| # | Riesgo | Probabilidad | Impacto | Mitigacion |
|---|--------|-------------|---------|------------|
| R1 | Cambiar FileFormat puede romper compatibilidad con HVR | Medio | Alto | Probar primero en entorno de desarrollo; mantener FileFormat original como fallback |
| R2 | Archivos mas grandes pueden causar timeout en COPY INTO | Bajo | Medio | Aumentar el timeout del warehouse; usar ON_ERROR = 'CONTINUE' |
| R3 | ZSTD puede no estar soportado en la version de HVR | Bajo | Alto | Verificar version de HVR; usar GZIP como fallback si ZSTD no es compatible |
| R4 | Reducir BurstCommitFrequency puede aumentar latencia de datos | Medio | Bajo | La latencia aceptable es de 4h; documentar el SLA actualizado |
| R5 | El patron de archivos (PATTERN) puede no coincidir con naming real | Medio | Alto | Verificar naming real de archivos en el stage antes de implementar |

### 1.3.5 Rollback Procedure

```sql
-- ROLLBACK - Restaurar FileFormat y configuracion original

-- Paso 1: Detener task actual
ALTER TASK ES_COVADONGA.HVR.COPY_ESPADA_MASTERS_TASK SUSPEND;

-- Paso 2: Restaurar task original
DROP TASK IF EXISTS ES_COVADONGA.HVR.COPY_ESPADA_MASTERS_TASK;

CREATE OR REPLACE TASK ES_COVADONGA.HVR.COPY_ESPADA_MASTERS_TASK
  WAREHOUSE = HVR_WH
  SCHEDULE = 'USING CRON 0 * * * UTC'  -- Cada hora (frecuencia original)
  COMMENT = 'COPY INTO de ES_ESPADA_MASTERS (RESTAURADO)'
AS
  COPY INTO ES_COVADONGA.HVR.ZCDS_6_MAT_MD_V
  FROM @ES_COVADONGA.HVR.HVR_ESPADA_STAGE
  FILE_FORMAT = ES_COVADONGA.HVR.HVR_FILE_FORMAT  -- Formato original
  ON_ERROR = 'CONTINUE';

ALTER TASK ES_COVADONGA.HVR.COPY_ESPADA_MASTERS_TASK RESUME;

-- Paso 3: En HVR Hub, restaurar parametros originales:
# MaxFileSize: 64 (MB)
# BurstCommitFrequency: 30 (segundos)
# CompressionAlgorithm: GZIP

-- Paso 4: Verificar que el COPY INTO funciona
SELECT COUNT(*) FROM ES_COVADONGA.HVR.ZCDS_6_MAT_MD_V
WHERE CREATED_AT >= DATEADD(HOUR, -1, CURRENT_TIMESTAMP());

-- Paso 5: Limpiar objetos (opcional)
-- DROP FILE FORMAT IF EXISTS ES_COVADONGA.HVR.HVR_FILE_FORMAT_OPTIMIZED;
-- DROP PROCEDURE IF EXISTS ES_COVADONGA.HVR.SP_COPY_ESPADA_MASTERS();
```

### 1.3.6 Tiempo Estimado

| Subtarea | Tiempo |
|----------|--------|
| Analisis de FileFormat actual y archivos en stage | 2h |
| Creacion de FileFormat optimizado | 1h |
| Testing de COPY INTO con nuevo formato | 2h |
| Configuracion de HVR Hub (FileFormat params) | 2h |
| Despliegue en produccion | 1h |
| Monitorizacion post-despliegue (2 dias) | 4h |
| **TOTAL** | **12h (~1.5 dias)** |

---

## ACCION 1.4 - APLICAR COALESCE EN CAPTURE TODOS LOS CANALES

### 1.4.1 Descripcion Tecnica

La accion Coalesce en HVR fusiona multiples operaciones sobre la misma fila
en una sola operacion. Cuando HVR captura cambios de CDC y multiples filas
en el origen se modifican en rapida sucesion, sin Coalesce cada cambio genera
una operacion separada en el destino (INSERT + UPDATE + DELETE + INSERT =
4 operaciones para una sola fila final).

**Problema:** Sin Coalesce, una fila que se modifica 5 veces en el origen
genera 5 operaciones en el destino, consumiendo 5x mas warehouse del
necesario.

**Solucion:** Configurar Action Capture -> Parameter Coalesce en todos los
canales HVR. Esto hace que HVR:
1. Agrupe todas las operaciones sobre la misma fila (misma PK) dentro de
   una ventana de tiempo
2. Genere solo la operacion final (INSERT si es nueva, UPDATE si existe,
   DELETE si se elimino)
3. Reduzca dramaticamente el numero de operaciones DML en el destino

### 1.4.2 Pasos de Implementacion

**PASO 1: Identificar todos los canales HVR activos**

```sql
-- En HVR Hub, listar todos los canales activos
-- (Esto se hace via HVR Hub UI o API)

-- Consulta via HVR Hub API:
# GET /api/v1/channels
# Response:
# [
#   {"name": "CH_ESPADA_MASTERS", "state": "running", "coalesce": false},
#   {"name": "CH_COVADONGA_PARCEL", "state": "running", "coalesce": false},
#   {"name": "CH_COVADONGA_TESEO", "state": "running", "coalesce": false},
#   {"name": "CH_FINOPS_STAGING", "state": "running", "coalesce": false},
#   ...
# ]

-- En la UI de HVR Hub:
# 1. Ir a "Channels" en el menu principal
# 2. Anotar todos los canales con estado "Running"
# 3. Para cada canal, verificar si Coalesce esta activo
```

**PASO 2: Verificar configuracion actual de Coalesce**

```
# Para cada canal, verificar:
# 1. Ir a Channel > Properties > Action Capture
# 2. Buscar el parametro "Coalesce"
# 3. Anotar el valor actual (probablemente "false" o "disabled")
# 4. Anotar el numero de tablas en el canal
```

**PASO 3: Aplicar Coalesce via HVR Hub UI**

```
# Para CADA canal HVR:

# 1. Ir a HVR Hub > Channels > [Nombre del Canal]
# 2. Click en "Properties" (o "Configure")
# 3. Navegar a: Action Capture > Parameter
# 4. Buscar: Coalesce
# 5. Cambiar a: true / enabled
# 6. Configurar parametros adicionales:
#    - Coalesce Window: 30 (segundos) -- ventana para agrupar cambios
#    - Coalesce Max Operations: 100 -- maximo de ops a coalescer
# 7. Click en "Save"
# 8. Click en "Recycle" (si es necesario) o "Restart"

# IMPORTANTE: Hacer un canal a la vez y verificar que sigue funcionando
# antes de pasar al siguiente.
```

**PASO 4: Aplicar Coalesce via HVR API (alternativa automatizada)**

```bash
# Script para aplicar Coalesce a todos los canales via API

#!/bin/bash
HVR_HUB_URL="https://hvr-hub.example.com"
HVR_API_KEY="your-api-key"

# Obtener lista de canales
CHANNELS=$(curl -s -H "Authorization: Bearer $HVR_API_KEY" \
  "$HVR_HUB_URL/api/v1/channels" | jq -r '.[] | .name')

for CHANNEL in $CHANNELS; do
    echo "Processing channel: $CHANNEL"

    # Verificar estado actual
    CURRENT=$(curl -s -H "Authorization: Bearer $HVR_API_KEY" \
      "$HVR_HUB_URL/api/v1/channels/$CHANNEL/properties" | \
      jq '.capture.coalesce')

    if [ "$CURRENT" = "true" ]; then
        echo "  Coalesce already enabled. Skipping."
        continue
    fi

    # Aplicar Coalesce
    curl -s -X PATCH \
      -H "Authorization: Bearer $HVR_API_KEY" \
      -H "Content-Type: application/json" \
      "$HVR_HUB_URL/api/v1/channels/$CHANNEL/properties" \
      -d '{
        "capture": {
          "coalesce": true,
          "coalesce_window_seconds": 30,
          "coalesce_max_operations": 100
        }
      }'

    echo "  Coalesce enabled for $CHANNEL"

    # Esperar 10 segundos entre canales
    sleep 10
done

echo "Coalesce applied to all channels."
```

**PASO 5: Configurar Coalesce por tabla (si es necesario)**

```
# Si Coalesce a nivel de canal no es suficiente, se puede configurar
# a nivel de tabla individual:

# 1. Ir a Channel > Tables > [Nombre de Tabla]
# 2. Click en "Properties"
# 3. Action Capture > Parameter > Coalesce
# 4. Enabled: true
# 5. Coalesce Key: [Primary Key column]
# 6. Save

# Esto es util para tablas con alta frecuencia de cambios donde
# el Coalesce a nivel de canal no es granular suficiente.
```

**PASO 6: Reiniciar canales para aplicar cambios**

```
# Despues de configurar Coalesce, los canales deben recargarse:

# Opcion A: Via UI
# Channel > Actions > Recycle (detiene y reinicia el canal)

# Opcion B: Via API
# POST /api/v1/channels/{channel_name}/recycle

# Opcion C: Via HVR command line
# hvrcli channel recycle {channel_name}

# NOTA: El recycle causa una breve interrupcion (segundos) en la
# replicacion. Programar en ventana de baja actividad.
```

### 1.4.3 Verificacion Post-Implementacion

```sql
-- Ver 1: Verificar que Coalesce esta activo en todos los canales
# Via HVR Hub UI: Channels > [cada canal] > Properties > Action Capture > Coalesce
# Debe mostrar: true / enabled

# Via API:
# GET /api/v1/channels/{name}/properties
# Response: {"capture": {"coalesce": true, ...}}

-- Ver 2: Medir reduccion de operaciones DML en destino
-- Comparar antes y despues de aplicar Coalesce

-- Antes (sin Coalesce): contar operaciones por segundo
SELECT
  DATE_TRUNC('MINUTE', LAST_MODIFIED) AS MINUTE,
  COUNT(*) AS OPERATIONS
FROM ES_COVADONGA.HVR.PARCEL_AUDIT  -- si existe tabla de auditoria
WHERE LAST_MODIFIED >= DATEADD(HOUR, -1, CURRENT_TIMESTAMP())
GROUP BY 1
ORDER BY 1;

-- Despues (con Coalesce): mismo query, deberia mostrar menos operaciones

-- Ver 3: Verificar que los datos son correctos (no se perdieron cambios)
SELECT
  COUNT(*) AS TOTAL_ROWS,
  MIN(LAST_MODIFIED) AS EARLIEST,
  MAX(LAST_MODIFIED) AS LATEST
FROM ES_COVADONGA.HVR.PARCEL;

-- Ver 4: Monitorizar latencia de replicacion
-- (Coalesce puede aumentar latencia por la ventana de agrupacion)
SELECT
  MAX(DATEDIFF('SECOND', SOURCE_TIMESTAMP, DESTINATION_TIMESTAMP)) AS MAX_LATENCY_SEC,
  AVG(DATEDIFF('SECOND', SOURCE_TIMESTAMP, DESTINATION_TIMESTAMP)) AS AVG_LATENCY_SEC
FROM HVR_REPLICATION_MONITOR  -- si existe tabla de monitorizacion
WHERE TIMESTAMP >= DATEADD(HOUR, -1, CURRENT_TIMESTAMP());
-- Resultado esperado: latencia promedio < 60s (incluyendo ventana de 30s)

-- Ver 5: Verificar que los canales siguen funcionando
# Via HVR Hub UI: Channels > Status
# Todos los canales deben mostrar: "Running" o "OK"

-- Ver 6: Monitorizar creditos (objetivo: reduccion de cloud services)
SELECT
  WAREHOUSE_NAME,
  SUM(CREDITS_USED) AS TOTAL_CREDITS,
  SUM(CREDITS_USED_CLOUD_SERVICES) AS CLOUD_CREDITS
FROM SNOWFLAKE.ACCOUNT_USAGE.WAREHOUSE_METERING_HISTORY
WHERE WAREHOUSE_NAME = 'HVR_WH'
  AND START_TIME >= DATEADD(DAY, -7, CURRENT_TIMESTAMP())
GROUP BY 1;
```

### 1.4.4 Riesgos

| # | Riesgo | Probabilidad | Impacto | Mitigacion |
|---|--------|-------------|---------|------------|
| R1 | Coalesce aumenta la latencia de replicacion (hasta 30s adicionales) | Alto | Bajo | La ventana de 30s es aceptable para la mayoria de casos de uso; reducir a 10s si la latencia es critica |
| R2 | Si el canal se reinicia durante la ventana de Coalesce, pueden perderse cambios en buffer | Bajo | Alto | HVR persiste el estado del Coalesce en disco; verificar que el estado se recupera tras reinicio |
| R3 | Coalesce puede causar conflictos con MERGE incremental (Accion 1.2) | Medio | Medio | Si se usa MERGE, Coalesce es complementario; probar combinacion en desarrollo primero |
| R4 | No todas las tablas soportan Coalesce (tablas sin PK) | Bajo | Bajo | Verificar que todas las tablas del canal tienen PK definida; Coalesce requiere PK |
| R5 | Coalesce puede causar error si hay DDL changes durante la ventana | Bajo | Medio | HVR maneja DDL changes automaticamente; el Coalesce se aplica solo a DML |

### 1.4.5 Rollback Procedure

```bash
# ROLLBACK - Desactivar Coalesce en todos los canales

# Opcion A: Via HVR Hub UI (recomendado para rollback rapido)
# Para CADA canal:
# 1. Ir a Channel > Properties > Action Capture
# 2. Coalesce: false / disabled
# 3. Save
# 4. Recycle channel

# Opcion B: Via API
HVR_HUB_URL="https://hvr-hub.example.com"
HVR_API_KEY="your-api-key"

CHANNELS=$(curl -s -H "Authorization: Bearer $HVR_API_KEY" \
  "$HVR_HUB_URL/api/v1/channels" | jq -r '.[] | .name')

for CHANNEL in $CHANNELS; do
    echo "Disabling Coalesce for: $CHANNEL"

    curl -s -X PATCH \
      -H "Authorization: Bearer $HVR_API_KEY" \
      -H "Content-Type: application/json" \
      "$HVR_HUB_URL/api/v1/channels/$CHANNEL/properties" \
      -d '{
        "capture": {
          "coalesce": false
        }
      }'

    # Recargar canal
    curl -s -X POST \
      -H "Authorization: Bearer $HVR_API_KEY" \
      "$HVR_HUB_URL/api/v1/channels/$CHANNEL/recycle"

    echo "  Coalesce disabled for $CHANNEL"
    sleep 10
done

echo "Rollback completed. Coalesce disabled on all channels."
```

```sql
-- Verificacion post-rollback
-- Verificar que los canales siguen funcionando sin Coalesce
-- Los datos deben seguir replicandose correctamente
SELECT COUNT(*) FROM ES_COVADONGA.HVR.PARCEL
WHERE LAST_MODIFIED >= DATEADD(MINUTE, -30, CURRENT_TIMESTAMP());
-- Debe mostrar filas recientes
```

### 1.4.6 Tiempo Estimado

| Subtarea | Tiempo |
|----------|--------|
| Inventario de canales y configuracion actual | 2h |
| Aplicar Coalesce via UI/API (canal por canal) | 4h |
| Testing de cada canal post-cambio | 2h |
| Monitorizacion post-despliegue (2 dias) | 4h |
| **TOTAL** | **12h (~1.5 dias)** |

---

## PLAN DE EJECUCION Y DEPENDENCIAS

### Orden recomendado

```
Semana 1:
  Dia 1-2:  Accion 1.4 (Coalesce) - mas rapido, menor riesgo
  Dia 1-2:  Accion 1.3 (COPY INTO) - rapido, bajo riesgo
  Dia 3-5:  Accion 1.1 (CLONE diario) - riesgo medio

Semana 2:
  Dia 1-5:  Accion 1.2 (REFRESH_CLONE) - mayor riesgo, mas testing
  Dia 5-7:  Monitorizacion y ajustes
```

### Dependencias

```
1.4 (Coalesce)  ──┐
                   ├──> 1.2 (MERGE incremental) - Coalesce complementa MERGE
1.3 (COPY INTO)  ──┤
                   │
1.1 (CLONE)      ──┘ (independiente, pero hacer despues de 1.2 para
                        no interferir con la medicion de resultados)
```

### Ventanas de mantenimiento necesarias

| Accion | Ventana | Duracion |
|--------|---------|----------|
| 1.4 | Sabado 02:00-06:00 UTC | 15 min por canal |
| 1.3 | Sabado 02:00-06:00 UTC | 30 min |
| 1.1 | Sabado 02:00-06:00 UTC | 1 hora |
| 1.2 | Sabado 02:00-10:00 UTC | 4 horas (incluye sync inicial) |

---

## METRICAS DE SEGUIMIENTO

### KPIs a monitorizar semanalmente

```sql
-- Dashboard de metricas post-Fase 1

-- 1. Creditos totales por warehouse
SELECT
  WAREHOUSE_NAME,
  DATE_TRUNC('WEEK', START_TIME) AS WEEK,
  SUM(CREDITS_USED) AS WEEKLY_CREDITS,
  SUM(CREDITS_USED_COMPUTE) AS COMPUTE_CREDITS,
  SUM(CREDITS_USED_CLOUD_SERVICES) AS CLOUD_CREDITS
FROM SNOWFLAKE.ACCOUNT_USAGE.WAREHOUSE_METERING_HISTORY
WHERE START_TIME >= DATEADD(WEEK, -4, CURRENT_TIMESTAMP())
GROUP BY 1, 2
ORDER BY 2 DESC, 1;

-- 2. Ejecuciones de tasks optimizados
SELECT
  NAME,
  STATE,
  COUNT(*) AS EXECUTIONS,
  AVG(TOTAL_ELAPSED_TIME) / 1000.0 AS AVG_EXEC_SECONDS,
  SUM(CASE WHEN STATE = 'FAILED' THEN 1 ELSE 0 END) AS FAILURES
FROM TABLE(INFORMATION_SCHEMA.TASK_HISTORY())
WHERE NAME IN (
  'SP_WEEKLY_BACKUP', 'SP_DAILY_CHECK_CHANGES',
  'MERGE_PARCEL_TASK', 'MERGE_TESEO_TASK',
  'COPY_ESPADA_MASTERS_TASK'
)
  AND START_TIME >= DATEADD(DAY, -7, CURRENT_TIMESTAMP())
GROUP BY 1, 2
ORDER BY 1;

-- 3. Storage usage (impacto de Time Travel extendido)
SELECT
  DATABASE_NAME,
  DATE_TRUNC('WEEK', USAGE_DATE) AS WEEK,
  AVERAGE_DATABASE_BYTES / 1073741824.0 AS AVG_DB_GB,
  AVERAGE_FAILSAFE_BYTES / 1073741824.0 AS AVG_FAILSAFE_GB
FROM SNOWFLAKE.ACCOUNT_USAGE.DATABASE_STORAGE_USAGE_HISTORY
WHERE DATABASE_NAME IN ('PRO_0_STAGING_DB', 'ES_COVADONGA')
  AND USAGE_DATE >= DATEADD(WEEK, -4, CURRENT_DATE())
GROUP BY 1, 2
ORDER BY 2 DESC, 1;
```

### Criterios de exito

| Metrica | Objetivo | Medicion |
|---------|----------|----------|
| Reduccion de creditos/mes | >= -25% (de 5.305 a <=3.979) | Warehouse metering |
| Task failures | < 1% | Task history |
| Latencia de replicacion | < 5 min | HVR monitor |
| Data correctness | 100% match | Row count comparison |
| Rollback test exitoso | 100% | Procedure test |

---

## NOTAS FINALES

1. TODOS los cambios deben probarse primero en un entorno de desarrollo
   antes de aplicar en produccion.

2. Mantener un canal de comunicacion con el equipo de HVR durante toda
   la implementacion.

3. Documentar cualquier desviacion del plan y obtener aprobacion antes
   de proceder.

4. El ahorro real puede variar dependiendo del volumen de datos y patron
   de uso. Las estimaciones se basan en los tiempos de ejecucion
   observados.

5. Despues de completar la Fase 1, evaluar resultados antes de proceder
   con la Fase 2 (optimizaciones mas agresivas).

---

*Documento generado: 2026-06-20*
*Version: 1.0*
*Estado: Borrador para revision*
*Proxima revision: despues de aprobacion del equipo HVR*
