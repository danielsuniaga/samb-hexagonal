import logging
import time

import apis.entities.events.EntityEvents as EntityEvents

import apis.repositories.events.RepositoryEvents as RepositoryEvents

logger = logging.getLogger('apis.services.events')

class ServicesEvents():

    entity = None

    repository = None

    ServicesDates = None

    def __init__(self):

        self.entity = EntityEvents.EntityEvents()

        self.repository = RepositoryEvents.RepositoryEvents()

    def get_project_name(self):

        return self.entity.get_project_name()

    def get_current_date_hour(self):

        return self.ServicesDates.get_current_date_hour()

    def init_services_dates(self, value):

        self.ServicesDates = value

        return True

    def set_events_field(self,field,value):

        return self.entity.set_events_field(field,value)
    
    def get_events(self):

        return self.entity.get_events()
    
    def generate_diferences_events(self):

        return self.entity.generate_diferences_events()
    
    def generate_id(self):

        return self.entity.generate_id()
    
    def get_config_condition(self):

        return self.entity.get_config_condition()
    
    def init_data_add_events(self, details, differences, id_cronjobs):

        dates = self.get_current_date_hour()

        return {
            'id': self.generate_id(),
            'details': details,
            'difference': differences,
            'registration_date': dates,
            'update_cate': dates,
            'state': self.get_config_condition(),
            'id_samb_cronjobs_id': id_cronjobs
        }
    
    def add_events_repository(self,data):

        return self.repository.add(data)
    
    def add_events(self,details,diferrences,id_cronjobs):

        data = self.init_data_add_events(details,diferrences,id_cronjobs)

        return self.add_events_repository(data)
    
    def get_events_daily_cron_repository(self):

        return self.repository.get_events_daily_crons()
    
    def init_data_result_events_daily_cron(self,resultado):

        return 'Condition_cron: {cond} Execution_time: {execution_time}, Details: {difference}'.format(
            execution_time=round(float(resultado['execution_time']), 2),
            difference=resultado['difference'],
            cond =resultado['cond']
        )
    
    def get_events_daily_cron(self):
        # Iniciar medición de tiempo
        start_time = time.time()

        data = self.get_events_daily_cron_repository()
        
        # Calcular tiempo de ejecución
        query_time = (time.time() - start_time) * 1000  # en milisegundos
        
        # Obtener información de contexto
        project_name = self.get_project_name()
        
        # Extraer datos del resultado
        if data.get('status') and data.get('result'):
            result = data['result']
            execution_time = result.get('execution_time', 0)
            difference = result.get('difference', 'N/A')
            condition = result.get('cond', 'unknown')
            
            # Log de rendimiento
            logger.info(
                f"⏱️ EVENTS DAILY QUERY | "
                f"Project: {project_name} | "
                f"Method: get_events_daily_cron | "
                f"Condition: {condition} | "
                f"Execution Time: {execution_time}s | "
                f"Difference: {difference} | "
                f"Query Time: {query_time:.2f}ms"
            )
        else:
            logger.warning(
                f"⚠️ EVENTS DAILY WARNING | "
                f"Project: {project_name} | "
                f"Method: get_events_daily_cron | "
                f"Message: {data.get('message', 'No events found')} | "
                f"Time: {query_time:.2f}ms"
            )

        return self.init_data_result_events_daily_cron(data['result']) if data['status'] else data['message']