import apis.entities.models.EntityModels as EntityModels

class ServicesModels(): 

    entity = None

    ServicesDatasets = None

    def __init__(self):
        
        self.entity = EntityModels.EntityModels()
    
    def init_services_datasets(self,value):

        self.ServicesDatasets = value

        return True

    def get_config_active(self):
        
        return self.entity.get_config_active()

    def get_active_model(self):

        if not self.get_config_active():
            
            return False
        
        return True
    
    def get_dataset(self):

        return self.ServicesDatasets.get_dataset()
    
    def init_data(self,data):

        return True
    
    def generate_training_model(self):

        data = self.get_dataset()

        print(data)
        
        return True