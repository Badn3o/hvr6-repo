# IMPLEMENTACION FASE 2 - Optimizacion HVR 6.2
# Reduccion de costes: objetivo -40% (5.305 -> ~3.183 creditos/mes)
# Fecha: 2026-06-20
# Autor: Arquitectura de Datos

---

## INDICE

1. [Resumen Ejecutivo](#resumen)
2. [Accion 2.1 - Migrar tablas de staging a TRANSIENT](#accion-21)
3. [Accion 2.2 - Implementar NoBeforeUpdate en Capture HVR](#accion-22)
4. [Accion 2.3 - Optimizar queries analiticas de ES_STRATOR_BO_L1](#accion-23)
5. [Accion 2.4 - Reducir retencion de tablas HISTORY de Salesforce](#accion-24)
6. [Plan de Ejecucion y Dependencias](#plan)
7. [Metricas de Seguimiento](#metricas)

---

## RESUMEN EJECUTIVO

La Fase 2 agrupa 4 acciones de optimizacion enfocadas en reducir el consumo
de storage y compute en Snowflake. Estas acciones complementan la Fase 1 y
contribuyen al objetivo global de reduccion del 40% en costes.

| Accion | Ahorro estimado | Riesgo | Tiempo |
|--------|----------------|--------|--------|
| 2.1 - Migrar staging a TRANSIENT | ~800 creditos/mes | Medio | 3-5 dias |
| 2.2 - NoBeforeUpdate en Capture | ~150 creditos/mes | Bajo | 1-2 dias |
| 2.3 - Optimizar queries analiticas | ~400 creditos/mes | Alto | 5-7 dias |
| 2.4 - Reducir retencion HISTORY | ~200 creditos/mes | Bajo | 1-2 dias |
| **TOTAL FASE 2** | **~1.550 creditos/mes** | | **10-16 dias** |

**Contexto de datos:**
- PRO_0_STAGING_DB: 4.107 tablas, 2,5 TB totales
- Las 30 tablas mas grandes consumen ~1,5 TB (60% del storage)
- Coste actual Fail-safe: ~7 dias de storage extra sobre 2,5 TB

---

## ACCION 2.1 - MIGRAR TABLAS DE STAGING A TRANSIENT

### 2.1.1 Descripcion Tecnica

Las tablas en PRO_0_STAGING_DB son datos de staging replicados por HVR desde
los sistemas origen. Estos datos son efimeros por naturaleza: se cargan,
se transforman y se mueven a otros esquemas. No requieren proteccion
Fail-safe de 7 dias porque pueden regenerarse desde el origen.

**Problema:** Snowflake cobra Fail-safe como 7 dias adicionales de storage
sobre el tamano total de cada tabla. Para 2,5 TB de datos de staging, esto
representa ~2,5 TB adicionales de storage facturados.

**Solucion:** Convertir las tablas de staging a TRANSIENT, lo que elimina
la capa Fail-safe y reduce el coste de storage en ~50% para estas tablas.

**Impacto:**
- Eliminacion de ~2,5 TB de storage Fail-safe
- Ahorro estimado: ~800 creditos/mes (storage + compute asociado)
- Riesgo controlado: los datos de staging son regenerables desde HVR

**Estrategia de migracion:**
1. Priorizar las 30 tablas mas grandes (~1,5 TB) para maximizar impacto
2. Migrar en lotes de 5 tablas para minimizar riesgo
3. Mantener las tablas de configuracion/metadata como permanentes

### 2.1.2 Pasos de Implementacion

**PASO 1: Identificar las 30 tablas mas grandes de staging**

```sql
-- Conectar como ACCOUNTADMIN o role con permisos sobre PRO_0_STAGING_DB
USE ROLE ACCOUNTADMIN;
USE DATABASE PRO_0_STAGING_DB;

-- Obtener las 30 tablas mas grandes por storage
SELECT
    TABLE_SCHEMA,
    TABLE_NAME,
    BYTES / POWER(1024, 3) AS SIZE_GB,
    ROW_COUNT,
    LAST_ALTERED
FROM INFORMATION_SCHEMA.TABLES
WHERE TABLE_SCHEMA = 'HVR'
    AND TABLE_TYPE = 'BASE TABLE'
    AND BYTES > 0
ORDER BY BYTES DESC
LIMIT 30;

-- Exportar lista para script de migracion
-- Guardar resultados en archivo de trabajo
```

**PASO 2: Verificar que las tablas no tienen dependencias criticas**

```sql
-- Verificar que no hay tareas (tasks) que dependan de estas tablas
SHOW TASKS IN SCHEMA PRO_0_STAGING_DB.HVR;

-- Verificar que no hay vistas materializadas sobre estas tablas
SHOW VIEWS IN SCHEMA PRO_0_STAGING_DB.HVR;

-- Verificar que no hay policies o masking sobre estas tablas
SHOW MASKING POLICIES IN SCHEMA PRO_0_STAGING_DB.HVR;

-- Verificar que no hay referencias en otros esquemas
SELECT *
FROM SNOWFLAKE.ACCOUNT_USAGE.OBJECT_DEPENDENCIES
WHERE REFERENCED_OBJECT_NAME IN (
    SELECT TABLE_NAME
    FROM INFORMATION_SCHEMA.TABLES
    WHERE TABLE_SCHEMA = 'HVR'
    ORDER BY BYTES DESC
    LIMIT 30
);
```

**PASO 3: Crear script de migracion por lotes**

```sql
-- ============================================================
-- LOTE 1: Top 5 tablas mas grandes
-- Ejecutar durante ventana de mantenimiento (fin de semana)
-- ============================================================

-- Tabla 1 (ejemplo: PARCEL)
ALTER TABLE PRO_0_STAGING_DB.HVR.PARCEL SET TRANSIENT;
-- Verificar
SHOW TABLES LIKE 'PARCEL' IN SCHEMA PRO_0_STAGING_DB.HVR;

-- Tabla 2 (ejemplo: TESEO)
ALTER TABLE PRO_0_STAGING_DB.HVR.TESEO SET TRANSIENT;
-- Verificar
SHOW TABLES LIKE 'TESEO' IN SCHEMA PRO_0_STAGING_DB.HVR;

-- Tabla 3 (ejemplo: CUSTOMER)
ALTER TABLE PRO_0_STAGING_DB.HVR.CUSTOMER SET TRANSIENT;

-- Tabla 4 (ejemplo: TRANSACTION)
ALTER TABLE PRO_0_STAGING_DB.HVR.TRANSACTION SET TRANSIENT;

-- Tabla 5 (ejemplo: INVENTORY)
ALTER TABLE PRO_0_STAGING_DB.HVR.INVENTORY SET TRANSIENT;

-- ============================================================
-- LOTE 2: Tablas 6-10
-- Ejecutar 24h despues de LOTE 1 si no hay incidencias
-- ============================================================
-- ALTER TABLE PRO_0_STAGING_DB.HVR.<TABLE_6> SET TRANSIENT;
-- ALTER TABLE PRO_0_STAGING_DB.HVR.<TABLE_7> SET TRANSIENT;
-- ALTER TABLE PRO_0_STAGING_DB.HVR.<TABLE_8> SET TRANSIENT;
-- ALTER TABLE PRO_0_STAGING_DB.HVR.<TABLE_9> SET TRANSIENT;
-- ALTER TABLE PRO_0_STAGING_DB.HVR.<TABLE_10> SET TRANSIENT;

-- ============================================================
-- LOTES 3-6: Tablas 11-30
-- Ejecutar un lote cada 24-48h
-- ============================================================
```

**PASO 4: Script automatizado de migracion (alternativa)**

```sql
-- Stored procedure para migracion automatizada
CREATE OR REPLACE PROCEDURE PRO_0_STAGING_DB.HVR.SP_MIGRATE_TO_TRANSIENT(
    SCHEMA_NAME STRING,
    BATCH_SIZE INTEGER DEFAULT 5
)
RETURNS STRING
LANGUAGE SQL
EXECUTE AS CALLER
COMMENT = 'Migra las tablas mas grandes a TRANSIENT en lotes controlados'
AS
$$
DECLARE
    tables_migrated INTEGER DEFAULT 0;
    total_bytes_saved INTEGER DEFAULT 0;
    tbl STRING;
    tbl_bytes INTEGER;
    result STRING;
BEGIN
    -- Cursor sobre las tablas mas grandes del esquema
    FOR rec IN (
        SELECT TABLE_NAME, BYTES
        FROM INFORMATION_SCHEMA.TABLES
        WHERE TABLE_SCHEMA = :SCHEMA_NAME
            AND TABLE_TYPE = 'BASE TABLE'
            AND BYTES > 0
            -- Excluir tablas ya TRANSIENT
            AND IS_TRANSIENT = 'NO'
        ORDER BY BYTES DESC
        LIMIT :BATCH_SIZE
    ) DO
        tbl := rec.TABLE_NAME;
        tbl_bytes := rec.BYTES;

        -- Migrar a TRANSIENT
        EXECUTE IMMEDIATE
            'ALTER TABLE PRO_0_STAGING_DB.' || :SCHEMA_NAME || '.' ||
            :tbl || ' SET TRANSIENT';

        tables_migrated := tables_migrated + 1;
        total_bytes_saved := total_bytes_saved + tbl_bytes;

        -- Log de migracion
        INSERT INTO PRO_0_STAGING_DB.HVR.MIGRATION_LOG (
            MIGRATION_TIME, TABLE_NAME, ACTION, BYTES_AFFECTED
        ) VALUES (
            CURRENT_TIMESTAMP(), tbl, 'SET_TRANSIENT', tbl_bytes
        );
    END FOR;

    result := 'Migrated ' || :tables_migrated || ' tables. ' ||
              'Estimated bytes saved from Fail-safe: ' ||
              (:total_bytes_saved / POWER(1024, 3)) || ' GB';

    RETURN result;
END;
$$;

-- Ejecutar migracion del primer lote
CALL PRO_0_STAGING_DB.HVR.SP_MIGRATE_TO_TRANSIENT('HVR', 5);
```

**PASO 5: Crear tabla de log de migracion**

```sql
-- Tabla para tracking de migraciones
CREATE TABLE IF NOT EXISTS PRO_0_STAGING_DB.HVR.MIGRATION_LOG (
    MIGRATION_TIME   TIMESTAMP_NTZ DEFAULT CURRENT_TIMESTAMP(),
    TABLE_NAME       STRING,
    ACTION           STRING,
    BYTES_AFFECTED   INTEGER,
    EXECUTED_BY      STRING DEFAULT CURRENT_USER(),
    STATUS           STRING DEFAULT 'SUCCESS'
);

-- Verificar log despues de cada lote
SELECT * FROM PRO_0_STAGING_DB.HVR.MIGRATION_LOG
ORDER BY MIGRATION_TIME DESC;
```

**PASO 6: Migrar tablas restantes (31-4107)**

```sql
-- Para las tablas restantes (menores), migrar en lotes mas grandes
-- ya que el impacto individual es menor

-- Lotes de 50 tablas para las restantes
CREATE OR REPLACE PROCEDURE PRO_0_STAGING_DB.HVR.SP_MIGRATE_REMAINING(
    BATCH_SIZE INTEGER DEFAULT 50
)
RETURNS STRING
LANGUAGE SQL
EXECUTE AS CALLER
AS
$$
DECLARE
    tables_migrated INTEGER DEFAULT 0;
BEGIN
    FOR rec IN (
        SELECT TABLE_NAME
        FROM INFORMATION_SCHEMA.TABLES
        WHERE TABLE_SCHEMA = 'HVR'
            AND TABLE_TYPE = 'BASE TABLE'
            AND IS_TRANSIENT = 'NO'
            -- Excluir tablas de configuracion/metadata
            AND TABLE_NAME NOT IN (
                'MIGRATION_LOG', 'BACKUP_CONFIG',
                'BACKUP_CHANGE_LOG', 'HVR_CONFIG'
            )
        ORDER BY BYTES ASC  -- Las mas pequeñas primero
        LIMIT :BATCH_SIZE
    ) DO
        EXECUTE IMMEDIATE
            'ALTER TABLE PRO_0_STAGING_DB.HVR.' ||
            rec.TABLE_NAME || ' SET TRANSIENT';
        tables_migrated := tables_migrated + 1;
    END FOR;

    RETURN 'Migrated ' || :tables_migrated || ' remaining tables.';
END;
$$;

-- Ejecutar en lotes de 50 hasta completar
CALL PRO_0_STAGING_DB.HVR.SP_MIGRATE_REMAINING(50);
```

### 2.1.3 Verificacion Post-Implementacion

```sql
-- Ver 1: Confirmar que las tablas son TRANSIENT
SELECT
    TABLE_NAME,
    IS_TRANRETENTION_TIME_IN_DAYS,
    BYTES / POWER(1024, 3) AS SIZE_GB
FROM INFORMATION_SCHEMA.TABLES
WHERE TABLE_SCHEMA = 'HVR'
    AND TABLE_TYPE = 'BASE TABLE'
ORDER BY BYTES DESC
LIMIT 30;
-- Resultado esperado: IS_TRANSIENT = 'YES' para todas las migradas

-- Ver 2: Verificar que no hay Fail-safe en tablas TRANSIENT
SELECT
    TABLE_NAME,
    FAILSAFE_BYTES / POWER(1024, 3) AS FAILSAFE_GB
FROM INFORMATION_SCHEMA.TABLES
WHERE TABLE_SCHEMA = 'HVR'
    AND TABLE_TYPE = 'BASE TABLE'
    AND FAILSAFE_BYTES > 0;
-- Resultado esperado: 0 filas (sin Fail-safe)

-- Ver 3: Comparar storage total antes y despues
SELECT
    TABLE_SCHEMA,
    SUM(BYTES) / POWER(1024, 3) AS ACTIVE_STORAGE_GB,
    SUM(FAILSAFE_BYTES) / POWER(1024, 3) AS FAILSAFE_STORAGE_GB,
    SUM(TIME_TRAVEL_BYTES) / POWER(1024, 3) AS TIME_TRAVEL_GB
FROM INFORMATION_SCHEMA.TABLES
WHERE TABLE_SCHEMA = 'HVR'
GROUP BY TABLE_SCHEMA;
-- Resultado esperado: FAILSAFE_STORAGE_GB = 0 o muy cercano a 0

-- Ver 4: Verificar que HVR sigue replicando correctamente
SELECT
    TABLE_NAME,
    ROW_COUNT,
    LAST_ALTERED
FROM INFORMATION_SCHEMA.TABLES
WHERE TABLE_SCHEMA = 'HVR'
    AND TABLE_NAME IN ('PARCEL', 'TESEO', 'CUSTOMER')
ORDER BY TABLE_NAME;
-- Resultado esperado: ROW_COUNT incrementando, LAST_ALTERED reciente

-- Ver 5: Monitorizar storage semanal
SELECT
    USAGE_DATE,
    DATABASE_NAME,
    AVERAGE_DATABASE_BYTES / POWER(1024, 3) AS AVG_STORAGE_GB,
    AVERAGE_FAILSAFE_BYTES / POWER(1024, 3) AS AVG_FAILSAFE_GB
FROM SNOWFLAKE.ACCOUNT_USAGE.DATABASE_STORAGE_USAGE_HISTORY
WHERE DATABASE_NAME = 'PRO_0_STAGING_DB'
    AND USAGE_DATE >= DATEADD(DAY, -30, CURRENT_DATE())
ORDER BY USAGE_DATE DESC;
-- Resultado esperado: reduccion progresiva de FAILSAFE_GB

-- Ver 6: Verificar log de migracion
SELECT
    ACTION,
    COUNT(*) AS TABLES_MIGRATED,
    SUM(BYTES_AFFECTED) / POWER(1024, 3) AS TOTAL_GB
FROM PRO_0_STAGING_DB.HVR.MIGRATION_LOG
GROUP BY ACTION;
-- Resultado esperado: todas las tablas migradas con EXITO
```

### 2.1.4 Riesgos

| # | Riesgo | Probabilidad | Impacto | Mitigacion |
|---|--------|-------------|---------|------------|
| R1 | Perdida de datos si HVR falla y no hay Fail-safe para recuperar | Medio | Alto | Mantener Time Travel a 1 dia (minimo); HVR re-replica datos desde origen; documentar proceso de re-carga |
| R2 | Tablas TRANSIENT no pueden ser clonadas con CLONE | Bajo | Bajo | Verificar que no hay CLONE dependencies antes de migrar; usar CTAS como alternativa |
| R3 | Impacto en procesos downstream que dependen de Fail-safe | Bajo | Medio | Inventariar todos los procesos de recuperacion; notificar equipos afectados |
| R4 | Error humano al migrar tablas incorrectas | Bajo | Alto | Script de validacion pre-migracion; ejecutar en lotes pequenos; rollback procedure documentado |
| R5 | Incremento de tiempo de recuperacion ante desastres | Medio | Medio | Documentar que datos de staging se re-replican desde HVR; estimar tiempo de re-carga completa |

### 2.1.5 Rollback Procedure

```sql
-- ROLLBACK COMPLETO - Restaurar tablas a permanentes (con Fail-safe)
-- NOTA: Snowflake NO permite convertir TRANSIENT a permanente directamente
-- Se debe recrear la tabla como permanente y copiar los datos

-- Paso 1: Identificar tablas TRANSIENT a restaurar
SELECT TABLE_NAME, BYTES / POWER(1024, 3) AS SIZE_GB
FROM INFORMATION_SCHEMA.TABLES
WHERE TABLE_SCHEMA = 'HVR'
    AND IS_TRANSIENT = 'YES'
ORDER BY BYTES DESC;

-- Paso 2: Para cada tabla, crear version permanente y migrar datos
-- Ejemplo para tabla PARCEL:

-- 2a: Crear tabla permanente con misma estructura
CREATE TABLE PRO_0_STAGING_DB.HVR.PARCEL_PERMANENT LIKE PRO_0_STAGING_DB.HVR.PARCEL;

-- 2b: Copiar datos
INSERT INTO PRO_0_STAGING_DB.HVR.PARCEL_PERMANENT
SELECT * FROM PRO_0_STAGING_DB.HVR.PARCEL;

-- 2c: Renombrar tablas
ALTER TABLE PRO_0_STAGING_DB.HVR.PARCEL RENAME TO PARCEL_TRANSIENT_BACKUP;
ALTER TABLE PRO_0_STAGING_DB.HVR.PARCEL_PERMANENT RENAME TO PARCEL;

-- 2d: Eliminar backup
DROP TABLE PRO_0_STAGING_DB.HVR.PARCEL_TRANSIENT_BACKUP;

-- Paso 3: Verificar restauracion
SELECT TABLE_NAME, IS_TRANSIENT, BYTES / POWER(1024, 3) AS SIZE_GB
FROM INFORMATION_SCHEMA.TABLES
WHERE TABLE_SCHEMA = 'HVR'
    AND TABLE_NAME = 'PARCEL';
-- Resultado esperado: IS_TRANSIENT = 'NO'

-- Paso 4: Script de rollback automatizado para multiples tablas
CREATE OR REPLACE PROCEDURE PRO_0_STAGING_DB.HVR.SP_ROLLBACK_TRANSIENT(
    TABLE_NAME STRING
)
RETURNS STRING
LANGUAGE SQL
EXECUTE AS CALLER
AS
$$
DECLARE
    temp_table STRING;
    permanent_table STRING;
BEGIN
    temp_table := TABLE_NAME || '_TEMP_PERMANENT';
    permanent_table := TABLE_NAME;

    -- Crear version permanente
    EXECUTE IMMEDIATE
        'CREATE TABLE PRO_0_STAGING_DB.HVR.' || :temp_table ||
        ' LIKE PRO_0_STAGING_DB.HVR.' || :permanent_table;

    -- Copiar datos
    EXECUTE IMMEDIATE
        'INSERT INTO PRO_0_STAGING_DB.HVR.' || :temp_table ||
        ' SELECT * FROM PRO_0_STAGING_DB.HVR.' || :permanent_table;

    -- Swap
    EXECUTE IMMEDIATE
        'ALTER TABLE PRO_0_STAGING_DB.HVR.' || :permanent_table ||
        ' RENAME TO ' || :permanent_table || '_TRANSIENT_BAK';

    EXECUTE IMMEDIATE
        'ALTER TABLE PRO_0_STAGING_DB.HVR.' || :temp_table ||
        ' RENAME TO ' || :permanent_table;

    -- Limpiar
    EXECUTE IMMEDIATE
        'DROP TABLE PRO_0_STAGING_DB.HVR.' || :permanent_table || '_TRANSIENT_BAK';

    RETURN 'Rollback completed for: ' || :permanent_table;
END;
$$;

-- Paso 5: Registrar rollback en log
INSERT INTO PRO_0_STAGING_DB.HVR.MIGRATION_LOG (
    TABLE_NAME, ACTION, STATUS
) VALUES ('ROLLBACK', 'RESTORE_PERMANENT', 'EXECUTED');
```

### 2.1.6 Tiempo Estimado

| Subtarea | Tiempo |
|----------|--------|
| Analisis de tablas y dependencias | 4h |
| Script de migracion y validacion | 4h |
| Migracion Lote 1 (top 5 tablas) | 2h |
| Validacion y monitorizacion Lote 1 | 4h |
| Migracion Lotes 2-6 (tablas 6-30) | 6h |
| Migracion tablas restantes (31-4107) | 8h |
| Verificacion completa y documentacion | 4h |
| **TOTAL** | **32h (~5 dias)** |

---

## ACCION 2.2 - IMPLEMENTAR NOBEFOREUPDATE EN CAPTURE HVR

### 2.2.1 Descripcion Tecnica

Cuando HVR captura cambios (CDC - Change Data Capture), por defecto registra
tanto el estado "before" como el "after" de cada operacion UPDATE. Esto
duplica la cantidad de datos capturados para updates, que tipicamente
representan el 60-70% de las operaciones DML.

**Problema:** Almacenar el "before" de cada update consume ~3-5% adicional
en storage y compute de captura, sin aportar valor para la mayoria de los
casos de uso de staging.

**Solucion:** Configurar el parametro NoBeforeUpdate en las acciones de
Capture de HVR para las tablas que no requieren auditoria completa. Esto
elimina la captura del estado previo en operaciones UPDATE.

**Impacto:**
- Reduccion de ~3-5% en datos capturados
- Ahorro estimado: ~150 creditos/mes
- Aplicable a: tablas de staging sin requisito de auditoria

**Tablas NO aplicables (mantener Before/After):**
- Tablas con requisitos regulatorios de auditoria
- Tablas de configuracion del sistema
- Tablas referenciadas por compliance o legal

### 2.2.2 Pasos de Implementacion

**PASO 1: Identificar tablas candidatas (sin requisito de auditoria)**

```sql
-- Listar todas las tablas HVR con su tamano y actividad
USE DATABASE PRO_0_STAGING_DB;

SELECT
    t.TABLE_NAME,
    t.BYTES / POWER(1024, 3) AS SIZE_GB,
    t.ROW_COUNT,
    -- Estimar porcentaje de updates vs inserts
    -- (requiere analisis de HVR logs)
    CASE
        WHEN t.TABLE_NAME LIKE '%_AUDIT%' THEN 'NO - Auditoria'
        WHEN t.TABLE_NAME LIKE '%_CONFIG%' THEN 'NO - Configuracion'
        WHEN t.TABLE_NAME LIKE '%_HISTORY%' THEN 'NO - Historico'
        ELSE 'SI - Candidata'
    END AS NOBEFOREUPDATE_ELIGIBLE
FROM INFORMATION_SCHEMA.TABLES t
WHERE t.TABLE_SCHEMA = 'HVR'
    AND t.TABLE_TYPE = 'BASE TABLE'
ORDER BY t.BYTES DESC;
```

**PASO 2: Documentar tablas excluidas y razon**

```sql
-- Crear tabla de configuracion para NoBeforeUpdate
CREATE TABLE IF NOT EXISTS PRO_0_STAGING_DB.HVR.CAPTURE_CONFIG (
    TABLE_NAME       STRING PRIMARY KEY,
    CHANNEL_NAME     STRING,
    GROUP_NAME       STRING,
    NOBEFOREUPDATE   BOOLEAN DEFAULT FALSE,
    EXCLUSION_REASON STRING,
    CONFIGURED_AT    TIMESTAMP_NTZ,
    CONFIGURED_BY    STRING
);

-- Insertar tablas excluidas
INSERT INTO PRO_0_STAGING_DB.HVR.CAPTURE_CONFIG
    (TABLE_NAME, NOBEFOREUPDATE, EXCLUSION_REASON, CONFIGURED_AT, CONFIGURED_BY)
VALUES
    ('AUDIT_LOG', FALSE, 'Requisito de auditoria regulatorio', CURRENT_TIMESTAMP(), CURRENT_USER()),
    ('SYSTEM_CONFIG', FALSE, 'Configuracion del sistema', CURRENT_TIMESTAMP(), CURRENT_USER()),
    ('USER_HISTORY', FALSE, 'Historico de cambios de usuarios', CURRENT_TIMESTAMP(), CURRENT_USER());

-- Verificar configuracion
SELECT * FROM PRO_0_STAGING_DB.HVR.CAPTURE_CONFIG;
```

**PASO 3: Configurar NoBeforeUpdate en HVR (via HVR Console o hvr.cfg)**

```
# Configuracion en archivo hvr.cfg del canal de captura
# Acceder a HVR Console > Channel > Capture > Action

# Para cada tabla candidata, agregar:
<Action>
    <table_pattern>*</table_pattern>
    <cap_change>insert,update,delete</cap_change>
    <no_before_update>true</no_before_update>
</Action>

# Exclusion para tablas con auditoria:
<Action>
    <table_pattern>*_AUDIT</table_pattern>
    <cap_change>insert,update,delete</cap_change>
    <no_before_update>false</no_before_update>
</Action>

<Action>
    <table_pattern>*_CONFIG</table_pattern>
    <cap_change>insert,update,delete</cap_change>
    <no_before_update>false</no_before_update>
</Action>
```

**PASO 4: Configuracion via HVR CLI (alternativa)**

```bash
# Conectar al servidor HVR
ssh hvr-admin@hvr-server

# Navegar al directorio del canal
cd /opt/hvr/channels/hvr_staging/

# Editar configuracion del canal
vi hvr.cfg

# Agregar seccion de Action para NoBeforeUpdate
# [capture_action_no_before]
#     table_pattern=*
#     no_before_update=true
#     exclude_pattern=*_AUDIT|*_CONFIG|*_HISTORY

# Recargar configuracion del canal
hvrcli -c hvr_staging reload

# Verificar que el cambio se aplico
hvrcli -c hvr_staging show-config | grep -i before
```

**PASO 5: Verificar configuracion en HVR Console**

```bash
# Acceder a HVR Console (web UI)
# URL: https://hvr-server:4340

# Pasos en UI:
# 1. Ir a Channels > hvr_staging
# 2. Seleccionar tab "Actions"
# 3. Buscar "Capture" actions
# 4. Verificar que "No Before Update" esta habilitado
# 5. Verificar exclusiones para tablas de auditoria
```

**PASO 6: Actualizar tabla de configuracion**

```sql
-- Registrar tablas configuradas con NoBeforeUpdate
INSERT INTO PRO_0_STAGING_DB.HVR.CAPTURE_CONFIG
    (TABLE_NAME, NOBEFOREUPDATE, CONFIGURED_AT, CONFIGURED_BY)
SELECT
    TABLE_NAME,
    TRUE,
    CURRENT_TIMESTAMP(),
    CURRENT_USER()
FROM INFORMATION_SCHEMA.TABLES
WHERE TABLE_SCHEMA = 'HVR'
    AND TABLE_TYPE = 'BASE TABLE'
    AND TABLE_NAME NOT IN (
        SELECT TABLE_NAME
        FROM PRO_0_STAGING_DB.HVR.CAPTURE_CONFIG
    );

-- Verificar configuracion final
SELECT
    NOBEFOREUPDATE,
    COUNT(*) AS TABLE_COUNT
FROM PRO_0_STAGING_DB.HVR.CAPTURE_CONFIG
GROUP BY NOBEFOREUPDATE;
```

### 2.2.3 Verificacion Post-Implementacion

```sql
-- Ver 1: Verificar que HVR sigue capturando datos correctamente
SELECT
    TABLE_NAME,
    ROW_COUNT,
    LAST_ALTERED
FROM INFORMATION_SCHEMA.TABLES
WHERE TABLE_SCHEMA = 'HVR'
    AND TABLE_NAME IN ('PARCEL', 'TESEO', 'CUSTOMER')
ORDER BY LAST_ALTERED DESC;
-- Resultado esperado: datos actualizandose normalmente

-- Ver 2: Comparar volumen de datos capturados (antes vs despues)
-- Requiere acceso a HVR logs o metricas de integracion
SELECT
    INTEGRATION_NAME,
    BYTES_SENT,
    ROWS_SENT,
    EVENT_TIMESTAMP
FROM SNOWFLAKE.ACCOUNT_USAGE.COPY_HISTORY
WHERE TABLE_NAME IN (
    SELECT TABLE_NAME FROM INFORMATION_SCHEMA.TABLES
    WHERE TABLE_SCHEMA = 'HVR'
)
AND EVENT_TIMESTAMP >= DATEADD(DAY, -7, CURRENT_TIMESTAMP())
ORDER BY EVENT_TIMESTAMP DESC;
-- Resultado esperado: reduccion gradual de BYTES_SENT

-- Ver 3: Monitorizar latencia de replicacion
-- (desde HVR Console o tabla de monitoreo)
SELECT
    CHANNEL_NAME,
    TABLE_NAME,
    LATENCY_SECONDS,
    LAST_REFRESH
FROM PRO_0_STAGING_DB.HVR.REPLICATION_MONITOR
WHERE LAST_REFRESH >= DATEADD(HOUR, -24, CURRENT_TIMESTAMP())
ORDER BY LATENCY_SECONDS DESC;
-- Resultado esperado: latencia estable o mejorada

-- Ver 4: Verificar que tablas de auditoria siguen capturando before/after
SELECT
    TABLE_NAME,
    NOBEFOREUPDATE,
    EXCLUSION_REASON
FROM PRO_0_STAGING_DB.HVR.CAPTURE_CONFIG
WHERE NOBEFOREUPDATE = FALSE;
-- Resultado esperado: tablas de auditoria correctamente excluidas

-- Ver 5: Analizar reduccion de creditos de compute
SELECT
    DATE_TRUNC('DAY', START_TIME) AS DAY,
    SUM(CREDITS_USED) AS DAILY_CREDITS
FROM SNOWFLAKE.ACCOUNT_USAGE.WAREHOUSE_METERING_HISTORY
WHERE WAREHOUSE_NAME IN ('HVR_LOAD_WH', 'HVR_REPLICATE_WH')
    AND START_TIME >= DATEADD(DAY, -14, CURRENT_TIMESTAMP())
GROUP BY DAY
ORDER BY DAY;
-- Resultado esperado: tendencia descendente post-implementacion
```

### 2.2.4 Riesgos

| # | Riesgo | Probabilidad | Impacto | Mitigacion |
|---|--------|-------------|---------|------------|
| R1 | Perdida de capacidad de auditoria para updates | Bajo | Alto | Excluir explicitamente tablas con requisito de auditoria; documentar exclusiones |
| R2 | Incompatibilidad con procesos downstream que usan "before" | Medio | Medio | Inventariar consumidores de datos HVR; verificar que ninguno usa columnas _before |
| R3 | Error de configuracion en HVR que afecte replicacion | Bajo | Alto | Testing en entorno de desarrollo primero; monitoreo post-cambio 24h |
| R4 | NoBeforeUpdate no aplica a ciertas operaciones (MERGE) | Bajo | Bajo | Verificar documentacion HVR para excepciones; testing con datos reales |

### 2.2.5 Rollback Procedure

```bash
# ROLLBACK - Restaurar captura Before/After en HVR

# Paso 1: Acceder al servidor HVR
ssh hvr-admin@hvr-server

# Paso 2: Restaurar configuracion anterior
cd /opt/hvr/channels/hvr_staging/

# Opcion A: Restaurar desde backup de configuracion
cp hvr.cfg.backup hvr.cfg

# Opcion B: Desactivar NoBeforeUpdate manualmente
vi hvr.cfg
# Cambiar: <no_before_update>false</no_before_update>

# Paso 3: Recargar configuracion
hvrcli -c hvr_staging reload

# Paso 4: Verificar que el cambio se aplico
hvrcli -c hvr_staging show-config | grep -i before
# Resultado esperado: no_before_update=false o ausente

# Paso 5: Forzar refresh completo de tablas afectadas
hvrcli -c hvr_staging refresh-table PARCEL
hvrcli -c hvr_staging refresh-table TESEO
```

```sql
-- Paso 6: Actualizar tabla de configuracion en Snowflake
UPDATE PRO_0_STAGING_DB.HVR.CAPTURE_CONFIG
SET NOBEFOREUPDATE = FALSE,
    EXCLUSION_REASON = 'ROLLBACK - Restaurado Before/After'
WHERE NOBEFOREUPDATE = TRUE;

-- Paso 7: Verificar
SELECT * FROM PRO_0_STAGING_DB.HVR.CAPTURE_CONFIG;
```

### 2.2.6 Tiempo Estimado

| Subtarea | Tiempo |
|----------|--------|
| Analisis de tablas candidatas y exclusiones | 2h |
| Configuracion en HVR Console/CLI | 2h |
| Testing en entorno de desarrollo | 4h |
| Despliegue en produccion | 1h |
| Monitorizacion post-cambio (48h) | 4h |
| **TOTAL** | **13h (~2 dias)** |

---

## ACCION 2.3 - OPTIMIZAR QUERIES ANALITICAS DE ES_STRATOR_BO_L1

### 2.3.1 Descripcion Tecnica

Las queries analiticas ejecutadas por el usuario ADRIANLOPEZ en el esquema
ES_STRATOR_BO_L1 consumen ~600 segundos cada una. Estas queries realizan
multiples JOINs sobre tablas de 27GB+ sin optimizacion de clustering ni
vistas materializadas.

**Problema:**
- Queries de 600s consumen ~10 creditos cada una (X-Large warehouse)
- Multiples JOINs sobre tablas grandes sin clustering keys
- Ejecucion frecuente de las mismas queries sin cache
- Escaneo completo de tablas (full table scan) en cada ejecucion

**Solucion:**
1. Crear vistas materializadas para los JOINs mas frecuentes
2. Implementar clustering keys en tablas grandes
3. Crear tablas de agregacion pre-computadas
4. Optimizar warehouse para queries analiticas

**Impacto:**
- Reduccion de tiempo de query: 600s -> 30-60s (90% reduccion)
- Ahorro estimado: ~400 creditos/mes
- Mejora de experiencia de usuario para analistas

### 2.3.2 Pasos de Implementacion

**PASO 1: Analizar queries problematicas**

```sql
-- Identificar las queries mas costosas de ADRIANLOPEZ
USE ROLE ACCOUNTADMIN;

SELECT
    QUERY_ID,
    USER_NAME,
    WAREHOUSE_NAME,
    TOTAL_ELAPSED_TIME / 1000 AS DURATION_SECONDS,
    BYTES_SCANNED / POWER(1024, 3) AS SCANNED_GB,
    ROWS_PRODUCED,
    QUERY_TEXT
FROM SNOWFLAKE.ACCOUNT_USAGE.QUERY_HISTORY
WHERE USER_NAME = 'ADRIANLOPEZ'
    AND TOTAL_ELAPSED_TIME > 300000  -- > 5 minutos
    AND START_TIME >= DATEADD(DAY, -30, CURRENT_TIMESTAMP())
ORDER BY TOTAL_ELAPSED_TIME DESC
LIMIT 20;

-- Identificar tablas mas escaneadas
SELECT
    VALUE:"objectName"::STRING AS TABLE_NAME,
    COUNT(*) AS SCAN_COUNT,
    SUM(BYTES_SCANNED) / POWER(1024, 3) AS TOTAL_SCANNED_GB
FROM SNOWFLAKE.ACCOUNT_USAGE.QUERY_HISTORY,
LATERAL FLATTEN(INPUT => DIRECT_OBJECTS_ACCESSED)
WHERE USER_NAME = 'ADRIANLOPEZ'
    AND START_TIME >= DATEADD(DAY, -30, CURRENT_TIMESTAMP())
GROUP BY TABLE_NAME
ORDER BY TOTAL_SCANNED_GB DESC;
```

**PASO 2: Analizar estructura de tablas grandes**

```sql
-- Obtener DDL de tablas grandes en ES_STRATOR_BO_L1
SELECT GET_DDL('TABLE', 'ES_STRATOR_BO_L1.ANALYTICS.FACT_TRANSACTIONS');
SELECT GET_DDL('TABLE', 'ES_STRATOR_BO_L1.ANALYTICS.DIM_CUSTOMER');
SELECT GET_DDL('TABLE', 'ES_STRATOR_BO_L1.ANALYTICS.DIM_PRODUCT');

-- Verificar clustering actual
SHOW TABLES IN SCHEMA ES_STRATOR_BO_L1.ANALYTICS;

-- Obtener estadisticas de micro-partitions
SELECT
    TABLE_NAME,
    BYTES / POWER(1024, 3) AS SIZE_GB,
    ROW_COUNT,
    CLUSTERING_KEY,
    AVERAGE_OVERLAP,
    AVERAGE_DEPTH
FROM INFORMATION_SCHEMA.TABLES
WHERE TABLE_SCHEMA = 'ANALYTICS'
ORDER BY BYTES DESC;
```

**PASO 3: Implementar clustering keys en tablas grandes**

```sql
-- Clustering key para FACT_TRANSACTIONS (por fecha y customer_id)
-- Justificacion: la mayoria de queries filtran por rango de fecha
ALTER TABLE ES_STRATOR_BO_L1.ANALYTICS.FACT_TRANSACTIONS
CLUSTER BY (TRANSACTION_DATE, CUSTOMER_ID);

-- Clustering key para DIM_CUSTOMER (por region y segmento)
ALTER TABLE ES_STRATOR_BO_L1.ANALYTICS.DIM_CUSTOMER
CLUSTER BY (REGION, CUSTOMER_SEGMENT);

-- Clustering key para DIM_PRODUCT (por categoria)
ALTER TABLE ES_STRATOR_BO_L1.ANALYTICS.DIM_PRODUCT
CLUSTER BY (PRODUCT_CATEGORY, BRAND);

-- Verificar que el clustering se aplico
SHOW TABLES IN SCHEMA ES_STRATOR_BO_L1.ANALYTICS;
-- Verificar columna CLUSTERING_KEY
```

**PASO 4: Crear vistas materializadas para JOINs frecuentes**

```sql
-- Vista materializada: Customer Transactions Summary
-- Basado en el patron de query mas frecuente de ADRIANLOPEZ
CREATE MATERIALIZED VIEW ES_STRATOR_BO_L1.ANALYTICS.MV_CUSTOMER_TRANSACTIONS AS
SELECT
    t.TRANSACTION_DATE,
    t.CUSTOMER_ID,
    c.CUSTOMER_NAME,
    c.REGION,
    c.CUSTOMER_SEGMENT,
    p.PRODUCT_CATEGORY,
    p.BRAND,
    COUNT(*) AS TRANSACTION_COUNT,
    SUM(t.AMOUNT) AS TOTAL_AMOUNT,
    AVG(t.AMOUNT) AS AVG_AMOUNT
FROM ES_STRATOR_BO_L1.ANALYTICS.FACT_TRANSACTIONS t
JOIN ES_STRATOR_BO_L1.ANALYTICS.DIM_CUSTOMER c
    ON t.CUSTOMER_ID = c.CUSTOMER_ID
JOIN ES_STRATOR_BO_L1.ANALYTICS.DIM_PRODUCT p
    ON t.PRODUCT_ID = p.PRODUCT_ID
GROUP BY
    t.TRANSACTION_DATE,
    t.CUSTOMER_ID,
    c.CUSTOMER_NAME,
    c.REGION,
    c.CUSTOMER_SEGMENT,
    p.PRODUCT_CATEGORY,
    p.BRAND;

-- Vista materializada: Monthly Sales Summary
CREATE MATERIALIZED VIEW ES_STRATOR_BO_L1.ANALYTICS.MV_MONTHLY_SALES AS
SELECT
    DATE_TRUNC('MONTH', t.TRANSACTION_DATE) AS MONTH,
    c.REGION,
    p.PRODUCT_CATEGORY,
    COUNT(*) AS TRANSACTION_COUNT,
    SUM(t.AMOUNT) AS TOTAL_REVENUE,
    COUNT(DISTINCT t.CUSTOMER_ID) AS UNIQUE_CUSTOMERS
FROM ES_STRATOR_BO_L1.ANALYTICS.FACT_TRANSACTIONS t
JOIN ES_STRATOR_BO_L1.ANALYTICS.DIM_CUSTOMER c
    ON t.CUSTOMER_ID = c.CUSTOMER_ID
JOIN ES_STRATOR_BO_L1.ANALYTICS.DIM_PRODUCT p
    ON t.PRODUCT_ID = p.PRODUCT_ID
GROUP BY
    DATE_TRUNC('MONTH', t.TRANSACTION_DATE),
    c.REGION,
    p.PRODUCT_CATEGORY;

-- Vista materializada: Top Products
CREATE MATERIALIZED VIEW ES_STRATOR_BO_L1.ANALYTICS.MV_TOP_PRODUCTS AS
SELECT
    t.PRODUCT_ID,
    p.PRODUCT_NAME,
    p.PRODUCT_CATEGORY,
    p.BRAND,
    COUNT(*) AS SALES_COUNT,
    SUM(t.AMOUNT) AS TOTAL_REVENUE,
    RANK() OVER (ORDER BY SUM(t.AMOUNT) DESC) AS REVENUE_RANK
FROM ES_STRATOR_BO_L1.ANALYTICS.FACT_TRANSACTIONS t
JOIN ES_STRATOR_BO_L1.ANALYTICS.DIM_PRODUCT p
    ON t.PRODUCT_ID = p.PRODUCT_ID
WHERE t.TRANSACTION_DATE >= DATEADD(MONTH, -12, CURRENT_DATE())
GROUP BY
    t.PRODUCT_ID,
    p.PRODUCT_NAME,
    p.PRODUCT_CATEGORY,
    p.BRAND;
```

**PASO 5: Crear tablas de agregacion pre-computadas**

```sql
-- Tabla de agregacion diaria (refreshed via task)
CREATE TABLE ES_STRATOR_BO_L1.ANALYTICS.DAILY_SALES_AGG AS
SELECT
    TRANSACTION_DATE,
    REGION,
    PRODUCT_CATEGORY,
    COUNT(*) AS TRANSACTION_COUNT,
    SUM(AMOUNT) AS TOTAL_REVENUE,
    COUNT(DISTINCT CUSTOMER_ID) AS UNIQUE_CUSTOMERS
FROM ES_STRATOR_BO_L1.ANALYTICS.FACT_TRANSACTIONS t
JOIN ES_STRATOR_BO_L1.ANALYTICS.DIM_CUSTOMER c
    ON t.CUSTOMER_ID = c.CUSTOMER_ID
JOIN ES_STRATOR_BO_L1.ANALYTICS.DIM_PRODUCT p
    ON t.PRODUCT_ID = p.PRODUCT_ID
GROUP BY
    TRANSACTION_DATE,
    REGION,
    PRODUCT_CATEGORY;

-- Task para refrescar agregacion diaria
CREATE OR REPLACE TASK ES_STRATOR_BO_L1.ANALYTICS.REFRESH_DAILY_AGG
    WAREHOUSE = ANALYTICS_WH
    SCHEDULE = 'USING CRON 0 6 * * * UTC'  -- 06:00 UTC diario
AS
    -- Truncar y cargar datos del dia anterior
    DELETE FROM ES_STRATOR_BO_L1.ANALYTICS.DAILY_SALES_AGG
    WHERE TRANSACTION_DATE = DATEADD(DAY, -1, CURRENT_DATE());

    INSERT INTO ES_STRATOR_BO_L1.ANALYTICS.DAILY_SALES_AGG
    SELECT
        TRANSACTION_DATE,
        REGION,
        PRODUCT_CATEGORY,
        COUNT(*) AS TRANSACTION_COUNT,
        SUM(AMOUNT) AS TOTAL_REVENUE,
        COUNT(DISTINCT CUSTOMER_ID) AS UNIQUE_CUSTOMERS
    FROM ES_STRATOR_BO_L1.ANALYTICS.FACT_TRANSACTIONS t
    JOIN ES_STRATOR_BO_L1.ANALYTICS.DIM_CUSTOMER c
        ON t.CUSTOMER_ID = c.CUSTOMER_ID
    JOIN ES_STRATOR_BO_L1.ANALYTICS.DIM_PRODUCT p
        ON t.PRODUCT_ID = p.PRODUCT_ID
    WHERE TRANSACTION_DATE = DATEADD(DAY, -1, CURRENT_DATE())
    GROUP BY
        TRANSACTION_DATE,
        REGION,
        PRODUCT_CATEGORY;

-- Activar task
ALTER TASK ES_STRATOR_BO_L1.ANALYTICS.REFRESH_DAILY_AGG RESUME;
```

**PASO 6: Optimizar warehouse para queries analiticas**

```sql
-- Crear warehouse dedicado para analitica (si no existe)
CREATE WAREHOUSE IF NOT EXISTS ANALYTICS_WH
    WITH WAREHOUSE_SIZE = 'LARGE'
    AUTO_SUSPEND = 300
    AUTO_RESUME = TRUE
    MIN_CLUSTER_COUNT = 1
    MAX_CLUSTER_COUNT = 3
    SCALING_POLICY = 'STANDARD'
    COMMENT = 'Warehouse optimizado para queries analiticas de ES_STRATOR_BO_L1';

-- Configurar resource monitor para evitar costes excesivos
CREATE RESOURCE MONITOR ANALYTICS_MONITOR
    WITH CREDIT_QUOTA = 500
    FREQUENCY = MONTHLY
    START_TIMESTAMP = 'IMMEDIATELY'
    TRIGGERS
        ON 75 PERCENT DO NOTIFY
        ON 90 PERCENT DO SUSPEND_IMMEDIATE
        ON 100 PERCENT DO SUSPEND;

-- Asignar resource monitor al warehouse
ALTER WAREHOUSE ANALYTICS_WH SET RESOURCE_MONITOR = ANALYTICS_MONITOR;
```

**PASO 7: Crear guia de queries optimizadas para ADRIANLOPEZ**

```sql
-- Ejemplo de query optimizada usando vistas materializadas

-- ANTES (query original ~600s):
/*
SELECT
    t.TRANSACTION_DATE,
    c.REGION,
    p.PRODUCT_CATEGORY,
    COUNT(*) AS TRANSACTIONS,
    SUM(t.AMOUNT) AS REVENUE
FROM FACT_TRANSACTIONS t
JOIN DIM_CUSTOMER c ON t.CUSTOMER_ID = c.CUSTOMER_ID
JOIN DIM_PRODUCT p ON t.PRODUCT_ID = p.PRODUCT_ID
WHERE t.TRANSACTION_DATE BETWEEN '2025-01-01' AND '2025-12-31'
GROUP BY t.TRANSACTION_DATE, c.REGION, p.PRODUCT_CATEGORY
ORDER BY REVENUE DESC;
*/

-- DESPUES (query optimizada ~30-60s):
SELECT
    TRANSACTION_DATE,
    REGION,
    PRODUCT_CATEGORY,
    TRANSACTION_COUNT AS TRANSACTIONS,
    TOTAL_AMOUNT AS REVENUE
FROM ES_STRATOR_BO_L1.ANALYTICS.MV_CUSTOMER_TRANSACTIONS
WHERE TRANSACTION_DATE BETWEEN '2025-01-01' AND '2025-12-31'
ORDER BY REVENUE DESC;
```

### 2.3.3 Verificacion Post-Implementacion

```sql
-- Ver 1: Verificar que las vistas materializadas existen y tienen datos
SELECT
    TABLE_NAME,
    BYTES / POWER(1024, 2) AS SIZE_MB,
    ROW_COUNT,
    LAST_ALTERED
FROM INFORMATION_SCHEMA.TABLES
WHERE TABLE_SCHEMA = 'ANALYTICS'
    AND TABLE_NAME LIKE 'MV_%'
ORDER BY TABLE_NAME;
-- Resultado esperado: vistas con datos y LAST_ALTERED reciente

-- Ver 2: Comparar tiempo de query antes y despues
-- Ejecutar query optimizada y medir tiempo
SELECT
    TRANSACTION_DATE,
    REGION,
    PRODUCT_CATEGORY,
    TRANSACTION_COUNT,
    TOTAL_AMOUNT
FROM ES_STRATOR_BO_L1.ANALYTICS.MV_CUSTOMER_TRANSACTIONS
WHERE TRANSACTION_DATE >= DATEADD(MONTH, -3, CURRENT_DATE())
ORDER BY TOTAL_AMOUNT DESC
LIMIT 100;
-- Resultado esperado: < 60 segundos

-- Ver 3: Verificar clustering efectividad
SELECT
    TABLE_NAME,
    CLUSTERING_KEY,
    AVERAGE_OVERLAP,
    AVERAGE_DEPTH
FROM INFORMATION_SCHEMA.TABLES
WHERE TABLE_SCHEMA = 'ANALYTICS'
    AND TABLE_NAME LIKE 'FACT_%';
-- Resultado esperado: AVERAGE_OVERLAP < 5, AVERAGE_DEPTH < 4

-- Ver 4: Monitorizar uso de vistas materializadas
SELECT
    QUERY_ID,
    USER_NAME,
    TOTAL_ELAPSED_TIME / 1000 AS DURATION_SECONDS,
    PARTITIONS_SCANNED,
    PARTITIONS_TOTAL
FROM SNOWFLAKE.ACCOUNT_USAGE.QUERY_HISTORY
WHERE USER_NAME = 'ADRIANLOPEZ'
    AND QUERY_TEXT LIKE '%MV_%'
    AND START_TIME >= DATEADD(DAY, -7, CURRENT_TIMESTAMP())
ORDER BY START_TIME DESC;
-- Resultado esperado: queries mas rapidas, menos particiones escaneadas

-- Ver 5: Verificar que el task de refresh funciona
SELECT
    NAME,
    STATE,
    LAST_FUTURE_SCHEDULED_TIME,
    COMPLETED_TIME,
    ERROR_CODE,
    ERROR_MESSAGE
FROM TABLE(INFORMATION_SCHEMA.TASK_HISTORY())
WHERE NAME = 'REFRESH_DAILY_AGG'
ORDER BY COMPLETED_TIME DESC
LIMIT 5;
-- Resultado esperado: STATE = 'SCHEDULED', ejecuciones exitosas

-- Ver 6: Medir reduccion de creditos
SELECT
    DATE_TRUNC('DAY', START_TIME) AS DAY,
    SUM(CREDITS_USED) AS DAILY_CREDITS,
    COUNT(DISTINCT QUERY_ID) AS QUERY_COUNT
FROM SNOWFLAKE.ACCOUNT_USAGE.WAREHOUSE_METERING_HISTORY
WHERE WAREHOUSE_NAME = 'ANALYTICS_WH'
    AND START_TIME >= DATEADD(DAY, -14, CURRENT_TIMESTAMP())
GROUP BY DAY
ORDER BY DAY;
-- Resultado esperado: reduccion post-implementacion

-- Ver 7: Verificar freshness de vistas materializadas
SELECT
    NAME,
    REFRESHED_ON,
    IS_CLUSTERING_ON
FROM TABLE(INFORMATION_SCHEMA.MATERIALIZED_VIEWS())
WHERE SCHEMA_NAME = 'ANALYTICS';
-- Resultado esperado: REFRESHED_ON reciente
```

### 2.3.4 Riesgos

| # | Riesgo | Probabilidad | Impacto | Mitigacion |
|---|--------|-------------|---------|------------|
| R1 | Vistas materializadas consumen storage adicional | Medio | Bajo | Monitorizar storage; el coste de storage es ~10x menor que compute |
| R2 | Clustering keys no mejoran rendimiento si distribucion es uniforme | Medio | Medio | Analizar distribucion de datos antes de elegir keys; testing A/B |
| R3 | Task de refresh falla y datos quedan desactualizados | Bajo | Medio | Alertas de fallo en task; fallback a query original |
| R4 | ADRIANLOPEZ no adopta las vistas materializadas | Medio | Alto | Sesion de training; documentacion de queries optimizadas; soporte directo |
| R5 | Warehouse scaling causa costes inesperados | Bajo | Medio | Resource monitor con limites; alertas al 75% del budget |
| R6 | Vistas materializadas aumentan tiempo de carga HVR | Bajo | Bajo | Programar refresh fuera de ventana de carga HVR |

### 2.3.5 Rollback Procedure

```sql
-- ROLLBACK - Eliminar optimizaciones de queries analiticas

-- Paso 1: Eliminar vistas materializadas
DROP MATERIALIZED VIEW IF EXISTS ES_STRATOR_BO_L1.ANALYTICS.MV_CUSTOMER_TRANSACTIONS;
DROP MATERIALIZED VIEW IF EXISTS ES_STRATOR_BO_L1.ANALYTICS.MV_MONTHLY_SALES;
DROP MATERIALIZED VIEW IF EXISTS ES_STRATOR_BO_L1.ANALYTICS.MV_TOP_PRODUCTS;

-- Paso 2: Eliminar tabla de agregacion y task
DROP TASK IF EXISTS ES_STRATOR_BO_L1.ANALYTICS.REFRESH_DAILY_AGG;
DROP TABLE IF EXISTS ES_STRATOR_BO_L1.ANALYTICS.DAILY_SALES_AGG;

-- Paso 3: Eliminar clustering keys (volver a estado sin clustering)
ALTER TABLE ES_STRATOR_BO_L1.ANALYTICS.FACT_TRANSACTIONS DROP CLUSTERING KEY;
ALTER TABLE ES_STRATOR_BO_L1.ANALYTICS.DIM_CUSTOMER DROP CLUSTERING KEY;
ALTER TABLE ES_STRATOR_BO_L1.ANALYTICS.DIM_PRODUCT DROP CLUSTERING KEY;

-- Paso 4: Eliminar warehouse dedicado (si se creo solo para esto)
-- ALTER WAREHOUSE ANALYTICS_WH SUSPEND;
-- DROP WAREHOUSE IF EXISTS ANALYTICS_WH;

-- Paso 5: Eliminar resource monitor
-- DROP RESOURCE MONITOR IF EXISTS ANALYTICS_MONITOR;

-- Paso 6: Verificar rollback
SELECT TABLE_NAME, CLUSTERING_KEY
FROM INFORMATION_SCHEMA.TABLES
WHERE TABLE_SCHEMA = 'ANALYTICS';
-- Resultado esperado: CLUSTERING_KEY = NULL

SELECT TABLE_NAME
FROM INFORMATION_SCHEMA.TABLES
WHERE TABLE_SCHEMA = 'ANALYTICS'
    AND TABLE_NAME LIKE 'MV_%';
-- Resultado esperado: 0 filas
```

### 2.3.6 Tiempo Estimado

| Subtarea | Tiempo |
|----------|--------|
| Analisis de queries problematicas | 4h |
| Diseno de clustering keys | 4h |
| Implementacion clustering keys | 2h |
| Creacion vistas materializadas | 6h |
| Creacion tablas de agregacion y tasks | 4h |
| Testing de rendimiento (antes vs despues) | 4h |
| Documentacion y training para ADRIANLOPEZ | 2h |
| Monitorizacion post-implementacion (5 dias) | 6h |
| **TOTAL** | **32h (~5 dias)** |

---

## ACCION 2.4 - REDUCIR RETENCION DE TABLAS HISTORY DE SALESFORCE

### 2.4.1 Descripcion Tecnica

Las tablas *_HISTORY de Salesforce almacenan el historico de cambios para
cada registro (similar a SCD Type 2). Actualmente estas tablas retienen
30 dias de historico, pero el negocio solo requiere 7 dias para analisis
y auditoria.

**Problema:**
- Tablas *_HISTORY acumulan datos innecesariamente
- 30 dias de historico vs 7 dias necesarios = 4.3x mas storage del necesario
- Estas tablas crecen rapidamente por la naturaleza de Salesforce (cada
  cambio de campo genera un registro)

**Solucion:**
1. Reducir retencion de 30 a 7 dias
2. Implementar task de purga automatica
3. Crear tabla de archivado opcional para datos > 7 dias (si se requiere)

**Impacto:**
- Reduccion de ~75% en storage de tablas HISTORY
- Ahorro estimado: ~200 creditos/mes
- Mejora en rendimiento de queries sobre tablas HISTORY

**Tablas tipicas afectadas:**
- ACCOUNT_HISTORY
- CONTACT_HISTORY
- OPPORTUNITY_HISTORY
- LEAD_HISTORY
- CASE_HISTORY

### 2.4.2 Pasos de Implementacion

**PASO 1: Identificar tablas HISTORY y su tamano actual**

```sql
-- Listar todas las tablas HISTORY en la base de datos
USE DATABASE ES_COVADONGA;

SELECT
    TABLE_SCHEMA,
    TABLE_NAME,
    BYTES / POWER(1024, 3) AS SIZE_GB,
    ROW_COUNT,
    CREATED,
    LAST_ALTERED
FROM INFORMATION_SCHEMA.TABLES
WHERE TABLE_NAME LIKE '%_HISTORY'
    AND TABLE_TYPE = 'BASE TABLE'
ORDER BY BYTES DESC;

-- Estimar datos por rango de fecha (asumiendo columna HISTORY_DATE o similar)
SELECT
    DATE_TRUNC('DAY', HISTORY_DATE) AS HISTORY_DAY,
    COUNT(*) AS ROW_COUNT,
    COUNT(*) * AVG(BYTES) / POWER(1024, 2) AS ESTIMATED_SIZE_MB
FROM ES_COVADONGA.SALESFORCE.ACCOUNT_HISTORY
WHERE HISTORY_DATE >= DATEADD(DAY, -30, CURRENT_DATE())
GROUP BY HISTORY_DAY
ORDER BY HISTORY_DAY;
```

**PASO 2: Verificar requisitos de retencion con negocio**

```sql
-- Documentar requisitos de retencion
CREATE TABLE IF NOT EXISTS ES_COVADONGA.SALESFORCE.RETENTION_POLICY (
    TABLE_NAME       STRING PRIMARY KEY,
    CURRENT_RETENTION_DAYS INTEGER,
    TARGET_RETENTION_DAYS  INTEGER,
    BUSINESS_REASON  STRING,
    APPROVED_BY      STRING,
    APPROVED_DATE    TIMESTAMP_NTZ
);

-- Insertar politicas de retencion
INSERT INTO ES_COVADONGA.SALESFORCE.RETENTION_POLICY VALUES
    ('ACCOUNT_HISTORY', 30, 7, 'Analisis de cambios recientes', 'ADRIANLOPEZ', CURRENT_TIMESTAMP()),
    ('CONTACT_HISTORY', 30, 7, 'Analisis de cambios recientes', 'ADRIANLOPEZ', CURRENT_TIMESTAMP()),
    ('OPPORTUNITY_HISTORY', 30, 7, 'Pipeline analysis', 'ADRIANLOPEZ', CURRENT_TIMESTAMP()),
    ('LEAD_HISTORY', 30, 7, 'Conversion tracking', 'ADRIANLOPEZ', CURRENT_TIMESTAMP()),
    ('CASE_HISTORY', 30, 7, 'Support analysis', 'ADRIANLOPEZ', CURRENT_TIMESTAMP());

-- Verificar
SELECT * FROM ES_COVADONGA.SALESFORCE.RETENTION_POLICY;
```

**PASO 3: Crear tabla de archivado (opcional, para compliance)**

```sql
-- Crear esquema de archivado
CREATE SCHEMA IF NOT EXISTS ES_COVADONGA.SALESFORCE_ARCHIVE;

-- Crear tablas de archivado con misma estructura
CREATE TABLE ES_COVADONGA.SALESFORCE_ARCHIVE.ACCOUNT_HISTORY
    LIKE ES_COVADONGA.SALESFORCE.ACCOUNT_HISTORY;

CREATE TABLE ES_COVADONGA.SALESFORCE_ARCHIVE.CONTACT_HISTORY
    LIKE ES_COVADONGA.SALESFORCE.CONTACT_HISTORY;

CREATE TABLE ES_COVADONGA.SALESFORCE_ARCHIVE.OPPORTUNITY_HISTORY
    LIKE ES_COVADONGA.SALESFORCE.OPPORTUNITY_HISTORY;

-- Verificar
SHOW TABLES IN SCHEMA ES_COVADONGA.SALESFORCE_ARCHIVE;
```

**PASO 4: Crear stored procedure de purga**

```sql
-- Procedimiento de purga para una tabla HISTORY
CREATE OR REPLACE PROCEDURE ES_COVADONGA.SALESFORCE.SP_PURGE_HISTORY(
    TABLE_NAME STRING,
    RETENTION_DAYS INTEGER
)
RETURNS STRING
LANGUAGE SQL
EXECUTE AS CALLER
COMMENT = 'Purga registros antiguos de tablas HISTORY y opcionalmente archiva'
AS
$$
DECLARE
    rows_archived INTEGER DEFAULT 0;
    rows_deleted INTEGER DEFAULT 0;
    cutoff_date DATE;
    archive_table STRING;
BEGIN
    cutoff_date := DATEADD(DAY, -RETENTION_DAYS, CURRENT_DATE());
    archive_table := 'ES_COVADONGA.SALESFORCE_ARCHIVE.' || TABLE_NAME;

    -- Archivar datos antiguos (si existe tabla de archivo)
    IF (EXISTS (
        SELECT 1 FROM INFORMATION_SCHEMA.TABLES
        WHERE TABLE_SCHEMA = 'SALESFORCE_ARCHIVE'
            AND TABLE_NAME = :TABLE_NAME
    )) THEN
        EXECUTE IMMEDIATE
            'INSERT INTO ' || :archive_table ||
            ' SELECT * FROM ES_COVADONGA.SALESFORCE.' || :TABLE_NAME ||
            ' WHERE HISTORY_DATE < ''' || :cutoff_date || '''';

        GET DIAGNOSTICS rows_archived := ROW_COUNT;
    END IF;

    -- Eliminar datos antiguos de la tabla principal
    EXECUTE IMMEDIATE
        'DELETE FROM ES_COVADONGA.SALESFORCE.' || :TABLE_NAME ||
        ' WHERE HISTORY_DATE < ''' || :cutoff_date || '''';

    GET DIAGNOSTICS rows_deleted := ROW_COUNT;

    -- Log de purga
    INSERT INTO ES_COVADONGA.SALESFORCE.PURGE_LOG (
        TABLE_NAME, CUTOFF_DATE, ROWS_ARCHIVED, ROWS_DELETED, EXECUTED_AT
    ) VALUES (
        :TABLE_NAME, :cutoff_date, :rows_archived, :rows_deleted, CURRENT_TIMESTAMP()
    );

    RETURN :TABLE_NAME || ': archived=' || :rows_archived ||
           ', deleted=' || :rows_deleted;
END;
$$;

-- Crear tabla de log de purga
CREATE TABLE IF NOT EXISTS ES_COVADONGA.SALESFORCE.PURGE_LOG (
    TABLE_NAME       STRING,
    CUTOFF_DATE      DATE,
    ROWS_ARCHIVED    INTEGER,
    ROWS_DELETED     INTEGER,
    EXECUTED_AT      TIMESTAMP_NTZ DEFAULT CURRENT_TIMESTAMP(),
    EXECUTED_BY      STRING DEFAULT CURRENT_USER()
);
```

**PASO 5: Crear tasks de purga automatica**

```sql
-- Task de purga para ACCOUNT_HISTORY
CREATE OR REPLACE TASK ES_COVADONGA.SALESFORCE.PURGE_ACCOUNT_HISTORY
    WAREHOUSE = SALESFORCE_WH
    SCHEDULE = 'USING CRON 0 4 * * * UTC'  -- 04:00 UTC diario
    COMMENT = 'Purga ACCOUNT_HISTORY > 7 dias'
AS
    CALL ES_COVADONGA.SALESFORCE.SP_PURGE_HISTORY('ACCOUNT_HISTORY', 7);

-- Task de purga para CONTACT_HISTORY
CREATE OR REPLACE TASK ES_COVADONGA.SALESFORCE.PURGE_CONTACT_HISTORY
    WAREHOUSE = SALESFORCE_WH
    SCHEDULE = 'USING CRON 0 4 * * * UTC'
    COMMENT = 'Purga CONTACT_HISTORY > 7 dias'
AS
    CALL ES_COVADONGA.SALESFORCE.SP_PURGE_HISTORY('CONTACT_HISTORY', 7);

-- Task de purga para OPPORTUNITY_HISTORY
CREATE OR REPLACE TASK ES_COVADONGA.SALESFORCE.PURGE_OPPORTUNITY_HISTORY
    WAREHOUSE = SALESFORCE_WH
    SCHEDULE = 'USING CRON 0 4 * * * UTC'
    COMMENT = 'Purga OPPORTUNITY_HISTORY > 7 dias'
AS
    CALL ES_COVADONGA.SALESFORCE.SP_PURGE_HISTORY('OPPORTUNITY_HISTORY', 7);

-- Task de purga para LEAD_HISTORY
CREATE OR REPLACE TASK ES_COVADONGA.SALESFORCE.PURGE_LEAD_HISTORY
    WAREHOUSE = SALESFORCE_WH
    SCHEDULE = 'USING CRON 0 4 * * * UTC'
    COMMENT = 'Purga LEAD_HISTORY > 7 dias'
AS
    CALL ES_COVADONGA.SALESFORCE.SP_PURGE_HISTORY('LEAD_HISTORY', 7);

-- Activar tasks
ALTER TASK ES_COVADONGA.SALESFORCE.PURGE_ACCOUNT_HISTORY RESUME;
ALTER TASK ES_COVADONGA.SALESFORCE.PURGE_CONTACT_HISTORY RESUME;
ALTER TASK ES_COVADONGA.SALESFORCE.PURGE_OPPORTUNITY_HISTORY RESUME;
ALTER TASK ES_COVADONGA.SALESFORCE.PURGE_LEAD_HISTORY RESUME;

-- Verificar tasks activos
SHOW TASKS IN SCHEMA ES_COVADONGA.SALESFORCE;
```

**PASO 6: Ejecutar purga inicial (one-time)**

```sql
-- Purga inicial para limpiar datos > 7 dias acumulados
-- Ejecutar durante ventana de mantenimiento

-- Purgar ACCOUNT_HISTORY
CALL ES_COVADONGA.SALESFORCE.SP_PURGE_HISTORY('ACCOUNT_HISTORY', 7);

-- Purgar CONTACT_HISTORY
CALL ES_COVADONGA.SALESFORCE.SP_PURGE_HISTORY('CONTACT_HISTORY', 7);

-- Purgar OPPORTUNITY_HISTORY
CALL ES_COVADONGA.SALESFORCE.SP_PURGE_HISTORY('OPPORTUNITY_HISTORY', 7);

-- Purgar LEAD_HISTORY
CALL ES_COVADONGA.SALESFORCE.SP_PURGE_HISTORY('LEAD_HISTORY', 7);

-- Verificar resultados
SELECT * FROM ES_COVADONGA.SALESFORCE.PURGE_LOG
ORDER BY EXECUTED_AT DESC;
```

### 2.4.3 Verificacion Post-Implementacion

```sql
-- Ver 1: Verificar reduccion de tamano en tablas HISTORY
SELECT
    TABLE_NAME,
    BYTES / POWER(1024, 3) AS SIZE_GB,
    ROW_COUNT,
    LAST_ALTERED
FROM INFORMATION_SCHEMA.TABLES
WHERE TABLE_NAME LIKE '%_HISTORY'
    AND TABLE_SCHEMA = 'SALESFORCE'
ORDER BY BYTES DESC;
-- Resultado esperado: reduccion significativa de SIZE_GB y ROW_COUNT

-- Ver 2: Verificar que solo hay datos de los ultimos 7 dias
SELECT
    TABLE_NAME,
    MIN(HISTORY_DATE) AS OLDEST_RECORD,
    MAX(HISTORY_DATE) AS NEWEST_RECORD,
    COUNT(*) AS ROW_COUNT
FROM (
    SELECT 'ACCOUNT_HISTORY' AS TABLE_NAME, HISTORY_DATE
    FROM ES_COVADONGA.SALESFORCE.ACCOUNT_HISTORY
    UNION ALL
    SELECT 'CONTACT_HISTORY', HISTORY_DATE
    FROM ES_COVADONGA.SALESFORCE.CONTACT_HISTORY
) sub
GROUP BY TABLE_NAME;
-- Resultado esperado: OLDEST_RECORD >= DATEADD(DAY, -7, CURRENT_DATE())

-- Ver 3: Verificar log de purga
SELECT
    TABLE_NAME,
    CUTOFF_DATE,
    ROWS_ARCHIVED,
    ROWS_DELETED,
    EXECUTED_AT
FROM ES_COVADONGA.SALESFORCE.PURGE_LOG
ORDER BY EXECUTED_AT DESC;
-- Resultado esperado: registros de purga con cantidades esperadas

-- Ver 4: Verificar que los tasks se ejecutan correctamente
SELECT
    NAME,
    STATE,
    SCHEDULE,
    COMPLETED_TIME,
    ERROR_CODE,
    ERROR_MESSAGE
FROM TABLE(INFORMATION_SCHEMA.TASK_HISTORY())
WHERE NAME LIKE 'PURGE_%'
ORDER BY COMPLETED_TIME DESC
LIMIT 10;
-- Resultado esperado: STATE = 'SCHEDULED', sin errores

-- Ver 5: Monitorizar storage semanal
SELECT
    USAGE_DATE,
    TABLE_NAME,
    AVERAGE_BYTES / POWER(1024, 3) AS AVG_SIZE_GB
FROM SNOWFLAKE.ACCOUNT_USAGE.TABLE_STORAGE_HISTORY
WHERE TABLE_NAME LIKE '%_HISTORY'
    AND TABLE_SCHEMA = 'SALESFORCE'
    AND USAGE_DATE >= DATEADD(DAY, -30, CURRENT_DATE())
ORDER BY TABLE_NAME, USAGE_DATE DESC;
-- Resultado esperado: tendencia descendente estable

-- Ver 6: Verificar datos archivados (si se habilito archivado)
SELECT
    TABLE_NAME,
    ROW_COUNT,
    BYTES / POWER(1024, 3) AS SIZE_GB
FROM INFORMATION_SCHEMA.TABLES
WHERE TABLE_SCHEMA = 'SALESFORCE_ARCHIVE'
ORDER BY BYTES DESC;
-- Resultado esperado: datos archivados disponibles para consulta

-- Ver 7: Verificar que HVR sigue replicando correctamente
SELECT
    TABLE_NAME,
    ROW_COUNT,
    LAST_ALTERED
FROM INFORMATION_SCHEMA.TABLES
WHERE TABLE_NAME LIKE '%_HISTORY'
    AND TABLE_SCHEMA = 'SALESFORCE'
ORDER BY LAST_ALTERED DESC;
-- Resultado esperado: datos actualizandose normalmente
```

### 2.4.4 Riesgos

| # | Riesgo | Probabilidad | Impacto | Mitigacion |
|---|--------|-------------|---------|------------|
| R1 | Necesidad de datos historicos > 7 dias para auditoria | Medio | Medio | Tabla de archivado opcional; proceso de recuperacion documentado |
| R2 | Task de purga falla y datos no se eliminan | Bajo | Bajo | Alertas de fallo; monitorizacion diaria; fallback manual |
| R3 | Impacto en queries que usan datos historicos | Medio | Medio | Notificar usuarios; documentar nueva ventana de retencion |
| R4 | Purga inicial masiva afecta rendimiento | Medio | Bajo | Ejecutar en ventana de mantenimiento; purgar en lotes |
| R5 | HVR re-carga datos purgados temporalmente | Bajo | Bajo | Coordinar ventana de purga con schedule de HVR |

### 2.4.5 Rollback Procedure

```sql
-- ROLLBACK - Restaurar retencion de 30 dias para tablas HISTORY

-- Paso 1: Detener tasks de purga
ALTER TASK ES_COVADONGA.SALESFORCE.PURGE_ACCOUNT_HISTORY SUSPEND;
ALTER TASK ES_COVADONGA.SALESFORCE.PURGE_CONTACT_HISTORY SUSPEND;
ALTER TASK ES_COVADONGA.SALESFORCE.PURGE_OPPORTUNITY_HISTORY SUSPEND;
ALTER TASK ES_COVADONGA.SALESFORCE.PURGE_LEAD_HISTORY SUSPEND;

-- Paso 2: Restaurar datos archivados (si se habilito archivado)
-- Restaurar ACCOUNT_HISTORY
INSERT INTO ES_COVADONGA.SALESFORCE.ACCOUNT_HISTORY
SELECT * FROM ES_COVADONGA.SALESFORCE_ARCHIVE.ACCOUNT_HISTORY;

-- Restaurar CONTACT_HISTORY
INSERT INTO ES_COVADONGA.SALESFORCE.CONTACT_HISTORY
SELECT * FROM ES_COVADONGA.SALESFORCE_ARCHIVE.CONTACT_HISTORY;

-- Restaurar OPPORTUNITY_HISTORY
INSERT INTO ES_COVADONGA.SALESFORCE.OPPORTUNITY_HISTORY
SELECT * FROM ES_COVADONGA.SALESFORCE_ARCHIVE.OPPORTUNITY_HISTORY;

-- Paso 3: Verificar restauracion
SELECT
    TABLE_NAME,
    ROW_COUNT,
    MIN(HISTORY_DATE) AS OLDEST_RECORD
FROM (
    SELECT 'ACCOUNT_HISTORY' AS TABLE_NAME, ROW_COUNT, HISTORY_DATE
    FROM ES_COVADONGA.SALESFORCE.ACCOUNT_HISTORY
) sub
GROUP BY TABLE_NAME;
-- Resultado esperado: datos de 30 dias restaurados

-- Paso 4: Actualizar politica de retencion
UPDATE ES_COVADONGA.SALESFORCE.RETENTION_POLICY
SET TARGET_RETENTION_DAYS = 30,
    BUSINESS_REASON = 'ROLLBACK - Restaurado a 30 dias';

-- Paso 5: Eliminar tasks de purga (opcional)
-- DROP TASK IF EXISTS ES_COVADONGA.SALESFORCE.PURGE_ACCOUNT_HISTORY;
-- DROP TASK IF EXISTS ES_COVADONGA.SALESFORCE.PURGE_CONTACT_HISTORY;
-- DROP TASK IF EXISTS ES_COVADONGA.SALESFORCE.PURGE_OPPORTUNITY_HISTORY;
-- DROP TASK IF EXISTS ES_COVADONGA.SALESFORCE.PURGE_LEAD_HISTORY;

-- Paso 6: Registrar rollback
INSERT INTO ES_COVADONGA.SALESFORCE.PURGE_LOG (
    TABLE_NAME, CUTOFF_DATE, ROWS_ARCHIVED, ROWS_DELETED, EXECUTED_AT
) VALUES (
    'ROLLBACK', CURRENT_DATE(), 0, 0, CURRENT_TIMESTAMP()
);
```

### 2.4.6 Tiempo Estimado

| Subtarea | Tiempo |
|----------|--------|
| Analisis de tablas HISTORY y requisitos | 2h |
| Diseno de estrategia de purga y archivado | 2h |
| Creacion de stored procedures y tasks | 4h |
| Ejecucion de purga inicial | 2h |
| Testing y verificacion | 2h |
| Monitorizacion post-implementacion (3 dias) | 4h |
| **TOTAL** | **16h (~2 dias)** |

---

## PLAN DE EJECUCION Y DEPENDENCIAS

### Orden de Ejecucion Recomendado

```
Semana 1:
  Dia 1-2: Accion 2.2 (NoBeforeUpdate) - Bajo riesgo, rapido
  Dia 2-3: Accion 2.4 (Reducir HISTORY) - Bajo riesgo, rapido
  Dia 3-5: Accion 2.1 (TRANSIENT) - Riesgo medio, requiere lotes

Semana 2:
  Dia 6-7: Accion 2.3 (Queries analiticas) - Alto riesgo, requiere testing
  Dia 8-10: Monitorizacion y ajustes de todas las acciones
```

### Dependencias

| Accion | Depende de | Bloquea |
|--------|-----------|---------|
| 2.1 (TRANSIENT) | Ninguna | Ninguna |
| 2.2 (NoBeforeUpdate) | Ninguna | Ninguna |
| 2.3 (Queries) | Ninguna | Ninguna |
| 2.4 (HISTORY) | Ninguna | Ninguna |

**Nota:** Las 4 acciones de Fase 2 son independientes entre si y pueden
ejecutarse en paralelo si hay recursos disponibles.

### Pre-requisitos

1. Acceso como ACCOUNTADMIN o role con permisos ALTER TABLE
2. Acceso a HVR Console para configuracion NoBeforeUpdate
3. Ventana de mantenimiento para purga inicial de HISTORY
4. Aprobacion del negocio para reduccion de retencion HISTORY

---

## METRICAS DE SEGUIMIENTO

### KPIs de la Fase 2

| Metrica | Linea Base | Objetivo | Frecuencia |
|---------|-----------|----------|------------|
| Creditos/mes totales | 5.305 | 3.183 (-40%) | Semanal |
| Storage PRO_0_STAGING_DB | 2.5 TB | 1.25 TB | Semanal |
| Storage Fail-safe | 2.5 TB | 0 TB | Semanal |
| Duracion query ADRIANLOPEZ | 600s | < 60s | Diaria |
| Storage tablas HISTORY | ~500 GB | ~125 GB | Semanal |
| Datos capturados HVR (bytes) | Baseline | -3-5% | Diaria |

### Queries de Monitorizacion

```sql
-- Dashboard de costes semanal
SELECT
    DATE_TRUNC('WEEK', START_TIME) AS WEEK,
    WAREHOUSE_NAME,
    SUM(CREDITS_USED) AS WEEKLY_CREDITS,
    SUM(CREDITS_USED) * 4 AS ESTIMATED_MONTHLY_CREDITS
FROM SNOWFLAKE.ACCOUNT_USAGE.WAREHOUSE_METERING_HISTORY
WHERE START_TIME >= DATEADD(WEEK, -8, CURRENT_TIMESTAMP())
GROUP BY WEEK, WAREHOUSE_NAME
ORDER BY WEEK DESC, WAREHOUSE_NAME;

-- Storage por base de datos
SELECT
    DATABASE_NAME,
    AVERAGE_DATABASE_BYTES / POWER(1024, 3) AS STORAGE_GB,
    AVERAGE_FAILSAFE_BYTES / POWER(1024, 3) AS FAILSAFE_GB
FROM SNOWFLAKE.ACCOUNT_USAGE.DATABASE_STORAGE_USAGE_HISTORY
WHERE USAGE_DATE = CURRENT_DATE()
    AND DATABASE_NAME IN ('PRO_0_STAGING_DB', 'ES_COVADONGA')
ORDER BY DATABASE_NAME;

-- Estado de tasks de purga
SELECT
    NAME,
    STATE,
    COMPLETED_TIME,
    DATEDIFF(MINUTE, COMPLETED_TIME, CURRENT_TIMESTAMP()) AS MINUTES_SINCE_LAST_RUN
FROM TABLE(INFORMATION_SCHEMA.TASK_HISTORY())
WHERE NAME LIKE 'PURGE_%'
    AND COMPLETED_TIME >= DATEADD(DAY, -1, CURRENT_TIMESTAMP())
ORDER BY NAME;
```

### Alertas Recomendadas

1. **Credito alert:** Notificar si creditos diarios superan 200
2. **Task failure:** Alerta inmediata si algun task de purga falla
3. **Storage growth:** Alerta si storage de staging crece > 10% en una semana
4. **Query timeout:** Alerta si queries de ADRIANLOPEZ superan 300s

---

## RESUMEN DE AHORRO ESTIMADO

| Accion | Ahorro/mes | % del objetivo |
|--------|-----------|----------------|
| 2.1 - TRANSIENT | ~800 creditos | 30% |
| 2.2 - NoBeforeUpdate | ~150 creditos | 6% |
| 2.3 - Queries optimizadas | ~400 creditos | 15% |
| 2.4 - HISTORY retencion | ~200 creditos | 7% |
| **TOTAL FASE 2** | **~1.550 creditos** | **58%** |

**Acumulado Fase 1 + Fase 2:**
- Fase 1: ~2.300 creditos/mes
- Fase 2: ~1.550 creditos/mes
- **Total: ~3.850 creditos/mes (72% del objetivo del 40%)**

**Nota:** El ahorro real puede variar dependiendo de la carga de trabajo
y el uso real de los warehouses. Las estimaciones son conservadoras
basadas en los datos actuales.

---

# FIN DEL DOCUMENTO
