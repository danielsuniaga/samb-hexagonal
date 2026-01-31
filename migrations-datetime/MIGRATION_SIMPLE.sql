-- ========================================
-- MIGRACIÓN SIMPLE: VARCHAR(14) → DATETIME
-- ========================================
-- ESTRATEGIA: Modificar columnas existentes directamente
-- SIN necesidad de cambiar código Python
-- 
-- IMPORTANTE: 
-- 1. MySQL convertirá automáticamente "20251128143025" → "2025-11-28 14:30:25"
-- 2. Las inserciones VARCHAR seguirán funcionando (MySQL hace cast automático)
-- 3. NO requiere modificar EntityDates.py ni repositorios
-- ========================================

USE guarvzpf_dev;

-- ========================================
-- FASE 1: BACKUP (Ejecutar manualmente)
-- ========================================
-- docker exec samb-hexagonal-database-1 mysqldump -uroot -p7CXIxo7b2MGC guarvzpf_dev > backup_$(Get-Date -Format 'yyyyMMdd_HHmmss').sql


-- ========================================
-- FASE 2: CAMBIAR TIPO DE COLUMNAS
-- ========================================
-- MySQL convierte automáticamente VARCHAR → DATETIME
-- Formato: "20251227143025" → "2025-12-27 14:30:25"

-- TABLA 1: samb_entrys (CRITICA)
ALTER TABLE samb_entrys 
    MODIFY COLUMN registration_date DATETIME NULL COMMENT 'Fecha de registro',
    MODIFY COLUMN update_date DATETIME NULL COMMENT 'Fecha de actualizacion';

-- TABLA 2: samb_entrys_results (CRITICA)
ALTER TABLE samb_entrys_results 
    MODIFY COLUMN registration_date DATETIME NULL COMMENT 'Fecha de registro',
    MODIFY COLUMN update_date DATETIME NULL COMMENT 'Fecha de actualizacion';

-- TABLA 3: samb_cronjobs (CRITICA)
ALTER TABLE samb_cronjobs 
    MODIFY COLUMN start_date DATETIME NULL COMMENT 'Fecha de inicio',
    MODIFY COLUMN end_date DATETIME NULL COMMENT 'Fecha de fin';

-- TABLA 4: samb_movements (CRITICA)
ALTER TABLE samb_movements 
    MODIFY COLUMN registration_date DATETIME NULL COMMENT 'Fecha de registro',
    MODIFY COLUMN update_date DATETIME NULL COMMENT 'Fecha de actualizacion';

-- TABLA 5: samb_indicators_entrys
ALTER TABLE samb_indicators_entrys 
    MODIFY COLUMN registration_date DATETIME NULL;

-- TABLA 6: samb_events
ALTER TABLE samb_events 
    MODIFY COLUMN registration_date DATETIME NULL,
    MODIFY COLUMN update_cate DATETIME NULL;

-- TABLA 7: samb_apis
ALTER TABLE samb_apis 
    MODIFY COLUMN registration_date DATETIME NULL,
    MODIFY COLUMN update_date DATETIME NULL;

-- TABLA 8: samb_financial_asset
ALTER TABLE samb_financial_asset 
    MODIFY COLUMN registration_date DATETIME NULL,
    MODIFY COLUMN update_date DATETIME NULL;

-- TABLA 9: samb_platform
ALTER TABLE samb_platform 
    MODIFY COLUMN registration_date DATETIME NULL,
    MODIFY COLUMN update_date DATETIME NULL;

-- TABLA 10: samb_methodologys
ALTER TABLE samb_methodologys 
    MODIFY COLUMN registration_date DATETIME NULL,
    MODIFY COLUMN update_date DATETIME NULL;

-- TABLA 11: samb_send_entrys
ALTER TABLE samb_send_entrys 
    MODIFY COLUMN registration_date DATETIME NULL;

-- TABLA 12: samb_reports
ALTER TABLE samb_reports 
    MODIFY COLUMN registration_date DATETIME NULL,
    MODIFY COLUMN update_date DATETIME NULL;

-- TABLA 13: samb_send_message_api_telegram
ALTER TABLE samb_send_message_api_telegram 
    MODIFY COLUMN registration_date DATETIME NULL,
    MODIFY COLUMN update_date DATETIME NULL;

-- TABLA 14: samb_notifications_exceptions_apis_independient
ALTER TABLE samb_notifications_exceptions_apis_independient 
    MODIFY COLUMN registration_date DATETIME NULL,
    MODIFY COLUMN update_date DATETIME NULL;

-- TABLA 15: samb_framework
ALTER TABLE samb_framework 
    MODIFY COLUMN registration_date DATETIME NULL;

-- TABLA 16: samb_predict_models
ALTER TABLE samb_predict_models 
    MODIFY COLUMN registration_date DATETIME NULL,
    MODIFY COLUMN update_date DATETIME NULL;

-- TABLA 17: samb_manager_days
ALTER TABLE samb_manager_days 
    MODIFY COLUMN registration_date DATETIME NULL,
    MODIFY COLUMN update_date DATETIME NULL;

-- TABLA 18: samb_api_financial_asset
ALTER TABLE samb_api_financial_asset 
    MODIFY COLUMN registration_date DATETIME NULL,
    MODIFY COLUMN update_date DATETIME NULL;

-- TABLA 19: samb_config
ALTER TABLE samb_config 
    MODIFY COLUMN registration_date DATETIME NULL;

-- TABLA 20: samb_exceptions_apis
ALTER TABLE samb_exceptions_apis 
    MODIFY COLUMN registration_date DATETIME NULL,
    MODIFY COLUMN update_date DATETIME NULL;

-- TABLA 21: samb_indicators
ALTER TABLE samb_indicators 
    MODIFY COLUMN registration_date DATETIME NULL;

-- TABLA 22: samb_models
ALTER TABLE samb_models 
    MODIFY COLUMN registration_date DATETIME NULL,
    MODIFY COLUMN update_date DATETIME NULL;

-- TABLA 24: samb_entrys_predict_models (ÚLTIMA TABLA)
ALTER TABLE samb_entrys_predict_models 
    MODIFY COLUMN registration_date DATETIME NULL,
    MODIFY COLUMN update_date DATETIME NULL;


-- ========================================
-- FASE 3: CREAR ÍNDICES OPTIMIZADOS
-- ========================================

-- Índices para tablas críticas
CREATE INDEX idx_entrys_regdate ON samb_entrys(registration_date);
CREATE INDEX idx_entrys_updatedate ON samb_entrys(update_date);

CREATE INDEX idx_entrys_results_regdate ON samb_entrys_results(registration_date);
CREATE INDEX idx_entrys_results_updatedate ON samb_entrys_results(update_date);

CREATE INDEX idx_cronjobs_startdate ON samb_cronjobs(start_date);
CREATE INDEX idx_cronjobs_enddate ON samb_cronjobs(end_date);

CREATE INDEX idx_movements_regdate ON samb_movements(registration_date);
CREATE INDEX idx_movements_updatedate ON samb_movements(update_date);


-- ========================================
-- FASE 4: VERIFICACIÓN
-- ========================================

-- Verificar que todas las columnas son DATETIME
SELECT 
    TABLE_NAME,
    COLUMN_NAME,
    DATA_TYPE,
    IS_NULLABLE
FROM INFORMATION_SCHEMA.COLUMNS 
WHERE TABLE_SCHEMA = 'guarvzpf_dev' 
  AND TABLE_NAME LIKE 'samb_%'
  AND COLUMN_NAME IN ('registration_date', 'update_date', 'start_date', 'end_date', 'update_cate')
ORDER BY TABLE_NAME, COLUMN_NAME;

-- Verificar datos en tablas críticas
SELECT 
    'samb_entrys' as tabla,
    COUNT(*) as total,
    MIN(registration_date) as fecha_min,
    MAX(registration_date) as fecha_max
FROM samb_entrys
UNION ALL
SELECT 
    'samb_entrys_results',
    COUNT(*),
    MIN(registration_date),
    MAX(registration_date)
FROM samb_entrys_results
UNION ALL
SELECT 
    'samb_cronjobs',
    COUNT(*),
    MIN(start_date),
    MAX(start_date)
FROM samb_cronjobs
UNION ALL
SELECT 
    'samb_movements',
    COUNT(*),
    MIN(registration_date),
    MAX(registration_date)
FROM samb_movements;

-- Verificar índices
SHOW INDEX FROM samb_entrys WHERE Key_name LIKE 'idx_%';
SHOW INDEX FROM samb_entrys_results WHERE Key_name LIKE 'idx_%';
SHOW INDEX FROM samb_cronjobs WHERE Key_name LIKE 'idx_%';
SHOW INDEX FROM samb_movements WHERE Key_name LIKE 'idx_%';

-- ========================================
-- NOTAS IMPORTANTES
-- ========================================

-- ✅ VENTAJAS DE ESTE ENFOQUE:
-- 1. NO necesitas modificar EntityDates.py
-- 2. NO necesitas modificar ningún repositorio
-- 3. MySQL acepta "20251128143025" y lo convierte automáticamente a DATETIME
-- 4. Las inserciones VARCHAR seguirán funcionando (cast implícito)
-- 5. Migración mucho más simple y rápida

-- ⚠️ CÓMO FUNCIONA EL CAST AUTOMÁTICO:
-- INSERT INTO samb_entrys (registration_date) VALUES ('20251128143025');
-- MySQL automáticamente convierte → 2025-11-28 14:30:25
-- 
-- También acepta formato ISO:
-- INSERT INTO samb_entrys (registration_date) VALUES ('2025-11-28 14:30:25');

-- 🔄 ROLLBACK (Si algo sale mal):
-- ALTER TABLE samb_entrys 
--     MODIFY COLUMN registration_date VARCHAR(14) NULL,
--     MODIFY COLUMN update_date VARCHAR(14) NULL;

-- ========================================
-- FIN DEL SCRIPT
-- ========================================
