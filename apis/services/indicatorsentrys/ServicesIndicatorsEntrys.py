import apis.repositories.indicatorsentrys.RepositoryIndicatorsEntrys as RepositoryIndicatorsEntrys
import apis.entities.indicatorsentrys.EntityIndicatorsEntrys as EntityIndicatorsEntrys

class ServicesIndicatorsEntrys():

    entity = None

    repository = None

    def __init__(self):

        self.entity = EntityIndicatorsEntrys.EntityIndicatorsEntrys()
        
        self.repository = RepositoryIndicatorsEntrys.RepositoryIndicatorsEntrys()

    def generate_id(self):

        return self.entity.generate_id()
    
    def get_condition(self):

        return self.entity.get_condition()
    
    def get_ids_indicators_rsi10(self):
        
        return self.entity.get_ids_indicators_rsi10()
    
    def get_ids_indicators_sma10(self):

        return self.entity.get_ids_indicators_sma10()
    
    def get_ids_indicators_sma30(self):

        return self.entity.get_ids_indicators_sma30()

    def init_data_add_persistence(self,data):
        
        return {
            'rsi10':{
                'id':self.generate_id(),
                'current_date':data['current_date'],
                'condition':self.get_condition(),
                'id_entry': data['data_entry']['id_entry'],
                'id_indicators':self.get_ids_indicators_rsi10(),
                'value_indicators':data['rsi']
            },
            'sma10':{
                'id':self.generate_id(),
                'current_date':data['current_date'],
                'condition':self.get_condition(),
                'id_entry': data['data_entry']['id_entry'],
                'id_indicators':self.get_ids_indicators_sma10(),
                'value_indicators':data['sma_short']
            },
            'sma30':{
                'id':self.generate_id(),
                'current_date':data['current_date'],
                'condition':self.get_condition(),
                'id_entry': data['data_entry']['id_entry'],
                'id_indicators':self.get_ids_indicators_sma30(),
                'value_indicators':data['sma_long']
            }
        }
    
    def add_persistence_repository(self,data):

        return self.repository.add(data)

    def add_persistence(self, data):

        data_persistence = self.init_data_add_persistence(data)

        for key in data_persistence:

            result = self.add_persistence_repository(data_persistence[key])

            if not result['status']:

                return False
        
        return result
    
    def init_data_get_indicators_entrys(self, data):

        return{
                'id_entry': data['id'],
                'condition': self.get_condition()
            }  

    def get_entrys_repository(self, data):

        return self.repository.get_entrys(data) 

    def init_result_get_entrys_repository(self, data):

        return data['data'] if 'data' in data else []     
    
    def get_data_indicators_entrys(self, data):

        data_persistence = self.init_data_get_indicators_entrys(data)

        result = self.get_entrys_repository(data_persistence)

        result_send = self.init_result_get_entrys_repository(result)

        return self.init_result_get_entrys_repository(result)