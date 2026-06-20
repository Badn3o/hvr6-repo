# PLAN DE IMPLEMENTACIÓN DETALLADO
## Optimización de Costes HVR 6.2 → Snowflake
### Objetivo: Reducción del 40% en créditos (5.305 → ~3.183 créditos/mes)

**Fecha:** 2026-06-20
**Versión:** 2.0
**Autor:** Los Cuatro Fantásticos (Hermes + Claude + Cortex + Codex)
**Repositorio:** https://github.com/Badn3o/hvr6-repo

---

## ÍNDICE GENERAL

1. [Resumen Ejecutivo](#1-resumen-ejecutivo)
2. [Estado Actual - Diagnóstico](#2-estado-actual--diagnóstico)
3. [FASE 1: Quick Wins (Semanas 1-2)](#3-fase-1-quick-wins-semanas-1-2)
4. [FASE 2: Optimización Media (Semanas 3-4)](#4-fase-2-optimización-media-semanas-3-4)
5. [FASE 3: Optimización Avanzada (Semanas 5-8)](#5-fase-3-optimización-avanzada-semanas-5-8)
6. [Scripts de Implementación](#6-scripts-de-implementación)
7. [Monitorización y KPIs](#7-monitorización-y-kpis)
8. [Gestión de Riesgos Global](#8-gestión-de-riesgos-global)
9. [Rollback Global](#9-rollback-global)

---

## 1. RESUMEN EJECUTIVO

### Situación Actual

| Métrica | Valor |
|---------|-------|
| Créditos/mes totales | ~5.305 |
| PRO_LOAD_WH | 1.927 (36,3%) |
| PRO_TRANSFORM_WH | 1.024 (19,3%) |
| PRO_TRANSFORM_COMPLEX_WH | 635 (12,0%) |
| Storage PRO_0_STAGING_DB | 2,5 TB (4.107 tablas) |
| Storage ES_COVADONGA | 1,34 TB (4.631 tablas) |
| Operación más costosa | REFRESH_CLONE_PARCEL (887s) |
| Segunda más costosa | CLONE diario PRO_0_STAGING_DB (680s) |

### Plan de Reducción

| Fase | Semanas | Acciones | Ahorro Estimado | Acumulado |
|------|---------|----------|-----------------|-----------|
| 1 | 1-2 | 4 | ~2.300 créditos/mes | -43% |
| 2 | 3-4 | 4 | ~1.550 créditos/mes | -72% |
| 3 | 5-8 | 5 | ~1.500 créditos/mes | -100%+ |
| **TOTAL** | **1-8** | **13** | **~5.350 créditos/mes** | **-40%+** |

### Orden de Ejecución

```
Semana 1:  1.4 Coalesce → 1.3 COPY INTO
Semana 2:  1.1 Eliminar CLONE → 1.2 Optimizar REFRESH_CLONE
Semana 3:  2.4 Retención HISTORY → 2.2 NoBeforeUpdate
Semana 4:  2.1 TRANSIENT tables
Semana 5:  2.3 Queries analíticas
Semana 6:  3.2 NoTriggerFiring → 3.5 Checkpoint
Semana 7:  3.3 Scheduling → 3.4 Eliminar duplicados
Semana 8:  3.1 APPEND method
```

---

## 2. ESTADO ACTUAL - DIAGNÓSTICO

### 2.1 Warehouses por Consumo (30 días)

| Warehouse | Créditos | % Total | Queries | Uso principal |
|-----------|----------|---------|---------|---------------|
| PRO_LOAD_WH | 1.927 | 36,3% | 737 | Carga HVR (COPY INTO) |
| PRO_TRANSFORM_WH | 1.024 | 19,3% | 653 | REFRESH_CLONE, CLONE |
| PRO_TRANSFORM_COMPLEX_WH | 635 | 12,0% | 564 | Queries analíticas |
| DEV_TRANSFORM_WH | 640 | 12,1% | 737 | Desarrollo |
| PRO_BI_WH | 310 | 5,8% | 736 | BI/Reporting |
| PRO_INTERNAL_BI_WH | 221 | 4,2% | 489 | BI interno |
| STREAMLIT_APPS_WH | 150 | 2,8% | 136 | Apps Streamlit |
| Otros | 398 | 7,5% | ~1.700 | Varios |

### 2.2 Top 10 Queries Más Costosas (7 días)

| # | Warehouse | Segundos | Operación | DB |
|---|-----------|----------|-----------|-----|
| 1 | PRO_TRANSFORM_COMPLEX_WH | 5.998 | Query UNION ALL compleja | PRO_0_STAGING_DB |
| 2 | PRO_TRANSFORM_WH | 887 | REFRESH_CLONE_PARCEL() | ES_COVADONGA |
| 3 | PRO_TRANSFORM_WH | 816 | REFRESH_CLONE_PARCEL() | ES_COVADONGA |
| 4 | PRO_TRANSFORM_WH | 802 | REFRESH_CLONE_PARCEL() | ES_COVADONGA |
| 5 | PRO_TRANSFORM_WH | 727 | REFRESH_CLONE_PARCEL() | ES_COVADONGA |
| 6 | PRO_TRANSFORM_WH | 683 | REFRESH_CLONE_PARCEL() | ES_COVADONGA |
| 7 | FINOPS_WH | 680 | SP_DAILY_BACKUP() | PRO_0_STAGING_BACKUP |
| 8 | FINOPS_WH | 679 | CREATE DATABASE CLONE | PRO_0_STAGING_BACKUP |
| 9 | PRO_INTERNAL_BI_WH | 598 | Query analítica JOINs | PRO_0_STAGING_DB |
| 10 | PRO_INTERNAL_BI_WH | 598 | Query analítica JOINs | PRO_0_STAGING_DB |

### 2.3 Tablas Más Grandes

**PRO_0_STAGING_DB (Top 5):**
| Tabla | Filas | Size |
|-------|-------|------|
| FR_FRISBI.SALES_AZ9_A_0011 | 5.257M | 216 GB |
| ES_TESEO.TW_GPS_HISTORIC_IO | 14.901M | 161 GB |
| FR_FRISBI.SALES_AZ9_A_0011_BACKUP | 4.257M | 157 GB |
| ES_ESPADA.SALES_AZ7_O014S00 | 3.918M | 128 GB |
| ES_ESPADA.SALES_AZ7_OR014S00_SEGURIDAD | 2.220M | 71 GB |

**ES_COVADONGA (Top 5):**
| Tabla | Filas | Size |
|-------|-------|------|
| ES_TESEO.TW_GPS_HISTORIC_IO | 14.901M | 161 GB |
| ES_PARCEL.TSIMAGES | 9.435M | 83 GB |
| ES_PARCEL.RHO | 444.884M | 82 GB |
| ES_PARCEL.PLSTMPIMAGENES | 1.403M | 75 GB |
| ES_TESEO.TW_HISTORIC_POSIC | 2.346M | 59 GB |

---

## 3. FASE 1: QUICK WINS (Semanas 1-2)

**Objetivo:** -21% de reducción (~2.300 créditos/mes)
**Riesgo global:** Bajo a Medio
**Documento detallado:** `IMPLEMENTACION_FASE_1.md`

---

### 3.1 Acción 1.4 - Aplicar Coalesce en Capture (DÍA 1)

**Impacto:** ~100 créditos/mes | **Riesgo:** Bajo | **Tiempo:** 1 día

#### Descripción
Coalesce fusiona múltiples operaciones sobre la misma fila en una sola operación. Un INSERT + UPDATE se convierten en un solo INSERT; 5 UPDATEs se reducen a 1.

#### Pasos

**1. Verificar canales HVR actuales:**
```bash
ssh hvradmin@hvr-hub-server
hvrcli -l channels
```

**2. Aplicar Coalesce a cada canal:**
```bash
# Para cada canal de replicación:
hvrcli -c <channel_name> -A Capture -p Coalesce

# Verificar configuración:
hvrcli -c <channel_name> -l actions | grep -i coalesce
```

**3. Verificación post-implementación:**
```sql
-- En Snowflake, comparar volumen de cambios antes/después
SELECT 
    DATE_TRUNC('hour', query_start_time) as hour,
    COUNT(*) as num_changes,
    SUM(bytes_scanned) as total_bytes
FROM SNOWFLAKE.ACCOUNT_USAGE.QUERY_HISTORY
WHERE query_text LIKE '%INSERT%PRO_0_STAGING_DB%'
    AND query_start_time >= DATEADD(day, -1, CURRENT_DATE())
GROUP BY 1 ORDER BY 1;
```

#### Riesgos

| Riesgo | Probabilidad | Impacto | Mitigación |
|--------|-------------|---------|------------|
| Inconsistencia intermedia en target | Baja | Medio | Solo afecta a staging; datos se re-sincronizan en siguiente ciclo |
| Incompatibilidad con SapUnpack | Baja | Alto | Verificar que ningún canal usa SapUnpack antes de aplicar |

#### Rollback
```bash
hvrcli -c <channel_name> -A Capture -d Coalesce
```

---

### 3.2 Acción 1.3 - Reducir Frecuencia COPY INTO ES_ESPADA_MASTERS (DÍA 1-2)

**Impacto:** ~200 créditos/mes | **Riesgo:** Bajo | **Tiempo:** 1 día

#### Descripción
Las operaciones `COPY INTO ZCDS_6_MAT_MD_V` consumen 200-257s cada una. Se optimiza el FileFormat HVR para reducir el número de archivos staging y aumentar el tamaño máximo.

#### Pasos

**1. Configurar FileFormat en HVR:**
```bash
# En el canal ES_ESPADA_MASTERS:
hvrcli -c ES_ESPADA_MASTERS -A FileFormat -p MaxFileSize=256MB
hvrcli -c ES_ESPADA_MASTERS -A FileFormat -p Compress=ZSTD
hvrcli -c ES_ESPADA_MASTERS -A Integrate -p BurstCommitFrequency=CYCLE
```

**2. Verificación:**
```sql
-- Comparar duración de COPY INTO antes/después
SELECT 
    query_id,
    execution_time / 1000 as exec_seconds,
    query_text
FROM SNOWFLAKE.ACCOUNT_USAGE.QUERY_HISTORY
WHERE query_text LIKE '%COPY INTO%ZCDS_6_MAT_MD_V%'
    AND start_time >= DATEADD(day, -7, CURRENT_DATE())
ORDER BY execution_time DESC;
```

#### Riesgos

| Riesgo | Probabilidad | Impacto | Mitigación |
|--------|-------------|---------|------------|
| Archivos más grandes fallan en carga | Baja | Bajo | Reducir MaxFileSize a 128MB si hay errores |

#### Rollback
```bash
hvrcli -c ES_ESPADA_MASTERS -A FileFormat -p MaxFileSize=128MB
```

---

### 3.3 Acción 1.1 - Eliminar CLONE Diario de PRO_0_STAGING_DB (DÍA 3-5)

**Impacto:** ~1.200 créditos/mes | **Riesgo:** Medio | **Tiempo:** 2-3 días

#### Descripción
El task `SP_DAILY_BACKUP` ejecuta `CREATE DATABASE CLONE PRO_0_STAGING_DB` diario (~680s en FINOPS_WH). Se reemplaza por Time Travel extendido + backup incremental semanal.

#### Pasos

**1. Verificar configuración actual de Time Travel:**
```sql
SELECT NAME, RETENTION_TIME_IN_DAYS
FROM SNOWFLAKE.ACCOUNT_USAGE.DATABASES
WHERE NAME = 'PRO_0_STAGING_DB';
```

**2. Extender Time Travel a 7 días:**
```sql
ALTER DATABASE PRO_0_STAGING_DB SET DATA_RETENTION_TIME_IN_DAYS = 7;
```

**3. Eliminar task de CLONE diario:**
```sql
DROP TASK IF EXISTS PRO_0_STAGING_BACKUP_DB.PUBLIC.SP_DAILY_BACKUP;
DROP TASK IF EXISTS PRO_0_STAGING_BACKUP_DB.PUBLIC.TASK_DAILY_CLONE;
```

**4. Crear backup incremental semanal:**
```sql
CREATE TASK PRO_0_STAGING_BACKUP_DB.PUBLIC.TASK_WEEKLY_BACKUP
  WAREHOUSE = FINOPS_WH
  SCHEDULE = 'USING CRON 0 2 * * 0'  -- Domingo 2AM
AS
  CREATE DATABASE IF NOT EXISTS PRO_0_STAGING_BKP_WEEKLY 
  CLONE PRO_0_STAGING_DB;
```

**5. Verificación:**
```sql
-- Confirmar que no hay CLONE tasks activos
SHOW TASKS IN DATABASE PRO_0_STAGING_BACKUP_DB;

-- Verificar Time Travel
SELECT NAME, RETENTION_TIME_IN_DAYS 
FROM SNOWFLAKE.ACCOUNT_USAGE.DATABASES 
WHERE NAME = 'PRO_0_STAGING_DB';
```

#### Riesgos

| Riesgo | Probabilidad | Impacto | Mitigación |
|--------|-------------|---------|------------|
| Necesidad de recuperar datos > 7 días | Baja | Alto | Mantener backup semanal como CLONE completo |
| Impacto en procesos que dependen del CLONE | Media | Alto | Notificar a equipos antes de eliminar |

#### Rollback
```sql
CREATE TASK PRO_0_STAGING_BACKUP_DB.PUBLIC.TASK_DAILY_CLONE
  WAREHOUSE = FINOPS_WH
  SCHEDULE = 'USING CRON 0 2 * * *'
AS
  CREATE DATABASE IF NOT EXISTS PRO_0_STAGING_BKP CLONE PRO_0_STAGING_DB;

ALTER TASK PRO_0_STAGING_BACKUP_DB.PUBLIC.TASK_DAILY_CLONE RESUME;
```

---

### 3.4 Acción 1.2 - Optimizar REFRESH_CLONE_PARCEL y REFRESH_CLONE_TESEO (DÍA 5-10)

**Impacto:** ~800 créditos/mes | **Riesgo:** Alto | **Tiempo:** 5-7 días

#### Descripción
Las stored procedures `REFRESH_CLONE_PARCEL()` y `REFRESH_CLONE_TESEO()` clonan tablas de 160GB+ (TW_GPS_HISTORIC_IO) y consumen 683-887s cada una. Se reemplazan por MERGE incremental con Snowflake Streams.

#### Pasos

**1. Crear Streams en tablas fuente:**
```sql
-- Stream para ES_PARCEL
CREATE STREAM IF NOT EXISTS PRO_0_STAGING_DB.ES_PARCEL.STREAM_PARCEL_CHANGES
  ON TABLE PRO_0_STAGING_DB.ES_PARCEL.SOURCE_TABLE
  APPEND_ONLY = FALSE;

-- Stream para ES_TESEO
CREATE STREAM IF NOT EXISTS PRO_0_STAGING_DB.ES_TESEO.STREAM_TESEO_CHANGES
  ON TABLE PRO_0_STAGING_DB.ES_TESEO.SOURCE_TABLE
  APPEND_ONLY = FALSE;
```

**2. Crear stored procedure de MERGE incremental:**
```sql
CREATE OR REPLACE PROCEDURE ES_COVADONGA.ES_PARCEL.REFRESH_INCREMENTAL_PARCEL()
RETURNS STRING
LANGUAGE SQL
AS $$
DECLARE
  rows_inserted INTEGER DEFAULT 0;
  rows_updated INTEGER DEFAULT 0;
  rows_deleted INTEGER DEFAULT 0;
BEGIN
  -- INSERT nuevos registros
  INSERT INTO ES_COVADONGA.ES_PARCEL.TARGET_TABLE
  SELECT * FROM PRO_0_STAGING_DB.ES_PARCEL.SOURCE_TABLE s
  WHERE NOT EXISTS (
    SELECT 1 FROM ES_COVADONGA.ES_PARCEL.TARGET_TABLE t WHERE t.ID = s.ID
  );
  rows_inserted := SQLROWCOUNT;
  
  -- UPDATE registros modificados
  MERGE INTO ES_COVADONGA.ES_PARCEL.TARGET_TABLE t
  USING PRO_0_STAGING_DB.ES_PARCEL.SOURCE_TABLE s
  ON t.ID = s.ID
  WHEN MATCHED AND t.LAST_MODIFIED < s.LAST_MODIFIED THEN
    UPDATE SET t.COL1 = s.COL1, t.COL2 = s.COL2, ...;
  rows_updated := SQLROWCOUNT;
  
  RETURN 'Incremental: ' || rows_inserted || ' inserts, ' || rows_updated || ' updates';
END;
$$;
```

**3. Programar ejecución cada 12 horas (en vez de cada 4h):**
```sql
CREATE TASK ES_COVADONGA.ES_PARCEL.TASK_REFRESH_INCREMENTAL
  WAREHOUSE = PRO_TRANSFORM_WH
  SCHEDULE = 'USING CRON 0 0,12 * * *'  -- Cada 12 horas
AS
  CALL ES_COVADONGA.ES_PARCEL.REFRESH_INCREMENTAL_PARCEL();
```

**4. Verificación:**
```sql
-- Comparar tiempo de ejecución antes/después
SELECT 
    query_id,
    execution_time / 1000 as exec_seconds,
    query_text
FROM SNOWFLAKE.ACCOUNT_USAGE.QUERY_HISTORY
WHERE query_text LIKE '%REFRESH%PARCEL%'
    AND start_time >= DATEADD(day, -7, CURRENT_DATE())
ORDER BY start_time DESC;
```

#### Riesgos

| Riesgo | Probabilidad | Impacto | Mitigación |
|--------|-------------|---------|------------|
| Datos inconsistentes durante transición | Media | Alto | Ejecutar sincronización completa (CLONE) una vez antes de activar incremental |
| Stream consume créditos adicionales | Baja | Bajo | Streams tienen coste negligible vs CLONE completo |
| Fallo en MERGE por volumen alto | Media | Medio | Implementar retry logic en la procedure |

#### Rollback
```sql
-- Restaurar procedure original
CREATE OR REPLACE PROCEDURE ES_COVADONGA.ES_PARCEL.REFRESH_CLONE_PARCEL()
RETURNS STRING
LANGUAGE SQL
AS $$
BEGIN
  DROP TABLE IF EXISTS ES_COVADONGA.ES_PARCEL.TARGET_TABLE;
  CREATE TABLE ES_COVADONGA.ES_PARCEL.TARGET_TABLE 
    CLONE PRO_0_STAGING_DB.ES_PARCEL.SOURCE_TABLE;
  RETURN 'Full clone completed';
END;
$$;

-- Restaurar task original
CREATE TASK ES_COVADONGA.ES_PARCEL.TASK_REFRESH_CLONE
  WAREHOUSE = PRO_TRANSFORM_WH
  SCHEDULE = 'USING CRON 0 */4 * * *'  -- Cada 4 horas
AS
  CALL ES_COVADONGA.ES_PARCEL.REFRESH_CLONE_PARCEL();
```

---

## 4. FASE 2: OPTIMIZACIÓN MEDIA (Semanas 3-4)

**Objetivo:** -31% acumulado (~1.550 créditos/mes adicionales)
**Riesgo global:** Medio
**Documento detallado:** `IMPLEMENTACION_FASE_2.md`

---

### 4.1 Acción 2.4 - Reducir Retención HISTORY Salesforce (DÍA 11-12)

**Impacto:** ~200 créditos/mes | **Riesgo:** Bajo | **Tiempo:** 1-2 días

#### Pasos

**1. Crear task de purga:**
```sql
CREATE TASK PRO_0_STAGING_DB.ES_SALESFORCE_PHARMA.TASK_PURGE_HISTORY
  WAREHOUSE = PRO_LOAD_WH
  SCHEDULE = 'USING CRON 0 3 * * *'  -- 3AM diario
AS
  DELETE FROM PRO_0_STAGING_DB.ES_SALESFORCE_PHARMA.PEDIDO_HISTORY
  WHERE created_date < DATEADD(day, -7, CURRENT_DATE());
```

**2. Aplicar a todas las tablas HISTORY:**
```sql
-- LINEA_DE_PEDIDO_HISTORY
DELETE FROM PRO_0_STAGING_DB.ES_SALESFORCE_PHARMA.LINEA_DE_PEDIDO_HISTORY
WHERE created_date < DATEADD(day, -7, CURRENT_DATE());

-- ASIGNACION_COMERCIAL_HISTORY
DELETE FROM PRO_0_STAGING_DB.ES_SALESFORCE_PHARMA.ASIGNACION_COMERCIAL_HISTORY
WHERE created_date < DATEADD(day, -7, CURRENT_DATE());

-- PRICING_HISTORY
DELETE FROM PRO_0_STAGING_DB.ES_SALESFORCE_PHARMA.PRICING_HISTORY
WHERE created_date < DATEADD(day, -7, CURRENT_DATE());
```

#### Riesgos

| Riesgo | Probabilidad | Impacto | Mitigación |
|--------|-------------|---------|------------|
| Pérdida de datos de auditoría | Baja | Medio | Verificar requisitos de compliance antes de purgar |

---

### 4.2 Acción 2.2 - Implementar NoBeforeUpdate en Capture HVR (DÍA 12-13)

**Impacto:** ~150 créditos/mes | **Riesgo:** Bajo | **Tiempo:** 1-2 días

#### Pasos

**1. Aplicar NoBeforeUpdate a canales de staging:**
```bash
# Canales de PRO_0_STAGING_DB (sin auditoría necesaria):
hvrcli -c ES_ESPADA_MASTERS -A Capture -p NoBeforeUpdate
hvrcli -c FR_FRISBI -A Capture -p NoBeforeUpdate
hvrcli -c FR_STRATOR_BO -A Capture -p NoBeforeUpdate
hvrcli -c ES_CDI_PARCEL -A Capture -p NoBeforeUpdate
```

**2. NO aplicar a canales con requisito de auditoría:**
```bash
# NO aplicar a ES_SALESFORCE_PHARMA (requiere auditoría)
# NO aplicar a ES_TESEO (operativo, puede necesitar before)
# NO aplicar a ES_PARCEL (operativo)
```

#### Riesgos

| Riesgo | Probabilidad | Impacto | Mitigación |
|--------|-------------|---------|------------|
| Pérdida de valores "before" para auditoría | Baja | Alto | Solo aplicar a canales sin requisito de auditoría |

---

### 4.3 Acción 2.1 - Migrar Tablas de Staging a TRANSIENT (DÍA 14-18)

**Impacto:** ~800 créditos/mes | **Riesgo:** Medio | **Tiempo:** 3-5 días

#### Pasos

**1. Migrar en lotes de 5 tablas:**
```sql
-- Lote 1 (las 5 más grandes):
ALTER TABLE PRO_0_STAGING_DB.FR_FRISBI.SALES_AZ9_A_0011 SET TRANSIENT;
ALTER TABLE PRO_0_STAGING_DB.ES_TESEO.TW_GPS_HISTORIC_IO SET TRANSIENT;
ALTER TABLE PRO_0_STAGING_DB.ES_ESPADA.SALES_AZ7_O014S00 SET TRANSIENT;
ALTER TABLE PRO_0_STAGING_DB.ES_ESPADA.SALES_AZ7_OR014S00 SET TRANSIENT;
ALTER TABLE PRO_0_STAGING_DB.ES_TESEO.TW_HISTORIC_POSIC SET TRANSIENT;

-- Esperar 24h, verificar que HVR sigue funcionando correctamente

-- Lote 2:
ALTER TABLE PRO_0_STAGING_DB.FR_STRATOR_BO_L4.SALES_L4_OPERATIONPRODUITREPORTING SET TRANSIENT;
ALTER TABLE PRO_0_STAGING_DB.ES_ESPADA.STOCK_AZ7_O015S00 SET TRANSIENT;
ALTER TABLE PRO_0_STAGING_DB.ES_ESPADA.STOCK_AZ7_O022S00 SET TRANSIENT;
ALTER TABLE PRO_0_STAGING_DB.ES_ESPADA.SALES_AZ7_OR014S00_SEGURIDAD SET TRANSIENT;
ALTER TABLE PRO_0_STAGING_DB.ES_ESPADA.SALES_AZ7_O014S00_SEGURIDAD SET TRANSIENT;

-- Continuar con lotes hasta completar las 30 tablas más grandes
```

**2. Verificación:**
```sql
-- Verificar que las tablas son TRANSIENT
SELECT table_schema, table_name, table_type
FROM PRO_0_STAGING_DB.INFORMATION_SCHEMA.TABLES
WHERE table_name IN ('SALES_AZ9_A_0011', 'TW_GPS_HISTORIC_IO', ...)
ORDER BY table_schema, table_name;
```

#### Riesgos

| Riesgo | Probabilidad | Impacto | Mitigación |
|--------|-------------|---------|------------|
| Imposibilidad de recuperar datos tras Time Travel | Baja | Alto | Verificar que HVR puede regenerar datos antes de migrar |
| Error en HVR por tabla TRANSIENT | Baja | Medio | Migrar en lotes y verificar después de cada lote |

#### Rollback
```sql
-- Snowflake no permite revertir TRANSIENT a PERMANENT directamente
-- Hay que recrear la tabla:
CREATE TABLE PRO_0_STAGING_DB.FR_FRISBI.SALES_AZ9_A_0011_PERM 
  CLONE PRO_0_STAGING_DB.FR_FRISBI.SALES_AZ9_A_0011;
DROP TABLE PRO_0_STAGING_DB.FR_FRISBI.SALES_AZ9_A_0011;
ALTER TABLE PRO_0_STAGING_DB.FR_FRISBI.SALES_AZ9_A_0011_PERM 
  RENAME TO SALES_AZ9_A_0011;
```

---

### 4.4 Acción 2.3 - Optimizar Queries Analíticas ES_STRATOR_BO_L1 (DÍA 16-22)

**Impacto:** ~400 créditos/mes | **Riesgo:** Alto | **Tiempo:** 5-7 días

#### Pasos

**1. Crear vistas materializadas:**
```sql
CREATE MATERIALIZED VIEW PRO_0_STAGING_DB.ES_STRATOR_BO_L1.MV_PRODUCT_REFERENCES AS
SELECT 
    irt.CODEREFFOURNISSEURTABAC AS reference_fournisseur,
    p.FK_REFERENCEPRODUITFOURNISSEUR,
    p.ID as product_id
FROM PRO_0_STAGING_DB.ES_STRATOR_BO_L1.PRODUCT_L1_PRODUIT p
INNER JOIN PRO_0_STAGING_DB.ES_STRATOR_BO_L1.PRODUCT_L1_REFERENCEPRODUITFOURNISSEUR rpf
    ON p.FK_REFERENCEPRODUITFOURNISSEUR = rpf.ID
INNER JOIN PRO_0_STAGING_DB.ES_STRATOR_BO_L1.PRODUCT_L1_INFORMATIONREFERENCETABAC irt
    ON rpf.FK_INFORMATIONREFERENCETABAC = irt.ID
WHERE irt.datesuppression IS NULL;
```

**2. Crear clustering keys:**
```sql
ALTER TABLE PRO_0_STAGING_DB.ES_STRATOR_BO_L1.PRODUCT_L1_PRODUIT
CLUSTER BY (FK_REFERENCEPRODUITFOURNISSEUR);

ALTER TABLE PRO_0_STAGING_DB.ES_STRATOR_BO_L1.PRODUCT_L1_REFERENCEPRODUITFOURNISSEUR
CLUSTER BY (FK_INFORMATIONREFERENCETABAC);
```

**3. Mover queries a warehouse dedicado:**
```sql
-- Crear warehouse dedicado para analytics
CREATE WAREHOUSE IF NOT EXISTS PRO_ANALYTICS_WH
  WITH WAREHOUSE_SIZE = 'SMALL'
  AUTO_SUSPEND = 60
  AUTO_RESUME = TRUE;

-- Asignar resource monitor
CREATE RESOURCE MONITOR PRO_ANALYTICS_MONITOR WITH CREDIT_QUOTA = 100
  TRIGGERS ON 90 PERCENT DO NOTIFY
           ON 100 PERCENT DO SUSPEND;
```

#### Riesgos

| Riesgo | Probabilidad | Impacto | Mitigación |
|--------|-------------|---------|------------|
| Vista materializada no cubre todos los casos | Media | Medio | Crear múltiples vistas para diferentes patrones de query |
| Clustering key no mejora rendimiento | Baja | Bajo | Moniturar y ajustar después de 7 días |

---

## 5. FASE 3: OPTIMIZACIÓN AVANZADA (Semanas 5-8)

**Objetivo:** -44% acumulado (~1.500 créditos/mes adicionales)
**Riesgo global:** Medio a Alto
**Documento detallado:** `IMPLEMENTACION_FASE_3.md`

---

### 5.1 Acción 3.2 - Implementar NoTriggerFiring en Integrate (DÍA 23)

**Impacto:** ~100 créditos/mes | **Riesgo:** Bajo | **Tiempo:** 1 día

#### Pasos

**1. Aplicar solo a canales de staging:**
```bash
# Solo PRO_0_STAGING_DB (staging):
hvrcli -c ES_ESPADA_MASTERS -A Integrate -p NoTriggerFiring
hvrcli -c FR_FRISBI -A Integrate -p NoTriggerFiring
hvrcli -c FR_STRATOR_BO -A Integrate -p NoTriggerFiring

# NO aplicar a ES_COVADONGA (operativo)
```

#### Riesgos

| Riesgo | Probabilidad | Impacto | Mitigación |
|--------|-------------|---------|------------|
| Triggers de negocio no se ejecutan | Baja | Alto | Solo aplicar a staging, nunca a operativo |

---

### 5.2 Acción 3.5 - Optimizar Checkpoint Frequency (DÍA 23)

**Impacto:** ~100 créditos/mes | **Riesgo:** Bajo | **Tiempo:** 0.5 día

#### Pasos

```bash
# Cambiar de 300s (default) a 600s:
hvrcli -l <location> -p Capture_Checkpoint_Frequency=600

# Aplicar a todas las locations:
for loc in ES_ESPADA ES_TESEO FR_FRISBI FR_STRATOR ES_PARCEL; do
  hvrcli -l $loc -p Capture_Checkpoint_Frequency=600
done
```

---

### 5.3 Acción 3.3 - Programar Captura en Ventanas de Menor Coste (DÍA 24-25)

**Impacto:** ~300 créditos/mes | **Riesgo:** Bajo | **Tiempo:** 1-2 días

#### Pasos

```bash
# Ventana recomendada: 2AM-6AM (horario de menor demanda)
hvrcli -c ES_ESPADA_MASTERS -A Scheduling -p CaptureStartTimes='0 2 * * *'
hvrcli -c ES_ESPADA_MASTERS -A Scheduling -p IntegrateStartTimes='0 3 * * *'

hvrcli -c ES_TESEO -A Scheduling -p CaptureStartTimes='0 2 * * *'
hvrcli -c ES_TESEO -A Scheduling -p IntegrateStartTimes='0 3 * * *'

hvrcli -c FR_FRISBI -A Scheduling -p CaptureStartTimes='0 4 * * *'
hvrcli -c FR_FRISBI -A Scheduling -p IntegrateStartTimes='0 5 * * *'
```

---

### 5.4 Acción 3.4 - Eliminar Tablas Duplicadas/Backup (DÍA 26-30)

**Impacto:** ~400 créditos/mes | **Riesgo:** Alto | **Tiempo:** 3-5 días

#### Pasos

**1. Identificar tablas duplicadas:**
```sql
-- Tablas _BACKUP
SELECT table_schema, table_name, 
       bytes / POWER(1024,2) as size_mb
FROM PRO_0_STAGING_DB.INFORMATION_SCHEMA.TABLES
WHERE table_name LIKE '%_BACKUP'
ORDER BY bytes DESC;

-- Tablas _SEGURIDAD
SELECT table_schema, table_name,
       bytes / POWER(1024,2) as size_mb
FROM PRO_0_STAGING_DB.INFORMATION_SCHEMA.TABLES
WHERE table_name LIKE '%_SEGURIDAD'
ORDER BY bytes DESC;
```

**2. Eliminar en lotes (verificar dependencias antes):**
```sql
-- Verificar que no hay dependencias
SELECT * FROM SNOWFLAKE.ACCOUNT_USAGE.OBJECT_DEPENDENCIES
WHERE REFERENCED_OBJECT_NAME = 'SALES_AZ9_A_0011_BACKUP';

-- Eliminar
DROP TABLE IF EXISTS PRO_0_STAGING_DB.FR_FRISBI.SALES_AZ9_A_0011_BACKUP;
DROP TABLE IF EXISTS PRO_0_STAGING_DB.FR_STRATOR_BO_L4.SALES_L4_OPERATIONPRODUITREPORTING_BACKUP;
DROP TABLE IF EXISTS PRO_0_STAGING_DB.ES_ESPADA.STOCK_AZ7_O022S00_SEGURIDAD;
DROP TABLE IF EXISTS PRO_0_STAGING_DB.ES_ESPADA.SALES_AZ7_O014S00_SEGURIDAD;
DROP TABLE IF EXISTS PRO_0_STAGING_DB.ES_ESPADA.SALES_AZ7_OR014S00_SEGURIDAD;
```

#### Riesgos

| Riesgo | Probabilidad | Impacto | Mitigación |
|--------|-------------|---------|------------|
| Dependencias no detectadas | Media | Alto | Verificar OBJECT_DEPENDENCIES antes de eliminar |
| Necesidad de recuperar datos eliminados | Baja | Alto | Usar Time Travel (7 días) si se necesita recuperar |

---

### 5.5 Acción 3.1 - Implementar APPEND Method para Snowflake (DÍA 31-35)

**Impacto:** ~600 créditos/mes | **Riesgo:** Medio | **Tiempo:** 3-5 días

**⚠️ REQUISITO CRÍTICO:** HVR 6.2.5+ instalado. Verificar con `hvrversion`.

#### Pasos

**1. Verificar que todas las tablas tienen TimeKey:**
```sql
-- En Snowflake, verificar columnas timestamp en tablas destino
SELECT table_name, column_name, data_type
FROM PRO_0_STAGING_DB.INFORMATION_SCHEMA.COLUMNS
WHERE (column_name LIKE '%DATE%' OR column_name LIKE '%TIME%' OR column_name LIKE '%MODIFIED%')
    AND table_schema IN ('ES_ESPADA', 'ES_TESEO', 'FR_FRISBI', 'FR_STRATOR_BO_L1')
ORDER BY table_name;
```

**2. Configurar TimeKey en HVR:**
```bash
# Para cada tabla, definir la columna TimeKey:
hvrcli -c ES_ESPADA_MASTERS -A ColumnProperties -p Name=LAST_MODIFIED -p TimeKey
hvrcli -c FR_FRISBI -A ColumnProperties -p Name=CREATED_ON -p TimeKey
```

**3. Prueba piloto con un canal:**
```bash
# Cambiar solo un canal primero:
hvrcli -c ES_ESPADA_MASTERS -A Integrate -p Method=APPEND

# Monitorear durante 48h
# Si no hay errores, aplicar al resto
```

**4. Aplicar a todos los canales:**
```bash
for chn in ES_ESPADA_MASTERS FR_FRISBI FR_STRATOR_BO ES_CDI_PARCEL; do
  hvrcli -c $chn -A Integrate -p Method=APPEND
done
```

#### Riesgos

| Riesgo | Probabilidad | Impacto | Mitigación |
|--------|-------------|---------|------------|
| Tablas sin TimeKey causan fallos | Media | Alto | Verificar TODAS las tablas antes de activar |
| Duplicados en cambio BURST→APPEND | Media | Alto | Implementar en ventana de mantenimiento con Compare previo |
| Versión HVR < 6.2.5 | Baja | Alto | Verificar versión antes de iniciar |

#### Rollback
```bash
hvrcli -c <channel> -A Integrate -p Method=BURST
```

---

## 6. SCRIPTS DE IMPLEMENTACIÓN

### 6.1 Estructura de Archivos

```
/root/hvr-analysis/
├── IMPLEMENTACION_FASE_1.md          # Detalle Fase 1
├── IMPLEMENTACION_FASE_2.md          # Detalle Fase 2
├── IMPLEMENTACION_FASE_3.md          # Detalle Fase 3
├── PLAN_OPTIMIZACION_HVR.md          # Plan consolidado
├── cortex_results.md                 # Análisis real Snowflake
├── claude_strategy.md                # Estrategia HVR
└── scripts/
    ├── monitor_costes.py             # Monitorización de créditos
    ├── verificacion_post_deploy.py   # Verificación post-implementación
    ├── rollback.py                   # Rollback de emergencia
    └── hvr_config_checker.py         # Verificación configuración HVR
```

### 6.2 Uso de Scripts

**Monitorización de costes:**
```bash
cd /root/hvr-analysis/scripts
python3 monitor_costes.py --output metricas.json
python3 monitor_costes.py --umbral-pct 15  # Alerta si sube >15%
```

**Verificación post-deploy:**
```bash
python3 verificacion_post_deploy.py --output reporte.md
```

**Rollback de emergencia:**
```bash
# Ver qué haría (sin ejecutar):
python3 rollback.py --dry-run

# Ejecutar rollback completo:
python3 rollback.py --execute

# Rollback solo de una fase:
python3 rollback.py --phase 1 --execute
```

**Verificación configuración HVR:**
```bash
python3 hvr_config_checker.py --output config_report.md
```

---

## 7. MONITORIZACIÓN Y KPIs

### 7.1 Queries de Seguimiento Semanal

```sql
-- 1. Créditos por warehouse (semana actual vs anterior)
SELECT 
    warehouse_name,
    DATE_TRUNC('week', start_time) as week,
    SUM(credits_used) as credits,
    LAG(SUM(credits_used)) OVER (PARTITION BY warehouse_name ORDER BY DATE_TRUNC('week', start_time)) as prev_week_credits,
    ROUND((SUM(credits_used) - LAG(SUM(credits_used)) OVER (PARTITION BY warehouse_name ORDER BY DATE_TRUNC('week', start_time))) 
        / NULLIF(LAG(SUM(credits_used)) OVER (PARTITION BY warehouse_name ORDER BY DATE_TRUNC('week', start_time)), 0) * 100, 2) as pct_change
FROM SNOWFLAKE.ACCOUNT_USAGE.WAREHOUSE_METERING_HISTORY
WHERE start_time >= DATEADD(week, -4, CURRENT_DATE())
GROUP BY 1, 2
ORDER BY 2 DESC, 3 DESC;

-- 2. Tiempo promedio de REFRESH_CLONE (antes/después)
SELECT 
    DATE_TRUNC('day', start_time) as day,
    AVG(execution_time / 1000) as avg_exec_seconds,
    COUNT(*) as executions
FROM SNOWFLAKE.ACCOUNT_USAGE.QUERY_HISTORY
WHERE query_text LIKE '%REFRESH%CLONE%'
    AND start_time >= DATEADD(day, -14, CURRENT_DATE())
GROUP BY 1 ORDER BY 1;

-- 3. Storage por base de datos
SELECT 
    database_name,
    SUM(bytes) / POWER(1024, 3) as size_gb,
    SUM(CASE WHEN table_type = 'TRANSIENT' THEN bytes ELSE 0 END) / POWER(1024, 3) as transient_gb
FROM SNOWFLAKE.ACCOUNT_USAGE.TABLE_STORAGE_METRICS
WHERE database_name IN ('PRO_0_STAGING_DB', 'ES_COVADONGA')
GROUP BY 1;
```

### 7.2 KPIs Objetivo

| KPI | Baseline | Fase 1 | Fase 2 | Fase 3 |
|-----|----------|--------|--------|--------|
| Créditos/mes PRO_LOAD_WH | 1.927 | 1.500 | 1.200 | 1.000 |
| Créditos/mes PRO_TRANSFORM_WH | 1.024 | 600 | 400 | 300 |
| Créditos/mes PRO_TRANSFORM_COMPLEX_WH | 635 | 500 | 350 | 250 |
| Storage PRO_0_STAGING_DB | 2,5 TB | 2,5 TB | 1,0 TB | 0,8 TB |
| Storage ES_COVADONGA | 1,34 TB | 1,34 TB | 1,2 TB | 1,1 TB |
| Tiempo REFRESH_CLONE | 780s | 400s | 300s | 200s |
| CLONEs diarios | 1 | 0 | 0 | 0 |
| **TOTAL CRÉDITOS** | **5.305** | **4.100** | **3.500** | **3.183** |
| **REDUCCIÓN** | **-** | **-23%** | **-34%** | **-40%** |

---

## 8. GESTIÓN DE RIESGOS GLOBAL

### 8.1 Matriz de Riesgos Consolidada

| ID | Riesgo | Probabilidad | Impacto | Fase | Mitigación |
|----|--------|-------------|---------|------|------------|
| R1 | Pérdida de datos por TRANSIENT | Baja | Alto | 2 | Verificar regenerabilidad HVR antes de migrar |
| R2 | Inconsistencia por NoBeforeUpdate | Baja | Medio | 2 | Solo aplicar a canales sin auditoría |
| R3 | Duplicados por BURST→APPEND | Media | Alto | 3 | Prueba piloto + Compare previo |
| R4 | Fallo en MERGE incremental | Media | Alto | 1 | Sincronización completa inicial + retry logic |
| R5 | Dependencias no detectadas en eliminación | Media | Alto | 3 | Verificar OBJECT_DEPENDENCIES |
| R6 | Versión HVR < 6.2.5 para APPEND | Baja | Alto | 3 | Verificar versión antes de iniciar |
| R7 | Regresión en queries analíticas | Bajo | Medio | 2 | Vistas materializadas + testing |
| R8 | Necesidad de recuperar datos > 7 días | Baja | Alto | 1 | Backup semanal como CLONE completo |

### 8.2 Procedimiento de Escalación

1. **Nivel 1 (Bajo):** Ajustar parámetros de configuración, no requiere ventana de mantenimiento
2. **Nivel 2 (Medio):** Requiere ventana de mantenimiento, notificar a equipos afectados
3. **Nivel 3 (Alto):** Requiere ventana de mantenimiento + rollback plan + aprobación de arquitectura

---

## 9. ROLLBACK GLOBAL

### 9.1 Rollback de Emergencia

Si se detecta un problema crítico durante la implementación:

```bash
# 1. Detener todos los cambios en curso
# 2. Ejecutar rollback según la fase afectada:

# Fase 1:
python3 rollback.py --phase 1 --execute

# Fase 2:
python3 rollback.py --phase 2 --execute

# Fase 3:
python3 rollback.py --phase 3 --execute

# Rollback completo:
python3 rollback.py --execute
```

### 9.2 Verificación Post-Rollback

```sql
-- Verificar que todo volvió al estado original
SELECT 'CLONE tasks' as check_name, COUNT(*) as count
FROM SNOWFLAKE.ACCOUNT_USAGE.TASKS
WHERE name LIKE '%CLONE%'

UNION ALL

SELECT 'TRANSIENT tables', COUNT(*)
FROM PRO_0_STAGING_DB.INFORMATION_SCHEMA.TABLES
WHERE table_type = 'TRANSIENT TABLE'

UNION ALL

SELECT 'Materialized views', COUNT(*)
FROM PRO_0_STAGING_DB.INFORMATION_SCHEMA.TABLES
WHERE table_type = 'MATERIALIZED VIEW';
```

---

## APÉNDICE: CRONOGRAMA DETALLADO

| Semana | Día | Acción | Responsable | Estado |
|--------|-----|--------|-------------|--------|
| 1 | 1 | 1.4 Coalesce en Capture | HVR Admin | ⬜ Pendiente |
| 1 | 1 | 1.3 COPY INTO optimization | HVR Admin | ⬜ Pendiente |
| 1 | 3 | 1.1 Eliminar CLONE diario | DBA Snowflake | ⬜ Pendiente |
| 1 | 5 | 1.2 Optimizar REFRESH_CLONE | DBA + HVR Admin | ⬜ Pendiente |
| 2 | 8 | Verificación Fase 1 | Arquitectura | ⬜ Pendiente |
| 2 | 10 | 2.4 Retención HISTORY | DBA Snowflake | ⬜ Pendiente |
| 2 | 11 | 2.2 NoBeforeUpdate | HVR Admin | ⬜ Pendiente |
| 3 | 14 | 2.1 TRANSIENT tables (lote 1) | DBA Snowflake | ⬜ Pendiente |
| 3 | 15 | 2.1 TRANSIENT tables (lote 2) | DBA Snowflake | ⬜ Pendiente |
| 4 | 18 | 2.1 TRANSIENT tables (lote 3) | DBA Snowflake | ⬜ Pendiente |
| 4 | 19 | 2.3 Vistas materializadas | DBA Snowflake | ⬜ Pendiente |
| 4 | 20 | 2.3 Clustering keys | DBA Snowflake | ⬜ Pendiente |
| 4 | 22 | Verificación Fase 2 | Arquitectura | ⬜ Pendiente |
| 5 | 23 | 3.2 NoTriggerFiring | HVR Admin | ⬜ Pendiente |
| 5 | 23 | 3.5 Checkpoint frequency | HVR Admin | ⬜ Pendiente |
| 5 | 24 | 3.3 Scheduling ventanas | HVR Admin | ⬜ Pendiente |
| 6 | 26 | 3.4 Eliminar duplicados (lote 1) | DBA Snowflake | ⬜ Pendiente |
| 6 | 28 | 3.4 Eliminar duplicados (lote 2) | DBA Snowflake | ⬜ Pendiente |
| 7 | 31 | 3.1 Verificar TimeKey todas tablas | HVR Admin | ⬜ Pendiente |
| 7 | 32 | 3.1 Prueba piloto APPEND | HVR Admin | ⬜ Pendiente |
| 8 | 34 | 3.1 APPEND todos los canales | HVR Admin | ⬜ Pendiente |
| 8 | 35 | Verificación Fase 3 + Global | Arquitectura | ⬜ Pendiente |

---

**Documento generado por Los Cuatro Fantásticos**
**Repositorio:** https://github.com/Badn3o/hvr6-repo
