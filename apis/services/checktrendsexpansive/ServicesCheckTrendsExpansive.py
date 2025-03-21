class ServicesCheckTrendsExpansive():

    ServicesDeriv = None

    ServicesMethodologyTrendsExpansive = None

    ServicesManagerDays = None

    ServicesEvents = None

    ServicesDates = None    

    ServicesIndicators = None

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
    
    async def loops(self):

        self.set_events_field('init_loop',self.init_data_set_events_field_result(self.get_current_date_mil_dynamic()))
        
        result_candles = await self.get_candles()

        self.set_events_field('get_candles',self.init_data_set_events_field_result(self.get_current_date_mil_dynamic()))
        
        result = self.check_candles(result_candles)

        self.set_events_field('check_candles',self.init_data_set_events_field_result(self.get_current_date_mil_dynamic(),result))
        
        result = self.check_indicators(result,result_candles)
        
        self.set_events_field('generate_indicators',self.init_data_set_events_field_result(self.get_current_date_mil_dynamic(),result))

        # result = self.check_monetary_filter(result)

        # self.set_events_field('get_filter_monetary',self.init_data_set_events_field_result(self.get_current_date_mil_dynamic(),result))

        # result = await self.add_entry_broker(result)

        # self.set_events_field('add_positions_brokers',self.init_data_set_events_field_result(self.get_current_date_mil_dynamic(),result))

        # result = self.add_entry_persistence(result,result_candles)

        # self.set_events_field('add_persistence',self.init_data_set_events_field_result(self.get_current_date_mil_dynamic(),result))

        # self.send_report_management(result)

        return True