# 📋 PLAN DE TESTING - MIGRACIÓN VARCHAR(14) → DATETIME

**Branch:** `optimization-date`  
**Fecha:** 26/12/2025  
**Objetivo:** Validar migración de fechas con cobertura 100% de cambios en repositorios

---

## 🎯 OBJETIVO

Validar que los **6 métodos modificados** en **4 repositorios** funcionan correctamente después de la migración y muestran mejora significativa de performance (≥70%).

---

## 📊 COBERTURA - MAPEO COMPLETO

| # | Repositorio | Método Modificado | Test que lo cubre | Línea |
|---|-------------|-------------------|-------------------|-------|
| 1 | RepositoryEntrysResults.py | get_sums_entrys_date() | TEST 4 + TEST 5 | 16 |
| 2 | RepositoryEntrysResults.py | get_entrys_results_curdate() | TEST 2 | 44 |
| 3 | RepositoryEntrysResults.py | get_entrys_results_curdate_complete() | TEST 2 | 64 |
| 4 | RepositoryCronjobs.py | get_data_cronjobs_curdate() | TEST 1 | 39 |
| 5 | RepositoryEvents.py | get_events_daily_crons() | TEST 1 | 29 |
| 6 | RepositoryEntrys.py | get_entrys_dataset() | TEST 3 | 244 |

**Cobertura:** ✅ **100%** (6 de 6 métodos cubiertos)

---

## ✅ TEST SUITE - 5 ENDPOINTS CRÍTICOS

---

### **TEST 1: Reportes de Cronjobs** 🔥 CRÍTICO

**Endpoint:** `POST /apis/get-daily-report-crons/`

**Cubre:**
- ✅ RepositoryCronjobs.get_data_cronjobs_curdate() (2 llamadas: success/fail)
- ✅ RepositoryEvents.get_events_daily_crons()

**Precondiciones:**
- Sistema debe estar ejecutando cronjobs (automático)
- Debe haber al menos un cronjob ejecutado hoy

**Comando de ejecución:**
```bash
curl -X POST http://localhost:8000/apis/get-daily-report-crons/ \
  -H "Content-Type: application/json"
```

**Logs esperados:**
```
INFO ⏰ CRONJOBS QUERY | Project: samb-hexagonal | Method: get_data_cronjobs_curdate | Condition: 1 | Count: X | Max Execution Time: Xs | Query Time: XXms
INFO ⏰ CRONJOBS QUERY | Project: samb-hexagonal | Method: get_data_cronjobs_curdate | Condition: 2 | Count: X | Max Execution Time: Xs | Query Time: XXms
INFO ⏱️ EVENTS DAILY QUERY | Project: samb-hexagonal | Method: get_events_daily_cron | Condition: X | Execution Time: Xs | Difference: X | Query Time: XXms
```
o
```
WARNING ⚠️ EVENTS DAILY WARNING | Project: samb-hexagonal | Method: get_events_daily_cron | Message: No events found for today | Time: XXms
```

**Validación:**
- ✅ Status code: 200 (no 500)
- ✅ Aparecen 3 logs en consola
- ✅ Query Time ANTES: 400-500ms → DESPUÉS: < 100ms
- ✅ Count de cronjobs es correcto
- ✅ Mejora ≥ 80%

**Cambios validados:**
- `WHERE DATE(start_date) = CURDATE()` → `WHERE start_date >= CURDATE() AND start_date < DATE_ADD(CURDATE(), INTERVAL 1 DAY)`

---

### **TEST 2: Reportes de Entries Diarios** 🔥 CRÍTICO

**Endpoint:** `POST /apis/get-daily-report-entrys/`

**Cubre:**
- ✅ RepositoryEntrysResults.get_entrys_results_curdate() (múltiples llamadas por metodología)
- ✅ RepositoryEntrysResults.get_entrys_results_curdate_complete()

**Precondiciones:**
- Debe haber entries ejecutadas hoy con resultados
- Metodologías activas en la base de datos

**Comando de ejecución:**
```bash
curl -X POST http://localhost:8000/apis/get-daily-report-entrys/ \
  -H "Content-Type: application/json"
```

**Logs esperados:**
```
INFO 💰 MONETARY FILTER | Project: samb-hexagonal | Method: get_data_entrys_results_curdate | Methodology: 3trendssimple... | Account: PRACTICE | Total: X | Positive: X | Negative: X | Balance: $XXX.XX | Query Time: XXms
INFO 💰 MONETARY FILTER | Project: samb-hexagonal | Method: get_data_entrys_results_curdate | Methodology: 3trendssimple... | Account: REAL | Total: X | Positive: X | Negative: X | Balance: $XXX.XX | Query Time: XXms
INFO 💰 MONETARY FILTER | Project: samb-hexagonal | Method: get_data_entrys_results_curdate_complete | Account: PRACTICE | Total: X | Positive: X | Negative: X | Balance: $XXX.XX | Query Time: XXms
INFO 💰 MONETARY FILTER | Project: samb-hexagonal | Method: get_data_entrys_results_curdate_complete | Account: REAL | Total: X | Positive: X | Negative: X | Balance: $XXX.XX | Query Time: XXms
```

**Validación:**
- ✅ Status code: 200 (no 500)
- ✅ Aparecen logs por cada metodología activa
- ✅ Query Time ANTES: 300-450ms → DESPUÉS: < 80ms
- ✅ Balances coinciden con datos reales
- ✅ Total = Positive + Negative (consistencia)
- ✅ Mejora ≥ 80%

**Cambios validados:**
- `WHERE DATE(registration_date) = CURDATE()` → `WHERE registration_date >= CURDATE() AND registration_date < DATE_ADD(CURDATE(), INTERVAL 1 DAY)`

---

### **TEST 3: Generación de Modelos ML** 🔥 CRÍTICO

**Endpoint:** `POST /apis/add-models/`

**Cubre:**
- ✅ RepositoryEntrys.get_entrys_dataset() (vía get_entrys_dataset_min)

**Precondiciones:**
- Debe haber entries históricas con resultados
- Debe haber indicadores asociados (SMA30, SMA10, RSI)
- Configuración de indicadores en base de datos

**Comando de ejecución:**
```bash
curl -X POST http://localhost:8000/apis/add-models/ \
  -H "Content-Type: application/json"
```

**Logs esperados:**
```
INFO 📊 ML DATASET MIN QUERY | Project: samb-hexagonal | Method: get_entrys_dataset_min | Records: XXX | Indicators: SMA30=abc123, SMA10=def456, RSI=ghi789 | Query Time: XXXms
```

**Validación:**
- ✅ Status code: 200 (no 500)
- ✅ Query Time ANTES: 600-900ms → DESPUÉS: < 180ms
- ✅ Records > 0 (dataset generado)
- ✅ Archivo de dataset creado en directorio
- ✅ Mensaje de éxito en respuesta
- ✅ Mejora ≥ 70%

**Cambios validados:**
- Subquery `MAX(registration_date)` ahora usa índice en columna DATETIME

---

### **TEST 4: Sesión de Trading - Metodología Trends** 🔥 CRÍTICO

**Endpoint:** `POST /apis/get-data-analysis-deriv/`

**Cubre:**
- ✅ RepositoryEntrysResults.get_sums_entrys_date() (filtro monetario)

**Precondiciones:**
- Metodología "trends" activa
- Configuración de balance en samb_manager_days
- Entries históricas con resultados

**Comando de ejecución:**
```bash
curl -X POST http://localhost:8000/apis/get-data-analysis-deriv/ \
  -H "Content-Type: application/json" \
  -d '{}'
```

**Logs esperados:**
```
INFO 💰 MONETARY FILTER | Project: samb-hexagonal | Method: get_sums_entrys_date | Date: 20251226 | Methodology: 3trendssimple0000000000000000000 | Balance: $XXX.XX | Query Time: XXms
```

**Validación:**
- ✅ Status code: 200 (no 500)
- ✅ Query Time ANTES: 250-400ms → DESPUÉS: < 60ms
- ✅ Balance calculado correctamente
- ✅ Decisión de trading basada en filtro monetario
- ✅ Respuesta contiene análisis de sesión
- ✅ Mejora ≥ 85%

**Cambios validados:**
- `WHERE DATE_FORMAT(registration_date, '%Y%m%d') = date` → `WHERE DATE(registration_date) = date`

---

### **TEST 5: Sesión de Trading - Metodología WMA** ⚠️ IMPORTANTE

**Endpoint:** `POST /apis/get-data-analysis-deriv-wma/`

**Cubre:**
- ✅ RepositoryEntrysResults.get_sums_entrys_date() (otra metodología)

**Precondiciones:**
- Metodología "wma" activa
- Configuración de balance en samb_manager_days

**Comando de ejecución:**
```bash
curl -X POST http://localhost:8000/apis/get-data-analysis-deriv-wma/ \
  -H "Content-Type: application/json" \
  -d '{}'
```

**Logs esperados:**
```
INFO 💰 MONETARY FILTER | Project: samb-hexagonal | Method: get_sums_entrys_date | Date: 20251226 | Methodology: 3wmasimple00000000000000000000000 | Balance: $XXX.XX | Query Time: XXms
```

**Validación:**
- ✅ Status code: 200
- ✅ Query Time ANTES: 250-400ms → DESPUÉS: < 60ms
- ✅ Balance correcto
- ✅ Filtro monetario funciona
- ✅ Mejora ≥ 85%

**Cambios validados:**
- Mismo cambio que TEST 4 (diferente metodología)

---

## 📝 PROCESO DE TESTING

### **FASE 1: Preparación (Baseline)**

```bash
# 1. Asegurarse de estar en branch correcto
git checkout optimization-date
git pull origin optimization-date

# 2. Verificar que el sistema está corriendo
docker ps | grep samb-hexagonal

# 3. Verificar que hay datos de hoy
# - Abrir phpMyAdmin: http://localhost:8080
# - Verificar samb_entrys_results con fecha de hoy
# - Verificar samb_cronjobs con fecha de hoy
```

**Ejecutar todos los tests y anotar tiempos:**

```bash
# TEST 1
curl -X POST http://localhost:8000/apis/get-daily-report-crons/
# Anotar: Query Time de cronjobs (condition 1): _____ ms
# Anotar: Query Time de cronjobs (condition 2): _____ ms
# Anotar: Query Time de events: _____ ms

# TEST 2
curl -X POST http://localhost:8000/apis/get-daily-report-entrys/
# Anotar: Query Time de entrys_results_curdate: _____ ms
# Anotar: Query Time de entrys_results_curdate_complete: _____ ms

# TEST 3
curl -X POST http://localhost:8000/apis/add-models/
# Anotar: Query Time de dataset_min: _____ ms

# TEST 4
curl -X POST http://localhost:8000/apis/get-data-analysis-deriv/
# Anotar: Query Time de sums_entrys_date (trends): _____ ms

# TEST 5
curl -X POST http://localhost:8000/apis/get-data-analysis-deriv-wma/
# Anotar: Query Time de sums_entrys_date (wma): _____ ms
```

**📸 Guardar screenshot de todos los logs ANTES de la migración**

---

### **FASE 2: Backup (OBLIGATORIO)**

```bash
# Crear backup de la base de datos
docker exec samb-hexagonal-database-1 mysqldump -uroot -p7CXIxo7b2MGC guarvzpf_dev > backup_pre_migration_$(Get-Date -Format 'yyyyMMdd_HHmmss').sql

# Verificar que el archivo se creó
ls -lh backup_pre_migration_*.sql
```

**⚠️ NO CONTINUAR SIN BACKUP EXITOSO**

---

### **FASE 3: Ejecutar Migración de Base de Datos**

```bash
# Opción 1: Desde phpMyAdmin
# - Abrir http://localhost:8080
# - Seleccionar base de datos: guarvzpf_dev
# - Ir a pestaña "SQL"
# - Copiar/pegar contenido completo de db/MIGRATION_SIMPLE.sql
# - Click "Go" / "Continuar"

# Opción 2: Desde MySQL CLI
docker exec -i samb-hexagonal-database-1 mysql -uroot -p7CXIxo7b2MGC guarvzpf_dev < db/MIGRATION_SIMPLE.sql
```

**Verificar migración exitosa:**

```sql
-- Ejecutar en phpMyAdmin o MySQL CLI:

-- 1. Verificar que columnas son DATETIME
SELECT 
    TABLE_NAME,
    COLUMN_NAME,
    DATA_TYPE,
    IS_NULLABLE
FROM INFORMATION_SCHEMA.COLUMNS 
WHERE TABLE_SCHEMA = 'guarvzpf_dev' 
  AND TABLE_NAME = 'samb_entrys_results'
  AND COLUMN_NAME IN ('registration_date', 'update_date');
-- Resultado esperado: DATA_TYPE = 'datetime'

-- 2. Verificar formato de datos
SELECT registration_date 
FROM samb_entrys_results 
LIMIT 5;
-- Resultado esperado: '2025-12-26 14:30:25' (no '20251226143025')

-- 3. Verificar índices creados
SHOW INDEX FROM samb_entrys_results 
WHERE Key_name LIKE 'idx_%';
-- Resultado esperado: idx_entrys_results_regdate, idx_entrys_results_updatedate
```

---

### **FASE 4: Modificar Repositorios**

**Archivo 1:** `apis/repositories/entrysresults/RepositoryEntrysResults.py`

```python
# Línea 16 - get_sums_entrys_date()
# ANTES:
query = "... WHERE DATE_FORMAT(samb_entrys_results.registration_date, %s) = %s ..."
self.cursor_db.execute(query, ('%Y%m%d', date, id_methodology))

# DESPUÉS:
query = "... WHERE DATE(samb_entrys_results.registration_date) = %s ..."
self.cursor_db.execute(query, (date, id_methodology))
```

```python
# Línea 44 - get_entrys_results_curdate()
# ANTES:
query = "... WHERE DATE(samb_entrys_results.registration_date) = CURDATE() ..."

# DESPUÉS:
query = "... WHERE samb_entrys_results.registration_date >= CURDATE() 
         AND samb_entrys_results.registration_date < DATE_ADD(CURDATE(), INTERVAL 1 DAY) ..."
```

```python
# Línea 64 - get_entrys_results_curdate_complete()
# ANTES:
query = "... WHERE DATE(samb_entrys_results.registration_date) = CURDATE() ..."

# DESPUÉS:
query = "... WHERE samb_entrys_results.registration_date >= CURDATE() 
         AND samb_entrys_results.registration_date < DATE_ADD(CURDATE(), INTERVAL 1 DAY) ..."
```

**Archivo 2:** `apis/repositories/cronjobs/RepositoryCronjobs.py`

```python
# Línea 39 - get_data_cronjobs_curdate()
# ANTES:
"... WHERE DATE(samb_cronjobs.start_date) = CURDATE() ..."

# DESPUÉS:
"... WHERE samb_cronjobs.start_date >= CURDATE() 
    AND samb_cronjobs.start_date < DATE_ADD(CURDATE(), INTERVAL 1 DAY) ..."
```

**Archivo 3:** `apis/repositories/events/RepositoryEvents.py`

```python
# Línea 29 - get_events_daily_crons()
# ANTES:
"... WHERE DATE(samb_cronjobs.start_date) = CURDATE() ..."

# DESPUÉS:
"... WHERE samb_cronjobs.start_date >= CURDATE() 
    AND samb_cronjobs.start_date < DATE_ADD(CURDATE(), INTERVAL 1 DAY) ..."
```

**Archivo 4:** `apis/repositories/entrys/RepositoryEntrys.py`

```python
# Línea 244 - get_entrys_dataset()
# ANTES (subquery):
"... WHERE samb_entrys_results.registration_date = (
     SELECT MAX(registration_date) 
     FROM samb_entrys_results AS ser 
     WHERE ser.id_entrys_id = samb_entrys.id
 ) ..."

# DESPUÉS (JOIN optimizado):
"... INNER JOIN (
     SELECT id_entrys_id, MAX(registration_date) AS max_date
     FROM samb_entrys_results
     GROUP BY id_entrys_id
 ) AS latest ON samb_entrys_results.id_entrys_id = latest.id_entrys_id 
 AND samb_entrys_results.registration_date = latest.max_date
 WHERE Last30Movements.rn <= 1 ..."
```

**Rebuild container:**

```bash
docker compose up -d --build
```

**Verificar que el sistema arrancó:**

```bash
docker logs samb-hexagonal --tail 50
# Verificar: "Starting development server at http://0.0.0.0:8000/"
```

---

### **FASE 5: Testing Post-Migración (Validación)**

**Ejecutar los mismos 5 tests:**

```bash
# TEST 1
curl -X POST http://localhost:8000/apis/get-daily-report-crons/
# Validar: ✅ Status 200 + ✅ Tiempos mejorados

# TEST 2
curl -X POST http://localhost:8000/apis/get-daily-report-entrys/
# Validar: ✅ Status 200 + ✅ Tiempos mejorados

# TEST 3
curl -X POST http://localhost:8000/apis/add-models/
# Validar: ✅ Status 200 + ✅ Tiempos mejorados

# TEST 4
curl -X POST http://localhost:8000/apis/get-data-analysis-deriv/
# Validar: ✅ Status 200 + ✅ Tiempos mejorados

# TEST 5
curl -X POST http://localhost:8000/apis/get-data-analysis-deriv-wma/
# Validar: ✅ Status 200 + ✅ Tiempos mejorados
```

**📸 Guardar screenshot de todos los logs DESPUÉS de la migración**

---

### **FASE 6: Validación Funcional Completa**

```bash
# 1. Verificar balances coinciden
# - Ejecutar TEST 2 y anotar balances
# - Comparar con balances de phpMyAdmin
# - Deben ser idénticos

# 2. Verificar conteos de entries
# - Ejecutar TEST 2 y anotar Total/Positive/Negative
# - Verificar: Total = Positive + Negative

# 3. Verificar decisiones de trading
# - Ejecutar TEST 4 y TEST 5
# - Verificar que el filtro monetario funciona
# - Si balance < threshold → No operar

# 4. Ejecutar sesión completa (30 minutos)
# - Monitorear logs en tiempo real
# - Verificar que no hay errores 500
# - Verificar que las operaciones se ejecutan correctamente
# - Verificar reportes en Telegram
```

---

## 📊 TABLA DE RESULTADOS

| Test | Endpoint | Método | Tiempo ANTES | Tiempo DESPUÉS | Mejora % | Status |
|------|----------|--------|--------------|----------------|----------|--------|
| TEST 1 | get-daily-report-crons | get_data_cronjobs_curdate (success) | _____ms | _____ms | _____% | ☐ |
| TEST 1 | get-daily-report-crons | get_data_cronjobs_curdate (fail) | _____ms | _____ms | _____% | ☐ |
| TEST 1 | get-daily-report-crons | get_events_daily_crons | _____ms | _____ms | _____% | ☐ |
| TEST 2 | get-daily-report-entrys | get_entrys_results_curdate | _____ms | _____ms | _____% | ☐ |
| TEST 2 | get-daily-report-entrys | get_entrys_results_curdate_complete | _____ms | _____ms | _____% | ☐ |
| TEST 3 | add-models | get_entrys_dataset_min | _____ms | _____ms | _____% | ☐ |
| TEST 4 | get-data-analysis-deriv | get_sums_entrys_date (trends) | _____ms | _____ms | _____% | ☐ |
| TEST 5 | get-data-analysis-deriv-wma | get_sums_entrys_date (wma) | _____ms | _____ms | _____% | ☐ |

**Mejora promedio esperada:** ≥ 75%

---

## 🚨 CRITERIOS DE ÉXITO

### **Todos los tests deben cumplir:**

1. ✅ **Sin errores 500** - Todas las respuestas exitosas
2. ✅ **Mejora ≥ 70%** - Tiempos reducidos al menos 70%
3. ✅ **Datos consistentes** - Balances y conteos idénticos antes/después
4. ✅ **Logs visibles** - Todos los logs configurados aparecen
5. ✅ **Funcionalidad intacta** - Sistema opera normalmente

### **Si algún test falla:**

```bash
# 🔴 ROLLBACK INMEDIATO

# 1. Detener container
docker compose down

# 2. Restaurar backup
docker exec -i samb-hexagonal-database-1 mysql -uroot -p7CXIxo7b2MGC guarvzpf_dev < backup_pre_migration_YYYYMMDD_HHMMSS.sql

# 3. Revertir cambios en código
git checkout apis/repositories/entrysresults/RepositoryEntrysResults.py
git checkout apis/repositories/cronjobs/RepositoryCronjobs.py
git checkout apis/repositories/events/RepositoryEvents.py
git checkout apis/repositories/entrys/RepositoryEntrys.py

# 4. Rebuild
docker compose up -d --build

# 5. Verificar que el sistema vuelve a funcionar
curl -X POST http://localhost:8000/apis/get-daily-report-crons/
```

### **Debugging:**

```bash
# Ver logs en tiempo real
docker logs -f samb-hexagonal

# Verificar queries en MySQL
# - Habilitar query log en MySQL
# - Ver queries que se están ejecutando
# - Verificar EXPLAIN de queries problemáticos

# Revisar sintaxis SQL
# - Comparar query modificado con ANALYSIS_QUERIES_CHANGES.md
# - Verificar paréntesis y AND/OR
```

---

## ✅ CHECKLIST FINAL

### **Pre-Migración:**
- [ ] Sistema corriendo sin errores
- [ ] Datos de hoy disponibles en BD
- [ ] 5 tests ejecutados exitosamente (baseline)
- [ ] Tiempos ANTES anotados en tabla
- [ ] Screenshot de logs guardado

### **Migración:**
- [ ] Backup de BD creado y verificado
- [ ] MIGRATION_SIMPLE.sql ejecutado
- [ ] Columnas verificadas como DATETIME
- [ ] Índices verificados como creados
- [ ] Formato de datos verificado

### **Modificación Código:**
- [ ] RepositoryEntrysResults.py modificado (3 métodos)
- [ ] RepositoryCronjobs.py modificado (1 método)
- [ ] RepositoryEvents.py modificado (1 método)
- [ ] RepositoryEntrys.py modificado (1 método)
- [ ] Container rebuildeado
- [ ] Sistema arrancó sin errores

### **Post-Migración:**
- [ ] TEST 1 ejecutado ✅ (200 + mejora ≥70%)
- [ ] TEST 2 ejecutado ✅ (200 + mejora ≥70%)
- [ ] TEST 3 ejecutado ✅ (200 + mejora ≥70%)
- [ ] TEST 4 ejecutado ✅ (200 + mejora ≥70%)
- [ ] TEST 5 ejecutado ✅ (200 + mejora ≥70%)
- [ ] Tiempos DESPUÉS anotados en tabla
- [ ] Screenshot de logs guardado
- [ ] Mejora promedio calculada: _____% 

### **Validación Funcional:**
- [ ] Balances coinciden antes/después
- [ ] Conteos son consistentes
- [ ] Decisiones de trading correctas
- [ ] Sesión completa ejecutada (30min)
- [ ] No errores 500 en producción
- [ ] Reportes Telegram funcionan

### **Documentación:**
- [ ] Tabla de resultados completada
- [ ] Screenshots archivados
- [ ] Mejoras documentadas
- [ ] Issues identificados (si los hay)

---

## 🎯 CONCLUSIÓN

Al completar este plan de testing tendrás:

- ✅ **100% de cobertura** de los 6 métodos modificados
- ✅ **Datos duros** de mejora de performance
- ✅ **Validación funcional** completa del sistema
- ✅ **Rollback plan** documentado y probado
- ✅ **Confianza** para migrar a producción

**Mejora esperada total:**
- Sesión completa: ~3.5-5.2s → ~0.7-1.1s (80% más rápido)
- CPU MySQL: 75% → 25% (67% menos uso)
- Queries lentos: 50-100 → 0-5 por sesión (95% reducción)

---

**Fecha de creación:** 26/12/2025  
**Branch:** optimization-date  
**Versión:** 1.0
