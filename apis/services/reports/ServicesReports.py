import apis.entities.reports.EntityReports as EntityReports
import apis.repositories.reports.RepositoryReports as RepositoryReports 

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

        return self.add_repository(data_peristence) 