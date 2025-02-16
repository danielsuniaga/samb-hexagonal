import apis.entities.deriv.EntityDeriv as EntityDeriv

class ServicesDeriv():

    entity = None

    def __init__(self):

        self.entity = EntityDeriv.EntityDeriv()
    
    async def init(self):

        return await self.entity.init()
    
    async def closed(self):

        return await self.entity.closed()
    
    async def check(self,mode):

        return await self.entity.check(mode)
    
    def get_par(self):

        return self.entity.get_par()
    
    async def get_candles(self):

        return await self.entity.get_candles()
    
    def get_duration(self):
        
        return self.entity.get_duration()
    
    def get_duration_unit(self):    

        return self.entity.get_duration_unit()
    
    async def add_entry(self,data):

        return await self.entity.add_entry(data)
    
    def add_result_positions_mode(self,data,mode):

        return self.entity.add_result_positions(data,mode,'mode')