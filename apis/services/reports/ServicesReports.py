import apis.entities.reports.EntityReports as EntityReports
import apis.repositories.reports.RepositoryReports as RepositoryReports
from decouple import config
import logging
import time

logger = logging.getLogger('ServicesPersistence')

class ServicesReports():

    entity = None

    repository = None

    def __init__(self):

        self.entity = EntityReports.EntityReports()

        self.repository = RepositoryReports.RepositoryReports()

    def generate_id(self):

        return self.entity.generate_id()
    
    def get_condition(self):

        return self.entity.get_condition()

    def init_data_add_persistence(self,type_reports,date):

        return {
            'id':self.generate_id(),
            'description':type_reports,
            'fecha':date,
            'condition':self.get_condition()
        }
    
    def add_repository(self,data):

        return self.repository.add(data)

    def add_persistence(self,type_reports,date):

        data_peristence = self.init_data_add_persistence(type_reports,date)

        start_time = time.time()
        result = self.add_repository(data_peristence)
        execution_time = (time.time() - start_time) * 1000

        if result.get('status'):
            logger.info(
                f"💾 ADD PERSISTENCE | "
                f"Table: samb_reports | "
                f"Project: {config('PROJECT_NAME', default='N/A')} | "
                f"Method: add_persistence | "
                f"Report ID: {data_peristence['id']} | "
                f"Type: {data_peristence['description']} | "
                f"Execution Time: {execution_time:.2f}ms | "
                f"Status: SUCCESS"
            )
        else:
            logger.error(
                f"💾 ADD PERSISTENCE | "
                f"Table: samb_reports | "
                f"Project: {config('PROJECT_NAME', default='N/A')} | "
                f"Method: add_persistence | "
                f"Report ID: {data_peristence['id']} | "
                f"Type: {data_peristence['description']} | "
                f"Execution Time: {execution_time:.2f}ms | "
                f"Status: FAILED | "
                f"Error: {result.get('msj', 'Unknown error')}"
            )

        return result