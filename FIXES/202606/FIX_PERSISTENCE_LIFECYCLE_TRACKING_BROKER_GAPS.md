# FIX-20260612-001 — TRACKING DE CICLO DE VIDA PERSISTENCE (broker CLOSE sin registro)

**Branch sugerido:** `feature/persistence-lifecycle-tracking-broker-gaps`  
**Fecha:** 2026-06-12  
**Prioridad:** 🔴 ALTA  
**Estado:** ✅ CERRADO EN DEV (2026-06-12) — pendiente colector RESPONSE Sec12b  
**Tipo:** Instrumentación / Observabilidad + diagnóstico de pérdida de datos  
**Impacto BD:** ❌ Ninguno (solo logging)  
**Relacionado con:** FIX-20260317-001, FIX-20260515-001, FIX-20260408-001

---

## RESUMEN

Sec12 detecta **huecos** (cierre en broker sin entry REAL en persistence). Con `logs_deriv.log` ya sabemos **qué** contract_ids faltan, pero **no por qué** no se persistieron.

**Caso confirmado 2026-06-12 — R_75-strsisma:**

| Fuente | Dato |
|--------|------|
| Broker REAL CLOSE (`account_id: 23227041`) | **7** contract_ids |
| Persistence REAL (`samb_entrys`) | **0** |
| Persistence PRACTICE ese día | **3** (46593261) |
| Contract IDs huérfanos | `417020859`, `417364559`, `417678599`, `417746639`, `418814219`, `419371879`, `420712119` |

No es error de clasificación PRACTICE↔REAL: el broker cerró cuenta REAL y esos IDs **no aparecen en persistence.log**.

---

## PROBLEMA

Hoy el flujo es observable solo en puntos discretos:

```
BROKER OPEN → BROKER VERIFIED → [???] → ADD PERSISTENCE entry/result
```

El tramo `[???]` puede abortar por filtros MODE, permision_real, accuracy ML, excepción pre-persistencia, fallo BD silencioso, etc. **Sin log explícito, el hueco es indetectable en causa raíz.**

Relacionado con FIX-20260317-001 (solo loggea SUCCESS en ADD POSITIONS), pero este issue cubre el **ciclo completo por contract_id** incluyendo **SKIP** y **FAILED** con motivo.

---

## SOLUCIÓN PROPUESTA

### 1. Logger dedicado o canal en `persistence.log` (append-only)

Eventos mínimos por `contract_id`:

| Evento | Cuándo | Campos obligatorios |
|--------|--------|---------------------|
| `PERSISTENCE LIFECYCLE \| stage: BROKER_CLOSE_RECEIVED` | Al recibir cierre broker | contract_id, account_type, broker_profit, methodology, container |
| `PERSISTENCE LIFECYCLE \| stage: ENTRY_ATTEMPT` | Antes de add_entrys | contract_id, account, stake, methodology |
| `PERSISTENCE LIFECYCLE \| stage: ENTRY_SUCCESS` | Tras SUCCESS | contract_id, entry_id |
| `PERSISTENCE LIFECYCLE \| stage: ENTRY_FAILED` | Tras FAILED | contract_id, reason, error |
| `PERSISTENCE LIFECYCLE \| stage: ENTRY_SKIPPED` | Decisión de no persistir | contract_id, **skip_reason** (ej. MODE_BLOCKED, FILTER_X, NO_SIGNAL) |
| `PERSISTENCE LIFECYCLE \| stage: RESULT_ATTEMPT/SUCCESS/FAILED` | Igual para results | contract_id, result, win |

**Regla:** todo `BROKER RESPONSE CLOSE` en `logs_deriv.log` debe tener **exactamente una** terminal lifecycle: SUCCESS, FAILED o SKIPPED con reason.

### 2. Punto de instrumentación (Python)

| Archivo | Cambio |
|---------|--------|
| `EntityDeriv.py` | Emitir `BROKER_CLOSE_RECEIVED` al procesar CLOSE |
| `ServicesEntrys.py` / `ServicesEntrysResults.py` | ATTEMPT / SUCCESS / FAILED |
| Capa de filtros pre-entry (MODE, permision, ML gate) | `ENTRY_SKIPPED` con reason enum |

### 3. Colector — nueva Sec12b o extensión Sec12

CSV `dc_sec12b_persistence_gaps_YYYY-MM-DD.csv`:

- contract_id en broker REAL CLOSE
- ¿Existe lifecycle terminal en persistence?
- skip_reason / fail_reason si aplica
- **Diagnóstico:** GAP_NO_LIFECYCLE | SKIPPED | FAILED | OK

---

## CRITERIOS DE ACEPTACIÓN

1. Reproducir caso R75-STRSISMA: cada uno de los 7 CIDs tendría al menos `BROKER_CLOSE_RECEIVED` + terminal (SUCCESS/SKIPPED/FAILED).
2. Sec12 huecos > 0 → Sec12b muestra **reason** en ≥90% de casos.
3. Sin rotación en persistence.log (mismo principio que logs_deriv).
4. Cero impacto en lógica de trading — solo logs.

---

## VERIFICACIÓN POST-DEPLOY

```powershell
# Buscar lifecycle de un CID huérfano conocido
docker exec R_75-strsisma grep "417020859" /var/log/samb/persistence.log
docker exec R_75-strsisma grep "417020859" /var/log/samb/logs_deriv.log
```

Esperado: línea broker CLOSE + línea SKIPPED/FAILED con motivo, o confirmación de bug (sin lifecycle → gap de instrumentación).

---

## NOTAS

- **logs_deriv** resuelve lectura broker; **este fix** resuelve diagnóstico persistence.
- No sustituye FIX-20260408 (recovery WS) — complementa: si WS falla, lifecycle debe registrar FAILED/RECOVERY_PENDING.
- Acción correctiva (fix de filtro, bug, etc.) viene **después** de tener el reason en logs.

**Solicitante:** Análisis diario SAMB BSI  
**Última actualización:** 2026-06-12
