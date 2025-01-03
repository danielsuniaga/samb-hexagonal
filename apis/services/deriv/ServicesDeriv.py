import apis.entities.deriv.EntityDeriv as EntityDeriv

class ServicesDeriv():

    entity = None

    ServicesManagerDays = None

    ServicesEvents = None

    ServicesDates = None

    ServicesMethodologyTrends = None

    ServicesIndicators = None

    def __init__(self):

        self.entity = EntityDeriv.EntityDeriv()

    def init_services_indicators(self,value):

        self.ServicesIndicators = value

        return True

    def init_services_methodology_trends(self,value):

        self.ServicesMethodologyTrends = value

        return True

    def init_services_dates(self,value):

        self.ServicesDates = value

        return True

    def init_services_events(self,value):

        self.ServicesEvents = value

        return True

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
    
    def get_par(self):

        return self.entity.get_par()
    
    def set_events_field(self,field,value):

        return self.ServicesEvents.set_events_field(field,value)

    def get_current_date_mil_dynamic(self):

        return self.ServicesDates.get_current_date_mil_dynamic()
    
    def get_events(self):

        return self.ServicesEvents.get_events()
    
    async def get_candles(self):

        return await self.entity.get_candles()
    
    async def check_candles(self,candles):

        return await self.ServicesMethodologyTrends.check_candles(candles)
    
    async def get_rsi(self,candles):

        return await self.ServicesIndicators.generate_rsi(candles)
    
    async def check_rsi(self,rsi):

        return await self.ServicesMethodologyTrends.check_rsi(rsi)
    
    async def get_sma_short_services(self):

        return self.ServicesIndicators.get_sma_short()
    
    async def get_sma_short(self,candles):

        indicators = await self.get_sma_short_services()

        return await self.ServicesIndicators.generate_sma(candles,indicators)
    
    async def check_indicators(self,result,candles):

        if not result:

            return False
        
        rsi = await self.get_rsi(candles)

        result_rsi = await self.check_rsi(rsi)
        
        sma_short = await self.get_sma_short(candles)

        return True

    async def loops(self):

        self.set_events_field('init_loop',self.get_current_date_mil_dynamic())

        result_candles = await self.get_candles()

        self.set_events_field('get_candles',self.get_current_date_mil_dynamic())

        result = await self.check_candles(result_candles)

        self.set_events_field('check_candles',self.get_current_date_mil_dynamic())

        result = await self.check_indicators(result,result_candles)

        return result