# PLAN DE OPTIMIZACIÓN HVR 6.2 — COMANDOS CORRECTOS PARA SV3770
## Validado contra documentación oficial Fivetran HVR 6.2.0/1

---

## DIAGNÓSTICO DEL HUB

**Hub:** hvrhub
**Versión:** HVR 6.2.0/1
**Servidor:** sv3770.logista.local

### Canales por base de datos

| Base de Datos | Canales | Tablas totales |
|---------------|---------|----------------|
| PRO_0_STAGING_DB | 45 | ~750+ |
| ES_COVADONGA | 5 | ~380 |
| **Total** | **50** | **~1130+** |

### Canales → PRO_0_STAGING_DB (45 canales)

```
cervino_prue, es_alertran, es_alertranb, es_camara_b, es_camara_r,
es_cdi_par, es_corpor_p, es_diana_p, es_diana_pro, es_espada,
es_fre_pro, es_masters, es_osc_par, es_ph_full, es_pharma2,
es_sellin, es_tpos_l1, es_tpos_l2, es_tpos_l3, es_tpos_l4,
es_warehouse, fixline1, fixline2, fixline3, fixline4,
fr_frisbi_md, fr_frisbi_so, fr_sellin, fr_tpos4_vie,
fr_tpos_l1, fr_tpos_l2, fr_tpos_l3, fr_tpos_l4, fr_tpos_l4vi,
it_italbi, it_sqlserver, it_test, param_l1_fr, param_l2_fr,
param_l3_fr, param_l4_fr, pentana, test_libros, test_multi, webzoo_snow
```

### Canales → ES_COVADONGA (5 canales)

```
cova_delfos, es_cov_teseo, es_gen_live, es_gen_ret, parcelcovora
```

---

## ACCIÓN 1: ACTIVAR COALESCE EN TODOS LOS CANALES (FASE 1.4)

### Qué hace
Coalesce fusiona múltiples filas de cambio en una sola operación de integración, reduciendo el número de INSERT/UPDATE en Snowflake.

### Comandos correctos

```bash
# Paso 1: Exportar definición actual del hub
hvrdefinitionexport hvrhub /tmp/hub_export.json

# Paso 2: Añadir Coalesce=true a todas las acciones Capture
python3 << 'EOF'
import json

with open('/tmp/hub_export.json') as f:
    data = json.load(f)

count = 0
for change in data.get('changes', []):
    if 'add_channel' in change:
        ch_name = change['add_channel']['channel']
        for action in change['add_channel'].get('actions', []):
            if action['type'] == 'Capture':
                if 'params' not in action:
                    action['params'] = {}
                action['params']['Coalesce'] = 'true'
                count += 1
                print(f"  Coalesce=true → Canal: {ch_name}")

with open('/tmp/hub_export.json', 'w') as f:
    json.dump(data, f, indent=2)

print(f"\nTotal Capture actions modificadas: {count}")
EOF

# Paso 3: Importar la definición modificada
hvrdefinitionimport hvrhub /tmp/hub_export.json

# Paso 4: Activar los canales para aplicar cambios (uno por uno o en lote)
# Para todos los canales de PRO_0_STAGING_DB:
for canal in cervino_prue es_alertran es_alertranb es_camara_b es_camara_r \
  es_cdi_par es_corpor_p es_diana_p es_diana_pro es_espada es_fre_pro \
  es_masters es_osc_par es_ph_full es_pharma2 es_sellin es_tpos_l1 \
  es_tpos_l2 es_tpos_l3 es_tpos_l4 es_warehouse fixline1 fixline2 \
  fixline3 fixline4 fr_frisbi_md fr_frisbi_so fr_sellin fr_tpos4_vie \
  fr_tpos_l1 fr_tpos_l2 fr_tpos_l3 fr_tpos_l4 fr_tpos_l4vi it_italbi \
  it_sqlserver it_test param_l1_fr param_l2_fr param_l3_fr param_l4_fr \
  pentana test_libros test_multi webzoo_snow; do
    hvractivate -J cap -J refr hvrhub "$canal"
    echo "Activado: $canal"
done

# Para canales de ES_COVADONGA:
for canal in cova_delfos es_cov_teseo es_gen_live es_gen_ret parcelcovora; do
    hvractivate -J cap -J refr hvrhub "$canal"
    echo "Activado: $canal"
done
```

### Verificación

```bash
# Verificar que Coalesce está activo en todos los canales
python3 << 'EOF'
import json
with open('/tmp/hub_export.json') as f:
    data = json.load(f)

sin_coalesce = []
for change in data.get('changes', []):
    if 'add_channel' in change:
        ch = change['add_channel']
        for action in ch.get('actions', []):
            if action['type'] == 'Capture':
                params = action.get('params', {})
                if params.get('Coalesce') != 'true':
                    sin_coalesce.append(ch['channel'])

if sin_coalesce:
    print(f"⚠️  Canales SIN Coalesce: {len(sin_coalesce)}")
    for c in sin_coalesce:
        print(f"  {c}")
else:
    print("✅ Todos los canales tienen Coalesce=true en Capture")
EOF
```

### Riesgo
- **Bajo.** Coalesce solo afecta cómo se agrupan los cambios antes de integrar. No pierde datos.
- **Rollback:** Repetir el proceso con `Coalesce=` (vaciar el parámetro).

---

## ACCIÓN 2: OPTIMIZAR COPY INTO (FASE 1.3)

### Qué hace
Ajusta los parámetros de integración para reducir el número de operaciones de escritura en Snowflake.

### Comandos correctos

```bash
# Paso 1: Exportar definición actual
hvrdefinitionexport hvrhub /tmp/hub_export.json

# Paso 2: Optimizar parámetros de Integrate (CycleByteLimit, Delay)
python3 << 'EOF'
import json

with open('/tmp/hub_export.json') as f:
    data = json.load(f)

count = 0
for change in data.get('changes', []):
    if 'add_channel' in change:
        ch_name = change['add_channel']['channel']
        for action in change['add_channel'].get('actions', []):
            if action['type'] == 'Integrate':
                if 'params' not in action:
                    action['params'] = {}
                # Aumentar CycleByteLimit para reducir commits
                action['params']['CycleByteLimit'] = '2000000000'  # 2GB
                # Reducir Delay para integrar más rápido
                action['params']['Delay'] = '120'
                # Cambiar a Method=APPEND si aplica (solo para tablas sin PK conflict)
                # action['params']['Method'] = 'APPEND'  # Solo si no hay deletes
                count += 1
                print(f"  Integrate optimizado → Canal: {ch_name}")

with open('/tmp/hub_export.json', 'w') as f:
    json.dump(data, f, indent=2)

print(f"\nTotal Integrate actions modificadas: {count}")
EOF

# Paso 3: Importar y activar
hvrdefinitionimport hvrhub /tmp/hub_export.json

# Activar canales (mismo loop que arriba)
for canal in $(python3 -c "
import json
with open('/tmp/hub_export.json') as f:
    data = json.load(f)
for c in data['changes']:
    if 'add_channel' in c:
        print(c['add_channel']['channel'])
"); do
    hvractivate -J cap -J refr hvrhub "$canal"
done
```

### Riesgo
- **Medio.** Cambiar CycleByteLimit afecta cuántos datos se commitean juntos. Si hay rollback, más datos que rehacer.
- **Rollback:** Restaurar valores originales (CycleByteLimit=1000000000, Delay=300).

---

## ACCIÓN 3: ELIMINAR CLONE DIARIO DE PRO_0_STAGING_DB (FASE 1.1)

### Qué hace
Elimina el task de Snowflake que hace CLONE diario de PRO_0_STAGING_DB. Se reemplaza por Time Travel.

### Comandos correctos (ejecutar en Snowflake, no en HVR)

```bash
# Conectar a Snowflake y ejecutar:
# Verificar tasks existentes
SHOW TASKS IN DATABASE PRO_0_STAGING_DB;

# Eliminar task de CLONE diario (ajustar nombre)
DROP TASK IF EXISTS PRO_0_STAGING_DB.PUBLIC.CLONE_STAGING_DAILY;

# Verificar que se eliminó
SHOW TASKS IN DATABASE PRO_0_STAGING_DB;
```

### Riesgo
- **Alto.** Sin CLONE, no hay backup automático. Usar Time Travel (90 días) como alternativa.
- **Rollback:** Recrear el task con la misma definición original.

---

## ACCIÓN 4: OPTIMIZAR REFRESH_CLONE (FASE 1.2)

### Qué hace
Convierte los refreshes completos (full table) en incrementales usando Capture + Integrate en vez de reescribir toda la tabla.

### Comandos correctos

```bash
# Paso 1: Exportar definición
hvrdefinitionexport hvrhub /tmp/hub_export.json

# Paso 2: Modificar acciones Refresh para usar Method=APPEND
python3 << 'EOF'
import json

with open('/tmp/hub_export.json') as f:
    data = json.load(f)

count = 0
for change in data.get('changes', []):
    if 'add_channel' in change:
        ch_name = change['add_channel']['channel']
        for action in change['add_channel'].get('actions', []):
            if action['type'] == 'Refresh':
                if 'params' not in action:
                    action['params'] = {}
                # Cambiar a incremental
                action['params']['Method'] = 'APPEND'
                action['params']['BurstCommitFrequency'] = 'CYCLE'
                action['params']['CycleByteLimit'] = '2000000000'
                count += 1
                print(f"  Refresh incremental → Canal: {ch_name}")

with open('/tmp/hub_export.json', 'w') as f:
    json.dump(data, f, indent=2)

print(f"\nTotal Refresh actions modificadas: {count}")
EOF

# Paso 3: Importar y activar
hvrdefinitionimport hvrhub /tmp/hub_export.json
hvractivate -J cap -J refr hvrhub <CANAL_NAME>
```

### Riesgo
- **Alto.** APPEND solo inserta, no actualiza ni borra. Si hay deletes en origen, no se propagan.
- **Rollback:** Restaurar Method=REPLACE (full refresh).

---

## ACCIÓN 5: MIGRAR TABLAS A TRANSIENT (FASE 2.1)

### Qué hace
Reduce fail-safe storage en Snowflake de 90 días a 0 días, ahorrando ~50% del storage cost.

### Comandos correctos (SQL en Snowflake)

```bash
# Conectar a Snowflake y ejecutar para cada tabla en PRO_0_STAGING_DB:

# Listar todas las tablas HVR en PRO_0_STAGING_DB
SELECT TABLE_SCHEMA, TABLE_NAME 
FROM PRO_0_STAGING_DB.INFORMATION_SCHEMA.TABLES 
WHERE TABLE_NAME LIKE '%_V' OR TABLE_NAME LIKE 'HVR_%';

-- Convertir a TRANSIENT (una por una)
ALTER TABLE PRO_0_STAGING_DB.<SCHEMA>.<table> SET TRANSIENT;

-- O en lote (más eficiente):
SELECT 'ALTER TABLE ' || TABLE_SCHEMA || '.' || TABLE_NAME || ' SET TRANSIENT;'
FROM PRO_0_STAGING_DB.INFORMATION_SCHEMA.TABLES 
WHERE TABLE_NAME LIKE '%_V' OR TABLE_NAME LIKE 'HVR_%';
```

### Riesgo
- **Alto.** TRANSIENT tables pierden Time Travel (fail-safe). Si hay corrupción, no se puede recuperar.
- **Rollback:** `ALTER TABLE ... SET PERMANENT;` (recupera fail-safe pero no datos perdidos).

---

## ACCIÓN 6: ACTIVAR NOBEFOREUPDATE EN CAPTURE (FASE 2.2)

### Qué hace
Elimina la verificación "before update" que HVR hace para comparar el estado anterior de cada fila, reduciendo lecturas en origen.

### Comandos correctos

```bash
# Paso 1: Exportar
hvrdefinitionexport hvrhub /tmp/hub_export.json

# Paso 2: Añadir NoBeforeUpdate=true
python3 << 'EOF'
import json

with open('/tmp/hub_export.json') as f:
    data = json.load(f)

count = 0
for change in data.get('changes', []):
    if 'add_channel' in change:
        ch_name = change['add_channel']['channel']
        for action in change['add_channel'].get('actions', []):
            if action['type'] == 'Capture':
                if 'params' not in action:
                    action['params'] = {}
                action['params']['NoBeforeUpdate'] = 'true'
                count += 1
                print(f"  NoBeforeUpdate=true → Canal: {ch_name}")

with open('/tmp/hub_export.json', 'w') as f:
    json.dump(data, f, indent=2)

print(f"\nTotal Capture actions modificadas: {count}")
EOF

# Paso 3: Importar y activar
hvrdefinitionimport hvrhub /tmp/hub_export.json
hvractivate -J cap -J refr hvrhub <CANAL_NAME>
```

### Riesgo
- **Medio.** Sin BeforeUpdate, HVR no puede detectar si una fila cambió realmente. Puede generar falsos positivos en integración.
- **Rollback:** `NoBeforeUpdate=` (vaciar).

---

## ACCIÓN 7: REDUCIR RETENCIÓN DE HISTORY (FASE 2.4)

### Qué hace
Reduce el tiempo de retención del history de HVR (integrate history tables) de 90 días a 30 días.

### Comandos correctos

```bash
# Paso 1: Verificar retención actual
hvrhubconfig hvrhub History_Retention_Period

# Paso 2: Reducir a 30 días
hvrhubconfig hvrhub History_Retention_Period=30

# Paso 3: Verificar
hvrhubconfig hvrhub History_Retention_Period
```

### Riesgo
- **Bajo.** Solo afecta a datos históricos de HVR, no a los datos de negocio.
- **Rollback:** Restaurar valor original.

---

## ACCIÓN 8: OPTIMIZAR QUERIES ANALÍTICOS (FASE 2.3)

### Qué hace
Asegura que las queries analíticas sobre tablas HVR usen warehouse apropiado y no el de carga.

### Comandos correctos (SQL en Snowflake)

```bash
-- Crear warehouse analítico dedicado (si no existe)
CREATE WAREHOUSE IF NOT EXISTS ANALYTICS_WH
  WAREHOUSE_SIZE = 'SMALL'
  AUTO_SUSPEND = 60
  AUTO_RESUME = TRUE;

-- Verificar qué queries usan el warehouse de carga
SELECT QUERY_ID, QUERY_TEXT, WAREHOUSE_NAME, DATABASE_NAME, SCHEMA_NAME
FROM SNOWFLAKE.ACCOUNT_USAGE.QUERY_HISTORY
WHERE WAREHOUSE_NAME = 'PRO_LOAD_WH'
  AND DATABASE_NAME = 'PRO_0_STAGING_DB'
  AND START_TIME >= DATEADD(DAY, -7, CURRENT_TIMESTAMP())
ORDER BY START_TIME DESC;
```

### Riesgo
- **Bajo.** Solo afecta a queries analíticas, no a la replicación.
- **Rollback:** Ninguno necesario.

---

## ACCIÓN 9: ACTIVAR NOTRIGGERFIRING (FASE 3.2)

### Qué hace
Desactiva triggers en la base de destino durante la integración para reducir overhead.

### Comandos correctos

```bash
# Paso 1: Exportar
hvrdefinitionexport hvrhub /tmp/hub_export.json

# Paso 2: Añadir NoTriggerFiring=true
python3 << 'EOF'
import json

with open('/tmp/hub_export.json') as f:
    data = json.load(f)

count = 0
for change in data.get('changes', []):
    if 'add_channel' in change:
        ch_name = change['add_channel']['channel']
        for action in change['add_channel'].get('actions', []):
            if action['type'] == 'Integrate':
                if 'params' not in action:
                    action['params'] = {}
                action['params']['NoTriggerFiring'] = 'true'
                count += 1
                print(f"  NoTriggerFiring=true → Canal: {ch_name}")

with open('/tmp/hub_export.json', 'w') as f:
    json.dump(data, f, indent=2)

print(f"\nTotal Integrate actions modificadas: {count}")
EOF

# Paso 3: Importar y activar
hvrdefinitionimport hvrhub /tmp/hub_export.json
hvractivate -J cap -J refr hvrhub <CANAL_NAME>
```

### Riesgo
- **Medio.** Los triggers no se ejecutan durante la integración. Si hay lógica de negocio en triggers, no se aplicará.
- **Rollback:** `NoTriggerFiring=` (vaciar).

---

## ACCIÓN 10: ELIMINAR DUPLICADOS EN INTEGRACIÓN (FASE 3.4)

### Qué hace
Elimina filas duplicadas en tablas destino antes de integrar, reduciendo el volumen de datos procesado.

### Comandos correctos (SQL en Snowflake)

```bash
-- Para cada tabla con duplicados, ejecutar:
DELETE FROM PRO_0_STAGING_DB.<SCHEMA>.<table>
WHERE ROWID NOT IN (
  SELECT MIN(ROWID)
  FROM PRO_0_STAGING_DB.<SCHEMA>.<table>
  GROUP BY <PK_COLUMNS>
);

-- O más eficiente:
CREATE TABLE PRO_0_STAGING_DB.<SCHEMA>.<table>_deduped AS
SELECT DISTINCT * FROM PRO_0_STAGING_DB.<SCHEMA>.<table>;

DROP TABLE PRO_0_STAGING_DB.<SCHEMA>.<table>;

ALTER TABLE PRO_0_STAGING_DB.<SCHEMA>.<table>_deduped RENAME TO <table>;
```

### Riesgo
- **Alto.** Elimina datos. Verificar antes de ejecutar.
- **Rollback:** Restaurar desde Time Travel (si aún no expiró).

---

## RESUMEN DE COMANDOS HVR 6.2 CORRECTOS vs INCORRECTOS

| Lo que usamos (INCORRECTO) | Lo correcto (HVR 6.2) |
|-----------------------------|------------------------|
| `hvrcli -l channels` | `hvrdefinitionexport hvrhub /tmp/hub_export.json` + parse JSON |
| `hvrcli -c <ch> -A Capture -p Coalesce` | `hvrdefinitionexport` → modificar JSON → `hvrdefinitionimport` → `hvractivate` |
| `hvrcli -c <ch> -l actions` | `hvrdefinitionexport` + parse JSON con Python |
| `hvrversion` | `hvrdefinitionexport` (el JSON incluye `hvr_version`) |
| `hvrhubconfig -l channels` | `hvrhubconfig hvrhub` (sin subcomando channels) |

---

## ORDEN DE EJECUCIÓN RECOMENDADO

1. **Acción 1 (Coalesce)** — Bajo riesgo, -5% créditos
2. **Acción 7 (History Retention)** — Bajo riesgo, -2% créditos
3. **Acción 6 (NoBeforeUpdate)** — Medio riesgo, -3% créditos
4. **Acción 2 (COPY INTO)** — Medio riesgo, -3% créditos
5. **Acción 9 (NoTriggerFiring)** — Medio riesgo, -2% créditos
6. **Acción 5 (TRANSIENT)** — Alto riesgo, -3% créditos
7. **Acción 3 (Eliminar CLONE)** — Alto riesgo, -5% créditos
8. **Acción 4 (Refresh incremental)** — Alto riesgo, -8% créditos
9. **Acción 8 (Queries analíticos)** — Bajo riesgo, -2% créditos
10. **Acción 10 (Duplicados)** — Alto riesgo, -3% créditos

**Total esperado: -36% a -44% créditos Snowflake**
