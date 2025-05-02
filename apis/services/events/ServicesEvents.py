import apis.entities.events.EntityEvents as EntityEvents

import apis.repositories.events.RepositoryEvents as RepositoryEvents

class ServicesEvents():

    entity = None

    repository = None

    ServicesDates = None

    def __init__(self):

        self.entity = EntityEvents.EntityEvents()

        self.repository = RepositoryEvents.RepositoryEvents()

    def get_current_date_hour(self):

        return self.ServicesDates.get_current_date_hour()

    def init_services_dates(self, value):

        self.ServicesDates = value

        return True

    def set_events_field(self,field,value):

        return self.entity.set_events_field(field,value)
    
    def get_events(self):

        return self.entity.get_events()
    
    def generate_diferences_events(self):

        return self.entity.generate_diferences_events()
    
    def generate_id(self):

        return self.entity.generate_id()
    
    def get_config_condition(self):

        return self.entity.get_config_condition()
    
    def init_data_add_events(self, details, differences, id_cronjobs):

        dates = self.get_current_date_hour()

        return {
            'id': self.generate_id(),
            'details': details,
            'difference': differences,
            'registration_date': dates,
            'update_cate': dates,
            'state': self.get_config_condition(),
            'id_samb_cronjobs_id': id_cronjobs
        }
    
    def add_events_repository(self,data):

        return self.repository.add(data)
    
    def add_events(self,details,diferrences,id_cronjobs):

        data = self.init_data_add_events(details,diferrences,id_cronjobs)

        return self.add_events_repository(data)