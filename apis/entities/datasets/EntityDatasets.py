from decouple import config

import os

import pandas as pd
class EntityDatasets():

    config = None

    def __init__(self):

        self.init_config()

    def init_config(self):

        self.config = {
            'name_general':config("DATASET_FILE_GENERAL"),
            'directory_general':config("DIRECTORY_FILE_GENERAL")
        }

        return True

    def get_config_name_general(self):

        return self.config['name_general']
    
    def get_config_directory_general(self):
        
        return self.config['directory_general']
    
    def check_directory(self, directory):

        if not os.path.exists(directory):

            os.makedirs(directory)

            self.check_directory(directory)

        return True
    
    def generate_dataframe_with_data(self,data):

        return pd.DataFrame(data)
    
    def get_config_add_dataset_route(self):
        
        return self.get_config_directory_general()+self.get_config_name_general()
    
    def add_dataset(self,dataframe):

        path = self.get_config_add_dataset_route()

        dataframe.to_csv(path,index=False)

        return True