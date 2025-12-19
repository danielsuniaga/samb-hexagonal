import logging
import time

import apis.entities.entrys.EntityEntrys as EntityEntrys
import apis.repositories.entrys.RepositoryEntrys as RepositoryEntrys

logger = logging.getLogger('apis.services.entrys')

class ServicesEntrys():

    entity = None

    repository = None

    def __init__(self):

        self.entity = EntityEntrys.EntityEntrys()   

        self.repository = RepositoryEntrys.RepositoryEntrys()

    def generate_id(self):

        return self.entity.generate_id()  

    def get_condition(self):
        
        return self.entity.get_condition()
    
    def get_project_name(self):
        
        return self.entity.get_project_name()

    def init_data_entrys(self,data):

        return {
            'id_entry': self.generate_id(),
            'type_operations': data['contract_details']['contract_type'],
            'mode': data['mode'],
            'candle_analized': data['candle_analisys'],
            'condition_entry': data['condition_entry'],
            'amount': data['amount'],
            'current_date': data['current_date'],
            'condition': self.get_condition(),
            'id_cronjobs': data['id_cronjobs'],
            'id_entry_platform': data['contract_details']['account_id'],
            'id_methodology': data['id_methodology'],
            're_entry_platform': data['re_entry_platform']
        }
    
    def add_entrys_repository(self,data):

        return self.repository.add(data)
    
    def add_data_entity(self,data):
        
        return self.entity.set_data(data)
    
    def get_data_entity(self):
        
        return self.entity.get_data()

    def add_entrys(self,entrys):

        data = self.init_data_entrys(entrys)

        self.add_data_entity(data)

        return self.add_entrys_repository(data)
    
    def init_get_data_dataset_entrys(self,data):

        if not data['status']:

            return False
        
        return data['data']
    
    def get_entrys_dataset_repository(self,data):

        return self.repository.get_entrys_dataset(data)
    
    def get_data_dataset_entrys(self,data_indicators):
        # Iniciar medición de tiempo
        start_time = time.time()

        result = self.get_entrys_dataset_repository(data_indicators)
        
        # Calcular tiempo de ejecución
        query_time = (time.time() - start_time) * 1000  # en milisegundos
        
        # Obtener información de contexto
        project_name = self.get_project_name()
        
        # Extraer datos del resultado
        if result.get('status'):
            record_count = len(result.get('data', []))
            sma30 = data_indicators.get('sma30', 'N/A')
            sma10 = data_indicators.get('sma10', 'N/A')
            rsi10 = data_indicators.get('rsi10', 'N/A')
            
            # Log de rendimiento
            logger.info(
                f"📊 ML DATASET QUERY | "
                f"Project: {project_name} | "
                f"Method: get_data_dataset_entrys | "
                f"Records: {record_count} | "
                f"Indicators: SMA30={sma30}, SMA10={sma10}, RSI={rsi10} | "
                f"Query Time: {query_time:.2f}ms"
            )
        else:
            logger.error(
                f"❌ ML DATASET ERROR | "
                f"Project: {project_name} | "
                f"Method: get_data_dataset_entrys | "
                f"Error: {result.get('msj', 'Unknown error')} | "
                f"Time: {query_time:.2f}ms"
            )

        return self.init_get_data_dataset_entrys(result)
    
    def get_entrys_dataset_min_repository(self,data):
        
        return self.repository.get_entrys_dataset_min(data)
    
    def get_entrys_dataset_min(self,data):
        # Iniciar medición de tiempo
        start_time = time.time()

        result = self.get_entrys_dataset_min_repository(data)
        
        # Calcular tiempo de ejecución
        query_time = (time.time() - start_time) * 1000  # en milisegundos
        
        # Obtener información de contexto
        project_name = self.get_project_name()
        
        # Extraer datos del resultado
        if result.get('status'):
            record_count = len(result.get('data', []))
            sma30 = data.get('sma30', 'N/A')
            sma10 = data.get('sma10', 'N/A')
            rsi10 = data.get('rsi10', 'N/A')
            
            # Log de rendimiento
            logger.info(
                f"📊 ML DATASET MIN QUERY | "
                f"Project: {project_name} | "
                f"Method: get_entrys_dataset_min | "
                f"Records: {record_count} | "
                f"Indicators: SMA30={sma30}, SMA10={sma10}, RSI={rsi10} | "
                f"Query Time: {query_time:.2f}ms"
            )
        else:
            logger.error(
                f"❌ ML DATASET MIN ERROR | "
                f"Project: {project_name} | "
                f"Method: get_entrys_dataset_min | "
                f"Error: {result.get('msj', 'Unknown error')} | "
                f"Time: {query_time:.2f}ms"
            )

        return self.init_get_data_dataset_entrys(result)
    
    def get_entrys_send_session_repository(self,data):

        if self.repository is None:

            raise ValueError("RepositoryEntrys not initialized")
        
        return self.repository.get_entrys_send_session(data)
    
    def init_data_get_entrys_send_session(self):

        return {
            "condition": self.get_condition(),
        }
    
    def init_data_result_get_entrys_send_session(self, data):

        if not data['status']:

            return False
        
        return data['data']
    
    def get_entrys_send_session(self):
        # Iniciar medición de tiempo
        start_time = time.time()

        data = self.init_data_get_entrys_send_session()

        result = self.get_entrys_send_session_repository(data)
        
        # Calcular tiempo de ejecución
        query_time = (time.time() - start_time) * 1000  # en milisegundos
        
        # Obtener información de contexto
        project_name = self.get_project_name()
        
        # Extraer datos del resultado
        if result.get('status'):
            record_count = len(result.get('data', []))
            condition = data.get('condition', 'unknown')
            
            # Log de rendimiento
            logger.info(
                f"📤 SEND SESSION QUERY | "
                f"Project: {project_name} | "
                f"Method: get_entrys_send_session | "
                f"Condition: {condition} | "
                f"Records: {record_count} | "
                f"Query Time: {query_time:.2f}ms"
            )
        else:
            logger.error(
                f"❌ SEND SESSION ERROR | "
                f"Project: {project_name} | "
                f"Method: get_entrys_send_session | "
                f"Error: {result.get('msj', 'Unknown error')} | "
                f"Time: {query_time:.2f}ms"
            )

        return self.init_data_result_get_entrys_send_session(result)
    