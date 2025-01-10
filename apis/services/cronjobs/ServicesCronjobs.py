import apis.entities.cronjobs.EntityCronjobs as EntityCronjobs

import apis.repositories.cronjobs.RepositoryCronjobs as RepositoryCronjobs

class ServicesCronjobs():

    entity = None

    repository = None

    def __init__(self):

        self.entity = EntityCronjobs.EntityCronjobs()

        self.repository = RepositoryCronjobs.RepositoryCronjobs()

    def add_repository(self,data):

        return self.repository.add(data)
    
    def set_id_cronjobs(self,id_cronjobs):

        return self.entity.set_id_cronjobs(id_cronjobs)

    def generate_cronjobs_id(self):

        result =  self.entity.generate_cronjobs_id()

        self.set_id_cronjobs(result)

        return result
    
    def get_id_cronjobs(self):

        return self.entity.get_id_cronjobs()
    
    def get_condition(self):

        return self.entity.get_condition()
    
    def get_id_api(self):

        return self.entity.get_id_api()
    
    def get_id_financial_asset(self):

        return self.entity.get_id_financial_asset()
    
    def get_default_execute(self):

        return self.entity.get_default_execute()
    
    def init_add_repository(self,id_cronjobs,date):

        return {
            'id':id_cronjobs,
            'date':date,
            'condition':self.get_condition(),
            'id_api':self.get_id_api(),
            'id_financial_asset':self.get_id_financial_asset(),
            'default_execute':self.get_default_execute()
        }
    
    def add(self,id_cronjobs,date):

        data = self.init_add_repository(id_cronjobs,date)

        return self.add_repository(data)