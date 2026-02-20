import logging
import re
import os
import uuid
import apis.entities.managerdays.EntityManagerDays as EntityManagerDays

import apis.repositories.ManagerDays.RepositoryManagerDays as RepositoryManagerDays

logger = logging.getLogger('apis.services.managerdays')

class ServicesManagerDays():

    entity = None

    repository = None

    def __init__(self):

        self.entity = EntityManagerDays.EntityManagerDays()

        self.repository = RepositoryManagerDays.RepositoryManagerDays()

    def get_project_name(self):

        return self.entity.get_project_name()

    def get_type_manager_days_repository(self,day):

        return self.repository.get_type_manager_day(day)
    
    def set_money(self,value):

        return self.entity.set_money(value)
    
    def set_profit(self,value):

        return self.entity.set_profit(value)
    
    def set_loss(self,value):

        return self.entity.set_loss(value)
    
    def set_mode(self,value,permision_real):

        if not self.check_permission_real(permision_real):

            return self.entity.set_mode(self.get_mode_env())
            
        return self.entity.set_mode(value)
    
    def set_data_manager(self,data):

        self.set_money(data['money'])

        self.set_profit(data['profit'])

        self.set_loss(data['loss'])

        self.set_mode(data['type'],data['permision_real'])

        return True
    
    def get_mode(self):

        return self.entity.get_mode()
    
    def get_profit(self):

        return self.entity.get_profit()
    
    def get_loss(self):

        return self.entity.get_loss()
    
    def get_mode_env(self):

        return self.entity.get_mode_env()
    
    def check_permission_real(self,permision_real):
            
        if(permision_real):
            
            return True
        
        return False
    
    def sanitize_type(self, type_value, context=None):
        """
        Limpia el valor type eliminando espacios, tabs, caracteres invisibles
        y convierte a mayúsculas. Registra cuando se necesita limpieza.
        
        Args:
            type_value: Valor a sanitizar
            context: Dict con day, id_methodology para contexto
        """
        if not type_value:
            logger.warning(
                f"⚠️ TYPE SANITIZATION | "
                f"Container: {self.get_project_name()} | "
                f"Day: {context.get('day', 'N/A') if context else 'N/A'} | "
                f"Methodology: {context.get('id_methodology', 'N/A') if context else 'N/A'} | "
                f"Issue: NULL or EMPTY value | "
                f"Original: {repr(type_value)} | "
                f"Cleaned: ''"
            )
            return ''
        
        original = str(type_value)
        # Elimina espacios, tabs, saltos de línea, zero-width chars
        cleaned = re.sub(r'[\s\u200b\u200c\u200d\ufeff]+', '', original)
        cleaned = cleaned.upper()
        
        # Log solo si hubo cambios (indica datos sucios)
        if original != cleaned:
            logger.warning(
                f"🧹 TYPE SANITIZATION | "
                f"Container: {self.get_project_name()} | "
                f"Day: {context.get('day', 'N/A') if context else 'N/A'} | "
                f"Methodology: {context.get('id_methodology', 'N/A') if context else 'N/A'} | "
                f"Issue: DIRTY DATA DETECTED | "
                f"Original: {repr(original)} | "
                f"Cleaned: {repr(cleaned)} | "
                f"Bytes: {original.encode('unicode_escape').decode('ascii')}"
            )
        
        return cleaned
    
    def generate_uuid(self):

        return self.entity.generate_uuid()
    
    def generate_context_for_logging(self, data):
        """
        Extrae el contexto necesario para logging.
        """
        return {
            'container': self.get_project_name(),
            'day': data.get('day_description', 'N/A'),
            'methodology': data.get('name_methodology', 'N/A')
        }
    
    def generate_log_permission_blocked(self, execution_id, context, permission):
        """
        Log cuando se bloquea por falta de permiso.
        """
        logger.info(
            f"❌ MODE OPERATIVITY CHECK | "
            f"🆔 {execution_id} | "
            f"Container: {context['container']} | "
            f"Day: {context['day']} | "
            f"Methodology: {context['methodology']} | "
            f"Result: BLOCKED | "
            f"Reason: No permission_real | "
            f"Permission: {permission}"
        )
    
    def generate_log_mode_check_start(self, execution_id, context, type_sanitized, mode_env, mode_real):
        """
        Log del inicio de la verificación de modo.
        """
        logger.info(
            f"🔍 MODE OPERATIVITY CHECK | "
            f"🆔 {execution_id} | "
            f"Container: {context['container']} | "
            f"Day: {context['day']} | "
            f"Methodology: {context['methodology']} | "
            f"Type (DB): '{type_sanitized}' | "
            f"MODE (env): '{mode_env}' | "
            f"MODE_REAL (env): '{mode_real}'"
        )
    
    def generate_log_practice_mode_blocked(self, execution_id, context, type_sanitized, mode_env):
        """
        Log cuando se bloquea en modo PRACTICE.
        """
        logger.info(
            f"🚫 MODE OPERATIVITY CHECK | "
            f"🆔 {execution_id} | "
            f"Container: {context['container']} | "
            f"Day: {context['day']} | "
            f"Methodology: {context['methodology']} | "
            f"Result: BLOCKED | "
            f"Reason: Type matches MODE (PRACTICE mode) | "
            f"Type: '{type_sanitized}' == MODE: '{mode_env}'"
        )
    
    def generate_log_real_mode_allowed(self, execution_id, context, type_sanitized, mode_real):
        """
        Log cuando se permite en modo REAL.
        """
        logger.info(
            f"✅ MODE OPERATIVITY CHECK | "
            f"🆔 {execution_id} | "
            f"Container: {context['container']} | "
            f"Day: {context['day']} | "
            f"Methodology: {context['methodology']} | "
            f"Result: ALLOWED | "
            f"Reason: Type matches MODE_REAL | "
            f"Type: '{type_sanitized}' == MODE_REAL: '{mode_real}' | "
            f"🚨 OPERATING IN REAL MODE 🚨"
        )
    
    def generate_log_unexpected_type_error(self, execution_id, context, type_sanitized, mode_env, mode_real):
        """
        Log cuando se detecta un tipo inesperado.
        """
        logger.error(
            f"❌ MODE OPERATIVITY CHECK | "
            f"🆔 {execution_id} | "
            f"Container: {context['container']} | "
            f"Day: {context['day']} | "
            f"Methodology: {context['methodology']} | "
            f"Result: BLOCKED | "
            f"Reason: UNEXPECTED TYPE VALUE | "
            f"Type: '{type_sanitized}' | "
            f"MODE: '{mode_env}' | "
            f"MODE_REAL: '{mode_real}' | "
            f"⚠️ DATA INCONSISTENCY DETECTED"
        )
    
    def check_mode_logic(self, type_sanitized, mode_env, mode_real):
        """
        Lógica pura de validación de modo sin logging.
        
        Returns:
            tuple: (is_valid, reason) donde reason es 'practice', 'real', o 'unexpected'
        """
        if type_sanitized == mode_env:
            return False, 'practice'
        
        if type_sanitized == mode_real:
            return True, 'real'
        
        return False, 'unexpected'
    
    def check_mode_operativity(self, data):
        """
        Verifica si se puede operar según el tipo de cuenta.
        Coordina la validación y logging delegando a métodos especializados.
        """
        execution_id = self.generate_uuid()
        context = self.generate_context_for_logging(data)
        
        # 1. Validar permiso
        if not self.check_permission_real(data['permision_real']):
            self.generate_log_permission_blocked(execution_id, context, data['permision_real'])
            return False
        
        # 2. Sanitizar y obtener configuración
        type_sanitized = self.sanitize_type(data['type'], {
            'day': context['day'],
            'id_methodology': context['methodology']
        })
        mode_env = self.get_mode_env()
        mode_real = self.entity.get_mode_real()
        
        # 3. Log del estado inicial
        self.generate_log_mode_check_start(execution_id, context, type_sanitized, mode_env, mode_real)
        
        # 4. Validar lógica de modo
        is_valid, reason = self.check_mode_logic(type_sanitized, mode_env, mode_real)
        
        # 5. Log según resultado
        if reason == 'practice':
            self.generate_log_practice_mode_blocked(execution_id, context, type_sanitized, mode_env)
        elif reason == 'real':
            self.generate_log_real_mode_allowed(execution_id, context, type_sanitized, mode_real)
        elif reason == 'unexpected':
            self.generate_log_unexpected_type_error(execution_id, context, type_sanitized, mode_env, mode_real)
        
        return is_valid
    
    def get_type_manager_days_reporting(self,day,id_methodology):

        result = self.repository.get_type_manager_day(day,id_methodology)

        if not result['status']:

            return result

        return result['data']

    def get_type_manager_days(self,day,id_methodology):

        result = self.repository.get_type_manager_day(day,id_methodology)

        if not result['status']:

            return result
    
        # Inyectar id_methodology en data para tracking
        result['data']['id_methodology'] = id_methodology
        
        self.set_data_manager(result['data'])

        return self.check_mode_operativity(result['data'])
    
    def get_money(self):

        return self.entity.get_money()
        
        
