
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
            're_entry_platform': data['re_entry_platform']
        }
    
    def add_entrys_repository(self,data):

        return self.repository.add(data)

    def add_entrys(self,entrys):

        data = self.init_data_entrys(entrys)

        return self.add_entrys_repository(data)