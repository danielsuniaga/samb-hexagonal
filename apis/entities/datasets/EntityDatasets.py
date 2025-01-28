from decouple import config

import os

class EntityDatasets():

    config = None

    def __init__(self):

        self.init_config()

    def init_config(self):

        self.config = {
            'name_general':config("DATASET_FILE_GENERAL"),
            'directory_general':config("DATASET_DIRECTORY_GENERAL")
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