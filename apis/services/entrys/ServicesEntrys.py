
import apis.entities.entrys.EntityEntrys as EntityEntrys
import apis.repositories.entrys.RepositoryEntrys as RepositoryEntrys    

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

        result = self.get_entrys_dataset_repository(data_indicators)

        return self.init_get_data_dataset_entrys(result)
    
    def get_entrys_dataset_min_repository(self,data):
        
        return self.repository.get_entrys_dataset_min(data)
    
    def get_entrys_dataset_min(self,data):

        result = self.get_entrys_dataset_min_repository(data)

        return self.init_get_data_dataset_entrys(result)
    