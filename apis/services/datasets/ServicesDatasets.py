import apis.entities.datasets.EntityDatasets as EntityDatasets

class ServicesDatasets():

    entity = None

    ServicesEntrys = None

    ServicesIndicators = None   

    def __init__(self):
        
        self.entity = EntityDatasets.EntityDatasets()

    def init_services_indicators(self,value):
        
        self.ServicesIndicators = value

        return True

    def init_services_entrys(self,value):
        
        self.ServicesEntrys = value

        return True

    def get_directory_general(self):
        
        return self.entity.get_config_directory_general()
    
    def check_directory(self, directory):
        
        return self.entity.check_directory(directory)
    
    def get_data_dataset_entrys(self):

        return self.ServicesEntrys.get_data_dataset_entrys()
    
    def get_ids_indicators(self):
        
        return self.ServicesIndicators.get_ids_indicators()

    def add_dataset(self):

        if not self.check_directory(self.get_directory_general()):
            
            return False
        
        data_indicators = self.get_ids_indicators()
        
        result = self.get_data_dataset_entrys(data_indicators)

        print(result)
        
        return True