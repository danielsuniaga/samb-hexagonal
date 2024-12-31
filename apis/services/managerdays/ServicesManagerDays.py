import apis.entities.managerdays.EntityManagerDays as EntityManagerDays

import apis.repositories.ManagerDays.RepositoryManagerDays as RepositoryManagerDays

class ServicesManagerDays():

    entity = None

    repository = None

    def __init__(self):

        self.entity = EntityManagerDays.EntityManagerDays()

        self.repository = RepositoryManagerDays.RepositoryManagerDays()

    def get_type_manager_days_repository(self,day):

        return self.repository.get_type_manager_day(day)
    
    def set_money(self,value):

        return self.entity.set_money(value)
    
    def set_profit(self,value):

        return self.entity.set_profit(value)
    
    def set_loss(self,value):

        return self.entity.set_loss(value)
    
    def set_data_manager(self,data):

        self.set_money(data['money'])

        self.set_profit(data['profit'])

        self.set_loss(data['loss'])

        return True
    
    def get_mode(self):

        return self.entity.get_mode()
    
    def check_mode_operativity(self,data):

        if(data['type']==self.get_mode()):

            return False   

        return True

    def get_type_manager_days(self,day):

        result = self.repository.get_type_manager_day(day)

        if not result['status']:

            return result
    
        self.set_data_manager(result['data'])

        return self.check_mode_operativity(result['data'])
        
        
