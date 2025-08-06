import apis.repositories.entryspredictmodels.RepositoryEntrysPredictModels as RepositoryEntrysPredictModels

import apis.entities.entryspredictmodels.EntityEntrysPredictModels as EntityEntrysPredictModels

class ServicesEntrysPredictModels: 

    ServicesDates = None   

    repository = None

    entity = None

    def __init__(self):
        self.repository = RepositoryEntrysPredictModels.RepositoryEntrysPredictModels()
        self.entity = EntityEntrysPredictModels.EntityEntrysPredictModels()

    def init_services_dates(self, value):
        self.ServicesDates = value
        return True
    
    def generate_id(self):
        return self.entity.generate_id()
    
    def get_current_date_hour(self):
        if not self.ServicesDates:
            return False
        
        return self.ServicesDates.get_current_date_hour()
    
    def get_config_condition(self):
        return self.entity.get_config_condition()
    
    def init_add(self,data):

        return {
            'id': self.generate_id(),
            'id_entrys': data['data_entry']['id_entry'],
            'id_predict_models': data['id_predict_models'],
            'registration_date': self.get_current_date_hour(),
            'update_date': self.get_current_date_hour(),
            'state': self.get_config_condition()
        }
    
    def add_repository(self, data):

        return self.repository.add(data)

    def add(self,data):

        data_persistence = self.init_add(data)  

        result = self.add_repository(data_persistence)

        return result
        