import apis.entities.deriv.EntityDeriv as EntityDeriv

class ServicesDeriv():

    entity = None

    ServicesManagerDays = None

    ServicesEvents = None

    ServicesDates = None

    ServicesMethodologyTrends = None

    ServicesIndicators = None

    ServicesEntrysResults = None

    ServicesEntrys = None

    ServicesCronjobs = None

    ServicesPlatform = None

    ServicesIndicatorsEntrys = None 

    ServicesMovements = None

    def __init__(self):

        self.entity = EntityDeriv.EntityDeriv()

    def init_services_movements(self,value):

        self.ServicesMovements = value

        return True 

    def init_services_indicators_entrys(self,value):

        self.ServicesIndicatorsEntrys = value

        return True

    def init_services_platform(self,value):

        self.ServicesPlatform = value

        return True

    def init_services_cronjobs(self,value):
        
        self.ServicesCronjobs = value

        return True
    
    def get_id_cronjobs(self):

        return self.ServicesCronjobs.get_id_cronjobs()

    def init_services_entrys(self,value):

        self.ServicesEntrys = value

        return True
    
    def init_services_entrys_results(self,value):

        self.ServicesEntrysResults = value

        return True
    
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
    
    def get_current_date_hour(self):

        return self.ServicesDates.get_current_date_hour()
    
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
    
    def get_current_date_only(self):

        return self.ServicesDates.get_current_date_only()
    
    def get_events(self):

        return self.ServicesEvents.get_events()
    
    async def get_candles(self):

        return await self.entity.get_candles()
    
    def check_candles(self,candles):

        return self.ServicesMethodologyTrends.check_candles(candles)
    
    def get_rsi(self,candles):

        return self.ServicesIndicators.generate_rsi(candles)
    
    def check_rsi(self,rsi):

        return self.ServicesMethodologyTrends.check_rsi(rsi)
    
    def get_sma_short_services(self):

        return self.ServicesIndicators.get_sma_short()
    
    def get_sma_short(self,candles):

        indicators = self.get_sma_short_services()

        return self.ServicesIndicators.generate_sma(candles,indicators)
    
    def check_sma(self,sma,last_candle):

        return self.ServicesMethodologyTrends.check_sma(sma,last_candle)
    
    def get_candle_last(self,candle):

        return self.ServicesIndicators.get_candles_last(candle)
    
    def get_sma_long(self,candles):

        indicators = self.ServicesIndicators.get_sma_long()

        return self.ServicesIndicators.generate_sma(candles,indicators)
    
    def init_data_indicators(self,candles):

        return {
            'rsi':self.get_rsi(candles),
            'sma_short':self.get_sma_short(candles),
            'sma_long':self.get_sma_long(candles),
            'last_candle':self.get_candle_last(candles),
        }
    
    def init_result_indicators(self,indicators):

        return {
            'rsi':self.check_rsi(indicators['rsi']),
            'sma_short':self.check_sma(indicators['sma_short'],indicators['last_candle']),
            'sma_long':self.check_sma(indicators['sma_long'],indicators['last_candle']),
        }
    
    def check_result_indicators(self,result_indicators):

        return self.ServicesMethodologyTrends.check_result_indicators(result_indicators)
    
    def add_result_indicators(self,result_indicators):

        return self.ServicesMethodologyTrends.add_indicator(result_indicators)
    
    def check_indicators(self,result,candles):

        if not result:

            return False
        
        data_indicators = self.init_data_indicators(candles)

        result_indicators = self.init_result_indicators(data_indicators)

        self.add_result_indicators(data_indicators)
        
        return self.check_result_indicators(result_indicators)
    
    def sum_entrys_dates(self):

        return self.ServicesEntrysResults.get_sums_entrys_date(self.get_current_date_only())
    
    def get_profit(self):

        return self.ServicesManagerDays.get_profit()
    
    def get_loss(self): 

        return self.ServicesManagerDays.get_loss()
    
    def init_data_monetary_filter(self):

        return {
            'sum_entrys_dates':self.sum_entrys_dates(),
            'profit':self.get_profit(),
            'loss':self.get_loss(),
        }
    
    def check_monetary_filter_services(self,result):

        return self.ServicesMethodologyTrends.check_monetary_filters(result)
        
    def check_monetary_filter(self,result):

        if not result:

            return False
        
        data = self.init_data_monetary_filter()

        return self.check_monetary_filter_services(data)
    
    def get_money(self):

        return self.ServicesManagerDays.get_money()
    
    def get_type_entry(self):

        return self.ServicesMethodologyTrends.get_type_entry_positions()
    
    def get_duration(self):
        
        return self.entity.get_duration()
    
    def get_duration_unit(self):    

        return self.entity.get_duration_unit()
    
    def init_data_add_entry(self):

        return {
            'amount':int(self.get_money()),
            'contract_type':self.get_type_entry(),
            'duration':int(self.get_duration()),
            'duration_unit':self.get_duration_unit(),
            'symbol':self.get_par()
        }
    
    async def add_entry_broker(self,result):

        if not result:

            return False

        return await self.entity.add_entry(self.init_data_add_entry())

    def set_result_positions(self,result):

        return self.ServicesMethodologyTrends.set_result_entrys(result)
    
    def set_candles_positions(self,candles):

        return self.ServicesMethodologyTrends.set_result_candles(candles)
    
    def add_entrys(self,result):

        return self.ServicesEntrys.add_entrys(result)
    
    def add_result_positions_mode(self,data,mode):

        return self.entity.add_result_positions(data,mode,'mode')
    
    def get_mode(self):

        return self.ServicesManagerDays.get_mode()
    
    def get_candle_removed(self):

        return self.ServicesMethodologyTrends.get_candle_removed()
    
    def add_result_positions_candle_analisys(self,data,candle):

        return self.entity.add_result_positions(data,candle,'candle_analisys')
    
    def get_condition_entry(self):

        return self.ServicesMethodologyTrends.get_condition_entry()
    
    def add_result_positions_condition_entry(self,data,condition):
        
        return self.entity.add_result_positions(data,condition,'condition_entry')
    
    def add_result_positions_amount(self,data,amount):

        return self.entity.add_result_positions(data,amount,'amount')
    
    def add_result_positions_current_date(self,data,date):

        return self.entity.add_result_positions(data,date,'current_date')
    
    def add_result_positions_id_cronjobs(self,data,id_cronjobs):

        return self.entity.add_result_positions(data,id_cronjobs,'id_cronjobs') 

    
    def get_re_platform(self):

        return self.ServicesPlatform.get_re_platform_deriv()
    
    def add_result_positions_re_platform(self,data,re_platform):    

        return self.entity.add_result_positions(data,re_platform,'re_entry_platform')
    
    def init_set_result_positions(self,result):

        return [
            (self.add_result_positions_mode, self.get_mode()),
            (self.add_result_positions_candle_analisys, self.get_candle_removed()),
            (self.add_result_positions_condition_entry, self.get_condition_entry()),
            (self.add_result_positions_amount, self.get_money()),
            (self.add_result_positions_current_date, self.get_current_date_hour()),
            (self.add_result_positions_id_cronjobs, self.get_id_cronjobs()),
            (self.add_result_positions_re_platform, self.get_re_platform())
        ]
    
    def set_result_positions(self,result):

        result_positions_methods = self.init_set_result_positions(result)

        for method, value in result_positions_methods:

            result = method(result, value)

        return result
    
    def get_indicators(self):

        return self.ServicesMethodologyTrends.get_indicators()
    
    def get_data_entrys(self):
        
        return self.ServicesEntrys.get_data_entity()

    def add_result_positions_data_entrys(self,result,data):

        return self.entity.add_result_positions(result,data,'data_entry')
    
    def set_result_indicators(self,result):

        result = self.add_result_positions_current_date(result,self.get_current_date_hour())

        result = self.add_result_positions_data_entrys(result,self.get_data_entrys())

        return result
    
    def add_entrys_results_persistence(self,data):

        return True
    
    def add_movements_persistence(self,data):

        result = self.ServicesMovements.add_persistence(data)

        if not result['status']:

            return False

        return True
    
    def add_indicators_entrys_persistence(self):

        data = self.set_result_indicators(self.get_indicators())

        result = self.ServicesIndicatorsEntrys.add_persistence(data)

        if not result['status']:

            return False

        return self.add_movements_persistence(data)
    
    def set_candles_movements(self,candles):
        
        return self.ServicesMovements.set_candles(candles)
    
    def add_entry_persistence(self,result,candles):

        if not result:

            return False
        
        self.set_candles_movements(candles)
        
        result = self.set_result_positions(result)
        
        self.set_result_positions(result)

        self.set_candles_positions(candles)

        result = self.add_entrys(result)

        if not result['status']:
            
            return False
        
        return self.add_indicators_entrys_persistence()
    
    async def loops(self):

        self.set_events_field('init_loop',self.get_current_date_mil_dynamic())

        result_candles = await self.get_candles()

        self.set_events_field('get_candles',self.get_current_date_mil_dynamic())

        result = self.check_candles(result_candles)

        self.set_events_field('check_candles',self.get_current_date_mil_dynamic())

        result = self.check_indicators(result,result_candles)

        self.set_events_field('generate_indicators',self.get_current_date_mil_dynamic())

        result = self.check_monetary_filter(result)

        self.set_events_field('get_filter_monetary',self.get_current_date_mil_dynamic())

        result = await self.add_entry_broker(result)

        self.set_events_field('add_positions_brokers',self.get_current_date_mil_dynamic())

        result = self.add_entry_persistence(result,result_candles)

        return result