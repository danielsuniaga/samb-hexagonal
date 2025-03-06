from unittest import TestCase, mock

import apis.services.checktrends.ServicesCkeckTrends as ServicesCkeckTrends
import apis.services.methodologytrends.ServicesMethodologyTrends as ServicesMethodologyTrends
import apis.services.managerdays.ServicesManagerDays as ServicesManagerDays

class TestCheckTrends(TestCase):

    ServicesCkeckTrends = None

    ServicesMethodologyTrends = None

    ServicesManagerDays = None  

    def setUp(self):

        self.init_services()

        self.init_services_intern()

    def init_services(self):

        self.ServicesCkeckTrends = ServicesCkeckTrends.ServicesCkeckTrends()

        self.ServicesMethodologyTrends = ServicesMethodologyTrends.ServicesMethodologyTrends()

        self.ServicesManagerDays = ServicesManagerDays.ServicesManagerDays()

        return True
    
    def init_services_intern(self):

        self.ServicesCkeckTrends.init_services_methodology_trends(self.ServicesMethodologyTrends)

        self.ServicesCkeckTrends.init_services_manager_days(self.ServicesManagerDays)
    
    def test_get_type_manager_days(self):

        day = 6

        result = self.ServicesCkeckTrends.get_type_manager_days(day)

        print(result)

        return True