# PLAN DE REDUCCIÓN DE COSTES HVR → SNOWFALKE
## Objetivo: -40% en créditos Snowflake
### Fecha: 2026-06-20 | Versión: 1.0

---

## 1. DIAGNÓSTICO ACTUAL (Datos Reales)

### 1.1 Consumo de Créditos por Warehouse (últimos 30 días)

| Warehouse | Créditos Total | Compute | Cloud Services | Queries |
|-----------|---------------|---------|----------------|---------|
| **PRO_LOAD_WH** | **1.927** | 1.374 | 553 | 737 |
| **PRO_TRANSFORM_WH** | **1.024** | 981 | 44 | 653 |
| DEV_TRANSFORM_WH | 640 | 486 | 154 | 737 |
| PRO_TRANSFORM_COMPLEX_WH | 636 | 631 | 5 | 564 |
| PRO_BI_WH | 310 | 306 | 4 | 736 |
| PRO_INTERNAL_BI_WH | 221 | 210 | 11 | 489 |
| STREAMLIT_APPS_WH | 150 | 149 | 1 | 136 |
| DEV_LOAD_WH | 148 | 135 | 14 | 610 |
| BAIKAL_DP_WH | 55 | 50 | 5 | 737 |
| Otros | 194 | 175 | 19 | ~1.000 |
| **TOTAL** | **~5.305** | **~4.497** | **~809** | **~5.763** |

**Hallazgo clave:** Los 3 warehouses de producción (PRO_LOAD_WH + PRO_TRANSFORM_WH + PRO_TRANSFORM_COMPLEX_WH) consumen **3.587 créditos (67,6%)** del total.

### 1.2 Top Queries Más Costosas (últimos 7 días)

| # | Warehouse | Segundos | Base de Datos | Operación |
|---|-----------|----------|---------------|-----------|
| 1 | PRO_TRANSFORM_COMPLEX_WH | 5.998s | PRO_0_STAGING_DB | Query compleja con UNION ALL (ES_STRATOR_BO_L1) |
| 2-6 | PRO_TRANSFORM_WH | 683-887s | ES_COVADONGA | `CALL REFRESH_CLONE_PARCEL()` |
| 7-8 | FINOPS_WH | 680s | PRO_0_STAGING_BACKUP_DB | `SP_DAILY_BACKUP()` + `CREATE DATABASE CLONE` |
| 9-11 | PRO_INTERNAL_BI_WH | 597-598s | PRO_0_STAGING_DB | Queries analíticas complejas (ES_STRATOR_BO_L1) |
| 12-13 | PRO_LOAD_WH | 546-547s | PRO_0_STAGING_BACKUP_DB | Backup + Clone |
| 14-22 | PRO_LOAD_WH | 203-257s | PRO_0_STAGING_DB | `COPY INTO ZCDS_6_MAT_MD_V` (ES_ESPADA_MASTERS) |
| 23-50 | PRO_TRANSFORM_WH | 170-207s | ES_COVADONGA | `REFRESH_CLONE_TESEO()` + `CREATE TABLE CLONE` |

**Hallazgos clave:**
- **REFRESH_CLONE_PARCEL()** y **REFRESH_CLONE_TESEO()** son las operaciones más costosas recurrentes (683-887s cada una)
- **CLONE de PRO_0_STAGING_DB** diario consume ~680s en FINOPS_WH
- **COPY INTO ZCDS_6_MAT_MD_V** (ES_ESPADA_MASTERS) son operaciones HVR de carga masiva que consumen 200-257s cada una
- **Queries analíticas de ADRIANLOPEZ** en ES_STRATOR_BO_L1 consumen ~600s cada una

### 1.3 Tablas Más Grandes en PRO_0_STAGING_DB

| Schema | Tabla | Filas | Size (MB) |
|--------|-------|-------|-----------|
| FR_FRISBI | SALES_AZ9_A_0011 | 5.256.765.083 | 216.203 |
| ES_TESEO | TW_GPS_HISTORIC_IO | 14.901.291.916 | 160.638 |
| FR_FRISBI | SALES_AZ9_A_0011_BACKUP | 4.257.265.297 | 156.648 |
| ES_ESPADA | SALES_AZ7_O014S00 | 3.917.818.314 | 128.058 |
| ES_ESPADA | SALES_AZ7_OR014S00_SEGURIDAD | 2.220.401.275 | 70.932 |
| ES_ESPADA | SALES_AZ7_OR014S00 | 2.220.401.275 | 70.932 |
| ES_TESEO | TW_HISTORIC_POSIC | 2.346.109.051 | 59.070 |
| FR_STRATOR_BO_L4 | SALES_L4_OPERATIONPRODUITREPORTING | 1.151.716.270 | 55.443 |
| ES_CDI_PARCEL | PLSTMPIMAGENES | 854.635 | 54.056 |
| ES_ESPADA | STOCK_AZ7_O015S00 | 2.776.220.914 | 51.698 |

**Total PRO_0_STAGING_DB: 4.107 tablas, 2.532.287 MB (~2,5 TB)**

### 1.4 Tablas Más Grandes en ES_COVADONGA

| Schema | Tabla | Filas | Size (MB) |
|--------|-------|-------|-----------|
| ES_TESEO | TW_GPS_HISTORIC_IO | 14.901.291.916 | 160.638 |
| ES_PARCEL | TSIMAGES | 9.435.390 | 83.046 |
| ES_PARCEL | RHO | 444.884.187 | 81.641 |
| ES_PARCEL | PLSTMPIMAGENES | 1.403.344 | 75.218 |
| ES_TESEO | TW_HISTORIC_POSIC | 2.346.109.051 | 59.070 |
| ES_PARCEL | ES_CDI_PLSTMPIMAGENES | 850.578 | 53.803 |
| ES_PARCEL | ES_ALERTRAN_PLSTMPIMAGENES | 626.269 | 42.652 |
| ES_TESEO_BCK | TW_HISTORIC_POSIC | 821.391.069 | 22.816 |
| ES_PARCEL | ES_ALERTRAN_RHO | 136.760.946 | 26.564 |
| ES_TESEO_BCK | TW_GPS_HISTORIC_IO | 2.491.795.640 | 22.136 |

**Total ES_COVADONGA: 4.631 tablas + 346 vistas + 2 materialized views, ~1,34 TB**

### 1.5 Objetos HVR Identificados en PRO_0_STAGING_DB

| Schema | Tabla | Filas | Size (MB) | Tipo |
|--------|-------|-------|-----------|------|
| ES_ALERTRAN_PARCEL | R2CAPTURASEXPEDICIONES | 9.916.548 | 4.570 | Captura |
| ES_ALERTRAN_PARCEL | I2EXPHUELLACAP | 209.883.155 | 3.227 | Integración |
| ES_ALERTRAN_PARCEL | I2COSTECAPILAR | 93.953.531 | 865 | Integración |
| ES_ALERTRAN_PARCEL | R2INTERNALCHARGES | 90.170.553 | 714 | Captura |
| ES_ALERTRAN_PARCEL | CDRIMGHISTORICO | 44.459.042 | 531 | Histórico |
| ES_SALESFORCE_PHARMA | PEDIDO_HISTORY | 5.455.774 | 127 | History SF |
| ES_SALESFORCE_PHARMA | LINEA_DE_PEDIDO_HISTORY | 4.097.970 | 69 | History SF |

---

## 2. PLAN DE REDUCCIÓN DE COSTES (-40%)

### FASE 1: QUICK WINS (Semanas 1-2) → Objetivo: -15% a -20%

#### 1.1 Eliminar CLONE diario de PRO_0_STAGING_DB
**Impacto: ~5% del coste total**

El `CREATE DATABASE CLONE PRO_0_STAGING_DB` diario consume ~680s en FINOPS_WH. Con 2,5 TB de datos, cada clone consume créditos masivos de compute.

**Acción:**
- Reemplazar CLONE por backup incremental (solo tablas modificadas)
- Alternativa: usar Time Travel de Snowflake (0-90 días) en vez de CLONE completo
- Si el backup es para DR, usar Replication Group de Snowflake en vez de CLONE

**Configuración:**
```sql
-- Eliminar task de CLONE diario
DROP TASK IF EXISTS PRO_0_STAGING_BACKUP_DB.PUBLIC.TASK_DAILY_CLONE;

-- Crear backup incremental solo de tablas grandes modificadas
CREATE TASK PRO_0_STAGING_BACKUP_DB.PUBLIC.TASK_INCREMENTAL_BACKUP
  WAREHOUSE = FINOPS_WH
  SCHEDULE = 'USING CRON 0 2 * * *'
AS
  -- Solo tablas que cambiaron desde último backup
  SELECT * FROM PRO_0_STAGING_DB.FR_FRISBI.SALES_AZ9_A_0011
  WHERE last_modified > (SELECT MAX(last_modified) FROM BACKUP_DB.FR_FRISBI.SALES_AZ9_A_0011);
```

#### 1.2 Optimizar REFRESH_CLONE_PARCEL() y REFRESH_CLONE_TESEO()
**Impacto: ~8% del coste total**

Estas stored procedures consumen 683-887s cada una en PRO_TRANSFORM_WH. El patrón `CREATE TABLE CLONE` + `REFRESH_CLONE` es extremadamente costoso porque:
- Clona tablas de 160.638 MB (TW_GPS_HISTORIC_IO)
- Clona tablas de 59.070 MB (TW_HISTORIC_POSIC)
- Se ejecuta múltiples veces al día (5+ ejecuciones observadas)

**Acción:**
- Reemplazar CLONE por TRUNCATE + INSERT incremental
- Usar Snowflake Streams para capturar solo cambios
- Reducir frecuencia de refresh de cada 4h a cada 12h para tablas históricas

**Configuración:**
```sql
-- En vez de: CALL REFRESH_CLONE_PARCEL()
-- Usar:
CREATE OR REPLACE PROCEDURE ES_COVADONGA.ES_PARCEL.REFRESH_INCREMENTAL_PARCEL()
RETURNS STRING
LANGUAGE SQL
AS $$
BEGIN
  -- Solo actualizar registros modificados en las últimas 12h
  MERGE INTO ES_COVADONGA.ES_PARCEL.TARGET_TABLE t
  USING (
    SELECT * FROM PRO_0_STAGING_DB.ES_PARCEL.SOURCE_TABLE
    WHERE last_modified > DATEADD(hour, -12, CURRENT_TIMESTAMP())
  ) s ON t.id = s.id
  WHEN MATCHED THEN UPDATE SET *
  WHEN NOT MATCHED THEN INSERT *;
  
  RETURN 'Incremental refresh completed';
END;
$$;
```

#### 1.3 Reducir frecuencia de COPY INTO para ES_ESPADA_MASTERS
**Impacto: ~3% del coste total**

Las operaciones `COPY INTO ZCDS_6_MAT_MD_V` consumen 200-257s cada una y se repiten frecuentemente.

**Acción HVR:**
- Aumentar `MaxFileSize` en FileFormat para reducir número de archivos staging
- Aumentar `BurstCommitFrequency` a CYCLE (si no está ya)
- Usar `Coalesce` en Capture para reducir volumen de cambios

**Configuración HVR:**
```
# En el canal HVR para ES_ESPADA_MASTERS:
Action: FileFormat
Parameter: MaxFileSize = 256MB  # Aumentar desde valor actual

Action: Integrate
Parameter: Method = BURST
Parameter: BurstCommitFrequency = CYCLE

Action: Capture
Parameter: Coalesce
```

#### 1.4 Aplicar Coalesce en Capture para todos los canales
**Impacto: ~5% del coste total**

Coalesce fusiona múltiples operaciones sobre la misma fila en una sola operación. Actualmente NO está activo en la mayoría de canales.

**Configuración HVR:**
```
# Para cada canal de replicación:
Action: Capture
Parameter: Coalesce
```

**Verificación:**
```bash
# En el hub HVR, verificar que Coalesce está activo:
hvrcli -l <channel> | grep -i coalesce
```

### FASE 2: OPTIMIZACIÓN MEDIA (Semanas 3-4) → Objetivo: -10% a -15%

#### 2.1 Migrar tablas de staging a TRANSIENT
**Impacto: ~3% del coste total**

Las tablas de PRO_0_STAGING_DB son regenerables. Convertirlas a TRANSIENT elimina el Fail-safe period (7 días de storage extra).

**Acción:**
```sql
-- Convertir tablas grandes de staging a TRANSIENT
ALTER TABLE PRO_0_STAGING_DB.FR_FRISBI.SALES_AZ9_A_0011 SET TRANSIENT;
ALTER TABLE PRO_0_STAGING_DB.ES_TESEO.TW_GPS_HISTORIC_IO SET TRANSIENT;
ALTER TABLE PRO_0_STAGING_DB.ES_ESPADA.SALES_AZ7_O014S00 SET TRANSIENT;
-- ... (repetir para las 30 tablas más grandes)
```

**Nota:** Las tablas TRANSIENT no tienen Fail-safe. Asegurar que el proceso HVR puede regenerar los datos.

#### 2.2 Implementar NoBeforeUpdate en Capture
**Impacto: ~3% del coste total**

Eliminar la captura del "before" en updates reduce el volumen de datos transportados.

**Configuración HVR:**
```
Action: Capture
Parameter: NoBeforeUpdate
```

**Nota:** Solo aplicar en tablas donde no se necesite auditoría de valores anteriores.

#### 2.3 Optimizar queries analíticas de ES_STRATOR_BO_L1
**Impacto: ~2% del coste total**

Las queries de ADRIANLOPEZ en ES_STRATOR_BO_L1 consumen ~600s cada una. Son queries con múltiples JOINs y UNION ALL sobre tablas de 27.713 MB.

**Acción:**
- Crear vistas materializadas para las consultas más frecuentes
- Añadir clustering keys en las tablas grandes
- Mover estas queries a PRO_INTERNAL_BI_WH con warehouse más pequeño

**Configuración:**
```sql
-- Crear vista materializada para la query recurrente
CREATE MATERIALIZED VIEW PRO_0_STAGING_DB.ES_STRATOR_BO_L1.MV_PRODUCT_REFERENCES AS
SELECT 
    irt.CODEREFFOURNISSEURTABAC AS reference_fournisseur,
    p.FK_REFERENCEPRODUITFOURNISSEUR
FROM PRO_0_STAGING_DB.ES_STRATOR_BO_L1.PRODUCT_L1_PRODUIT p
INNER JOIN PRO_0_STAGING_DB.ES_STRATOR_BO_L1.PRODUCT_L1_REFERENCEPRODUITFOURNISSEUR rpf
    ON p.FK_REFERENCEPRODUITFOURNISSEUR = rpf.ID
INNER JOIN PRO_0_STAGING_DB.ES_STRATOR_BO_L1.PRODUCT_L1_INFORMATIONREFERENCETABAC irt
    ON rpf.FK_INFORMATIONREFERENCETABAC = irt.ID
WHERE irt.datesuppression IS NULL;

-- Añadir clustering key
ALTER TABLE PRO_0_STAGING_DB.ES_STRATOR_BO_L1.PRODUCT_L1_PRODUIT
CLUSTER BY (FK_REFERENCEPRODUITFOURNISSEUR);
```

#### 2.4 Reducir retención de tablas de historial HVR
**Impacto: ~2% del coste total**

Las tablas `*_HISTORY` de Salesforce (PEDIDO_HISTORY, LINEA_DE_PEDIDO_HISTORY, etc.) acumulan datos innecesariamente.

**Acción:**
```sql
-- Reducir retención de 30 días a 7 días para tablas HVR history
CREATE TASK PRO_0_STAGING_DB.ES_SALESFORCE_PHARMA.TASK_PURGE_HISTORY
  WAREHOUSE = PRO_LOAD_WH
  SCHEDULE = 'USING CRON 0 3 * * *'
AS
  DELETE FROM PRO_0_STAGING_DB.ES_SALESFORCE_PHARMA.PEDIDO_HISTORY
  WHERE created_date < DATEADD(day, -7, CURRENT_DATE());
```

### FASE 3: OPTIMIZACIÓN AVANZADA (Semanas 5-8) → Objetivo: -10% a -15%

#### 3.1 Implementar APPEND method para Snowflake (HVR 6.2.5+)
**Impacto: ~5% del coste total**

El método APPEND inserta cambios directamente en tablas con TimeKey, sin necesidad de BURST intermedio. Elimina la creación de tablas `_b` intermedias.

**Requisito:** Todas las tablas deben tener TimeKey definido.

**Configuración HVR:**
```
# Primero, definir TimeKey en ColumnProperties para cada tabla:
Action: ColumnProperties
Parameter: Name = <columna_timestamp>
Parameter: TimeKey

# Luego cambiar el método de integración:
Action: Integrate
Parameter: Method = APPEND
```

**Nota:** Implementar durante ventana de mantenimiento. Verificar que todas las tablas tengan TimeKey antes del cambio.

#### 3.2 Implementar NoTriggerFiring en Integrate
**Impacto: ~2% del coste total**

Deshabilita triggers en las tablas destino durante la integración HVR.

**Configuración HVR:**
```
Action: Integrate
Parameter: NoTriggerFiring
```

**Nota:** Solo para PRO_0_STAGING_DB (staging). Evaluar cuidadosamente para ES_COVADONGA.

#### 3.3 Programar captura en ventanas de menor coste
**Impacto: ~2% del coste total**

Programar captura HVR en horarios de menor demanda.

**Configuración HVR:**
```
Action: Scheduling
Parameter: CaptureStartTimes = 0 2 * * *    # 2 AM diario
Parameter: IntegrateStartTimes = 0 3 * * *  # 3 AM diario
Parameter: TimeContext = * * * * 1-5         # Solo lun-vie
```

#### 3.4 Eliminar tablas duplicadas/backup innecesarias
**Impacto: ~3% del coste total**

Se identificaron tablas BACKUP duplicadas que consumen ~156.648 MB solo en FR_FRISBI.

**Acción:**
```sql
-- Eliminar tablas backup duplicadas
DROP TABLE IF EXISTS PRO_0_STAGING_DB.FR_FRISBI.SALES_AZ9_A_0011_BACKUP;
DROP TABLE IF EXISTS PRO_0_STAGING_DB.FR_STRATOR_BO_L4.SALES_L4_OPERATIONPRODUITREPORTING_BACKUP;
DROP TABLE IF EXISTS PRO_0_STAGING_DB.ES_ESPADA.STOCK_AZ7_O022S00_SEGURIDAD;
DROP TABLE IF EXISTS PRO_0_STAGING_DB.ES_ESPADA.SALES_AZ7_O014S00_SEGURIDAD;
DROP TABLE IF EXISTS PRO_0_STAGING_DB.ES_ESPADA.SALES_AZ7_OR014S00_SEGURIDAD;
```

#### 3.5 Optimizar checkpoint frequency
**Impacto: ~1% del coste total**

**Configuración HVR:**
```
# Para transacciones largas frecuentes:
Location Property: Capture_Checkpoint_Frequency = 600
```

---

## 3. RESUMEN DE IMPACTO ESTIMADO

| Fase | Acción | Impacto | Acumulado |
|------|--------|---------|-----------|
| 1.1 | Eliminar CLONE diario | -5% | -5% |
| 1.2 | Optimizar REFRESH_CLONE | -8% | -13% |
| 1.3 | Reducir COPY INTO frequency | -3% | -16% |
| 1.4 | Coalesce en Capture | -5% | -21% |
| 2.1 | TRANSIENT tables | -3% | -24% |
| 2.2 | NoBeforeUpdate | -3% | -27% |
| 2.3 | Optimizar queries analíticas | -2% | -29% |
| 2.4 | Reducir retención HISTORY | -2% | -31% |
| 3.1 | APPEND method | -5% | -36% |
| 3.2 | NoTriggerFiring | -2% | -38% |
| 3.3 | Scheduling en ventanas | -2% | -40% |
| 3.4 | Eliminar duplicados | -3% | -43% |
| 3.5 | Checkpoint tuning | -1% | -44% |

**Objetivo: -40% a -44% reducción en créditos Snowflake**

---

## 4. MONITOREO Y VERIFICACIÓN

### 4.1 Queries de verificación post-implementación

```sql
-- Verificar reducción de créditos por warehouse
SELECT 
    warehouse_name,
    SUM(credits_used) as total_credits,
    DATE_TRUNC('week', start_time) as week
FROM SNOWFLAKE.ACCOUNT_USAGE.WAREHOUSE_METERING_HISTORY
WHERE start_time >= DATEADD(day, -30, CURRENT_DATE())
GROUP BY warehouse_name, DATE_TRUNC('week', start_time)
ORDER BY week, total_credits DESC;

-- Verificar reducción de queries costosas
SELECT 
    warehouse_name,
    AVG(execution_time / 1000) as avg_exec_seconds,
    COUNT(*) as query_count
FROM SNOWFLAKE.ACCOUNT_USAGE.QUERY_HISTORY
WHERE start_time >= DATEADD(day, -7, CURRENT_DATE())
    AND (database_name LIKE '%PRO_0_STAGING%' OR database_name LIKE '%ES_COVADONGA%')
GROUP BY warehouse_name
ORDER BY avg_exec_seconds DESC;

-- Verificar storage reducido
SELECT 
    database_name,
    SUM(bytes) / POWER(1024, 3) as size_gb
FROM SNOWFLAKE.ACCOUNT_USAGE.TABLE_STORAGE_METRICS
WHERE database_name IN ('PRO_0_STAGING_DB', 'ES_COVADONGA')
GROUP BY database_name;
```

### 4.2 KPIs a monitorizar

| KPI | Baseline | Objetivo |
|-----|----------|----------|
| Créditos/mes PRO_LOAD_WH | 1.927 | <1.156 (-40%) |
| Créditos/mes PRO_TRANSFORM_WH | 1.024 | <614 (-40%) |
| Créditos/mes PRO_TRANSFORM_COMPLEX_WH | 636 | <382 (-40%) |
| Storage PRO_0_STAGING_DB | 2,5 TB | <1,5 TB (-40%) |
| Storage ES_COVADONGA | 1,34 TB | <938 GB (-30%) |
| Tiempo promedio REFRESH_CLONE | 780s | <300s (-62%) |
| Número de CLONEs diarios | 1 | 0 (-100%) |

---

## 5. RIESGOS Y MITIGACIONES

| Riesgo | Probabilidad | Impacto | Mitigación |
|--------|-------------|---------|------------|
| Pérdida de datos por TRANSIENT tables | Bajo | Alto | Verificar que HVR puede regenerar datos antes de convertir |
| Inconsistencia por NoBeforeUpdate | Medio | Medio | Solo aplicar en tablas sin requisito de auditoría |
| Duplicados por cambio BURST→APPEND | Medio | Alto | Implementar en ventana de mantenimiento con Compare previo |
| Regresión en queries analíticas | Bajo | Medio | Crear vistas materializadas antes de eliminar queries directas |
| Fallo en backup incremental | Bajo | Alto | Mantener Time Travel como fallback |

---

## 6. ORDEN DE EJECUCIÓN RECOMENDADO

1. **Semana 1:** Fase 1.4 (Coalesce) → Sin riesgo, impacto inmediato
2. **Semana 1:** Fase 1.3 (COPY INTO optimization) → Bajo riesgo
3. **Semana 2:** Fase 1.1 (Eliminar CLONE) → Medio impacto, requiere validación
4. **Semana 2:** Fase 1.2 (Optimizar REFRESH_CLONE) → Requiere cambios en stored procedures
5. **Semana 3:** Fase 2.1 (TRANSIENT tables) → Requiere verificación de regenerabilidad
6. **Semana 3:** Fase 2.2 (NoBeforeUpdate) → Requiere auditoría de tablas
7. **Semana 4:** Fase 2.3 (Queries analíticas) → Requiere creación de vistas materializadas
8. **Semana 4:** Fase 2.4 (Retención HISTORY) → Bajo riesgo
9. **Semana 5-6:** Fase 3.1 (APPEND method) → Requiere ventana de mantenimiento
10. **Semana 6:** Fase 3.2 (NoTriggerFiring) → Requiere evaluación de triggers
11. **Semana 7:** Fase 3.3 (Scheduling) → Bajo riesgo
12. **Semana 7:** Fase 3.4 (Eliminar duplicados) → Requiere verificación de dependencias
13. **Semana 8:** Fase 3.5 (Checkpoint tuning) → Bajo riesgo
