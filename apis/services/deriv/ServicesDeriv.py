import apis.entities.deriv.EntityDeriv as EntityDeriv

class ServicesDeriv():

    entity = None

    ServicesManagerDays = None

    def __init__(self):

        self.entity = EntityDeriv.EntityDeriv()

    def init_services_manager_days(self, value):

        self.ServicesManagerDays = value

        return True
    
    def get_type_manager_days(self,day):

        return self.ServicesManagerDays.get_type_manager_days(day)

    async def init(self):

        return await self.entity.init()
    
    async def closed(self):

        return await self.entity.closed()
    
    def check_mode(self,day):

        return self.get_type_manager_days(day)
    
    async def check_broker(self,mode):

        return await self.entity.check(mode)
    
    async def set_balance(self,day):

        result = self.check_mode(day)

        if result:

            return await self.check_broker(result)

        return True