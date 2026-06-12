# FIX-20260602-001 — EXTENDER logs_deriv.log CON EVENTOS DE RECOVERY WEBSOCKET (Sec17)

**Branch sugerido:** `feature/extend-logs-deriv-ws-recovery-events`  
**Fecha:** 2026-06-02  
**Prioridad:** 🟠 ALTA  
**Estado:** ✅ CERRADO EN DEV (2026-06-12) — pendiente colector RESPONSE Sec17  
**Tipo:** Instrumentación / Observabilidad (complemento de FIX-20260515-001)  
**Impacto en base de datos:** ❌ Ninguno  
**Impacto en lógica de negocio:** ❌ Ninguno — logging puro  
**Variables de entorno nuevas:** ❌ Ninguna  
**Depende de:** FIX-20260515-001 (`logs_deriv.log` + handler `deriv` en `settings.py`)  
**Relacionado con:** FIX-20260408-001 (recovery WebSocket en `EntityDeriv.py`)

---

## RESUMEN EJECUTIVO

Tras migrar las Secciones **12, 16 y 18** del colector a `logs_deriv.log`, la **Sección 17** (recovery WebSocket) sigue leyendo `response.log` vía `Get-DockerLogsForDate`. Eso expone el **mismo riesgo de rotación** que generaba falsos huérfanos en Sec12: eventos del día pueden no estar en el fragmento activo del archivo al momento del análisis.

**Objetivo:** espejar en `logs_deriv.log` todos los eventos de interacción broker necesarios para Sec17, y actualizar el colector para leerlos con `Get-DerivLogsForDate` (mismo patrón que Sec12/16).

Con este cambio, **todas las secciones de reconciliación broker ↔ persistence** del análisis diario usarán una única fuente confiable (`logs_deriv.log` + `persistence.log`).

---

## CONTEXTO — ESTADO ACTUAL DEL MAPEO

| Sección | Propósito | Fuente broker hoy | Fuente persistence | Estado |
|---------|-----------|-------------------|----------------------|--------|
| **12** | Huérfanos / huecos REAL (OPEN, VERIFIED, CLOSE) | ✅ `logs_deriv.log` | `persistence.log` | Migrado (colector RESPONSE) |
| **16** | Empates y descuadres profit broker vs BD | ✅ `logs_deriv.log` | `persistence.log` | Migrado |
| **18** | Cross-validation account_id REAL/PRACTICE | ✅ `logs_deriv.log` (vía `response_*.txt` generado en Sec16) | `persistence.log` | Migrado |
| **17** | Recovery WebSocket (RECONNECT, RECOVERED, UNRECOVERABLE) | ⚠️ `response.log` (grep rotado) | `persistence.log` | **Pendiente este fix** |

Secciones que **no** son reconciliación broker↔BD y pueden seguir en `response.log` sin bloquear el objetivo:

| Sección | Propósito | Fuente razonable |
|---------|-----------|-----------------|
| 1 | Errores críticos HTTP/Traceback | `response.log` |
| 7 | MODE OPERATIVITY CHECK | `response.log` |

---

## PROBLEMA RAÍZ

### Síntoma

En días con activaciones de recovery WS (ej. 2026-06-05: 2 contratos recuperados), Sec17 depende de:

```powershell
# samb_data_collector.ps1 — Sec17 (estado actual)
$dlogs17 = Get-DockerLogsForDate -Container $c -Date $TODAY
# Get-DockerLogsForDate internamente:
docker exec $Container grep "BROKER RESPONSE CLOSE\|...\|WEBSOCKET" /var/log/samb/response.log
```

Si `response.log` rotó después de esos eventos, el colector puede reportar:

- Sec17 = **N/A** o CSV vacío cuando sí hubo recovery
- Subconteo de `Recovered` / `Unrecoverable`
- Imposibilidad de cruzar `PersistConfirmed` para contratos recuperados

### Evidencia histórica

| Fecha | Sec17 observado | Riesgo |
|-------|-----------------|--------|
| 2026-06-01 | N/A — "sin eventos BROKER RESPONSE CLOSE en response.log" | Rotación / lectura parcial |
| 2026-06-05 | 2 RECOVERED detectados | Funcionó ese día; frágil ante rotación |
| 2026-06-09 | Sec12 huérfanos corregidos con logs_deriv; Sec17 sin incidencias | Sec17 aún no beneficia de logs_deriv |

---

## ALCANCE — EVENTOS A ESPEJAR EN logs_deriv.log

El handler `deriv` (`logger_deriv = logging.getLogger('deriv')`) debe recibir **la misma línea** que ya se escribe al logger principal de broker, inmediatamente después, sin alterar `response.log`.

### Eventos obligatorios para Sec17

Patrones que parsea hoy `samb_data_collector.ps1` (Sec17):

| Patrón regex (colector) | Origen (FIX-20260408-001) | Prioridad |
|-------------------------|---------------------------|-----------|
| `Recovery: WEBSOCKET_RECONNECT` + `contract_id:` | Inicio de intento de reconexión | 🔴 Obligatorio |
| `Recovery: RECONNECT_OK` + `contract_id:` | Reconexión WS exitosa | 🔴 Obligatorio |
| `Recovery: RECONNECT_FAILED` + `contract_id:` | Reconexión WS fallida | 🔴 Obligatorio |
| `BROKER RESPONSE CLOSE RECOVERED` + `contract_id:` + `broker_profit:` | Cierre recuperado con datos raw | 🔴 Obligatorio |
| `BROKER RESPONSE CLOSE UNRECOVERABLE` + `contract_id:` | Reintentos agotados | 🔴 Obligatorio |

### Eventos recomendados (consistencia con Sec12)

Ya consumidos por Sec12 desde `logs_deriv.log`; confirmar que **dev los incluye** en el espejo:

| Evento | Uso |
|--------|-----|
| `BROKER RESPONSE OPEN` | Conteo aperturas / cruce entrys |
| `BROKER CONTRACT VERIFIED` (status OK/FAILED) | Verificación post-apertura |
| `BROKER RESPONSE CLOSE` (cierre normal con `broker_profit`) | Sec12/16/18 |
| `BROKER REQUEST` | Trazabilidad completa del ciclo |
| `ACCOUNT TYPE CHECK` | Sec12 `AcctMismatch` |
| `WARNING.*BROKER RESPONSE CLOSE.*is_sold=False` | Sec12 `IsSoldFalse` |

> **Nota de alineación con FIX-20260408-001:** el documento del fix WS usa también `Recovery: FAILED` y `Recovery: EXHAUSTED` en algunas trazas. El colector Sec17 busca `RECONNECT_OK` / `RECONNECT_FAILED`. Dev debe espejar **exactamente** lo que emite producción hoy; si hay divergencia de strings, unificar en `EntityDeriv.py` y actualizar regex del colector en el mismo PR.

---

## SOLUCIÓN PROPUESTA

### 1. Python — espejo en `EntityDeriv.py` (y `ServicesBrokerSession.py` si aplica)

En **cada** punto donde se loggea un evento de recovery o cierre broker, agregar:

```python
import logging
logger_deriv = logging.getLogger('deriv')

# Ejemplo — patrón mirror (NO tocar la línea logger.info existente):
msg = (
    f"BROKER RESPONSE CLOSE RECOVERED | contract_id: {contract_id} | "
    f"account_id: {account_id} | broker_profit: {profit} | "
    f"broker_sell_price: {sell} | broker_buy_price: {buy} | "
    f"broker_payout: {payout} | status: {status} | "
    f"Recovery: WEBSOCKET_RECONNECT | attempt: {attempt}"
)
logger.info(msg)          # response.log — sin cambios
logger_deriv.info(msg)    # logs_deriv.log — NUEVO espejo
```

Puntos mínimos a cubrir en `EntityDeriv.py`:

1. Bloque `except WebSocketException` → log `Recovery: WEBSOCKET_RECONNECT`
2. Tras reconexión exitosa → `Recovery: RECONNECT_OK`
3. Tras reconexión fallida → `Recovery: RECONNECT_FAILED` (o `Recovery: FAILED` — alinear)
4. Cierre recuperado → `BROKER RESPONSE CLOSE RECOVERED`
5. Reintentos agotados → `BROKER RESPONSE CLOSE UNRECOVERABLE`

**Principio:** `propagate: False` en logger `deriv` (ya definido en FIX-20260515-001) — evitar duplicados en `response.log`.

### 2. Colector — migrar Sec17 a `Get-DerivLogsForDate`

```powershell
# ANTES (Sec17):
$dlogs17 = Get-DockerLogsForDate -Container $c -Date $TODAY

# DESPUÉS (Sec17):
$dlogs17 = Get-DerivLogsForDate -Container $c -Date $TODAY
```

Sin cambios en la lógica de agrupación por `contract_id` ni en el cruce `PersistConfirmed` contra `persistence.log`.

**Responsabilidad dev vs RESPONSE:** el cambio en `samb_data_collector.ps1` puede hacerse en paralelo o en el repo RESPONSE tras deploy del espejo en contenedores. Recomendación: **mismo sprint** — deploy Python primero, luego actualizar colector.

### 3. Verificación post-deploy

```powershell
# En contenedor (ej. R_75-strsi):
docker exec R_75-strsi grep "Recovery:\|RECOVERED\|UNRECOVERABLE" /var/log/samb/logs_deriv.log | tail -20

# Colector:
cd C:\Users\Janus\SAMB\RESPONSE\POWERSHELL
.\samb_data_collector.ps1
# Revisar TEMPORAL\dc_sec17_ws_recovery_YYYY-MM-DD.csv
```

---

## CRITERIOS DE ACEPTACIÓN

| # | Criterio | Verificación |
|---|----------|--------------|
| 1 | Todo evento Sec17 visible en `response.log` también existe en `logs_deriv.log` (mismo día UTC) | diff de conteos por patrón en día con recovery |
| 2 | Sec17 alimentada solo por `Get-DerivLogsForDate` | grep colector no usa `Get-DockerLogsForDate` en bloque Sec17 |
| 3 | Día con recovery conocido (ej. 2026-06-05) reproduce mismos `Recovered`/`Unrecoverable` que antes | comparar CSV histórico vs nuevo |
| 4 | Día sin recovery → CSV vacío, mensaje "sin incidencias WS" | comportamiento idempotente |
| 5 | Sec12 sigue `Huérfanos = 0` en días normales | regresión Sec12 |
| 6 | `logs_deriv.log` sigue append-only, sin rotación | revisar `settings.py` handler |

---

## MAPA FINAL — ¿TODAS LAS INTERACCIONES BROKER MAPEADAS?

**Sí, para el propósito de auditoría y matching con base de datos:**

```
persistence.log (append-only, cat completo)
        ↕ contract_id / Account REAL|PRACTICE / Result / Win
logs_deriv.log (append-only, cat completo)
        ↕ OPEN → VERIFIED → CLOSE | CLOSE RECOVERED | CLOSE UNRECOVERABLE
        ↕ Recovery: WEBSOCKET_RECONNECT | RECONNECT_OK | RECONNECT_FAILED
```

| Flujo | Sec | Matching |
|-------|-----|----------|
| Apertura broker vs entry persistence | 12 | ✅ |
| Cierre broker vs resultado persistence | 12, 16 | ✅ |
| account_id broker vs Account persistence | 18 | ✅ |
| Recovery WS vs persistencia post-recovery | 17 | ✅ tras este fix |
| Balance REAL agregado (WIN/LOSS/PENDING) | 11 | persistence only |

**No cubierto por logs_deriv** (y no debe bloquear este issue):

- Telegram / reportes metodología (Sec2)
- MODE operativity (Sec7)
- Errores HTTP 500 genéricos (Sec1)

---

## ARCHIVOS A MODIFICAR

| Repo | Archivo | Cambio |
|------|---------|--------|
| SAMB (dev) | `settings.py` | Sin cambio si FIX-20260515-001 ya desplegado |
| SAMB (dev) | `apis/entities/deriv/EntityDeriv.py` | `logger_deriv.info(...)` en todos los puntos recovery + cierres especiales |
| SAMB (dev) | `apis/services/ServicesBrokerSession.py` | Espejo si los logs RECONNECT_* se emiten aquí |
| RESPONSE | `POWERSHELL/samb_data_collector.ps1` | Sec17: `Get-DerivLogsForDate` en lugar de `Get-DockerLogsForDate` |
| RESPONSE | `PROMPTS/PROMPT_OPTIMIZADO_ANALISIS_DIARIO_V21.md` | Nota: Sec17 fuente = `logs_deriv.log` (opcional, post-deploy) |

---

## PLAN DE TESTING

### Test manual — contenedor con FIX desplegado

1. Forzar o esperar un `WebSocketException` en polling de cierre (staging).
2. Confirmar secuencia en **ambos** archivos:
   - `/var/log/samb/response.log`
   - `/var/log/samb/logs_deriv.log`
3. Ejecutar colector para la fecha del evento.
4. Validar fila en `dc_sec17_ws_recovery_*.csv` con `PersistConfirmed = 1` si hubo `ADD PERSISTENCE`.

### Test de regresión — día sin recovery

1. Ejecutar colector en fecha sin eventos WS.
2. Sec17 debe exportar CSV vacío y log: `FIX-20260408-001 ACTIVO - sin activaciones hoy`.

### Test de regresión — Sec12

1. Día con trades REAL cerrados (ej. 2026-06-09).
2. `BrokerRealCIDs ≈ PersistRealCIDs`, `Huerfanos = 0`.

---

## ROLLBACK

| Nivel | Acción |
|-------|--------|
| Python | Revertir líneas `logger_deriv.info` — `response.log` intacto |
| Colector | Revertir Sec17 a `Get-DockerLogsForDate` |

Sin impacto en BD ni en operativa de trading.

---

## INSTRUCCIONES PARA DEV / LLM

1. Localizar en `EntityDeriv.py` todos los `logger.info` / `logger.warning` / `logger.error` que contengan:
   - `Recovery:`
   - `BROKER RESPONSE CLOSE RECOVERED`
   - `BROKER RESPONSE CLOSE UNRECOVERABLE`
2. Añadir `logger_deriv.info(msg)` con el **mismo string** inmediatamente después.
3. Confirmar que FIX-20260515-001 está en la rama (handler `file_deriv` activo).
4. Desplegar en **un** contenedor staging, simular recovery, validar espejo.
5. Rollout a los 12 contenedores `R_*`.
6. Avisar a RESPONSE para merge del cambio Sec17 en colector (o incluir en PR coordinado).

---

## REFERENCIAS

- [FIX_ADD_LOGS_DERIV_DEDICATED_BROKER_FILE.md](FIX_ADD_LOGS_DERIV_DEDICATED_BROKER_FILE.md) — FIX-20260515-001
- [FIX_WEBSOCKET_RECONNECT_CONTRACT_RECOVERY.md](FIX_WEBSOCKET_RECONNECT_CONTRACT_RECOVERY.md) — FIX-20260408-001
- Colector Sec17: `POWERSHELL/samb_data_collector.ps1` líneas ~489–571
- Función compartida: `Get-DerivLogsForDate` (cat `/var/log/samb/logs_deriv.log`)

---

**Solicitante:** Análisis diario SAMB BSI / equipo RESPONSE  
**Última actualización:** 2026-06-02
