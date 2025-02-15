from unittest import TestCase, mock

import unittest

import apis.test.services.deriv.services.ServicesTestServicesDeriv as ServicesTestServicesDeriv

import apis.services.deriv.ServicesDeriv as ServicesDeriv

import apis.services.methodologytrends.ServicesMethodologyTrends as ServicesMethodologyTrends

import apis.services.managerdays.ServicesManagerDays as ServicesManagerDays

import apis.services.entrys.ServicesEntrys as ServicesEntrys

import apis.services.dates.ServicesDates as ServicesDate

import apis.services.cronjobs.ServicesCronjobs as ServicesCronjobs

import apis.services.platform.ServicesPlatform as ServicesPlatform

import apis.services.indicatorsentrys.ServicesIndicatorsEntrys as ServicesIndicatorsEntrys

import apis.services.movements.ServicesMovements as ServicesMovements 

import apis.services.entrysresults.ServicesEntrysResults as ServicesEntrysResults

import apis.services.telegram.ServicesTelegram as ServicesTelegram

class TestServicesDeriv(unittest.IsolatedAsyncioTestCase):

    ServicesTestServicesDeriv = None
    
    Services = None

    ServicesMethodologyTrends = None

    ServicesEntrys = None

    ServicesManagerDays = None

    ServicesDates = None

    ServicesCronjobs = None

    ServicesPlatform = None

    ServicesIndicatorsEntrys = None

    ServicesMovements = None

    ServicesEntrysResults = None

    ServicesTelegram = None

    def setUp(self):

        self.ServicesTestServicesDeriv = ServicesTestServicesDeriv.ServicesTestServicesDeriv()

        self.Services = ServicesDeriv.ServicesDeriv()

        self.ServicesMethodologyTrends = ServicesMethodologyTrends.ServicesMethodologyTrends()

        self.ServicesEntrys = ServicesEntrys.ServicesEntrys()

        self.ServicesManagerDays = ServicesManagerDays.ServicesManagerDays()  

        self.ServicesDates = ServicesDate.ServicesDate()  

        self.ServicesCronjobs = ServicesCronjobs.ServicesCronjobs()

        self.ServicesPlatform = ServicesPlatform.ServicesPlatform()

        self.ServicesIndicatorsEntrys = ServicesIndicatorsEntrys.ServicesIndicatorsEntrys()

        self.ServicesMovements = ServicesMovements.ServicesMovements()

        self.ServicesEntrysResults = ServicesEntrysResults.ServicesEntrysResults()

        self.ServicesTelegram = ServicesTelegram.ServicesTelegram()
        
        self.ServicesCronjobs.set_id_cronjobs("000497e5e7cc401fb6022257c7b7ca80")

        self.ServicesManagerDays.set_money(2)

        self.Services.init_services_methodology_trends(self.ServicesMethodologyTrends)

        self.Services.init_services_entrys(self.ServicesEntrys)

        self.Services.init_services_manager_days(self.ServicesManagerDays)

        self.Services.init_services_dates(self.ServicesDates)

        self.Services.init_services_cronjobs(self.ServicesCronjobs)

        self.Services.init_services_platform(self.ServicesPlatform) 

        self.Services.init_services_indicators_entrys(self.ServicesIndicatorsEntrys)   

        self.Services.init_services_movements(self.ServicesMovements)  

        self.Services.init_services_entrys_results(self.ServicesEntrysResults) 

        self.Services.init_services_telegram(self.ServicesTelegram)
    
    def get_data_entrys_true(self):

        return self.ServicesTestServicesDeriv.get_data_entry_true()
    
    def get_data_entrys_false(self):

        return self.ServicesTestServicesDeriv.get_data_entry_false()

    def get_data_candles(self):

        return self.ServicesTestServicesDeriv.get_data_candles()    
    
    def get_data_indicators(self):

        return self.ServicesTestServicesDeriv.get_data_indicators()

    def add_entry_persistence_profit(self):

        data = self.get_data_entrys_true()

        data_indicators =  self.get_data_indicators()

        self.Services.add_result_indicators(data_indicators)

        data_candles = self.get_data_candles()

        result = self.Services.add_entry_persistence(data,data_candles)

        print("services:", result)

        return True
    
    def add_entry_persistence_false(self):

        data = self.get_data_entrys_false()

        data_indicators =  self.get_data_indicators()

        self.Services.add_result_indicators(data_indicators)

        data_candles = self.get_data_candles()

        result = self.Services.add_entry_persistence(data,data_candles)

        print("services:", result)

        return True