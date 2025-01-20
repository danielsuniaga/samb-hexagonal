import apis.entities.shedule.EntityShedule as EntityShedule

import apis.repositories.shedule.RepositoryShedule as RepositoryShedule

class ServicesShedule():

    entity = None

    repository = None

    def __init__(self):

        self.entity = EntityShedule.EntityShedule()

        self.repository = RepositoryShedule.RepositoryShedule()

    def get_shedule_permission(self):

        return self.entity.get_shedule_permission()
    
    def get_condition(self):

        return self.entity.get_condition()
    
    def init_get_shedule_result(self,hour):

        return {
            'hour':hour,
            'shedule_permission':self.get_shedule_permission(),
            'condition':self.get_condition()
        }
    
    def get(self,data):

        return self.repository.get(data)

    def get_shedule_result(self,hour):

        data = self.init_get_shedule_result(hour)

        result = self.get(data)

        return result