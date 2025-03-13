class ServicesCheckWMA:

    ServicesDeriv = None

    ServvicesMethodologyWMA = None

    ServicesManagerDays = None

    ServicesEvents = None

    ServicesDates = None

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

        self.ServvicesMethodologyWMA = value

        return True

    def init_services_deriv(self,value):

        self.ServicesDeriv = value

        return True
    
    def get_id_methodology(self):

        return self.ServvicesMethodologyWMA.get_id()
    
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
    
    async def loops(self):

        self.set_events_field('init_loop',self.init_data_set_events_field_result(self.get_current_date_mil_dynamic()))
        
        # result_candles = await self.get_candles()

        # self.set_events_field('get_candles',self.init_data_set_events_field_result(self.get_current_date_mil_dynamic()))
        
        # result = self.check_candles(result_candles)

        # self.set_events_field('check_candles',self.init_data_set_events_field_result(self.get_current_date_mil_dynamic(),result))
        
        # result = self.check_indicators(result,result_candles)
        
        # self.set_events_field('generate_indicators',self.init_data_set_events_field_result(self.get_current_date_mil_dynamic(),result))

        # result = self.check_monetary_filter(result)

        # self.set_events_field('get_filter_monetary',self.init_data_set_events_field_result(self.get_current_date_mil_dynamic(),result))

        # result = await self.add_entry_broker(result)

        # self.set_events_field('add_positions_brokers',self.init_data_set_events_field_result(self.get_current_date_mil_dynamic(),result))

        # result = self.add_entry_persistence(result,result_candles)

        # self.set_events_field('add_persistence',self.init_data_set_events_field_result(self.get_current_date_mil_dynamic(),result))

        # self.send_report_management(result)

        return True
    