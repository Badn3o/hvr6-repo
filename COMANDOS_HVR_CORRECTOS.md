# COMANDOS HVR 6.2 CORRECTOS — AUDITORÍA DEL ESTADO ACTUAL
## Validación contra documentación oficial Fivetran HVR 6.2.0/1

---

## ⚠️ COMANDOS INCORRECTOS QUE USAMOS ANTES (NO EXISTEN EN HVR 6.2)

| Comando incorrecto | Motivo |
|-------------------|--------|
| `hvrcli -l channels` | No existe `hvrcli` en HVR 6.2 |
| `hvrcli -c <channel> -A Capture -p Coalesce` | No existe `hvrcli` |
| `hvrcli -c <channel> -l actions` | No existe `hvrcli` |
| `hvrversion` | No existe como comando independiente |

---

## ✅ COMANDOS CORRECTOS PARA AUDITORÍA

### Paso 1: Verificar el hub server y listar hubs

```bash
# Listar todos los hubs configurados en el servidor
hvrhubconfig

# Ver propiedades de un hub específico (reemplaza <HUB_NAME>)
hvrhubconfig <HUB_NAME>

# Ver el repositorio del hub
hvrreposconfig
```

### Paso 2: Ver la definición del hub (channels, locations, actions)

HVR 6.2 no tiene un comando "list channels". La definición está en el repositorio.
Para ver la configuración actual, exportar la definición completa:

```bash
# Exportar definición completa del hub a JSON
hvrdefinitionexport <HUB_NAME> /tmp/hub_export.json

# Ver el contenido
cat /tmp/hub_export.json | python3 -m json.tool | head -100
```

### Paso 3: Ver los canales y sus acciones

```bash
# Exportar la definición del hub
hvrdefinitionexport <HUB_NAME> /tmp/hub_export.json

# Filtrar canales y acciones
cat /tmp/hub_export.json | python3 -c "
import json, sys
data = json.load(sys.stdin)
channels = data.get('channels', {})
for ch_name, ch_def in channels.items():
    print(f'\\n=== Canal: {ch_name} ===')
    print(f'  Description: {ch_def.get(\"description\", \"N/A\")}')
    actions = ch_def.get('actions', [])
    for a in actions:
        print(f'  Action: {a[\"type\"]} (scope: {a.get(\"loc_scope\", \"N/A\")})')
        if a.get('params'):
            for k, v in a['params'].items():
                print(f'    {k}: {v}')
    loc_groups = ch_def.get('loc_groups', {})
    for lg_name, lg_def in loc_groups.items():
        members = lg_def.get('members', [])
        print(f'  Location Group [{lg_name}]: {members}')
"
```

### Paso 4: Ver los jobs en ejecución

```bash
# No hay comando directo para listar jobs en CLI.
# Se puede usar la REST API con el token de login:

# Primero, login para obtener token
hvrlogin -R http://localhost:4343 -u hvradmin -s

# Luego, consultar jobs vía API
curl -s -H "Authorization: Bearer $HVR_LOGIN_TOKEN" \
  http://localhost:4343/api/v0/hubs/<HUB_NAME>/jobs | python3 -m json.tool
```

### Paso 5: Ver las locations

```bash
# Exportar definición y filtrar locations
hvrdefinitionexport <HUB_NAME> /tmp/hub_export.json

cat /tmp/hub_export.json | python3 -c "
import json, sys
data = json.load(sys.stdin)
locations = data.get('locations', {})
for loc_name, loc_def in locations.items():
    props = loc_def.get('props', {})
    print(f'\\n=== Location: {loc_name} ===')
    print(f'  Class: {props.get(\"Class\", \"N/A\")}')
    print(f'  Capture_Method: {props.get(\"Capture_Method\", \"N/A\")}')
    print(f'  Database_Host: {props.get(\"Database_Host\", \"N/A\")}')
    print(f'  Database_Name: {props.get(\"Database_Name\", \"N/A\")}')
"
```

---

## COMANDOS CORRECTOS PARA LAS ACCIONES DEL PLAN

### Fase 1.4: Activar Coalesce en Capture

```bash
# NO existe hvrcli. La configuración de acciones se hace:
# 1. Exportar definición actual
hvrdefinitionexport <HUB_NAME> /tmp/hub_export.json

# 2. Modificar el JSON para añadir Coalesce=true en Capture actions
python3 -c "
import json
with open('/tmp/hub_export.json') as f:
    data = json.load(f)
for ch_name, ch_def in data.get('channels', {}).items():
    for action in ch_def.get('actions', []):
        if action['type'] == 'Capture':
            action['params']['Coalesce'] = 'true'
            print(f'Coalesce activado en canal {ch_name}')
with open('/tmp/hub_export.json', 'w') as f:
    json.dump(data, f, indent=2)
"

# 3. Importar la definición modificada
hvrdefinitionimport <HUB_NAME> /tmp/hub_export.json

# 4. Activar el canal para aplicar cambios
hvractivate -J cap -J refr <HUB_NAME> <CHANNEL_NAME>
```

### Fase 1.1: Eliminar task de CLONE diario

```bash
# No es un comando HVR. Es una task de Snowflake.
# Se elimina desde Snowflake:
# DROP TASK IF EXISTS <task_name>;
```

### Fase 1.2: Optimizar REFRESH_CLONE

```bash
# El refresh se configura con acciones en el canal.
# Para modificar la acción Refresh:
# 1. Exportar definición
hvrdefinitionexport <HUB_NAME> /tmp/hub_export.json

# 2. Modificar parámetros de Refresh (ej: añadir Method=APPEND)
python3 -c "
import json
with open('/tmp/hub_export.json') as f:
    data = json.load(f)
for ch_name, ch_def in data.get('channels', {}).items():
    for action in ch_def.get('actions', []):
        if action['type'] == 'Refresh':
            action['params']['Method'] = 'APPEND'
            print(f'Refresh Method=APPEND configurado en canal {ch_name}')
with open('/tmp/hub_export.json', 'w') as f:
    json.dump(data, f, indent=2)
"

# 3. Importar y activar
hvrdefinitionimport <HUB_NAME> /tmp/hub_export.json
hvractivate -J cap -J refr <HUB_NAME> <CHANNEL_NAME>
```

### Fase 2.1: Migrar tablas a TRANSIENT

```bash
# No es un comando HVR. Es SQL de Snowflake:
# ALTER TABLE <schema>.<table_name> SET TRANSIENT;
```

### Fase 2.2: Activar NoBeforeUpdate en Capture

```bash
# Mismo patrón que Coalesce:
# 1. Exportar
# 2. Modificar JSON: action.params['NoBeforeUpdate'] = 'true'
# 3. Importar
# 4. Activar
```

---

## RESUMEN DE COMANDOS HVR 6.2 OFICIALES

| Comando | Función |
|---------|---------|
| `hvrhubconfig` | Gestionar propiedades del hub (listar, crear, modificar) |
| `hvrreposconfig` | Configurar el repositorio del hub |
| `hvrdefinitionexport` | Exportar definición completa a JSON |
| `hvrdefinitionimport` | Importar definición desde JSON |
| `hvrrefresh` | Ejecutar refresh (carga inicial o completa) |
| `hvractivate` | Activar replication jobs de un canal |
| `hvrcompare` | Comparar datos entre locations |
| `hvradapt` | Adaptar tablas del canal al schema real |
| `hvrlogin` | Autenticación remota al hub |
| `hvragentlistener` | Gestionar HVR Agent |
| `hvragentconfig` | Configurar propiedades del Agent |
| `hvragentuserconfig` | Gestionar usuarios del Agent |
| `hvralertconfig` | Gestionar alertas del hub |
| `hvruserconfig` | Gestionar usuarios del hub |
| `hvrlicense` | Gestionar licencia |
| `hvreventtool` | Herramienta de eventos |
| `hvreventview` | Ver eventos |
| `hvrfingerprint` | Ver fingerprint del hub |
| `hvralertmanager` | Gestionar ejecución de alertas |

---

## PRÓXIMO PASO

Ejecuta en sv3770:

```bash
# 1. Listar hubs
hvrhubconfig

# 2. Una vez tengas el nombre del hub, exportar definición
hvrdefinitionexport <HUB_NAME> /tmp/hub_export.json

# 3. Ver canales y acciones
cat /tmp/hub_export.json | python3 -c "
import json, sys
data = json.load(sys.stdin)
channels = data.get('channels', {})
for ch_name, ch_def in channels.items():
    print(f'Canal: {ch_name}')
    for a in ch_def.get('actions', []):
        params = ', '.join([f'{k}={v}' for k,v in a.get('params', {}).items()])
        print(f'  {a[\"type\"]}: {params}')
"
```

Pásame el output y te doy los comandos exactos para cada acción del plan.
