import logging
import time
import os

import apis.entities.cronjobs.EntityCronjobs as EntityCronjobs

import apis.repositories.cronjobs.RepositoryCronjobs as RepositoryCronjobs

logger = logging.getLogger('apis.services.cronjobs')

class ServicesCronjobs():

    entity = None

    repository = None

    def __init__(self):

        self.entity = EntityCronjobs.EntityCronjobs()

        self.repository = RepositoryCronjobs.RepositoryCronjobs()

    def add_repository(self,data):

        return self.repository.add(data)
    
    def set_id_cronjobs(self,id_cronjobs):

        return self.entity.set_id_cronjobs(id_cronjobs)

    def generate_cronjobs_id(self):

        result =  self.entity.generate_cronjobs_id()

        self.set_id_cronjobs(result)

        return result
    
    def get_id_cronjobs(self):

        return self.entity.get_id_cronjobs()
    
    def get_condition(self):

        return self.entity.get_condition()
    
    def get_id_api_trends(self):

        return self.entity.get_id_api_trends()
    
    def get_id_api_trends_recent(self):

        return self.entity.get_id_api_trends_recent()

    def get_id_api_trends_recent_ml(self):

        return self.entity.get_id_api_trends_recent_ml()
    
    def get_id_api_trends_minus_recent_ml(self):

        return self.entity.get_id_api_trends_minus_recent_ml()

    def get_id_api_trends_ml(self):

        return self.entity.get_id_api_trends_ml()

    def get_id_api_trends_minus_ml(self):

        return self.entity.get_id_api_trends_minus_ml()

    def get_id_api_trends_expansive(self):

        return self.entity.get_id_api_trends_expansive()

    def get_id_api_trends_expansive_ml(self):

        return self.entity.get_id_api_trends_expansive_ml()

    def get_id_api_trends_expansive_recent(self):

        return self.entity.get_id_api_trends_expansive_recent()

    def get_id_api_trends_expansive_recent_ml(self):

        return self.entity.get_id_api_trends_expansive_recent_ml()

    def get_id_api_wma(self):

        return self.entity.get_id_api_wma()

    def get_id_api_wma_recent(self):

        return self.entity.get_id_api_wma_recent()
    
    def get_id_api_wma_recent_ml(self):

        return self.entity.get_id_api_wma_recent_ml()

    def get_id_api_wma_ml(self):

        return self.entity.get_id_api_wma_ml()
    
    def get_id_api_trends_minus(self):

        return self.entity.get_id_api_trends_minus()
    
    def get_id_api_trends_minus_recent(self):

        return self.entity.get_id_api_trends_minus_recent()
    
    def get_id_api_envolvent(self):

        return self.entity.get_id_api_envolvent()
    
    def get_id_api_envolvent_ml(self):

        return self.entity.get_id_api_envolvent_ml()
    
    def get_id_api_pinbar(self):

        return self.entity.get_id_api_pinbar()
    
    def get_id_api_pinbar_ml(self):

        return self.entity.get_id_api_pinbar_ml()
    
    def get_id_financial_asset(self):

        return self.entity.get_id_financial_asset()
    
    def get_default_execute(self):

        return self.entity.get_default_execute()
    
    def init_add_trends_expansive_recent_repository(self,id_cronjobs,date):

        return {
            'id':id_cronjobs,
            'date':date,
            'condition':self.get_condition(),
            'id_api':self.get_id_api_trends_expansive_recent(),
            'id_financial_asset':self.get_id_financial_asset(),
            'default_execute':self.get_default_execute()
        }
    
    def init_add_trends_expansive_recent_ml_repository(self,id_cronjobs,date):

        return {
            'id':id_cronjobs,
            'date':date,
            'condition':self.get_condition(),
            'id_api':self.get_id_api_trends_expansive_recent_ml(),
            'id_financial_asset':self.get_id_financial_asset(),
            'default_execute':self.get_default_execute()
        }
    
    def init_add_trends_expansive_repository(self,id_cronjobs,date):

        return {
            'id':id_cronjobs,
            'date':date,
            'condition':self.get_condition(),
            'id_api':self.get_id_api_trends_expansive(),
            'id_financial_asset':self.get_id_financial_asset(),
            'default_execute':self.get_default_execute()
        }
    
    def init_add_trends_expansive_ml_repository(self,id_cronjobs,date):

        return {
            'id':id_cronjobs,
            'date':date,
            'condition':self.get_condition(),
            'id_api':self.get_id_api_trends_expansive_ml(),
            'id_financial_asset':self.get_id_financial_asset(),
            'default_execute':self.get_default_execute()
        }
    
    def init_add_trends_repository(self,id_cronjobs,date):

        return {
            'id':id_cronjobs,
            'date':date,
            'condition':self.get_condition(),
            'id_api':self.get_id_api_trends(),
            'id_financial_asset':self.get_id_financial_asset(),
            'default_execute':self.get_default_execute()
        }
    
    def init_add_trends_recent_repository(self,id_cronjobs,date):

        return {
            'id':id_cronjobs,
            'date':date,
            'condition':self.get_condition(),
            'id_api':self.get_id_api_trends_recent(),
            'id_financial_asset':self.get_id_financial_asset(),
            'default_execute':self.get_default_execute()
        }
    
    def init_add_trends_recent_ml_repository(self,id_cronjobs,date):

        return {
            'id':id_cronjobs,
            'date':date,
            'condition':self.get_condition(),
            'id_api':self.get_id_api_trends_recent_ml(),
            'id_financial_asset':self.get_id_financial_asset(),
            'default_execute':self.get_default_execute()
        }
    
    def init_add_trends_minus_recent_ml_repository(self,id_cronjobs,date):

        return {
            'id':id_cronjobs,
            'date':date,
            'condition':self.get_condition(),
            'id_api':self.get_id_api_trends_minus_recent_ml(),
            'id_financial_asset':self.get_id_financial_asset(),
            'default_execute':self.get_default_execute()
        }
    
    def init_add_trends_ml_repository(self,id_cronjobs,date):

        return {
            'id':id_cronjobs,
            'date':date,
            'condition':self.get_condition(),
            'id_api':self.get_id_api_trends_ml(),
            'id_financial_asset':self.get_id_financial_asset(),
            'default_execute':self.get_default_execute()
        }
    
    def init_add_trends_minus_ml_repository(self,id_cronjobs,date):

        return {
            'id':id_cronjobs,
            'date':date,
            'condition':self.get_condition(),
            'id_api':self.get_id_api_trends_minus_ml(),
            'id_financial_asset':self.get_id_financial_asset(),
            'default_execute':self.get_default_execute()
        }
    
    def init_add_wma_repository(self,id_cronjobs,date):

        return {
            'id':id_cronjobs,
            'date':date,
            'condition':self.get_condition(),
            'id_api':self.get_id_api_wma(),
            'id_financial_asset':self.get_id_financial_asset(),
            'default_execute':self.get_default_execute()
        }

    def init_add_wma_recent_repository(self,id_cronjobs,date):

        return {
            'id':id_cronjobs,
            'date':date,
            'condition':self.get_condition(),
            'id_api':self.get_id_api_wma_recent(),
            'id_financial_asset':self.get_id_financial_asset(),
            'default_execute':self.get_default_execute()
        }
    
    def init_add_wma_recent_ml_repository(self,id_cronjobs,date):

        return {
            'id':id_cronjobs,
            'date':date,
            'condition':self.get_condition(),
            'id_api':self.get_id_api_wma_recent_ml(),
            'id_financial_asset':self.get_id_financial_asset(),
            'default_execute':self.get_default_execute()
        }

    def init_add_wma_ml_repository(self,id_cronjobs,date):

        return {
            'id':id_cronjobs,
            'date':date,
            'condition':self.get_condition(),
            'id_api':self.get_id_api_wma_ml(),
            'id_financial_asset':self.get_id_financial_asset(),
            'default_execute':self.get_default_execute()
        }
    def add_trends_ml(self,id_cronjobs,date):

        data = self.init_add_trends_ml_repository(id_cronjobs,date)

        return self.add_repository(data)
    
    def add_trends_minus_ml(self,id_cronjobs,date):

        data = self.init_add_trends_minus_ml_repository(id_cronjobs,date)

        return self.add_repository(data)
    
    def add_trends(self,id_cronjobs,date):

        data = self.init_add_trends_repository(id_cronjobs,date)

        return self.add_repository(data)
    
    def add_trends_recent(self,id_cronjobs,date):

        data = self.init_add_trends_recent_repository(id_cronjobs,date)

        return self.add_repository(data)
    
    def add_trends_recent_ml(self,id_cronjobs,date):

        data = self.init_add_trends_recent_ml_repository(id_cronjobs,date)

        return self.add_repository(data)
    
    def add_trends_minus_recent_ml(self,id_cronjobs,date):

        data = self.init_add_trends_minus_recent_ml_repository(id_cronjobs,date)

        return self.add_repository(data)
    
    def add_trends_expansive_recent(self,id_cronjobs,date):

        data = self.init_add_trends_expansive_recent_repository(id_cronjobs,date)

        return self.add_repository(data)
    
    def add_trends_expansive_recent_ml(self,id_cronjobs,date):

        data = self.init_add_trends_expansive_recent_ml_repository(id_cronjobs,date)

        return self.add_repository(data)
    
    def add_trends_expansive(self,id_cronjobs,date):

        data = self.init_add_trends_expansive_repository(id_cronjobs,date)

        return self.add_repository(data)
    
    def add_trends_expansive_ml(self,id_cronjobs,date):

        data = self.init_add_trends_expansive_ml_repository(id_cronjobs,date)

        return self.add_repository(data)

        return self.add_repository(data)

    def init_data_add_trends_minus_repository(self,id_cronjobs,date):

        return {
            'id':id_cronjobs,
            'date':date,
            'condition':self.get_condition(),
            'id_api':self.get_id_api_trends_minus(),
            'id_financial_asset':self.get_id_financial_asset(),
            'default_execute':self.get_default_execute()
        }
    
    def add_trends_minus(self,id_cronjobs,date):

        data = self.init_data_add_trends_minus_repository(id_cronjobs,date)

        return self.add_repository(data)
    
    def init_data_add_trends_minus_recent_repository(self,id_cronjobs,date):

        return {
            'id':id_cronjobs,
            'date':date,
            'condition':self.get_condition(),
            'id_api':self.get_id_api_trends_minus_recent(),
            'id_financial_asset':self.get_id_financial_asset(),
            'default_execute':self.get_default_execute()
        }
    
    def add_trends_minus_recent(self,id_cronjobs,date):

        data = self.init_data_add_trends_minus_recent_repository(id_cronjobs,date)

        return self.add_repository(data)
    
    def init_data_add_envolvent_repository(self,id_cronjobs,date):

        return {
            'id':id_cronjobs,
            'date':date,
            'condition':self.get_condition(),
            'id_api':self.get_id_api_envolvent(),
            'id_financial_asset':self.get_id_financial_asset(),
            'default_execute':self.get_default_execute()
        }
    
    def add_envolvent(self,id_cronjobs,date):

        data = self.init_data_add_envolvent_repository(id_cronjobs,date)

        return self.add_repository(data)
    
    def init_data_add_envolvent_ml_repository(self,id_cronjobs,date):

        return {
            'id':id_cronjobs,
            'date':date,
            'condition':self.get_condition(),
            'id_api':self.get_id_api_envolvent_ml(),
            'id_financial_asset':self.get_id_financial_asset(),
            'default_execute':self.get_default_execute()
        }
    
    def add_envolvent_ml(self,id_cronjobs,date):

        data = self.init_data_add_envolvent_ml_repository(id_cronjobs,date)

        return self.add_repository(data)
    
    def init_data_add_pinbar_repository(self,id_cronjobs,date):

        return {
            'id':id_cronjobs,
            'date':date,
            'condition':self.get_condition(),
            'id_api':self.get_id_api_pinbar(),
            'id_financial_asset':self.get_id_financial_asset(),
            'default_execute':self.get_default_execute()
        }
    
    def init_data_add_pinbar_ml_repository(self,id_cronjobs,date):

        return {
            'id':id_cronjobs,
            'date':date,
            'condition':self.get_condition(),
            'id_api':self.get_id_api_pinbar_ml(),
            'id_financial_asset':self.get_id_financial_asset(),
            'default_execute':self.get_default_execute()
        }
    
    def add_pinbar(self,id_cronjobs,date):

        data = self.init_data_add_pinbar_repository(id_cronjobs,date)

        return self.add_repository(data)
    
    def add_pinbar_ml(self,id_cronjobs,date):

        data = self.init_data_add_pinbar_ml_repository(id_cronjobs,date)

        return self.add_repository(data)
    
    def add_wma(self,id_cronjobs,date):

        data = self.init_add_wma_repository(id_cronjobs,date)

        return self.add_repository(data)
    
    def add_wma_recent_ml(self,id_cronjobs,date):

        data = self.init_add_wma_recent_ml_repository(id_cronjobs,date)

        return self.add_repository(data)
    
    def add_wma_recent(self,id_cronjobs,date):

        data = self.init_add_wma_recent_repository(id_cronjobs,date)

        return self.add_repository(data)
    
    def add_wma_ml(self,id_cronjobs,date):

        data = self.init_add_wma_ml_repository(id_cronjobs,date)

        return self.add_repository(data)
    
    def get_success_condition(self):

        return self.entity.get_success_condition()
    
    def init_data_set_ejecution(self,date,time_execution,id_cronjobs):

        return {
            'success_condition':self.get_success_condition(),
            'end_date':date,
            'execute_time':time_execution,
            'id_cronjobs':id_cronjobs
        }
    
    def set_ejecution_repository(self,data):

        return self.repository.set(data)
    
    def set_ejecution(self,date,time_execution,id_cronjobs):

        data_persistence = self.init_data_set_ejecution(date,time_execution,id_cronjobs)

        return self.set_ejecution_repository(data_persistence)
    
    def init_data_get_data_cronjobs_curdate(self,data,result):

        if result['status']:

            data['data']['quantities'] = result['result']['quantities']

            data['data']['max_durations'] = result['result']['max_durations']

        return data
    
    def get_data_cronjobs_curdate(self,data):
        # Iniciar medición de tiempo
        start_time = time.time()

        result = self.repository.get_data_cronjobs_curdate(data)
        
        # Calcular tiempo de ejecución
        query_time = (time.time() - start_time) * 1000  # en milisegundos
        
        # Obtener información de contexto
        project_name = self.entity.get_project_name()
        condition = data.get('state', 'unknown')
        
        # Extraer datos del resultado
        if result.get('status') and result.get('result'):
            count = result['result'].get('quantities', 0)
            max_time = result['result'].get('max_durations', 0)
        else:
            count = 0
            max_time = 0
        
        # Log de rendimiento
        logger.info(
            f"⏰ CRONJOBS QUERY | "
            f"Project: {project_name} | "
            f"Method: get_data_cronjobs_curdate | "
            f"Condition: {condition} | "
            f"Count: {count} | "
            f"Max Execution Time: {max_time}s | "
            f"Query Time: {query_time:.2f}ms"
        )

        return self.init_data_get_data_cronjobs_curdate(data,result)