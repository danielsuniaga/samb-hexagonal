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
    
    def set_mode(self,value,permision_real):

        if not self.check_permission_real(permision_real):

            return self.entity.set_mode(self.get_mode_env())
            
        return self.entity.set_mode(value)
    
    def set_data_manager(self,data):

        self.set_money(data['money'])

        self.set_profit(data['profit'])

        self.set_loss(data['loss'])

        self.set_mode(data['type'],data['permision_real'])

        return True
    
    def get_mode(self):

        return self.entity.get_mode()
    
    def get_profit(self):

        return self.entity.get_profit()
    
    def get_loss(self):

        return self.entity.get_loss()
    
    def get_mode_env(self):

        return self.entity.get_mode_env()
    
    def check_permission_real(self,permision_real):
            
        if(permision_real):
            
            return True
        
        return False
    
    def check_mode_operativity(self,data):

        if not self.check_permission_real(data['permision_real']):

            return False

        if(data['type']==self.get_mode_env()):

            return False   

        return True
    
    def get_type_manager_days_reporting(self,day,id_methodology):

        result = self.repository.get_type_manager_day(day,id_methodology)

        if not result['status']:

            return result

        return result['data']

    def get_type_manager_days(self,day,id_methodology):

        result = self.repository.get_type_manager_day(day,id_methodology)

        if not result['status']:

            return result
    
        self.set_data_manager(result['data'])

        return self.check_mode_operativity(result['data'])
    
    def get_money(self):

        return self.entity.get_money()
        
        
