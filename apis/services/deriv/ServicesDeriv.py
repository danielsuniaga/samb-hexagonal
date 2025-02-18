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
    
    def add_result_positions_candle_analisys(self,data,candle):

        return self.entity.add_result_positions(data,candle,'candle_analisys')
    
    def add_result_positions_condition_entry(self,data,condition):
        
        return self.entity.add_result_positions(data,condition,'condition_entry')
    
    def add_result_positions_amount(self,data,amount):

        return self.entity.add_result_positions(data,amount,'amount')
    
    def add_result_positions_current_date(self,data,date):

        return self.entity.add_result_positions(data,date,'current_date')
    
    def add_result_positions_id_cronjobs(self,data,id_cronjobs):

        return self.entity.add_result_positions(data,id_cronjobs,'id_cronjobs')
    
    def add_result_positions_id_methodology(self,data,id_methodology):

        return self.entity.add_result_positions(data,id_methodology,'id_methodology') 
    
    def add_result_positions_re_platform(self,data,re_platform):    

        return self.entity.add_result_positions(data,re_platform,'re_entry_platform')
    
    def add_result_positions_data_entrys(self,result,data):

        return self.entity.add_result_positions(result,data,'data_entry')
    
    def get_duration_seconds(self):

        return self.entity.get_duration_seconds()  