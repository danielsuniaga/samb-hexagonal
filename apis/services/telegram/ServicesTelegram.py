import apis.entities.telegram.EntityTelegram as EntityTelegram
import apis.repositories.telegram.RepositoryTelegram as RepositoryTelegram

class ServicesTelegram():

    entity = None

    repository = None

    def __init__(self):

        self.entity = EntityTelegram.EntityTelegram()

        self.repository = RepositoryTelegram.RepositoryTelegram()

    def add_persistences(self,data):

        return self.repository.add(data)
    
    def generate_id(self):
        
        return self.entity.generate_id()
    
    def get_config_platform_type_entry(self):

        return self.entity.get_config_platform_type_entry()
    
    def get_config_platform_chat_id(self):

        return self.entity.get_config_platform_chat_id()    

    def get_condition(self):

        return self.entity.get_condition()  
    
    def init_data_add_persistence(self,result,mensaje,date):

        return {
            'id':self.generate_id(),
            'type':self.get_config_platform_type_entry(),
            'message':mensaje,
            'chat':self.get_config_platform_chat_id(),
            'response_method':result,
            'current_date':date,
            'condition':self.get_condition()
        }

    def send_message_entity(self,mensaje):

        return self.entity.send(mensaje)
    
    def generate_message_add_entry(self):

        return self.entity.generate_message_add_entry()

    def send_message(self,mensaje,date):

        result = self.send_message_entity(mensaje)

        data = self.init_data_add_persistence(result['message'],mensaje,date)

        return self.add_persistences(data)
    
    def send_message_report(self,mensaje):

        return self.send_message_entity(mensaje)