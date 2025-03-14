class ServicesCheckWMA:

    ServicesDeriv = None

    ServicesMethodologyWMA = None

    ServicesManagerDays = None

    ServicesEvents = None

    ServicesDates = None

    ServicesIndicators = None

    def init_services_indicators(self,value):

        self.ServicesIndicators = value

        return True

    def init_services_dates(self,value):

        self.ServicesDates = value  

        return True

    def init_services_events(self,value):

        self.ServicesEvents = value

        return True

    def init_services_manager_days(self,value):

        self.ServicesManagerDays = value

        return True

    def init_services_methodology_wma(self,value):

        self.ServicesMethodologyWMA = value

        return True

    def init_services_deriv(self,value):

        self.ServicesDeriv = value

        return True
    
    def get_id_methodology(self):

        return self.ServicesMethodologyWMA.get_id()
    
    async def init(self):

        return await self.ServicesDeriv.init()
    
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
    
    def get_current_date_mil_dynamic(self):

        return self.ServicesDates.get_current_date_mil_dynamic()
    
    def init_data_set_events_field_result(self,date,result=0):

        return date+" Result: "+str(result)+" "
    
    def set_events_field(self,field,value):

        return self.ServicesEvents.set_events_field(field,value)
    
    async def closed(self):

        return await self.ServicesDeriv.closed()
    
    async def get_candles(self):

        return await self.ServicesDeriv.get_candles()
    
    def generate_candles(self,candles):

        return self.ServicesMethodologyWMA.generate_candles(candles)
    
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
    
    def set_indicators_methodology(self,indicators):

        return self.ServicesMethodologyWMA.set_indicators(indicators)
    
    def get_indicators(self,result,candles):

        if not result:

            return False
        
        data_indicators = self.init_data_indicators(candles)
        
        self.set_indicators_methodology(data_indicators)

        return True
    
    def check_candles(self,result):

        if not result:

            return False
        
        return self.ServicesMethodologyWMA.check_candles()
    
    def get_indicators_methodology(self):

        return self.ServicesMethodologyWMA.get_indicators()
    
    # def check_rsi(self,rsi):

    #     return self.ServicesMethodologyWMA.check_rsi(rsi)
    
    # def init_result_indicators(self,indicators):

    #     return {
    #         'rsi':self.check_rsi(indicators['rsi']),
    #         'sma_short':self.check_sma(indicators['sma_short'],indicators['last_candle']),
    #         'sma_long':self.check_sma(indicators['sma_long'],indicators['last_candle']),
    #     }
    
    def check_indicators(self,result):

        if not result:

            return False
        
        data_indicators = self.get_indicators_methodology()

        # result_indicators = self.init_result_indicators(data_indicators)

        print("data_indicators",data_indicators)
        
        return True
    
    async def loops(self):

        self.set_events_field('init_loop',self.init_data_set_events_field_result(self.get_current_date_mil_dynamic()))
        
        result_candles = await self.get_candles()

        result = self.generate_candles(result_candles)

        result = self.get_indicators(result,result_candles)

        self.set_events_field('get_candles',self.init_data_set_events_field_result(self.get_current_date_mil_dynamic()))

        result = self.check_candles(result)

        self.set_events_field('check_candles',self.init_data_set_events_field_result(self.get_current_date_mil_dynamic(),result))
        
        result = self.check_indicators(result)
        
        print("result",result)

        # self.set_events_field('get_filter_monetary',self.init_data_set_events_field_result(self.get_current_date_mil_dynamic(),result))

        # result = await self.add_entry_broker(result)

        # self.set_events_field('add_positions_brokers',self.init_data_set_events_field_result(self.get_current_date_mil_dynamic(),result))

        # result = self.add_entry_persistence(result,result_candles)

        # self.set_events_field('add_persistence',self.init_data_set_events_field_result(self.get_current_date_mil_dynamic(),result))

        # self.send_report_management(result)

        return True
    