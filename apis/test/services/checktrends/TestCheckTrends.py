from unittest import TestCase, mock

import apis.services.checktrends.ServicesCkeckTrends as ServicesCkeckTrends
import apis.services.methodologytrends.ServicesMethodologyTrends as ServicesMethodologyTrends
import apis.services.managerdays.ServicesManagerDays as ServicesManagerDays
import apis.services.dates.ServicesDates as ServicesDates
import apis.services.entrysresults.ServicesEntrysResults as ServicesEntrysResults   

class TestCheckTrends(TestCase):

    ServicesCkeckTrends = None

    ServicesMethodologyTrends = None

    ServicesManagerDays = None  

    ServicesDates = None

    ServicesEntrysResults = None

    def setUp(self):

        self.init_services()

        self.init_services_intern()

    def init_services(self):

        self.ServicesCkeckTrends = ServicesCkeckTrends.ServicesCkeckTrends()

        self.ServicesMethodologyTrends = ServicesMethodologyTrends.ServicesMethodologyTrends()

        self.ServicesManagerDays = ServicesManagerDays.ServicesManagerDays()

        self.ServicesDates = ServicesDates.ServicesDate()

        self.ServicesEntrysResults = ServicesEntrysResults.ServicesEntrysResults()  

        return True
    
    def init_services_intern(self):

        self.ServicesCkeckTrends.init_services_methodology_trends(self.ServicesMethodologyTrends)

        self.ServicesCkeckTrends.init_services_manager_days(self.ServicesManagerDays)

        self.ServicesCkeckTrends.init_services_dates(self.ServicesDates)

        self.ServicesCkeckTrends.init_services_entrys_results(self.ServicesEntrysResults)

        return True
    
    def test_get_type_manager_days(self):

        day = 6

        result = self.ServicesCkeckTrends.get_type_manager_days(day)

        print(result)

        return True
    
    def test_sum_entrys_dates(self):

        result = self.ServicesCkeckTrends.sum_entrys_dates()

        print(result)

        return True