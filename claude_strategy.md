# Estrategia de Optimizacion de Costes HVR → Snowflake

**Autor:** Claude (Especialista en Arquitectura de Datos)
**Fecha:** 2026-06-20
**Version HVR:** 6.2
**Objetivo:** Reducir coste en creditos Snowflake en un 40%
**Bases de datos:** PRO_0_STAGING_DB (staging), ES_COVADONGA (operativa)

---

## Resumen Ejecutivo

Esta estrategia analiza 7 areas de optimizacion en el pipeline HVR 6.2
para reducir el consumo de creditos Snowflake. Se priorizan las acciones
de mayor impacto y menor riesgo, con un objetivo acumulado de reduccion
del 40% en costes.

### Tabla de Impacto Estimado por Area

| Area                          | Impacto Estimado | Riesgo | Prioridad |
|-------------------------------|------------------|--------|-----------|
| A. Capture (Coalesce+NoBefore) | 10-15%          | Bajo   | 1         |
| B. Integrate (BURST+APPEND)   | 10-15%          | Medio  | 2         |
| C. Refresh (Slicing+Condition)| 5-8%            | Bajo   | 3         |
| D. Storage (Transient+Cleanup) | 3-5%            | Bajo   | 4         |
| E. Scheduling (Ventanas)      | 3-5%            | Bajo   | 5         |
| F. Transformaciones           | 2-3%            | Medio  | 6         |
| G. Reduccion de Volumen       | 5-10%           | Medio  | 2         |
| **TOTAL ESTIMADO**            | **40-55%**      |        |           |

---

## A. Optimizacion de Capture (Captura de Cambios)

### A1. Coalesce — Fusionar Multiples Operaciones

**Parametro:** `Coalesce` (accion Capture)

**Descripcion:** Coalesce fusiona multiples operaciones sobre la misma fila
en una sola operacion. Por ejemplo, un INSERT + UPDATE se convierten en
un solo INSERT; 5 UPDATEs se reducen a 1; un INSERT + DELETE se elimina.

**Impacto esperado:** 5-10% reduccion en volumen de cambios replicados.

**Implementacion:**
```
# En la accion Capture del canal (afecta a todas las tablas del location)
Action: Capture
Parameter: Coalesce
```

**Riesgos:**
- Las restricciones de consistencia intermedia pueden violarse en el target.
  Esto es aceptable si el destino es un staging/analitico (PRO_0_STAGING_DB).
- No usar junto con SapUnpack (incompatible segun documentacion).

**Recomendacion:** Aplicar en ES_COVADONGA (operatica) solo si las tablas
destino son de tipo staging/analitico donde la consistencia intermedia
no es critica. En PRO_0_STAGING_DB aplicar sin restricciones.

---

### A2. NoBeforeUpdate — Eliminar "Before" en Updates

**Parametro:** `NoBeforeUpdate` (accion Capture)

**Descripcion:** Por defecto HVR captura tanto el "before" como el "after"
de cada update. Con NoBeforeUpdate solo se captura el "after", reduciendo
el volumen de datos transportados.

**Impacto esperado:** 3-5% reduccion en volumen (proporcional a la
frecuencia de updates).

**Implementacion:**
```
Action: Capture
Parameter: NoBeforeUpdate
```

**Riesgos:**
- Integrate actualizara TODAS las columnas (no solo las cambiadas).
- CollisionDetect no funcionara correctamente (no disponible con BURST
  de todos modos).
- Si se necesita auditar valores anteriores, este parametro NO debe usarse.

**Recomendacion:** Ideal para tablas de ES_COVADONGA donde solo importa
el estado final. No usar si se requiere auditoria de cambios.

---

### A3. Capture Method — Log-based (Confirmar)

**Parametro:** `Capture_Method` (propiedad de ubicacion)

**Descripcion:** HVR 6.2 ha deprecado trigger-based capture (DB_TRIGGER).
Log-based capture lee directamente de los logs de la base de datos sin
impactar las transacciones.

**Impacto esperado:** Indirecto — elimina overhead en source DB, reduce
latencia de captura, mejora throughput.

**Implementacion:**
```
Location Property: Capture_Method = LOGMINER  (para Oracle)
Location Property: Capture_Method = SQL      (para SQL Server)
```

**Riesgos:**
- Requiere supplemental logging habilitado en la base de datos fuente.
- Si ya esta en log-based, no hay cambio necesario.

**Recomendacion:** Verificar que ambas ubicaciones (PRO_0_STAGING_DB y
ES_COVADONGA) usen log-based capture. Si alguna usa trigger-based,
migrar inmediatamente.

---

### A4. Checkpoint Tuning — Frecuencia de Checkpoints

**Parametro:** `Capture_Checkpoint_Frequency` (propiedad de ubicacion)

**Descripcion:** Controla la frecuencia (en segundos) con la que HVR
escribe checkpoints para recuperacion ante interrupciones.

**Impacto esperado:** 1-2% mejora en eficiencia de I/O del hub.

**Implementacion:**
```
# Valor por defecto: 300 segundos (5 minutos)
# Para tablas con transacciones largas frecuentes:
Location Property: Capture_Checkpoint_Frequency = 600

# Para minimizar I/O en el hub (si las transacciones son cortas):
Location Property: Capture_Checkpoint_Frequency = 1200
```

**Riesgos:**
- Valores muy bajos (ej: 10s) generan I/O excesivo sin beneficio.
- Valores muy altos obligan a re-lectura prolongada de logs ante fallos.

**Recomendacion:** Usar 600s como balance. No reducir debajo de 300s.

---

### A5. IgnoreSessionName — Filtrar Sesiones Innecesarias

**Parametro:** `IgnoreSessionName` (accion Capture)

**Descripcion:** Ignora cambios realizados por sesiones especificas.
Por defecto HVR ya ignora la sesion "hvr_integrate" para evitar loops.

**Impacto esperado:** Variable — depende de cuantas sesiones ruidosas existan.

**Implementacion:**
```
# Si hay procesos ETL, purging o mantenimiento que genera cambios
# que no necesitan replicarse:
Action: Capture
Parameter: IgnoreSessionName = ETL_USER
Parameter: IgnoreSessionName = PURGE_ADMIN
```

**Riesgos:**
- Si se ignora una sesion que SI debe replicarse, habra perdida de datos.

**Recomendacion:** Auditar las sesiones activas en ES_COVADONGA y
PRO_0_STAGING_DB para identificar candidatas.

---

## B. Optimizacion de Integrate (Integracion de Cambios)

### B1. Method — APPEND para Snowflake (v6.2.5+)

**Parametro:** `Method` (accion Integrate)

**Descripcion:** El metodo APPEND inserta cambios directamente en tablas
con TimeKey definido, sin necesidad de BURST intermedio. Es mas eficiente
para Snowflake porque elimina la creacion de tablas _b intermedias.

**Impacto esperado:** 5-10% reduccion en creditos (menos staging files,
menos tablas temporales).

**Requisito:** Todas las tablas en el target deben tener TimeKey definido.

**Implementacion:**
```
# Primero, definir TimeKey en ColumnProperties para cada tabla:
Action: ColumnProperties
Parameter: Name = <columna_timestamp>
Parameter: TimeKey

# Luego cambiar el metodo de integracion:
Action: Integrate
Parameter: Method = APPEND
```

**Riesgos:**
- Solo funciona con Snowflake, BigQuery y Databricks como target.
- No puede usarse con IntegrateExpression que requiera evaluacion en DB.
- Si se cambia de BURST a APPEND mientras Integrate esta activo, el
  primer ciclo BURST puede re-insertar cambios existentes (duplicados).

**Recomendacion:** Implementar durante ventana de mantenimiento.
Verificar que todas las tablas tengan TimeKey antes del cambio.

---

### B2. Method — BURST (Confirmar como Default)

**Parametro:** `Method` (accion Integrate)

**Descripcion:** BURST es el metodo default recomendado para Snowflake.
Ordena y coalesce cambios, los carga en tablas _b intermedias, y luego
aplica INSERT/UPDATE/DELETE en una sola transaccion por tipo.

**Impacto esperado:** Ya optimizado por defecto. Verificar que este activo.

**Implementacion:**
```
Action: Integrate
Parameter: Method = BURST
```

**Riesgos:**
- Crea tablas _b intermedias que consumen storage temporal.
- No puede usarse con CollisionDetect ni con DbSequence.

**Recomendacion:** Confirmar que BURST este activo. Si APPEND es viable
(ver B1), preferir APPEND para mayor eficiencia.

---

### B3. BurstCommitFrequency — Frecuencia de Commit

**Parametro:** `BurstCommitFrequency` (accion Integrate)

**Descripcion:** Controla cuando se hace commit en modo BURST.

**Opciones:**
- `CYCLE` (default): Un solo commit por ciclo completo.
- `TABLE`: Un commit por tabla.
- `STATEMENT`: Un commit por cada statement SQL.

**Impacto esperado:** CYCLE (default) es el mas eficiente para Snowflake.

**Implementacion:**
```
Action: Integrate
Parameter: BurstCommitFrequency = CYCLE
```

**Riesgos:**
- CYCLE puede mantener transacciones largas abiertas en Snowflake,
  consumiendo creditos de warehouse.
- STATEMENT genera muchos commits pequeños (overhead).

**Recomendacion:** Mantener CYCLE. Si hay problemas de warehouse timeout,
cambiar a TABLE como compromiso.

---

### B4. NoTriggerFiring — Deshabilitar Triggers en Target

**Parametro:** `NoTriggerFiring` (accion Integrate)

**Descripcion:** Deshabilita triggers en las tablas destino durante
la integracion, mejorando rendimiento y reduciendo operaciones.

**Impacto esperado:** 2-5% mejora en rendimiento de integracion.

**Implementacion:**
```
Action: Integrate
Parameter: NoTriggerFiring
```

**Riesgos:**
- Los triggers definidos en las tablas destino no se ejecutaran
  durante la integracion HVR.
- Si hay triggers criticos para logica de negocio, NO usar.

**Recomendacion:** Ideal para PRO_0_STAGING_DB (staging). Evaluar
cuidadosamente para ES_COVADONGA si es target operativo.

---

### B5. Coalesce en Integrate — No Usar con BURST

**Parametro:** `Coalesce` (accion Integrate)

**Descripcion:** La documentacion especifica que Coalesce en Integrate
NO debe usarse cuando Method=BURST, ya que BURST ya coalesce
automaticamente.

**Impacto esperado:** Evitar configuracion redundante.

**Implementacion:**
```
# NO definir Coalesce en Integrate si Method=BURST
# El coalesce ya ocurre dentro del algoritmo BURST
```

**Riesgos:**
- Definir Coalesce con BURST es redundante y puede causar
  comportamiento impredecible.

---

## C. Optimizacion de Refresh (Carga Inicial)

### C1. RefreshCondition — Filtrar Datos a Cargar

**Parametro:** `RefreshCondition` (accion Restrict)

**Descripcion:** Define un filtro SQL para limitar las filas que se
cargan durante un Refresh. Aplica tanto en source como en target.

**Impacto esperado:** 3-8% reduccion (depende del filtro).

**Implementacion:**
```
# Ejemplo: Solo cargar datos de los ultimos 90 dias
Action: Restrict
Parameter: RefreshCondition = created_date >= CURRENT_DATE - 90

# Ejemplo: Solo cargar registros activos
Action: Restrict
Parameter: RefreshCondition = status = 'ACTIVE'
```

**Riesgos:**
- Si el filtro es muy agresivo, datos historicos no estaran en target.
- Puede causar inconsistencias si hay referencias a datos filtrados.

**Recomendacion:** Usar para tablas de staging donde solo se necesitan
datos recientes. No usar en cargas completas requeridas para reporting.

---

### C2. Slicing — Paralelizacion de Cargas

**Parametro:** `SliceCountCondition` o `SliceSeriesCondition` (accion Restrict)

**Descripcion:** Divide tablas grandes en segmentos que se procesan
en paralelo durante Refresh.

**Impacto esperado:** 2-5% reduccion en tiempo de refresh (menos
warehouse uptime).

**Implementacion:**
```
# Slicing por conteo (divide en N segmentos):
Action: Restrict
Parameter: SliceCountCondition = MOD(id, {hvr_slice_total}) = {hvr_slice_num}

# Ejemplo con 4 slices:
# hvrrefresh -S4 chn tgt
```

**Riesgos:**
- Requiere definir la condicion en source Y target.
- No debe usarse junto con RefreshCondition.
- Slices muy pequenos generan overhead de coordinacion.

**Recomendacion:** Usar para tablas > 1M de filas. Definir 4-8 slices
como punto de partida.

---

### C3. Bulk Refresh vs Row-wise Refresh

**Parametro:** Granularidad de Refresh (CLI: `-gb` vs `-gr`)

**Descripcion:**
- **Bulk Refresh:** Trunca target y bulk-load desde source. Mucho mas
  eficiente para Snowflake.
- **Row-wise Refresh:** Compara fila por fila. Muy costoso en
  column-oriented databases como Snowflake.

**Impacto esperado:** 3-5% reduccion en creditos de warehouse.

**Implementacion:**
```
# CLI:
hvrrefresh -gb chn tgt    # Bulk refresh (recomendado para Snowflake)

# Evitar:
hvrrefresh -gr chn tgt    # Row-wise refresh (costoso en Snowflake)
```

**Riesgos:**
- Bulk Refresh hace TRUNCATE — los datos anteriores se pierden.
- Row-wise es necesario solo para tablas pequeñas con cambios minimos.

**Recomendacion:** Usar Bulk Refresh (-gb) por defecto para Snowflake.
Reservar Row-wise (-gr) solo para tablas < 100K filas.

---

### C4. Programar Refresh en Horas de Menor Coste

**Descripcion:** Snowflake cobra diferentes tarifas segun el warehouse
y el momento. Programar Refreshes fuera de horas pico.

**Impacto esperado:** 1-3% ahorro indirecto.

**Implementacion:**
```
# Usar Scheduling para programar refreshes:
Action: Scheduling
Parameter: CaptureStartTimes = 0 2 * * *    # 2 AM diario
Parameter: TimeContext = * * * * 1-5         # Solo lun-vie
```

---

## D. Optimizacion de Storage en Snowflake

### D1. Transient Tables — Tablas Transitorias en Snowflake

**Parametro:** `TransientTable` (accion TableProperties)

**Descripcion:** Las tablas transitorias en Snowflake no tienen Fail-safe
period (90 dias), reduciendo significativamente el costo de storage.

**Impacto esperado:** 2-4% reduccion en storage costs.

**Implementacion:**
```
Action: TableProperties
Parameter: TransientTable
```

**Riesgos:**
- Sin Fail-safe, Snowflake no puede recuperar datos despues del
  Time Travel period (max 1 dia para transient).
- Si se necesita retencion larga, NO usar.

**Recomendacion:** Ideal para PRO_0_STAGING_DB (staging) donde los datos
pueden regenerarse. No usar para datos irreemplazables.

---

### D2. Limpieza de Staging Files

**Descripcion:** Durante BURST integrate, HVR crea archivos staging
temporales. Asegurar que se limpian correctamente.

**Impacto esperado:** 1-2% reduccion en storage.

**Implementacion:**
```
# Verificar que el directorio staging se limpia:
# HVR_CONFIG/hubs/<hub>/channels/<chn>/locs/<loc>/

# Configurar limpieza automatica en Snowflake:
# El staging interno de Snowflake se limpia automaticamente,
# pero verificar que no queden archivos residuales.
```

**Riesgos:**
- Si los archivos staging no se limpian, acumulan storage cost.

---

### D3. Burst Tables — Tablas _b Intermedias

**Descripcion:** Las tablas _b se crean durante BURST integrate y se
deberian limpiar automaticamente. Verificar que no persisten.

**Impacto esperado:** 1-2% reduccion en storage.

**Implementacion:**
```
# Verificar que las tablas _b se eliminan despues de cada ciclo:
# En el schema de Snowflake, buscar tablas con sufijo _b
# Si persisten, investigar si hay errores en el ciclo BURST
```

---

### D4. State Tables — Tablas de Estado HVR

**Descripcion:** HVR crea tablas de estado en el target. Asegurar
que no se duplican ni crecen sin control.

**Impacto esperado:** <1% reduccion.

**Implementacion:**
```
# Las state tables son necesarias para el funcionamiento de HVR.
# No eliminarlas, pero verificar que no hay redundancia.
```

---

## E. Optimizacion de Scheduling

### E1. CaptureStartTimes / IntegrateStartTimes — Ventanas de Ejecucion

**Parametro:** `CaptureStartTimes`, `IntegrateStartTimes` (accion Scheduling)

**Descripcion:** Define momentos especificos en lugar de ejecucion
continua. Reduce ciclos vacios que consumen creditos.

**Impacto esperado:** 2-5% reduccion en creditos de warehouse.

**Implementacion:**
```
# Ejecutar solo durante horas de negocio (ej: lun-vie 6AM-10PM):
Action: Scheduling
Parameter: CaptureStartTimes = 0 6-22 * * 1-5
Parameter: TimeContext = * * * * 1-5

# Para weekends, reducir frecuencia:
Action: Scheduling
Parameter: CaptureStartTimes = 0 8,20 * * 0,6
Parameter: TimeContext = * * * * 0,6
```

**Riesgos:**
- Si las ventanas son muy estrechas, la latencia de replicacion aumenta.
- Datos fuera de ventana se acumulan y procesan en la siguiente ventana.

**Recomendacion:** Definir ventanas basadas en necesidades de negocio.
Para staging, ejecutar solo en horas no pico es aceptable.

---

### E2. LatencySLA — Ajustar SLA de Latencia

**Parametro:** `LatencySLA` (accion Scheduling)

**Descripcion:** Define el umbral de latencia en segundos. Un SLA mas
permisivo permite a HVR batching mas agresivo.

**Impacto esperado:** 1-3% reduccion (batch mas grande = menos transacciones).

**Implementacion:**
```
# SLA mas permisivo para staging:
Action: Scheduling
Parameter: LatencySLA = 300    # 5 minutos (en lugar de 10s)
Parameter: TimeContext = * * * * 1-5

# SLA mas estricto para operacional:
Action: Scheduling
Parameter: LatencySLA = 60     # 1 minuto
Parameter: TimeContext = * * * * 0,6
```

**Riesgos:**
- Latencia mas alta = datos mas desactualizados en target.
- Si el negocio necesita datos near-real-time, no aumentar SLA.

**Recomendacion:** PRO_0_STAGING_DB puede tolerar SLA de 300s+.
ES_COVADONGA como target necesita evaluar requisitos de latencia.

---

### E3. IntegrateStartAfterCapture — Encadenar Jobs

**Parametro:** `IntegrateStartAfterCapture` (accion Scheduling)

**Descripcion:** Hace que el job de Integrate solo se ejecute despues
de que Capture enrute datos nuevos, en lugar de ejecutar continuamente.

**Impacto esperado:** 1-2% reduccion (evita ciclos vacios de Integrate).

**Implementacion:**
```
Action: Scheduling
Parameter: IntegrateStartAfterCapture
```

**Riesgos:**
- Si Capture no encuentra datos, Integrate no se ejecuta (esperado).
- Puede añadir pequena latencia adicional.

---

## F. Optimizacion de Transformaciones

### F1. ExecOnHub — Ejecutar en Hub vs Agente

**Parametro:** `ExecOnHub` (accion Transform)

**Descripcion:** Ejecuta transformaciones en el hub en lugar de en
la maquina del agente. Reduce movimiento de datos.

**Impacto esperado:** 1-2% reduccion en trafico de red.

**Implementacion:**
```
Action: Transform
Parameter: ExecOnHub
```

**Riesgos:**
- El hub puede convertirse en bottleneck si hay muchas transformaciones.
- No recomendado para SapUnpack (documentacion lo desaconseja).

**Recomendacion:** Usar para transformaciones ligeras. Para transformaciones
pesadas, mantener en el agente cerca de los datos.

---

### F2. Parallel — Paralelizacion de Transformaciones

**Parametro:** `Parallel` (accion Transform)

**Descripcion:** Ejecuta transformaciones en N ramas paralelas.

**Impacto esperado:** 1-2% mejora en rendimiento.

**Implementacion:**
```
Action: Transform
Parameter: Parallel = 4
```

**Riesgos:**
- Solo inicia paralelizacion despues de las primeras 1000 filas.
- Consume mas recursos en el hub/agente.

**Recomendacion:** Usar para tablas grandes con transformaciones costosas.

---

### F3. Minimizar Transformaciones en Hub

**Descripcion:** Las transformaciones con Command/CommandArguments que
definen scripts externos anaden overhead. Evaluar si son necesarias
o pueden reemplazarse por IntegrateExpression (SQL nativo).

**Impacto esperado:** 1-2% reduccion.

**Implementacion:**
```
# Preferir IntegrateExpression sobre Command cuando sea posible:
Action: ColumnProperties
Parameter: Name = my_col
Parameter: IntegrateExpression = UPPER({my_col})   # SQL nativo

# En lugar de:
Action: Transform
Parameter: Command = /path/to/script.sh            # Script externo
```

**Riesgos:**
- IntegrateExpression no puede hacer todo lo que un script puede.
- Algunos casos requieren transformaciones complejas que solo scripts
  pueden manejar.

---

## G. Reduccion de Volumen de Datos

### G1. CaptureCondition — Filtrar en Origen

**Parametro:** `CaptureCondition` (accion Restrict)

**Descripcion:** Filtra filas durante la CAPTURA (no durante integracion).
Solo los cambios que cumplen la condicion se replican. Esto reduce
volumen en TODA la pipeline.

**Impacto esperado:** 3-8% reduccion (depende del filtro).

**Implementacion:**
```
# Ejemplo: Solo replicar cambios de los ultimos 6 meses
Action: Restrict
Parameter: CaptureCondition = last_modified >= ADD_MONTHS(SYSDATE, -6)

# Ejemplo: Excluir registros de prueba
Action: Restrict
Parameter: CaptureCondition = record_type != 'TEST'
```

**Riesgos:**
- Filtrado en Capture significa que los datos JAMAS llegaran al target.
- Update conversion: si un update cambia un filtro de incluido a excluido,
  se convierte en DELETE en el target.
- Si un update cambia de excluido a incluido, se convierte en INSERT.

**Recomendacion:** La mas poderosa herramienta de reduccion de volumen.
Usar con cuidado y documentar claramente los filtros aplicados.

---

### G2. ColumnProperties Absent/Extra — Omitir Columnas

**Parametro:** `Absent` / `Extra` (accion ColumnProperties)

**Descripcion:**
- `Extra`: Columna existe en DB pero no en HVR repository. No se captura.
- `Absent`: Columna no existe en DB. Se usa default.

**Impacto esperado:** 1-3% reduccion (depende de columnas omitidas).

**Implementacion:**
```
# Para columnas que no necesitan replicarse (ej: columnas de auditoria
# que ya existen en el target con defaults):
Action: ColumnProperties
Parameter: Name = audit_col
Parameter: Extra
Parameter: Datatype = varchar
```

**Riesgos:**
- No se puede usar en columnas que son parte de la replication key.
- No se puede combinar con BaseName.

**Recomendacion:** Identificar columnas grandes (LOB, CLOB, BLOB) que
no son necesarias en el staging y marcarlas como Extra.

---

### G3. ColumnProperties IgnoreDuringCompare — Reducir Comparaciones

**Descripcion:** Reduce el volumen de datos comparado durante
operaciones de Compare.

**Impacto esperado:** 1-2% reduccion en costes de Compare.

**Implementacion:**
```
# Definir CompareCondition para limitar comparacion:
Action: Restrict
Parameter: CompareCondition = created_date >= CURRENT_DATE - 30
```

---

### G4. SelectDistinct — Eliminar Duplicados

**Descripcion:** En la documentacion de Restrict, se menciona que
SelectDistinct puede usarse para reducir filas duplicadas.

**Impacto esperado:** Variable.

**Implementacion:**
```
# Usar con cautela — solo si hay duplicados conocidos en source
```

---

## Plan de Implementacion

### Fase 1: Quick Wins (Semana 1-2) — Impacto: 15-20%

| Accion                                    | Area | Impacto | Riesgo |
|-------------------------------------------|------|---------|--------|
| Activar Coalesce en Capture               | A    | 5-10%   | Bajo   |
| Activar NoBeforeUpdate en Capture         | A    | 3-5%    | Bajo   |
| Verificar Capture_Method = log-based      | A    | 1-2%    | Bajo   |
| Confirmar Method=BURST en Integrate       | B    | 3-5%    | Bajo   |
| Activar NoTriggerFiring en Integrate      | B    | 2-5%    | Bajo   |
| Usar Bulk Refresh (-gb) por defecto       | C    | 3-5%    | Bajo   |

### Fase 2: Optimizacion Media (Semana 3-4) — Impacto: 10-15%

| Accion                                    | Area | Impacto | Riesgo |
|-------------------------------------------|------|---------|--------|
| Definir TransientTable en staging         | D    | 2-4%    | Bajo   |
| Ajustar LatencySLA a 300s para staging    | E    | 1-3%    | Bajo   |
| Programar ventanas con CaptureStartTimes  | E    | 2-5%    | Bajo   |
| Agregar IgnoreSessionName para ETL/purge   | A    | 1-3%    | Bajo   |
| Reducir Transformaciones con Command       | F    | 1-2%    | Medio  |

### Fase 3: Optimizacion Avanzada (Semana 5-8) — Impacto: 10-15%

| Accion                                    | Area | Impacto | Riesgo |
|-------------------------------------------|------|---------|--------|
| Implementar APPEND method (v6.2.5+)       | B    | 5-10%   | Medio  |
| Definir CaptureCondition en tablas grandes| G    | 3-8%    | Medio  |
| Marcar columnas innecesarias como Extra   | G    | 1-3%    | Bajo   |
| Implementar Slicing para Refresh grandes  | C    | 2-5%    | Bajo   |
| Agregar RefreshCondition en staging       | C    | 3-5%    | Bajo   |

---

## Metricas de Seguimiento

### KPIs a Monitorear

1. **Creditos Snowflake por dia/semana** — Comparar antes vs despues
2. **Volumen de datos replicados (GB/dia)** — Deberia reducirse
3. **Numero de operaciones DML en target** — Deberia reducirse
4. **Latencia de replicacion** — No deberia aumentar significativamente
5. **Tamanio de storage en Snowflake** — Deberia estabilizarse
6. **Numero de ciclos vacios** — Deberia reducirse

### Comandos de Verificacion

```sql
-- En Snowflake: Ver creditos consumidos por warehouse
SELECT *
FROM SNOWFLAKE.ACCOUNT_USAGE.WAREHOUSE_METERING_HISTORY
WHERE WAREHOUSE_NAME = 'HVR_WAREHOUSE'
  AND START_TIME >= DATEADD(DAY, -7, CURRENT_TIMESTAMP());

-- En Snowflake: Ver tamano de tablas HVR
SELECT TABLE_NAME, BYTES, ROW_COUNT
FROM INFORMATION_SCHEMA.TABLES
WHERE TABLE_SCHEMA = 'PRO_0_STAGING_DB'
ORDER BY BYTES DESC;

-- En Snowflake: Ver tablas _b residuales (deberian limpiarse)
SELECT TABLE_NAME
FROM INFORMATION_SCHEMA.TABLES
WHERE TABLE_NAME LIKE '%\_b' ESCAPE '\';
```

---

## Riesgos Generales y Mitigacion

| Riesgo                              | Probabilidad | Impacto | Mitigacion                                    |
|-------------------------------------|-------------|---------|-----------------------------------------------|
| Perdida de datos por filtro agresivo | Media       | Alto    | Probar primero en ambiente no productivo      |
| Inconsistencia en target             | Baja        | Alto    | Ejecutar Compare despues de cada cambio       |
| Degradacion de latencia             | Media       | Medio   | Monitorear LatencySLA y ajustar               |
| Fallo al cambiar Method a APPEND    | Baja        | Alto    | Ventana de mantenimiento + rollback plan      |
| Exceso de recursos en hub           | Baja        | Medio   | Monitorear CPU/del hub con Performance Metrics|
| Datos duplicados por cambio BURST→APPEND | Baja    | Alto    | Verificar integridad post-cambio              |

---

## Notas Especificas para HVR 6.2

1. **Trigger-based capture deprecado:** Si alguna ubicacion usa
   DB_TRIGGER, migrar a log-based inmediatamente.

2. **APPEND method:** Requiere v6.2.5/3 o superior. Verificar version
   actual antes de implementar.

3. **Transient Tables:** Disponible desde v6.2.5/1 para Snowflake.

4. **Maximo 7 start times por job:** Limitacion de scheduling en 6.2.

5. **IntegrateOnceOnStart:** Evita integraciones innecesarias cuando
   el job se inicia manualmente.

---

## Conclusion

La combinacion de estas optimizaciones puede lograr una reduccion del
40% en creditos Snowflake, con las siguientes palancas principales:

1. **Coalesce + NoBeforeUpdate** → Reduce volumen de cambios en 10-15%
2. **APPEND method** → Elimina overhead de tablas intermedias en 5-10%
3. **CaptureCondition** → Filtra datos innecesarios en origen en 3-8%
4. **Scheduling optimizado** → Reduce ciclos vacios en 3-5%
5. **Transient Tables** → Reduce storage en 2-4%

Se recomienda implementar en fases, monitoreando el impacto de cada
cambio antes de proceder al siguiente. Documentar todas las acciones
aplicadas y mantener un registro de metricas antes/despues para validar
el ahorro.
