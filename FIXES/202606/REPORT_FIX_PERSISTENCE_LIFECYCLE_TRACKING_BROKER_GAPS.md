# REPORTE — FIX-20260612-001 (Cierre DEV)

**Fecha cierre DEV:** 2026-06-12  
**Estado:** ✅ CERRADO EN DEV — pendiente colector RESPONSE (Sec12b)  
**Contenedor verificado:** `samb-hexagonal`  
**Branch:** `set-reporting-entrys`

---

## Qué se hizo

Se añadió **tracking de ciclo de vida por `contract_id`** en `persistence.log`, usando el logger existente `ServicesPersistence`. Mismo estilo de campos que `ADD PERSISTENCE` (Project, Methodology, Contract ID, Account REAL/PRACTICE, etc.).

**Nuevo módulo:** `apis/services/persistencelifecycle/PersistenceLifecycleLogger.py`

| Stage | Dónde se emite | Propósito |
|-------|----------------|-----------|
| `BROKER_CLOSE_RECEIVED` | `EntityDeriv.py` | Cierre broker (won/lost/recovered) |
| `ENTRY_ATTEMPT` / `ENTRY_SUCCESS` / `ENTRY_FAILED` | `ServicesEntrys.py` | Persistencia entry |
| `RESULT_ATTEMPT` / `RESULT_SUCCESS` / `RESULT_FAILED` | `ServicesEntrysResults.py` | Persistencia result |
| `ENTRY_SKIPPED` | `ServicesManagerDays.py` | MODE / permisos |
| `ENTRY_SKIPPED` | 20 servicios Check + wrapper | Broker inválido o cadena abortada |

Formato de línea:

```
🔄 PERSISTENCE LIFECYCLE | stage: ENTRY_SUCCESS | Project: ... | Methodology: ... | Contract ID: ... | Account: PRACTICE | Entry ID: ...
```

**Sin cambios** de lógica de negocio ni esquema BD — solo logs adicionales junto a `ADD PERSISTENCE`.

---

## Evidencia DEV (2026-06-12 ~18:46–18:47 UTC)

Contract ID de prueba: `2009964699` (Trends-Expansive, PRACTICE)

Secuencia en `/var/log/samb/persistence.log`:

1. `ENTRY_SKIPPED | Skip Reason: MODE_BLOCKED_PRACTICE` (check MODE previo)
2. `BROKER_CLOSE_RECEIVED | Contract ID: 2009964699 | Account: PRACTICE | Broker Profit: 0.92`
3. `ENTRY_ATTEMPT` → `ENTRY_SUCCESS` → `ADD PERSISTENCE samb_entrys SUCCESS`
4. `RESULT_ATTEMPT` → `RESULT_SUCCESS` → `ADD PERSISTENCE samb_entrys_results SUCCESS`

Cada cierre broker queda con terminal lifecycle (SUCCESS en este caso).

---

## Qué resuelve vs caso R_75-strsisma

Antes: Sec12 veía huecos (broker CLOSE sin entry) pero **no el motivo**.

Ahora: por cada `contract_id` con cierre broker debería existir en `persistence.log`:
- `BROKER_CLOSE_RECEIVED` + terminal (`ENTRY_SUCCESS` / `ENTRY_FAILED` / `ENTRY_SKIPPED` con `Skip Reason`)

Si solo aparece `BROKER_CLOSE_RECEIVED` sin terminal → el flujo no llegó a intentar persistencia (crash/corte entre pasos).

---

## Pendiente fuera de DEV

| Item | Repo | Acción |
|------|------|--------|
| Sec12b colector | RESPONSE | CSV `dc_sec12b_persistence_gaps` cruzando `logs_deriv` + lifecycle |

---

## Archivos modificados (DEV)

- `apis/services/persistencelifecycle/PersistenceLifecycleLogger.py` *(nuevo)*
- `apis/entities/deriv/EntityDeriv.py`
- `apis/services/entrys/ServicesEntrys.py`
- `apis/services/entrysresults/ServicesEntrysResults.py`
- `apis/services/managerdays/ServicesManagerDays.py`
- 20× `apis/services/check*/ServicesCheck*.py` (wrapper lifecycle)

---

## Rollback

Eliminar módulo `persistencelifecycle` y revertir imports/wrapper. `ADD PERSISTENCE` existente no se toca.
