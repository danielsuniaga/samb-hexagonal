class ServicesCheckTrendsExpansive():

    ServicesDeriv = None

    ServicesMethodologyTrendsExpansive = None

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

        print('id_methodology',id_methodology)

        return True

        # return self.ServicesManagerDays.get_type_manager_days(day,id_methodology)
    
    def check_mode(self,day):

        return self.get_type_manager_days(day)
    
    async def set_balance(self,day):

        result = self.check_mode(day)

        # if result:

        #     return await self.check_broker(result)

        return True