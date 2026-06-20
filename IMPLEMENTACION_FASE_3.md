# IMPLEMENTACION FASE 3 - Optimizacion HVR 6.2
# Reduccion de costes: objetivo -40% (5.305 -> ~3.183 creditos/mes)
# Fecha: 2026-06-20
# Autor: Arquitectura de Datos

---

## INDICE

1. [Resumen Ejecutivo](#resumen)
2. [Accion 3.1 - Implementar APPEND method para Snowflake](#accion-31)
3. [Accion 3.2 - Implementar NoTriggerFiring en Integrate](#accion-32)
4. [Accion 3.3 - Programar captura en ventanas de menor coste](#accion-33)
5. [Accion 3.4 - Eliminar tablas duplicadas/backup innecesarias](#accion-34)
6. [Accion 3.5 - Optimizar checkpoint frequency](#accion-35)
7. [Plan de Ejecucion y Dependencias](#plan)
8. [Metricas de Seguimiento](#metricas)

---

## RESUMEN EJECUTIVO

La Fase 3 agrupa 5 acciones de optimizacion enfocadas en mejorar la eficiencia
operativa de la replicacion HVR hacia Snowflake. Estas acciones complementan las
Fases 1 y 2, y contribuyen al objetivo global de reduccion del 40% en costes.

| Accion | Ahorro estimado | Riesgo | Tiempo |
|--------|----------------|--------|--------|
| 3.1 - APPEND method para Snowflake | ~600 creditos/medio | Medio | 3-5 dias |
| 3.2 - NoTriggerFiring en Integrate | ~100 creditos/mes | Bajo | 1 dia |
| 3.3 - Programar en ventanas de menor coste | ~300 creditos/mes | Bajo | 1-2 dias |
| 3.4 - Eliminar tablas duplicadas/backup | ~400 creditos/mes | Alto | 3-5 dias |
| 3.5 - Optimizar checkpoint frequency | ~100 creditos/mes | Bajo | 0.5 dia |
| **TOTAL FASE 3** | **~1.500 creditos/mes** | | **8.5-13.5 dias** |

**Contexto de datos:**
- PRO_0_STAGING_DB: 4.107 tablas, 2,5 TB totales
- ES_COVADONGA: esquema principal de reporting
- Tablas BACKUP duplicadas: ~156 GB solo en FR_FRISBI
- Metodo actual: BURST (crea tablas _b intermedias)
- Checkpoint frequency actual: 300s (valor por defecto)

**Requisitos previos:**
- HVR 6.2.5 o superior instalado (para APPEND method)
- Acceso administrativo a HVR Hub Server
- Permisos ALTER en tablas destino Snowflake
- Ventana de mantenimiento programada

---

## ACCION 3.1 - IMPLEMENTAR APPEND METHOD PARA SNOWFLAKE

### 3.1.1 Descripcion Tecnica

**Que es APPEND:**
APPEND es un metodo de integracion disponible en HVR 6.2.5+ que inserta los
cambios directamente en las tablas destino utilizando la columna TimeKey,
sin crear tablas intermedias _b (BURST tables). Esto elimina la sobrecarga
de crear, llenar y eliminar tablas temporales en cada ciclo de replicacion.

**Por que implementarlo:**
- El metodo actual BURST crea tablas intermedias _b por cada ciclo
- Cada tabla _b consume storage temporal y genera I/O adicional
- Para 4.107 tablas, esto representa miles de operaciones DDL por hora
- APPEND reduce el tiempo de integracion y el consumo de creditos Snowflake

**Impacto esperado:**
- Eliminacion de ~4.107 tablas _b intermedias por ciclo
- Reduccion de I/O en Snowflake: ~30% menos operaciones DDL
- Ahorro estimado: ~600 creditos/mes (compute + storage temporal)
- Mejora en latencia de integracion: ~20-40% mas rapido

**Requisito critico:**
TODAS las tablas deben tener TimeKey definido. Sin TimeKey, APPEND no puede
determinar el orden de los cambios y la replicacion fallara.

**Procedimiento de validacion TimeKey:**
Antes de activar APPEND, verificar que cada tabla destino tiene la columna
TimeKey configurada correctamente en HVR.

### 3.1.2 Pasos de Implementacion

**PASO 1: Verificar version de HVR**

```bash
# Conectar al HVR Hub Server
ssh hvradmin@hvr-hub-server

# Verificar version instalada
hvrversion

# Salida esperada: HVR 6.2.5 o superior
# Si la version es inferior, actualizar primero:
# ./hvrinstall --upgrade /path/to/hvr-6.2.5-installer
```

**PASO 2: Verificar que todas las tablas tienen TimeKey**

```sql
-- En Snowflake, verificar columnas TimeKey en tablas destino
USE DATABASE PRO_0_STAGING_DB;

SELECT
    TABLE_SCHEMA,
    TABLE_NAME,
    COLUMN_NAME,
    DATA_TYPE
FROM INFORMATION_SCHEMA.COLUMNS
WHERE COLUMN_NAME LIKE '%TIMEKEY%'
   OR COLUMN_NAME LIKE '%HVR_%_TIME%'
ORDER BY TABLE_SCHEMA, TABLE_NAME;

-- Verificar que no hay tablas SIN TimeKey
SELECT
    t.TABLE_SCHEMA,
    t.TABLE_NAME
FROM INFORMATION_SCHEMA.TABLES t
LEFT JOIN INFORMATION_SCHEMA.COLUMNS c
    ON t.TABLE_SCHEMA = c.TABLE_SCHEMA
    AND t.TABLE_NAME = c.TABLE_NAME
    AND (c.COLUMN_NAME LIKE '%TIMEKEY%' OR c.COLUMN_NAME LIKE '%HVR_%_TIME%')
WHERE t.TABLE_SCHEMA = 'STAGING'
  AND t.TABLE_TYPE = 'BASE TABLE'
  AND c.COLUMN_NAME IS NULL;
```

**PASO 3: Configurar APPEND en HVR (via HVR Console o hvrcli)**

```bash
# Opcion A: Via hvrcli
hvrcli

# Seleccionar el canal correspondiente
ch_list
# Anotar el nombre del canal (ej: SNOWFLAKE_REPLICATION)

# Configurar APPEND para el canal
ch_edit -c SNOWFLAKE_REPLICATION

# Navegar a: Actions > Integrate > Method
# Cambiar de BURST a APPEND

# Guardar y salir
ch_save
exit

# Opcion B: Via HVR Console (GUI)
# 1. Abrir HVR Console en navegador
# 2. Navegar a: Channels > [canal] > Actions
# 3. Editar accion Integrate
# 4. En "Method", seleccionar "APPEND"
# 5. Aplicar cambios
```

**PASO 4: Configurar TimeKey en tablas que lo requieran**

```sql
-- Si faltan columnas TimeKey, agregarlas
-- NOTA: Esto requiere coordinacion con el equipo de HVR

-- Ejemplo para una tabla especifica
ALTER TABLE PRO_0_STAGING_DB.STAGING.TABLA_EJEMPLO
ADD COLUMN HVR_REPLICATION_TIME TIMESTAMP_LTZ DEFAULT CURRENT_TIMESTAMP();

-- Crear indice para optimizar APPEND
CREATE INDEX IDX_HVR_TIMEKEY ON PRO_0_STAGING_DB.STAGING.TABLA_EJEMPLO
(HVR_REPLICATION_TIME);
```

**PASO 5: Prueba piloto con subset de tablas**

```bash
# Crear subconjunto de prueba (10 tablas representativas)
hvrcli
ch_edit -c SNOWFLAKE_REPLICATION

# Configurar Location Property para filtrar tablas de prueba
# Tables = TABLA_1, TABLA_2, TABLA_3, TABLA_4, TABLA_5,
#          TABLA_6, TABLA_7, TABLA_8, TABLA_9, TABLA_10

# Activar APPEND solo para este subconjunto
ch_save
exit

# Iniciar replicacion de prueba
hvrcli
ch_refresh -c SNOWFLAKE_REPLICATION --refresh
```

**PASO 6: Activar APPEND para todas las tablas**

```bash
# Una vez validada la prueba piloto
hvrcli
ch_edit -c SNOWFLAKE_REPLICATION

# Restaurar lista completa de tablas
# Tables = ALL (o lista completa)

# Verificar que Method = APPEND esta activo
ch_verify -c SNOWFLAKE_REPLICATION

# Guardar configuracion
ch_save
exit
```

### 3.1.3 Verificacion Post-Implementacion

```sql
-- Verificar que no se crean tablas _b intermedias
USE DATABASE PRO_0_STAGING_DB;

SELECT
    TABLE_SCHEMA,
    TABLE_NAME,
    BYTES / POWER(1024, 3) AS SIZE_GB
FROM INFORMATION_SCHEMA.TABLES
WHERE TABLE_NAME LIKE '%\_b' ESCAPE '\\'
  AND TABLE_SCHEMA = 'STAGING'
ORDER BY BYTES DESC;

-- Resultado esperado: 0 filas (no hay tablas _b)

-- Verificar que TimeKey se esta utilizando correctamente
SELECT
    TABLE_SCHEMA,
    TABLE_NAME,
    MAX(HVR_REPLICATION_TIME) AS LAST_REPLICATION
FROM PRO_0_STAGING_DB.STAGING.TABLA_EJEMPLO
GROUP BY TABLE_SCHEMA, TABLE_NAME;

-- Verificar rendimiento de integracion
-- En HVR: Revisar metricas de ciclo de integracion
-- Comparar tiempos antes/desactivar APPEND
```

### 3.1.4 Riesgos

| Riesgo | Probabilidad | Impacto | Mitigacion |
|--------|-------------|---------|------------|
| Tablas sin TimeKey causan fallo | Alta | Alto | Verificar TODAS las tablas antes de activar APPEND |
| Perdida de datos por orden incorrecto | Baja | Critico | Validar TimeKey con datos historicos antes de activar |
| Incompatibilidad con HVR < 6.2.5 | Media | Alto | Verificar version antes de iniciar |
| Degradacion de rendimiento en tablas grandes | Media | Medio | Monitorear y ajustar batch size si necesario |

### 3.1.5 Rollback Procedure

```bash
# Si APPEND causa problemas, revertir a BURST

# Paso 1: Detener replicacion
hvrcli
ch_stop -c SNOWFLAKE_REPLICATION

# Paso 2: Revertir a BURST
hvrcli
ch_edit -c SNOWFLAKE_REPLICATION
# Actions > Integrate > Method = BURST
ch_save

# Paso 3: Limpiar tablas _b residuales si existen
# (En Snowflake)
DROP TABLE IF EXISTS PRO_0_STAGING_DB.STAGING.TABLA_EJEMPLO_B;

# Paso 4: Reiniciar replicacion
hvrcli
ch_start -c SNOWFLAKE_REPLICATION

# Paso 5: Verificar que BURST funciona correctamente
# Monitorear durante 24 horas
```

### 3.1.6 Tiempo Estimado

| Actividad | Duracion |
|-----------|----------|
| Verificacion de version HVR | 0.5 hora |
| Validacion TimeKey en tablas | 2-4 horas |
| Configuracion APPEND en HVR | 1 hora |
| Prueba piloto (10 tablas) | 4-8 horas |
| Activacion completa | 1 hora |
| Monitoreo post-activacion | 24 horas |
| **TOTAL** | **3-5 dias** |

---

## ACCION 3.2 - IMPLEMENTAR NOTRIGGERFIRING EN INTEGRATE

### 3.2.1 Descripcion Tecnica

**Que es NoTriggerFiring:**
NoTriggerFiring es un parametro de la accion Integrate en HVR que deshabilita
los triggers en las tablas destino durante la integracion. Cuando HVR inserta
datos, los triggers no se ejecutan, lo que reduce el consumo de compute.

**Por que implementarlo:**
- Las tablas de staging en PRO_0_STAGING_DB pueden tener triggers de auditoria
- Estos triggers consumen creditos Snowflake en cada operacion DML
- Para datos de staging, los triggers son innecesarios (datos efimeros)
- ES_COVADONGA NO debe tener NoTriggerFiring (datos de reporting con triggers)

**Impacto esperado:**
- Reduccion de ~15% en creditos de compute por integracion
- Ahorro estimado: ~100 creditos/mes
- Sin impacto en datos de ES_COVADONGA

**Restriccion importante:**
Solo aplicar a PRO_0_STAGING_DB. ES_COVADONGA requiere triggers activos
para mantener integridad de datos de reporting.

### 3.2.2 Pasos de Implementacion

**PASO 1: Identificar triggers en tablas de staging**

```sql
-- Listar triggers en PRO_0_STAGING_DB
USE DATABASE PRO_0_STAGING_DB;

SELECT
    TRIGGER_SCHEMA,
    TRIGGER_NAME,
    EVENT_OBJECT_SCHEMA,
    EVENT_OBJECT_TABLE,
    ACTION_TIMING,
    EVENT_MANIPULATION
FROM INFORMATION_SCHEMA.TRIGGERS
WHERE EVENT_OBJECT_SCHEMA = 'STAGING'
ORDER BY EVENT_OBJECT_TABLE;

-- Documentar triggers existentes para referencia
```

**PASO 2: Configurar NoTriggerFiring en HVR**

```bash
# Conectar a HVR Hub Server
ssh hvradmin@hvr-hub-server

# Editar canal de replicacion
hvrcli
ch_edit -c SNOWFLAKE_REPLICATION

# Navegar a: Actions > Integrate > Parameters
# Agregar parametro: NoTriggerFiring = true

# Alternativamente, via HVR Console:
# 1. Channels > [canal] > Actions > Integrate
# 2. En "Parameters", agregar:
#    - Name: NoTriggerFiring
#    - Value: true
# 3. Aplicar cambios

ch_save
exit
```

**PASO 3: Verificar que ES_COVADONGA NO se ve afectado**

```bash
# Verificar configuracion del canal ES_COVADONGA
hvrcli
ch_edit -c ES_COVADONGA_REPLICATION

# Confirmar que NoTriggerFiring NO esta activo
# Actions > Integrate > Parameters
# NoTriggerFiring debe estar ausente o en false

ch_save
exit
```

**PASO 4: Prueba de integracion**

```bash
# Forzar ciclo de integracion
hvrcli
ch_refresh -c SNOWFLAKE_REPLICATION --refresh

# Monitorear logs de HVR
tail -f /var/log/hvr/hub.log | grep -i "trigger\|integrate"
```

### 3.2.3 Verificacion Post-Implementacion

```sql
-- Verificar que triggers NO se ejecutan durante integracion HVR
-- (Monitorear durante un ciclo completo)

-- En Snowflake, verificar que no hay registros de triggers
SELECT *
FROM PRO_0_STAGING_DB.INFORMATION_SCHEMA.QUERY_HISTORY
WHERE QUERY_TEXT LIKE '%TRIGGER%'
  AND START_TIME >= DATEADD(HOUR, -1, CURRENT_TIMESTAMP())
ORDER BY START_TIME DESC;

-- Resultado esperado: No hay queries de triggers durante integracion HVR

-- Verificar que datos se integran correctamente
SELECT
    TABLE_NAME,
    COUNT(*) AS ROW_COUNT,
    MAX(HVR_REPLICATION_TIME) AS LAST_UPDATE
FROM PRO_0_STAGING_DB.STAGING.TABLA_EJEMPLO
GROUP BY TABLE_NAME;
```

### 3.2.4 Riesgos

| Riesgo | Probabilidad | Impacto | Mitigacion |
|--------|-------------|---------|------------|
| Triggers necesarios se deshabilitan | Baja | Medio | Solo aplicar a staging, no a ES_COVADONGA |
| Auditoria de datos se pierde | Baja | Bajo | Staging es efemero, auditoria no es critico |
| Configuracion incorrecta afecta ES_COVADONGA | Media | Alto | Verificar canales por separado |

### 3.2.5 Rollback Procedure

```bash
# Si NoTriggerFiring causa problemas

# Paso 1: Detener replicacion
hvrcli
ch_stop -c SNOWFLAKE_REPLICATION

# Paso 2: Eliminar parametro NoTriggerFiring
hvrcli
ch_edit -c SNOWFLAKE_REPLICATION
# Actions > Integrate > Parameters
# Eliminar NoTriggerFiring
ch_save

# Paso 3: Reiniciar replicacion
hvrcli
ch_start -c SNOWFLAKE_REPLICATION

# Paso 4: Verificar que triggers se ejecutan normalmente
```

### 3.2.6 Tiempo Estimado

| Actividad | Duracion |
|-----------|----------|
| Identificar triggers existentes | 1 hora |
| Configurar NoTriggerFiring | 0.5 hora |
| Verificar ES_COVADONGA no afectado | 0.5 hora |
| Prueba de integracion | 2-4 horas |
| Monitoreo | 4 horas |
| **TOTAL** | **1 dia** |

---

## ACCION 3.3 - PROGRAMAR CAPTURA EN VENTANAS DE MENOR COSTE

### 3.3.1 Descripcion Tecnica

**Que es la programacion por ventanas:**
HVR permite programar las operaciones de Capture e Integrate para que se ejecuten
en horarios especificos. Snowflake cobra menos creditos durante horas de baja
demanda (tipicamente 2AM-6AM hora del warehouse).

**Por que implementarlo:**
- El coste de compute en Snowflake varia segun la demanda del warehouse
- Horas valle (2AM-6AM) tienen menor coste por credito
- La replicacion HVR no requiere ejecucion continua 24/7
- Se puede acumular cambios y procesarlos en ventanas programadas

**Impacto esperado:**
- Reduccion de ~20% en coste de compute por integracion
- Ahorro estimado: ~300 creditos/mes
- Latencia de datos aumenta a maximo 4 horas (aceptable para staging)

**Ventana recomendada:**
- Capture: 2:00 AM - 6:00 AM (captura cambios acumulados)
- Integrate: 2:30 AM - 6:30 AM (integra cambios capturados)
- Fuera de ventana: HVR en standby, acumulando cambios en log

### 3.3.2 Pasos de Implementacion

**PASO 1: Analizar patrones de uso actual**

```bash
# Revisar logs de HVR para entender frecuencia actual
ssh hvradmin@hvr-hub-server

# Ver ciclos de integracion en ultimas 24 horas
grep "Integrate.*completed" /var/log/hvr/hub.log | tail -50

# Contar ciclos por hora
grep "Integrate.*completed" /var/log/hvr/hub.log | \
  awk '{print $2}' | cut -d: -f1 | sort | uniq -c | sort -rn
```

**PASO 2: Configurar CaptureStartTimes en HVR**

```bash
# Editar canal de replicacion
hvrcli
ch_edit -c SNOWFLAKE_REPLICATION

# Navegar a: Actions > Scheduling > CaptureStartTimes
# Configurar ventana de captura:
# CaptureStartTimes = 02:00-06:00

# Alternativamente, via HVR Console:
# 1. Channels > [canal] > Actions > Scheduling
# 2. En "Capture Start Times", especificar:
#    - Start: 02:00
#    - End: 06:00
# 3. Aplicar cambios

ch_save
exit
```

**PASO 3: Configurar IntegrateStartTimes en HVR**

```bash
hvrcli
ch_edit -c SNOWFLAKE_REPLICATION

# Navegar a: Actions > Scheduling > IntegrateStartTimes
# Configurar ventana de integracion (desfase de 30 min):
# IntegrateStartTimes = 02:30-06:30

ch_save
exit
```

**PASO 4: Configurar comportamiento fuera de ventana**

```bash
# Configurar HVR para acumular cambios fuera de ventana
hvrcli
ch_edit -c SNOWFLAKE_REPLICATION

# Location Property: Capture_Outside_Window = REFRESH
# Esto permite que capture acumule cambios incluso fuera de ventana

ch_save
exit
```

**PASO 5: Verificar configuracion**

```bash
# Verificar programacion
hvrcli
ch_verify -c SNOWFLAKE_REPLICATION

# Mostrar programacion actual
ch_list -v SNOWFLAKE_REPLICATION | grep -i "schedule\|window\|time"
```

### 3.3.3 Verificacion Post-Implementacion

```bash
# Monitorear que HVR respeta las ventanas programadas

# Verificar que no hay integracion fuera de ventana
tail -f /var/log/hvr/hub.log | grep -i "integrate\|capture"

# Despues de 24 horas, verificar patron
grep "Integrate.*completed" /var/log/hvr/hub.log | \
  awk '{print $1, $2}' | sort | uniq -c
```

```sql
-- En Snowflake, verificar que datos se integran correctamente
-- dentro de la ventana programada

SELECT
    DATE_TRUNC('HOUR', HVR_REPLICATION_TIME) AS HOUR,
    COUNT(*) AS ROWS_REPLICATED
FROM PRO_0_STAGING_DB.STAGING.TABLA_EJEMPLO
WHERE HVR_REPLICATION_TIME >= CURRENT_DATE()
GROUP BY DATE_TRUNC('HOUR', HVR_REPLICATION_TIME)
ORDER BY HOUR;

-- Resultado esperado: Mayoria de filas entre 2AM-6AM
```

### 3.3.4 Riesgos

| Riesgo | Probabilidad | Impacto | Mitigacion |
|--------|-------------|---------|------------|
| Acumulacion excesiva de cambios | Media | Medio | Monitorear tamano de log HVR |
| Latencia de datos aumenta | Alta | Bajo | Aceptable para datos de staging |
| Cambios urgentes se retrasan | Baja | Medio | Permitir refresh manual si necesario |
| Warehouse no disponible en ventana | Baja | Alto | Configurar auto-resume del warehouse |

### 3.3.5 Rollback Procedure

```bash
# Si la programacion causa problemas de latencia

# Paso 1: Detener replicacion
hvrcli
ch_stop -c SNOWFLAKE_REPLICATION

# Paso 2: Eliminar restricciones de ventana
hvrcli
ch_edit -c SNOWFLAKE_REPLICATION
# Actions > Scheduling > CaptureStartTimes = (vacio)
# Actions > Scheduling > IntegrateStartTimes = (vacio)
ch_save

# Paso 3: Reiniciar replicacion continua
hvrcli
ch_start -c SNOWFLAKE_REPLICATION

# Paso 4: Monitorear que vuelve a operacion normal
```

### 3.3.6 Tiempo Estimado

| Actividad | Duracion |
|-----------|----------|
| Analisis de patrones actuales | 2 horas |
| Configurar CaptureStartTimes | 0.5 hora |
| Configurar IntegrateStartTimes | 0.5 hora |
| Prueba de ventana programada | 4-8 horas |
| Monitoreo y ajuste | 24 horas |
| **TOTAL** | **1-2 dias** |

---

## ACCION 3.4 - ELIMINAR TABLAS DUPLICADAS/BACKUP INNECESARIAS

### 3.4.1 Descripcion Tecnica

**Que son las tablas duplicadas:**
Durante la operacion de HVR, se han acumulado tablas BACKUP y SEGURIDAD
que son duplicados de tablas principales. Estas tablas consumen ~156 GB
solo en el esquema FR_FRISBI, y existen en otros esquemas tambien.

**Por que eliminarlas:**
- Las tablas _BACKUP son snapshots manuales que ya no son necesarias
- HVR mantiene su propio mecanismo de recuperacion
- El storage consumido por backups duplicados es desperdicio puro
- Eliminarlas libera storage inmediatamente

**Impacto esperado:**
- Liberacion de ~156 GB (solo FR_FRISBI) + estimado 300 GB global
- Ahorro estimado: ~400 creditos/mes (storage)
- Sin impacto en operacion de HVR

**Identificacion de tablas:**
- Patrones de nombre: %_BACKUP, %_SEGURIDAD, %_OLD, %_PREV
- Creadas por usuarios, no por HVR
- Sin actividad de escritura reciente (>90 dias)

### 3.4.2 Pasos de Implementacion

**PASO 1: Identificar tablas duplicadas/backup**

```sql
-- Buscar tablas con sufijos de backup en todos los esquemas
USE DATABASE PRO_0_STAGING_DB;

SELECT
    TABLE_SCHEMA,
    TABLE_NAME,
    BYTES / POWER(1024, 3) AS SIZE_GB,
    CREATED,
    LAST_ALTERED
FROM INFORMATION_SCHEMA.TABLES
WHERE (
    TABLE_NAME LIKE '%\_BACKUP' ESCAPE '\\'
    OR TABLE_NAME LIKE '%\_SEGURIDAD' ESCAPE '\\'
    OR TABLE_NAME LIKE '%\_OLD' ESCAPE '\\'
    OR TABLE_NAME LIKE '%\_PREV' ESCAPE '\\'
    OR TABLE_NAME LIKE '%\_BK' ESCAPE '\\'
    OR TABLE_NAME LIKE '%\_BAK' ESCAPE '\\'
)
AND TABLE_TYPE = 'BASE TABLE'
ORDER BY BYTES DESC;

-- Calcular espacio total recuperable
SELECT
    TABLE_SCHEMA,
    COUNT(*) AS TABLE_COUNT,
    SUM(BYTES) / POWER(1024, 3) AS TOTAL_SIZE_GB
FROM INFORMATION_SCHEMA.TABLES
WHERE (
    TABLE_NAME LIKE '%\_BACKUP' ESCAPE '\\'
    OR TABLE_NAME LIKE '%\_SEGURIDAD' ESCAPE '\\'
    OR TABLE_NAME LIKE '%\_OLD' ESCAPE '\\'
    OR TABLE_NAME LIKE '%\_PREV' ESCAPE '\\'
)
AND TABLE_TYPE = 'BASE TABLE'
GROUP BY TABLE_SCHEMA
ORDER BY TOTAL_SIZE_GB DESC;
```

**PASO 2: Verificar que no estan en uso**

```sql
-- Verificar ultima actividad en tablas backup
SELECT
    TABLE_SCHEMA,
    TABLE_NAME,
    LAST_ALTERED,
    DATEDIFF(DAY, LAST_ALTERED, CURRENT_DATE()) AS DAYS_INACTIVE
FROM INFORMATION_SCHEMA.TABLES
WHERE TABLE_NAME LIKE '%\_BACKUP' ESCAPE '\\'
  AND TABLE_TYPE = 'BASE TABLE'
ORDER BY LAST_ALTERED ASC;

-- Verificar si hay queries recientes contra estas tablas
SELECT
    QUERY_TEXT,
    USER_NAME,
    START_TIME
FROM SNOWFLAKE.ACCOUNT_USAGE.QUERY_HISTORY
WHERE (QUERY_TEXT LIKE '%_BACKUP%'
   OR QUERY_TEXT LIKE '%_SEGURIDAD%')
  AND START_TIME >= DATEADD(DAY, -30, CURRENT_TIMESTAMP())
ORDER BY START_TIME DESC;
```

**PASO 3: Crear backup de seguridad (opcional pero recomendado)**

```sql
-- Para tablas grandes, crear backup en stage antes de eliminar
CREATE STAGE IF NOT EXISTS PRO_0_STAGING_DB.STAGING.BACKUP_STAGE
FILE_FORMAT = (TYPE = 'PARQUET');

-- Exportar tabla a stage (ejemplo para una tabla grande)
COPY INTO @PRO_0_STAGING_DB.STAGING.BACKUP_STAGE/FR_FRISBI_BACKUP/
FROM PRO_0_STAGING_DB.FR_FRISBI.TABLA_BACKUP
FILE_FORMAT = (TYPE = 'PARQUET')
OVERWRITE = TRUE;
```

**PASO 4: Eliminar tablas duplicadas**

```sql
-- Eliminar tablas backup (ejecutar una por una o en lotes)

-- Lote 1: Tablas sin actividad en mas de 180 dias
DROP TABLE IF EXISTS PRO_0_STAGING_DB.FR_FRISBI.TABLA_BACKUP_1;
DROP TABLE IF EXISTS PRO_0_STAGING_DB.FR_FRISBI.TABLA_BACKUP_2;
DROP TABLE IF EXISTS PRO_0_STAGING_DB.FR_FRISBI.TABLA_SEGURIDAD_1;
-- ... (continuar con todas las tablas identificadas)

-- Lote 2: Tablas con actividad entre 90-180 dias
-- (Verificar antes de eliminar)
DROP TABLE IF EXISTS PRO_0_STAGING_DB.OTRO_ESQUEMA.TABLA_OLD_1;
DROP TABLE IF EXISTS PRO_0_STAGING_DB.OTRO_ESQUEMA.TABLA_OLD_2;
-- ... (continuar)

-- Verificar eliminacion
SELECT
    TABLE_SCHEMA,
    TABLE_NAME
FROM INFORMATION_SCHEMA.TABLES
WHERE TABLE_NAME LIKE '%\_BACKUP' ESCAPE '\\'
  AND TABLE_TYPE = 'BASE TABLE';
-- Resultado esperado: 0 filas
```

**PASO 5: Documentar tablas eliminadas**

```sql
-- Crear tabla de auditoria de eliminaciones
CREATE TABLE IF NOT EXISTS PRO_0_STAGING_DB.AUDIT.DROPPED_TABLES_LOG (
    TABLE_SCHEMA VARCHAR(255),
    TABLE_NAME VARCHAR(255),
    SIZE_GB NUMBER(10,2),
    DROPPED_AT TIMESTAMP_LTZ,
    DROPPED_BY VARCHAR(255),
    REASON VARCHAR(500)
);

-- Registrar eliminaciones
INSERT INTO PRO_0_STAGING_DB.AUDIT.DROPPED_TABLES_LOG
VALUES (
    'FR_FRISBI',
    'TABLA_BACKUP_1',
    12.5,
    CURRENT_TIMESTAMP(),
    'ADMIN',
    'Duplicado eliminado - Fase 3 optimizacion'
);
```

### 3.4.3 Verificacion Post-Implementacion

```sql
-- Verificar espacio liberado
SELECT
    TABLE_SCHEMA,
    COUNT(*) AS REMAINING_BACKUP_TABLES,
    SUM(BYTES) / POWER(1024, 3) AS REMAINING_SIZE_GB
FROM INFORMATION_SCHEMA.TABLES
WHERE (
    TABLE_NAME LIKE '%\_BACKUP' ESCAPE '\\'
    OR TABLE_NAME LIKE '%\_SEGURIDAD' ESCAPE '\\'
)
AND TABLE_TYPE = 'BASE TABLE'
GROUP BY TABLE_SCHEMA;

-- Resultado esperado: 0 filas o reduccion significativa

-- Verificar que no hay errores en aplicaciones
SELECT *
FROM SNOWFLAKE.ACCOUNT_USAGE.QUERY_HISTORY
WHERE ERROR_CODE IS NOT NULL
  AND START_TIME >= DATEADD(HOUR, -1, CURRENT_TIMESTAMP())
ORDER BY START_TIME DESC;
```

### 3.4.4 Riesgos

| Riesgo | Probabilidad | Impacto | Mitigacion |
|--------|-------------|---------|------------|
| Tabla en uso se elimina | Media | Alto | Verificar actividad antes de eliminar |
| Dependencias rotas | Alta | Alto | Buscar referencias en views, procedures |
| Error humano en eliminacion | Media | Alto | Usar transacciones y verificar cada tabla |
| Recuperacion necesaria | Baja | Medio | Mantener backup en stage por 30 dias |

### 3.4.5 Rollback Procedure

```sql
-- Si se elimino una tabla por error

-- Opcion 1: Restaurar desde stage (si se exporto)
CREATE TABLE PRO_0_STAGING_DB.FR_FRISBI.TABLA_BACKUP_1
AS SELECT * FROM @PRO_0_STAGING_DB.STAGING.BACKUP_STAGE/FR_FRISBI_BACKUP/;

-- Opcion 2: Restaurar desde Time Travel (si no paso 7 dias)
CREATE TABLE PRO_0_STAGING_DB.FR_FRISBI.TABLA_BACKUP_1
CLONE PRO_0_STAGING_DB.FR_FRISBI.TABLA_BACKUP_1
AT(OFFSET => -3600); -- 1 hora antes de eliminacion

-- Opcion 3: Restaurar desde backup externo
-- (Depende de la estrategia de backup de la organizacion)
```

### 3.4.6 Tiempo Estimado

| Actividad | Duracion |
|-----------|----------|
| Identificar tablas duplicadas | 2-4 horas |
| Verificar que no estan en uso | 4-8 horas |
| Crear backups de seguridad | 4-8 horas |
| Eliminar tablas en lotes | 4-8 horas |
| Verificacion y documentacion | 2-4 horas |
| **TOTAL** | **3-5 dias** |

---

## ACCION 3.5 - OPTIMIZAR CHECKPOINT FREQUENCY

### 3.5.1 Descripcion Tecnica

**Que es Capture_Checkpoint_Frequency:**
Es un parametro de HVR que define cada cuantos segundos se escribe un checkpoint
en el log de captura. Un checkpoint guarda el estado de la captura para permitir
recuperacion en caso de fallo.

**Valor actual:** 300s (5 minutos) - valor por defecto
**Valor optimo:** 600s (10 minutos)

**Por que optimizarlo:**
- Cada checkpoint genera I/O adicional en el HVR Hub Server
- Frecuencia muy alta causa overhead innecesario
- Frecuencia muy baja aumenta tiempo de recuperacion
- 600s es el balance optimo entre I/O y recovery

**Impacto esperado:**
- Reduccion de ~50% en operaciones I/O de checkpoint
- Ahorro estimado: ~100 creditos/mes (I/O + compute)
- Tiempo de recovery aumenta en maximo 5 minutos (aceptable)

### 3.5.2 Pasos de Implementacion

**PASO 1: Verificar valor actual del parametro**

```bash
# Conectar al HVR Hub Server
ssh hvradmin@hvr-hub-server

# Verificar configuracion actual
hvrcli
ch_list -v SNOWFLAKE_REPLICATION | grep -i "checkpoint\|frequency"

# O via HVR Console:
# Channels > [canal] > Location Properties > Capture_Checkpoint_Frequency
```

**PASO 2: Configurar nuevo valor**

```bash
# Editar canal de replicacion
hvrcli
ch_edit -c SNOWFLAKE_REPLICATION

# Navegar a: Location Properties
# Capture_Checkpoint_Frequency = 600

# Alternativamente, via HVR Console:
# 1. Channels > [canal] > Location Properties
# 2. Buscar "Capture_Checkpoint_Frequency"
# 3. Cambiar valor de 300 a 600
# 4. Aplicar cambios

ch_save
exit
```

**PASO 3: Verificar que el cambio se aplica**

```bash
# Verificar nueva configuracion
hvrcli
ch_verify -c SNOWFLAKE_REPLICATION

# Mostrar valor actual
ch_list -v SNOWFLAKE_REPLICATION | grep -i "checkpoint"
```

**PASO 4: Monitorear rendimiento**

```bash
# Monitorear I/O del servidor HVR
iostat -x 10 6

# Monitorear logs de HVR
tail -f /var/log/hvr/hub.log | grep -i "checkpoint"
```

### 3.5.3 Verificacion Post-Implementacion

```bash
# Verificar que checkpoints se ejecutan cada 600s
grep "Checkpoint" /var/log/hvr/hub.log | tail -20

# Calcular intervalo entre checkpoints
# Debe ser ~600 segundos (10 minutos)
```

```sql
-- En Snowflake, verificar que replicacion funciona correctamente
SELECT
    TABLE_NAME,
    MAX(HVR_REPLICATION_TIME) AS LAST_REPLICATION,
    COUNT(*) AS ROW_COUNT
FROM PRO_0_STAGING_DB.STAGING.TABLA_EJEMPLO
GROUP BY TABLE_NAME;
```

### 3.5.4 Riesgos

| Riesgo | Probabilidad | Impacto | Mitigacion |
|--------|-------------|---------|------------|
| Recovery mas lento en fallo | Baja | Medio | Aceptable, maximo 5 min adicional |
| Perdida de datos en fallo | Baja | Alto | HVR garantiza consistencia con checkpoint |
| Incompatibilidad con HVR version | Baja | Alto | Verificar documentacion HVR 6.2 |

### 3.5.5 Rollback Procedure

```bash
# Si el nuevo valor causa problemas

# Paso 1: Detener replicacion
hvrcli
ch_stop -c SNOWFLAKE_REPLICATION

# Paso 2: Restaurar valor original
hvrcli
ch_edit -c SNOWFLAKE_REPLICATION
# Location Properties > Capture_Checkpoint_Frequency = 300
ch_save

# Paso 3: Reiniciar replicacion
hvrcli
ch_start -c SNOWFLAKE_REPLICATION

# Paso 4: Monitorear que vuelve a operacion normal
```

### 3.5.6 Tiempo Estimado

| Actividad | Duracion |
|-----------|----------|
| Verificar valor actual | 0.25 hora |
| Configurar nuevo valor | 0.25 hora |
| Verificacion | 0.5 hora |
| Monitoreo | 4 horas |
| **TOTAL** | **0.5 dia** |

---

## PLAN DE EJECUCION Y DEPENDENCIAS

### Orden de Ejecucion Recomendado

```
Semana 1:
  - Dia 1-2: Accion 3.5 (Checkpoint) - Bajo riesgo, ganancia rapida
  - Dia 2-3: Accion 3.2 (NoTriggerFiring) - Bajo riesgo
  - Dia 3-5: Accion 3.3 (Ventanas) - Requiere monitoreo 24h

Semana 2:
  - Dia 1-3: Accion 3.1 (APPEND) - Requiere validacion TimeKey
  - Dia 3-5: Accion 3.4 (Eliminar backups) - Alto riesgo, requiere cuidado

Semana 3:
  - Monitoreo y ajustes de todas las acciones
  - Documentacion final
```

### Dependencias

| Accion | Depende de | Bloquea a |
|--------|-----------|-----------|
| 3.1 (APPEND) | Version HVR 6.2.5+ | - |
| 3.2 (NoTriggerFiring) | - | - |
| 3.3 (Ventanas) | - | - |
| 3.4 (Eliminar backups) | Verificacion de uso | - |
| 3.5 (Checkpoint) | - | - |

### Dependencias entre Fases

- Fase 3 puede ejecutarse en paralelo con Fase 2
- Accion 3.1 (APPEND) debe coordinarse con Fase 1 (optimizacion de tablas)
- Accion 3.4 (Eliminar backups) debe coordinarse con equipo de operaciones

---

## METRICAS DE SEGUIMIENTO

### KPIs a Monitorear

| KPI | Linea Base | Objetivo | Frecuencia |
|-----|-----------|----------|------------|
| Creditos/mes totales | 5.305 | < 3.183 | Semanal |
| Tablas _b intermedias | ~4.107/ciclo | 0 | Diario |
| Triggers ejecutados/integracion | Variable | 0 (staging) | Diario |
| Ventana de integracion | 24h | 2AM-6AM | Diario |
| Storage backups duplicados | ~456 GB | 0 GB | Semanal |
| Checkpoint frequency | 300s | 600s | Diario |
| I/O operaciones checkpoint | Baseline | -50% | Semanal |

### Queries de Monitoreo

```sql
-- Monitoreo semanal de costes
SELECT
    DATE_TRUNC('WEEK', USAGE_DATE) AS WEEK,
    SUM(CREDITS_USED) AS TOTAL_CREDITS,
    SUM(CREDITS_USED_STORAGE) AS STORAGE_CREDITS,
    SUM(CREDITS_USED_COMPUTE) AS COMPUTE_CREDITS
FROM SNOWFLAKE.ACCOUNT_USAGE.WAREHOUSE_METERING_HISTORY
WHERE USAGE_DATE >= DATEADD(MONTH, -1, CURRENT_DATE())
GROUP BY DATE_TRUNC('WEEK', USAGE_DATE)
ORDER BY WEEK;

-- Monitoreo de storage por esquema
SELECT
    TABLE_SCHEMA,
    SUM(BYTES) / POWER(1024, 3) AS SIZE_GB,
    COUNT(*) AS TABLE_COUNT
FROM PRO_0_STAGING_DB.INFORMATION_SCHEMA.TABLES
WHERE TABLE_TYPE = 'BASE TABLE'
GROUP BY TABLE_SCHEMA
ORDER BY SIZE_GB DESC;
```

### Alertas Recomendadas

1. **Alerta de coste:** Si creditos/mes > 3.500 (por encima del objetivo)
2. **Alerta de tablas _b:** Si existen tablas _b despues de activar APPEND
3. **Alerta de triggers:** Si triggers se ejecutan en staging durante integracion
4. **Alerta de ventana:** Si integracion ocurre fuera de ventana programada
5. **Alerta de checkpoint:** Si checkpoint falla o tarda > 600s

---

## NOTAS FINALES

### Supuestos

1. HVR 6.2.5+ esta instalado o puede instalarse antes de la Fase 3
2. Todas las tablas destino tienen TimeKey o pueden modificarlo
3. Las tablas BACKUP duplicadas no estan en uso activo
4. La organizacion acepta latencia de 4 horas para datos de staging
5. Snowflake warehouse esta disponible en ventana 2AM-6AM

### Próximos Pasos Post-Fase 3

1. Evaluar resultados despues de 30 dias
2. Considerar Fase 4: Optimizacion avanzada (clustering, search optimization)
3. Revisar posibilidad de Snowflake Edition upgrade para mejor coste
4. Evaluar migracion de datos historicos a cold storage

### Contactos

- **Arquitectura de Datos:** [email]
- **Operaciones HVR:** [email]
- **Administracion Snowflake:** [email]

---

*Documento generado: 2026-06-20*
*Version: 1.0*
*Proxima revision: Post-implementacion Fase 3*
