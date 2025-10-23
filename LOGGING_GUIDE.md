# 📊 Guía de Logging - EntityModels ML Cache

## 🎯 Objetivo
Sistema de logging robusto para monitorear el performance y funcionamiento de los modelos ML con cache en producción.

---

## 📝 Logs Implementados

### 1️⃣ **Cache Operations**

#### ✅ Cache HIT (Modelo cargado desde cache)
```
INFO 🟢 CACHE HIT | Model: ml_random_forest.pkl | Time: 0.45ms | Cache: 2/10
```
**Datos:**
- Nombre del archivo
- Tiempo de acceso (ms)
- Estado del cache (items actuales/máximo)

---

#### ❌ Cache MISS (Modelo cargado desde disco)
```
WARNING 🔴 CACHE MISS | Model: ml_random_forest.pkl | Loading from disk...
INFO 💾 MODEL LOADED & CACHED | Model: ml_random_forest.pkl | Size: 185.42MB | Load time: 145.23ms | Total: 145.68ms | Cache: 1/10
```
**Datos:**
- Nombre del archivo
- Tamaño del archivo (MB)
- Tiempo de carga desde disco (ms)
- Tiempo total (ms)
- Estado del cache

---

#### ⚠️ Cache Invalidation (Cache expirado o archivo modificado)
```
WARNING ⚠️ CACHE INVALIDATED | Path: ml_random_forest.pkl | Reason: Expired or file modified
```
**Causas:**
- TTL expirado (24 horas por defecto)
- Archivo .pkl modificado (reentrenamiento detectado)

---

#### 🗑️ Cache Eviction (LRU - Least Recently Used)
```
WARNING ⚠️ CACHE FULL | Evicting LRU entry | Cache: 10/10
INFO 🗑️ CACHE EVICTION | Removed: old_model.pkl | Age: 3:45:12 | Cache: 9/10
```
**Cuando ocurre:**
- Cache lleno (10 modelos máximo)
- Se remueve el modelo menos usado recientemente

---

### 2️⃣ **Prediction Operations**

#### 🚀 Inicio de predicción
```
INFO 🚀 PREDICTION START | Model ID: 07e8baccf8724f21a5e51877fe61af48
```

---

#### ✅ Predicción exitosa
```
INFO ✅ MODEL & SCALER LOADED | Model: ml_random_forest.pkl | Time: 145.68ms
INFO ✅ PREDICTION COMPLETE | Model: ml_random_forest.pkl | Result: WIN | Confidence: 87.45% | Win prob: 87.45% | Times [Load: 145ms, Prep: 2ms, Pred: 3ms, Prob: 1ms] | TOTAL: 151ms
```

**Métricas incluidas:**
- **Load time:** Tiempo de carga del modelo y scaler
- **Prep time:** Tiempo de preparación de datos (scaling)
- **Pred time:** Tiempo de predicción del modelo
- **Prob time:** Tiempo de cálculo de probabilidades
- **TOTAL:** Tiempo total de la operación

---

#### ❌ Error en predicción
```
ERROR ❌ PREDICTION ERROR | Model ID: xxx | Error: [error message] | Time: 150ms
[Stack trace completo]
```

---

### 3️⃣ **File Operations**

#### ❌ Archivo no encontrado
```
ERROR ❌ FILE NOT FOUND | Scaler: scaler.pkl | Path: /path/to/scaler.pkl
```

#### ❌ Error al cargar archivo
```
ERROR ❌ LOAD FAILED | Model: ml_random_forest.pkl | Reason: pickle.load returned None
ERROR ❌ ERROR LOADING SCALER | Scaler: scaler.pkl | Error: [error message]
```

---

### 4️⃣ **Cache Statistics**

#### 📊 Estadísticas del cache (método manual)
```python
from apis.entities.models.EntityModels import EntityModels
stats = EntityModels.get_cache_stats()
```

**Output:**
```
INFO 📊 CACHE STATS | Size: 5/10 | Items: ['ml_random_forest.pkl', 'scaler.pkl', 'ml_mlp.pkl', ...]
```

**Response:**
```json
{
  "size": 5,
  "max_size": 10,
  "ttl_hours": 24,
  "cached_items": [
    {
      "name": "ml_random_forest.pkl",
      "age_seconds": 1234.56,
      "last_access": "2025-10-23T16:18:36.925000"
    }
  ]
}
```

---

## 🔧 Configuración

### Archivo: `dev/settings.py`

```python
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '{levelname} {asctime} {module} {message}',
            'style': '{',
        },
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'formatter': 'verbose',
        },
    },
    'loggers': {
        'apis.entities.models.EntityModels': {
            'handlers': ['console'],
            'level': 'INFO',  # Cambiar a 'DEBUG' para más detalles
            'propagate': False,
        },
    },
}
```

### Niveles de Logging

| Nivel | Descripción | Uso |
|-------|-------------|-----|
| `DEBUG` | Logs muy detallados (TTL expired, file modified, data shapes) | Development/Debugging |
| `INFO` | Operaciones normales (cache hits, predictions, loads) | **Production (Recomendado)** |
| `WARNING` | Cache miss, evictions, invalidations | Siempre activo |
| `ERROR` | Errores y excepciones | Siempre activo |

---

## 📈 Monitoreo en Producción

### Ver logs en tiempo real
```bash
docker logs -f samb-hexagonal
```

### Ver solo logs de EntityModels
```bash
docker logs -f samb-hexagonal | grep "EntityModels"
```

### Ver solo errores
```bash
docker logs -f samb-hexagonal | grep "ERROR"
```

### Ver estadísticas de cache
```bash
docker logs -f samb-hexagonal | grep "CACHE"
```

### Ver performance de predicciones
```bash
docker logs -f samb-hexagonal | grep "PREDICTION COMPLETE"
```

---

## 📊 Análisis de Performance

### Ejemplo de salida completa de un request:

```
INFO 2025-10-23 16:18:36,920 EntityModels 🚀 PREDICTION START | Model ID: 07e8baccf8724f21a5e51877fe61af48
WARNING 2025-10-23 16:18:36,921 EntityModels 🔴 CACHE MISS | Model: ml_random_forest.pkl | Loading from disk...
INFO 2025-10-23 16:18:37,066 EntityModels 💾 MODEL LOADED & CACHED | Model: ml_random_forest.pkl | Size: 185.42MB | Load time: 145.23ms | Total: 145.68ms | Cache: 1/10
WARNING 2025-10-23 16:18:37,067 EntityModels 🔴 CACHE MISS | Scaler: scaler.pkl | Loading from disk...
INFO 2025-10-23 16:18:37,068 EntityModels 💾 SCALER LOADED & CACHED | Scaler: scaler.pkl | Size: 0.05MB | Load time: 0.89ms | Total: 1.12ms | Cache: 2/10
INFO 2025-10-23 16:18:37,069 EntityModels ✅ MODEL & SCALER LOADED | Model: ml_random_forest.pkl | Time: 146.80ms
INFO 2025-10-23 16:18:37,074 EntityModels ✅ PREDICTION COMPLETE | Model: ml_random_forest.pkl | Result: WIN | Confidence: 87.45% | Win prob: 87.45% | Times [Load: 147ms, Prep: 2ms, Pred: 3ms, Prob: 1ms] | TOTAL: 153ms
```

### Métricas clave para monitorear:

1. **Cache Hit Rate:** `(CACHE HIT / Total requests) × 100%`
   - **Objetivo:** >95% después del warm-up inicial

2. **Load Time (Cache MISS):** Tiempo de carga desde disco
   - **Esperado:** 100-200ms para modelos de 50-200MB

3. **Prediction Time:** Tiempo total de predicción
   - **Con cache HIT:** <10ms
   - **Con cache MISS:** 150-250ms (primera carga)

4. **Cache Evictions:** Frecuencia de LRU evictions
   - **Si es alto:** Considerar aumentar `_cache_max_size`

---

## 🛠️ Troubleshooting

### Problema: Muchos CACHE MISS
**Causa:** Auto-reload de Django en desarrollo
**Solución:** Normal en desarrollo. En producción persiste correctamente.

### Problema: Evictions frecuentes
**Causa:** Cache lleno (10 modelos máximo)
**Solución:** Aumentar `_cache_max_size` en EntityModels.py:
```python
_cache_max_size = 20  # Aumentar a 20 modelos
```

### Problema: Cache invalidations frecuentes
**Causa:** Archivos .pkl modificándose constantemente
**Solución:** Verificar procesos de reentrenamiento. El cache detecta automáticamente cambios.

### Problema: No veo logs
**Causa:** Nivel de logging muy alto
**Solución:** Cambiar `level` a `INFO` o `DEBUG` en `settings.py`

---

## 📌 Mejores Prácticas

1. ✅ **Monitorear logs diariamente** para identificar patrones
2. ✅ **Analizar prediction times** para detectar degradación de performance
3. ✅ **Revisar cache hit rate** para optimizar `_cache_max_size`
4. ✅ **Alertas en errores** para respuesta rápida
5. ✅ **Logs en nivel INFO en producción** (DEBUG solo para debugging)

---

## 🎯 KPIs Sugeridos

| Métrica | Objetivo | Alerta |
|---------|----------|--------|
| Cache Hit Rate | >95% | <80% |
| Prediction Time (Cache HIT) | <10ms | >50ms |
| Prediction Time (Cache MISS) | <250ms | >500ms |
| Cache Evictions | <5/día | >20/día |
| Errors | 0 | >0 |

---

## 📞 Soporte

Para más información sobre el sistema de cache, revisar:
- `apis/entities/models/EntityModels.py` (líneas 462-900)
- `dev/settings.py` (configuración LOGGING)

**Desarrollado por:** GitHub Copilot + Daniel Suniaga  
**Fecha:** Octubre 23, 2025  
**Versión:** 1.0
