from unittest import TestCase, mock

import apis.services.checkwma.ServicesCheckWMA as ServicesCheckWMA
import apis.services.methodologywma.ServicesMethodologyWMA as ServicesMethodologyWMA
import apis.services.movements.ServicesMovements as ServicesMovements
import apis.services.deriv.ServicesDeriv as ServicesDeriv
import apis.services.managerdays.ServicesManagerDays as ServicesManagerDays
import apis.services.cronjobs.ServicesCronjobs as ServicesCronjobs
import apis.services.platform.ServicesPlatform as ServicesPlatform
import apis.services.dates.ServicesDates as ServicesDates
import apis.services.entrys.ServicesEntrys as ServicesEntrys
import apis.services.indicatorsentrys.ServicesIndicatorsEntrys as ServicesIndicatorsEntrys
import apis.services.entrysresults.ServicesEntrysResults as ServicesEntrysResults

import apis.test.services.checkwma.services.ServicesTestCheckWMA as ServicesTestCheckWMA    

import unittest

class TestCheckWMA(unittest.IsolatedAsyncioTestCase):

    ServicesTestCheckWMA = None

    ServicesCheckWMA = None

    ServicesMethodologyWMA = None

    ServicesMovements = None

    ServicesDeriv = None

    ServicesManagerDays = None

    ServicesCronjobs = None

    ServicesPlatform = None

    ServicesDates = None

    ServicesEntrys = None

    ServicesIndicatorsEntrys = None

    ServicesEntrysResults = None

    def setUp(self):

        self.init_services()

        self.init_services_intenal()

        self.ServicesCronjobs.set_id_cronjobs("000497e5e7cc401fb6022257c7b7ca80")

        self.ServicesManagerDays.set_money(2)

    def init_services(self):

        self.ServicesTestCheckWMA = ServicesTestCheckWMA.ServicesTestCheckWMA()

        self.ServicesCheckWMA = ServicesCheckWMA.ServicesCheckWMA()

        self.ServicesMethodologyWMA = ServicesMethodologyWMA.ServicesMethodologyWMA()

        self.ServicesMovements = ServicesMovements.ServicesMovements()

        self.ServicesDeriv = ServicesDeriv.ServicesDeriv()

        self.ServicesManagerDays = ServicesManagerDays.ServicesManagerDays()

        self.ServicesCronjobs = ServicesCronjobs.ServicesCronjobs()

        self.ServicesPlatform = ServicesPlatform.ServicesPlatform()

        self.ServicesDates = ServicesDates.ServicesDate()

        self.ServicesEntrys = ServicesEntrys.ServicesEntrys()

        self.ServicesIndicatorsEntrys = ServicesIndicatorsEntrys.ServicesIndicatorsEntrys()

        self.ServicesEntrysResults = ServicesEntrysResults.ServicesEntrysResults()

        return True
    
    def init_services_intenal(self):

        self.ServicesCheckWMA.init_services_methodology_wma(self.ServicesMethodologyWMA)

        self.ServicesCheckWMA.init_services_movements(self.ServicesMovements)

        self.ServicesCheckWMA.init_services_deriv(self.ServicesDeriv)   

        self.ServicesCheckWMA.init_services_manager_days(self.ServicesManagerDays)

        self.ServicesCheckWMA.init_services_cronjobs(self.ServicesCronjobs)

        self.ServicesCheckWMA.init_services_platform(self.ServicesPlatform)

        self.ServicesCheckWMA.init_services_dates(self.ServicesDates)

        self.ServicesCheckWMA.init_services_entrys(self.ServicesEntrys) 

        self.ServicesCheckWMA.init_services_indicators_entrys(self.ServicesIndicatorsEntrys)  

        self.ServicesCheckWMA.init_services_entrys_results(self.ServicesEntrysResults)  

        return True

    def get_data_entrys_true(self):

        return self.ServicesTestCheckWMA.get_data_entry_true()
    
    def get_data_entrys_false(self):

        return self.ServicesTestCheckWMA.get_data_entry_false()
    
    def get_data_indicators(self):

        return self.ServicesTestCheckWMA.get_data_indicators()
    
    def set_indicators_methodology(self,indicator):

        return self.ServicesCheckWMA.set_indicators_methodology(indicator)
    
    def get_data_candles(self):

        return self.ServicesTestCheckWMA.get_data_candles()   

    def add_entry_persistence_profit(self):

        data = self.get_data_entrys_true()

        data_indicators =  self.get_data_indicators()

        self.set_indicators_methodology(data_indicators)

        data_candles = self.get_data_candles()

        result = self.ServicesCheckWMA.add_entry_persistence(data,data_candles)

        print(result)

        return True
    
    def add_entry_persistence_false(self):

        data = self.get_data_entrys_false()

        data_indicators =  self.get_data_indicators()

        self.set_indicators_methodology(data_indicators)

        data_candles = self.get_data_candles()

        result = self.ServicesCheckWMA.add_entry_persistence(data,data_candles)

        print("services:", result)

        return True

