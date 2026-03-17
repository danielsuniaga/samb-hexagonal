import apis.entities.sendentrys.EntitySendEntrys as EntitySendEntrys

import apis.repositories.sendentrys.RepositorySendEntrys as RepositorySendEntrys

from decouple import config
import logging
import time

logger = logging.getLogger('ServicesPersistence')

class ServicesSendEntrys:

    services_dates = None 

    entity = None

    repository = None

    def __init__(self):

        self.init_entity()

        self.init_repository()

    def init_repository(self):
        self.repository = RepositorySendEntrys.RepositorySendEntrys()

        return True

    def init_services_dates(self, value):

        self.services_dates = value

        return True
    
    def get_current_date(self):

        if self.services_dates is not None:

            return self.services_dates.get_current_date_hour()

        return None

    def init_entity(self):

        self.entity = EntitySendEntrys.EntitySendEntrys()

        return True
    
    def generate_id(self):

        return self.entity.generate_id()
    
    def get_config(self, key):

        return self.entity.get_config(key)

    def init_data_add_send_entrys(self, data, result):

        return {
            "id": self.generate_id(),
            "registration_date": self.get_current_date(),
            "conditions": self.get_config("condition"),
            "id_entrys": data.get("id", []),
            "response": result.get("status_code", 0)
        }
    
    def add_send_entrys_repository(self, data):

        return self.repository.add(data)

    def add_send_entrys(self,data,result):

        data_persistence = self.init_data_add_send_entrys(data, result)

        start_time = time.time()
        result = self.add_send_entrys_repository(data_persistence)
        execution_time = (time.time() - start_time) * 1000

        if result.get('status'):
            logger.info(
                f"💾 ADD PERSISTENCE | "
                f"Table: samb_send_entrys | "
                f"Project: {config('PROJECT_NAME', default='N/A')} | "
                f"Method: add_send_entrys | "
                f"Send ID: {data_persistence['id']} | "
                f"Response: {data_persistence['response']} | "
                f"Execution Time: {execution_time:.2f}ms | "
                f"Status: SUCCESS"
            )
        else:
            logger.error(
                f"💾 ADD PERSISTENCE | "
                f"Table: samb_send_entrys | "
                f"Project: {config('PROJECT_NAME', default='N/A')} | "
                f"Method: add_send_entrys | "
                f"Send ID: {data_persistence['id']} | "
                f"Response: {data_persistence['response']} | "
                f"Execution Time: {execution_time:.2f}ms | "
                f"Status: FAILED | "
                f"Error: {result.get('msj', 'Unknown error')}"
            )

        return result