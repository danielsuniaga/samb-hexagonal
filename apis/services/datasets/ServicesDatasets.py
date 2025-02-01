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
    
    def get_data_dataset_entrys(self,data_indicators):

        return self.ServicesEntrys.get_data_dataset_entrys(data_indicators)
    
    def get_ids_indicators(self):
        
        return self.ServicesIndicators.get_ids_indicators()
    
    def generate_dataframe_with_data(self,data):
        
        return self.entity.generate_dataframe_with_data(data)
    
    def add_dataset_entity(self,dataframe):

        return self.entity.add_dataset(dataframe)
    
    def get_data_dataset_entrys_min(self,data_indicators):
        
        return self.ServicesEntrys.get_entrys_dataset_min(data_indicators)

    def add_dataset(self):

        if not self.check_directory(self.get_directory_general()):
            
            return False
        
        data_indicators = self.get_ids_indicators()
        
        result = self.get_data_dataset_entrys_min(data_indicators)

        dataframe = self.generate_dataframe_with_data(result)
        
        return self.add_dataset_entity(dataframe)
    
    def get_dataset(self):

        return self.entity.get_dataset()