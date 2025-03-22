from unittest import TestCase, mock

import unittest

import apis.test.services.checktrendsexpansive.services.ServicesTestCheckTrendsExpansive as ServicesTestCheckTrendsExpansive

import apis.services.checktrendsexpansive.ServicesCheckTrendsExpansive as ServicesCheckTrendsExpansive
import apis.services.methodologytrendsexpansive.ServicesMethodologyTrendsExpansive as ServicesMethodologyTrendsExpansive
import apis.services.movements.ServicesMovements as ServicesMovements
import apis.services.deriv.ServicesDeriv as ServicesDeriv
import apis.services.managerdays.ServicesManagerDays as ServicesManagerDays
import apis.services.dates.ServicesDates as ServicesDates
import apis.services.cronjobs.ServicesCronjobs as ServicesCronjobs
import apis.services.platform.ServicesPlatform as ServicesPlatform

class TestCheckTrendsExpansive(unittest.IsolatedAsyncioTestCase):

    ServicesTestCheckTrendsExpansive = None

    ServicesCheckTrendsExpansive = None

    ServicesMethodologyTrendsExpansive = None

    ServicesMovements = None

    ServicesDeriv = None

    ServicesManagerDays = None

    ServicesDates = None

    ServicesCronjobs = None

    ServicesPlatform = None

    def setUp(self):
            
        self.init_services()

        self.init_services_internal()

        self.ServicesCronjobs.set_id_cronjobs("000497e5e7cc401fb6022257c7b7ca80")

        self.ServicesManagerDays.set_money(2)

    def init_services(self):

        self.ServicesTestCheckTrendsExpansive = ServicesTestCheckTrendsExpansive.ServicesTestCheckTrendsExpansive()

        self.ServicesCheckTrendsExpansive = ServicesCheckTrendsExpansive.ServicesCheckTrendsExpansive()

        self.ServicesMethodologyTrendsExpansive = ServicesMethodologyTrendsExpansive.ServicesMethodologyTrendsExpansive()

        self.ServicesMovements = ServicesMovements.ServicesMovements()

        self.ServicesDeriv = ServicesDeriv.ServicesDeriv()

        self.ServicesManagerDays = ServicesManagerDays.ServicesManagerDays()

        self.ServicesDates = ServicesDates.ServicesDate()

        self.ServicesCronjobs = ServicesCronjobs.ServicesCronjobs()

        self.ServicesPlatform = ServicesPlatform.ServicesPlatform()

    def init_services_internal(self):

        self.ServicesCheckTrendsExpansive.init_services_methodology_trendsExpansive(self.ServicesMethodologyTrendsExpansive)

        self.ServicesCheckTrendsExpansive.init_services_movements(self.ServicesMovements)

        self.ServicesCheckTrendsExpansive.init_services_deriv(self.ServicesDeriv)

        self.ServicesCheckTrendsExpansive.init_services_manager_days(self.ServicesManagerDays)  

        self.ServicesCheckTrendsExpansive.init_services_dates(self.ServicesDates)

        self.ServicesCheckTrendsExpansive.init_services_cronjobs(self.ServicesCronjobs)

        self.ServicesCheckTrendsExpansive.init_services_platform(self.ServicesPlatform)

    def get_data_entrys_true(self):

        return self.ServicesTestCheckTrendsExpansive.get_data_entry_true()
    
    def get_data_indicators(self):

        return self.ServicesTestCheckTrendsExpansive.get_data_indicators()
    
    def get_data_candles(self):

        return self.ServicesTestCheckTrendsExpansive.get_data_candles()   

    def add_entry_persistence_profit(self):

        data = self.get_data_entrys_true()

        data_indicators =  self.get_data_indicators()

        self.ServicesCheckTrendsExpansive.add_result_indicators(data_indicators)

        data_candles = self.get_data_candles()

        result = self.ServicesCheckTrendsExpansive.add_entry_persistence(data,data_candles)

        print("services:", result)  