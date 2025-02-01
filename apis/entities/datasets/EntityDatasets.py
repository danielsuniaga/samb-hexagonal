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
    
    def get_csv(self,path): 

        return pd.read_csv(path)
    
    def check_dataset(self,data):

        if 'entry_registration_date' in data.columns:
                    
            data['entry_registration_date'] = data['entry_registration_date'].astype(str)
            
            data['year'] = data['entry_registration_date'].str[:4].astype(int)
            
            data['month'] = data['entry_registration_date'].str[4:6].astype(int)

            data['day'] = data['entry_registration_date'].str[6:8].astype(int)

            data['hour'] = data['entry_registration_date'].str[8:10].astype(int) 

            data.drop(columns=['entry_registration_date'], inplace=True)

            data.drop(columns=['id_entry_id'], inplace=True)

        return data
    
    def get_dataset(self):

        path = self.get_config_add_dataset_route()

        data = self.get_csv(path)

        return self.check_dataset(data)