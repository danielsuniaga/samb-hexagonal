# INSTRUCCIONES MAPPING — Sesión análisis diario (post-fix DEV 2026-06-12)

Usar este bloque en el **prompt de mapping / análisis diario** (repo RESPONSE) para la sesión de mañana.

---

## 1. Fuentes de datos broker (actualizado)

| Sección | Fuente | Comando lectura |
|---------|--------|-----------------|
| Sec 12 / 16 / 18 | `logs_deriv.log` | `Get-DerivLogsForDate` → `docker exec $c cat /var/log/samb/logs_deriv.log` |
| Sec 17 (recovery WS) | `logs_deriv.log` | **Migrar** de `Get-DockerLogsForDate` → `Get-DerivLogsForDate` |
| Sec 11 / persistence | `persistence.log` | `cat` completo (sin rotación agresiva en fragmento activo) |

**Regla:** broker = `logs_deriv.log` únicamente. No usar `grep` sobre `response.log` para reconciliación broker↔BD.

---

## 2. Patrones broker en `logs_deriv.log`

```
BROKER REQUEST | contract_type: | symbol:
BROKER RESPONSE OPEN | contract_id:
BROKER CONTRACT VERIFIED | contract_id: | status:
BROKER RESPONSE CLOSE | contract_id: | account_id: | broker_profit:
BROKER RESPONSE CLOSE RECOVERED | contract_id: | broker_profit:
BROKER RESPONSE CLOSE UNRECOVERABLE | contract_id:
BROKER SESSION | Event: RECONNECT_OK | contract_id:
BROKER SESSION | Event: RECONNECT_FAILED | contract_id:
ACCOUNT TYPE CHECK | account_type: REAL|DEMO
Recovery: WEBSOCKET_RECONNECT | contract_id:
Recovery: FAILED | contract_id:
```

**Account REAL:** `account_id` numérico (ej. `23227041`) o `account_type: REAL`.  
**Account PRACTICE:** `account_id` demo (ej. `46593261`, prefijo DOT) o `Account: PRACTICE` en lifecycle.

---

## 3. Patrones lifecycle en `persistence.log` (NUEVO — Sec12b)

Prefijo fijo:

```
PERSISTENCE LIFECYCLE | stage:
```

| Stage | Significado | Terminal |
|-------|-------------|----------|
| `BROKER_CLOSE_RECEIVED` | Broker cerró posición | No |
| `ENTRY_ATTEMPT` | Inicio persist entry | No |
| `ENTRY_SUCCESS` | Entry en BD OK | **Sí (OK)** |
| `ENTRY_FAILED` | Fallo BD entry | **Sí (FAILED)** |
| `ENTRY_SKIPPED` | No se persistió | **Sí (SKIPPED)** |
| `RESULT_ATTEMPT` | Inicio persist result | No |
| `RESULT_SUCCESS` | Result en BD OK | **Sí (OK)** |
| `RESULT_FAILED` | Fallo BD result | **Sí (FAILED)** |

**Campos clave para cruce:**

```
Project: | Methodology: | Contract ID: | Account: REAL|PRACTICE | Skip Reason: | Error:
```

**Skip reasons conocidos:**

| Skip Reason | Diagnóstico |
|-------------|-------------|
| `MODE_BLOCKED_PRACTICE` | Día/metodología en PRACTICE, no operó REAL |
| `NO_PERMISSION_REAL` | `permision_real` bloqueó operación |
| `MODE_BLOCKED_UNEXPECTED` | Tipo manager day inconsistente |
| `INVALID_BROKER_RESULT` | Broker no devolvió resultado válido antes de persistence |
| `PERSISTENCE_CHAIN_ABORTED` | Entry OK parcial pero falló indicators/movements/results |
| `RECOVERY_EXHAUSTED` | WS recovery agotado (ver también UNRECOVERABLE en deriv) |

---

## 4. Algoritmo Sec12b (nuevo CSV sugerido)

Para cada `contract_id` en **broker REAL CLOSE** del día (`logs_deriv.log`):

1. Buscar `PERSISTENCE LIFECYCLE` con mismo `Contract ID` en `persistence.log`.
2. Clasificar:

| Condición | Diagnóstico CSV |
|-----------|-----------------|
| Terminal `ENTRY_SUCCESS` + `RESULT_SUCCESS` | `OK` |
| Terminal `ENTRY_SKIPPED` | `SKIPPED` + `skip_reason` |
| Terminal `ENTRY_FAILED` / `RESULT_FAILED` | `FAILED` + `error` |
| Solo `BROKER_CLOSE_RECEIVED`, sin terminal | `GAP_NO_LIFECYCLE` |
| Sin ninguna línea lifecycle | `GAP_NO_INSTRUMENTATION` (pre-deploy o bug) |

3. Cruzar con Sec12 huecos: todo huérfano Sec12 debe tener fila Sec12b con reason.

---

## 5. Ejemplo verificado DEV (referencia)

```
Contract ID: 2009964699
logs_deriv:     OPEN → VERIFIED → CLOSE (profit 0.92)
persistence:    BROKER_CLOSE_RECEIVED → ENTRY_SUCCESS → RESULT_SUCCESS
Account:        PRACTICE
Project:        samb-hexagonal
Methodology:    3trendssimple0000000000000000000
```

Comando reproducción:

```powershell
docker exec samb-hexagonal grep "2009964699" /var/log/samb/logs_deriv.log
docker exec samb-hexagonal grep "2009964699" /var/log/samb/persistence.log
```

---

## 6. Checklist sesión mañana

- [ ] Deploy SAMB con este commit en contenedores `R_*`
- [ ] Confirmar `logs_deriv.log` y lifecycle en un contenedor piloto
- [ ] Actualizar `samb_data_collector.ps1`: Sec17 → `Get-DerivLogsForDate`
- [ ] Añadir Sec12b según sección 4
- [ ] Actualizar prompt análisis diario con secciones 1–3 de este documento
- [ ] Re-ejecutar día con huecos conocidos (ej. R_75-strsisma 2026-06-12) **solo post-deploy prod**

---

## 7. Texto listo para pegar en prompt de mapping

```
MAPPING BROKER ↔ PERSISTENCE (vigente desde 2026-06-12 DEV):

1) Broker: leer SOLO /var/log/samb/logs_deriv.log (cat completo, Get-DerivLogsForDate).
   Incluye OPEN, CLOSE, RECOVERED, UNRECOVERABLE, SESSION RECONNECT, ACCOUNT TYPE CHECK.

2) Persistence lifecycle: leer /var/log/samb/persistence.log buscando líneas
   "PERSISTENCE LIFECYCLE | stage:" por Contract ID.

3) Por cada broker REAL CLOSE del día, debe existir terminal lifecycle:
   ENTRY_SUCCESS+RESULT_SUCCESS (OK), ENTRY_SKIPPED (motivo), ENTRY/RESULT_FAILED (error),
   o GAP_NO_LIFECYCLE si solo hay BROKER_CLOSE_RECEIVED.

4) Campos cruce: Contract ID + Project + Methodology + Account (REAL|PRACTICE).

5) Sec17 recovery: fuente logs_deriv.log (no response.log).
   Sec12b gaps: cruce logs_deriv CLOSE vs persistence lifecycle terminal + Skip Reason.
```
