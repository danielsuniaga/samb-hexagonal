class ServicesCheckTrendsExpansive():

    ServicesDeriv = None

    ServicesMethodologyTrendsExpansive = None

    ServicesManagerDays = None

    ServicesEvents = None

    ServicesDates = None    

    ServicesIndicators = None

    ServicesEntrysResults = None

    ServicesMovements = None

    ServicesCronjobs = None

    ServicesPlatform = None

    def init_services_platform(self,value):

        self.ServicesPlatform = value

        return True

    def init_services_cronjobs(self,value):

        self.ServicesCronjobs = value

        return True

    def init_services_movements(self,value):

        self.ServicesMovements = value

        return True

    def init_services_entrys_results(self,value):

        self.ServicesEntrysResults = value

        return True

    def init_services_indicators(self,value):

        self.ServicesIndicators = value

        return True

    def init_services_events(self,value):

        self.ServicesEvents = value

        return True
    
    def init_services_dates(self,value):

        self.ServicesDates = value

        return True

    def init_services_manager_days(self,value):

        self.ServicesManagerDays = value

        return True

    def init_services_methodology_trendsExpansive(self,value):

        self.ServicesMethodologyTrendsExpansive = value

        return True

    def init_services_deriv(self,value):

        self.ServicesDeriv = value

        return True

    async def init(self):

        return await self.ServicesDeriv.init()
    
    def get_id_methodology(self):

        return self.ServicesMethodologyTrendsExpansive.get_id()
    
    def get_type_manager_days(self,day):

        id_methodology = self.get_id_methodology()

        return self.ServicesManagerDays.get_type_manager_days(day,id_methodology)
    
    def check_mode(self,day):

        return self.get_type_manager_days(day)
    
    async def check_broker(self,mode):

        return await self.ServicesDeriv.check(mode)
    
    async def set_balance(self,day):

        result = self.check_mode(day)

        if result:

            return await self.check_broker(result)

        return True
    
    async def closed(self):

        return await self.ServicesDeriv.closed()
    
    def get_current_date_mil_dynamic(self):

        return self.ServicesDates.get_current_date_mil_dynamic()
    
    def init_data_set_events_field_result(self,date,result=0):

        return date+" Result: "+str(result)+" "
    
    def set_events_field(self,field,value):

        return self.ServicesEvents.set_events_field(field,value)
    
    async def get_candles(self):

        return await self.ServicesDeriv.get_candles()
    
    def check_candles(self,candles):

        return self.ServicesMethodologyTrendsExpansive.check_candles(candles)
    
    def get_rsi(self,candles):

        return self.ServicesIndicators.generate_rsi(candles)
    
    def get_sma_short_services(self):

        return self.ServicesIndicators.get_sma_short()
    
    def get_sma_short(self,candles):

        indicators = self.get_sma_short_services()

        return self.ServicesIndicators.generate_sma(candles,indicators)
    
    def get_sma_long(self,candles):

        indicators = self.ServicesIndicators.get_sma_long()

        return self.ServicesIndicators.generate_sma(candles,indicators)
    
    def get_candle_last(self,candle):

        return self.ServicesIndicators.get_candles_last(candle)
    
    def init_data_indicators(self,candles):

        return {
            'rsi':self.get_rsi(candles),
            'sma_short':self.get_sma_short(candles),
            'sma_long':self.get_sma_long(candles),
            'last_candle':self.get_candle_last(candles),
        }
    
    def check_rsi(self,rsi):

        return self.ServicesMethodologyTrendsExpansive.check_rsi(rsi)
    
    def check_sma(self,sma,last_candle):

        return self.ServicesMethodologyTrendsExpansive.check_sma(sma,last_candle)
    
    def init_result_indicators(self,indicators):

        return {
            'rsi':self.check_rsi(indicators['rsi']),
            'sma_short':self.check_sma(indicators['sma_short'],indicators['last_candle']),
            'sma_long':self.check_sma(indicators['sma_long'],indicators['last_candle']),
        }

    def add_result_indicators(self,result_indicators):

        return self.ServicesMethodologyTrendsExpansive.add_indicator(result_indicators)  

    def check_result_indicators(self,result_indicators):

        return self.ServicesMethodologyTrendsExpansive.check_result_indicators(result_indicators)  
    
    def check_indicators(self,result,candles):

        if not result:

            return False
        
        data_indicators = self.init_data_indicators(candles)

        result_indicators = self.init_result_indicators(data_indicators)

        self.add_result_indicators(data_indicators)
        
        return self.check_result_indicators(result_indicators)
    
    def check_monetary_filter_services(self,result):

        return self.ServicesMethodologyTrendsExpansive.check_monetary_filters(result)
    
    def get_current_date_only(self):

        return self.ServicesDates.get_current_date_only()
    
    def sum_entrys_dates(self):

        id_methodology = self.get_id_methodology()

        return self.ServicesEntrysResults.get_sums_entrys_date(self.get_current_date_only(),id_methodology)
    
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
    
    def check_monetary_filter(self,result):

        if not result:

            return False
        
        data = self.init_data_monetary_filter()

        return self.check_monetary_filter_services(data)
    
    def get_money(self):

        return self.ServicesManagerDays.get_money()
    
    def get_type_entry(self):

        return self.ServicesMethodologyTrendsExpansive.get_type_entry_positions()
    
    def get_duration(self):
        
        return self.ServicesDeriv.get_duration()
    
    def get_duration_unit(self):    

        return self.ServicesDeriv.get_duration_unit()
    
    def get_par(self):

        return self.ServicesDeriv.get_par()
    
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
        
        result = self.init_data_add_entry()

        return await self.ServicesDeriv.add_entry(self.init_data_add_entry())
    
    def set_candles_movements(self,candles):
        
        return self.ServicesMovements.set_candles(candles)
    
    def set_candles_positions(self,candles):

        return self.ServicesMethodologyTrendsExpansive.set_result_candles(candles)
    
    def add_result_positions_mode(self,data,mode):

        return self.ServicesDeriv.add_result_positions_mode(data,mode)
    
    def get_mode(self):

        return self.ServicesManagerDays.get_mode()
    
    def add_result_positions_candle_analisys(self,data,candle):

        return self.ServicesDeriv.add_result_positions_candle_analisys(data,candle)
    
    def get_candle_removed(self):

        return self.ServicesMethodologyTrendsExpansive.get_candle_removed()
    
    def add_result_positions_condition_entry(self,data,condition):
        
        return self.ServicesDeriv.add_result_positions_condition_entry(data,condition)
    
    def get_condition_entry(self):

        return self.ServicesMethodologyTrendsExpansive.get_condition_entry()
    
    def add_result_positions_amount(self,data,amount):

        return self.ServicesDeriv.add_result_positions_amount(data,amount)
    
    def add_result_positions_current_date(self,data,date):

        return self.ServicesDeriv.add_result_positions_current_date(data,date)
    
    def get_current_date_hour(self):

        return self.ServicesDates.get_current_date_hour()
    
    def add_result_positions_id_cronjobs(self,data,id_cronjobs):

        return self.ServicesDeriv.add_result_positions_id_cronjobs(data,id_cronjobs)
    
    def get_id_cronjobs(self):

        return self.ServicesCronjobs.get_id_cronjobs()
    
    def add_result_positions_re_platform(self,data,re_platform):    

        return self.ServicesDeriv.add_result_positions_re_platform(data,re_platform)
    
    def get_re_platform(self):

        return self.ServicesPlatform.get_re_platform_deriv()
    
    def add_result_positions_id_methodology(self,data,id_methodology):

        return self.ServicesDeriv.add_result_positions_id_methodology(data,id_methodology) 
    
    def init_set_result_positions(self,result):

        return [
            (self.add_result_positions_mode, self.get_mode()),
            (self.add_result_positions_candle_analisys, self.get_candle_removed()),
            (self.add_result_positions_condition_entry, self.get_condition_entry()),
            (self.add_result_positions_amount, self.get_money()),
            (self.add_result_positions_current_date, self.get_current_date_hour()),
            (self.add_result_positions_id_cronjobs, self.get_id_cronjobs()),
            (self.add_result_positions_re_platform, self.get_re_platform()),
            (self.add_result_positions_id_methodology, self.get_id_methodology()),
        ]
    
    def set_result_positions(self,result):

        result_positions_methods = self.init_set_result_positions(result)

        for method, value in result_positions_methods:

            result = method(result, value)

        return result
    
    def set_result_positions_entity(self,result):

        return self.ServicesMethodologyTrendsExpansive.set_result_entrys(result)
    
    def add_entry_persistence(self,result,candles):

        if not result:

            return False
        
        self.set_candles_movements(candles)
        
        result = self.set_result_positions(result)
        
        # self.set_result_positions_entity(result)

        return True

        self.set_candles_positions(candles)

        result = self.add_entrys(result)

        if not result['status']:
            
            return False
        
        return self.add_indicators_entrys_persistence()
    
    async def loops(self):

        self.set_events_field('init_loop',self.init_data_set_events_field_result(self.get_current_date_mil_dynamic()))
        
        result_candles = await self.get_candles()

        self.set_events_field('get_candles',self.init_data_set_events_field_result(self.get_current_date_mil_dynamic()))
        
        result = self.check_candles(result_candles)

        self.set_events_field('check_candles',self.init_data_set_events_field_result(self.get_current_date_mil_dynamic(),result))
        
        result = self.check_indicators(result,result_candles)
        
        self.set_events_field('generate_indicators',self.init_data_set_events_field_result(self.get_current_date_mil_dynamic(),result))

        result = self.check_monetary_filter(result)

        self.set_events_field('get_filter_monetary',self.init_data_set_events_field_result(self.get_current_date_mil_dynamic(),result))

        result = await self.add_entry_broker(result)

        self.set_events_field('add_positions_brokers',self.init_data_set_events_field_result(self.get_current_date_mil_dynamic(),result))

        result = self.add_entry_persistence(result,result_candles)

        # self.set_events_field('add_persistence',self.init_data_set_events_field_result(self.get_current_date_mil_dynamic(),result))

        # self.send_report_management(result)

        return True