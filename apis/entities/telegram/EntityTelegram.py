import requests

import uuid

from decouple import config

class EntityTelegram():

    config_platform = None

    condition = None

    project_name = None

    def __init__(self):

        self.init_config_platform()

        self.init_condition()

        self.init_project_name()

    def init_project_name(self):
        
        self.project_name = config("PROJECT_NAME")

        return True
    
    def get_project_name(self):
        
        return self.project_name

    def init_condition(self):

        self.condition = config("CONDITION")

        return True
    
    def get_condition(self):

        return self.condition

    def init_config_platform(self):

        self.config_platform = {
            'base_url': config("URL_TELEGRAM"),
            'chat_id': config("CHAT_ID"),
            'type_entry':config("TYPE_NOTIFICATION_TELEGRAM")
        }

        return True
    
    def generate_id(self):

        return uuid.uuid4().hex
    
    def get_config_platform_type_entry(self):
        
        return self.config_platform['type_entry']
    
    def get_config_platform_base_url(self):

        return self.config_platform['base_url'] 
    
    def get_config_platform_chat_id(self):

        return self.config_platform['chat_id']  

    def send(self, mensaje):

        try:

            url = self.get_config_platform_base_url() 
            
            params = {
            
                'chat_id': self.get_config_platform_chat_id(),
            
                'text': mensaje
            
            }
            
            response = requests.post(url, params=params)

            if response.status_code != 200:

                return {'status':False,'message':'Error al enviar el mensaje. Codigo de respuesta:'+str(response.status_code)}

        except Exception as err:

            return {'status': False, 'message':'Hubo una incidencia en el envio del mensaje por telegram: '+str(err)}
        
        return {'status': True, 'message':'Success'}
    
    def generate_message_add_entry(self):
        
        return self.get_project_name()+': Registry Entry Success'