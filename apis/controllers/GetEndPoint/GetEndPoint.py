
import apis.services.framework.ServicesFramework as ServicesFramework
import apis.services.dates.ServicesDates as ServicesDate
import apis.services.smtp.ServicesSmtp as ServicesSmtp
import apis.services.api.ServicesApi as ServicesApi

class ControllerGetEndPoint:

    ServicesFramework = None

    ServicesDates = None

    ServicesSmtp = None

    ServicesApi = None

    def __init__(self):

        self.initialize_services()

        self.initialize_services_interns()

    def initialize_services(self):
        
        self.ServicesFramework = ServicesFramework.ServicesFramework()

        self.ServicesDate = ServicesDate.ServicesDate()

        self.ServicesSmtp = ServicesSmtp.ServicesSmtp()

        self.ServicesApi = ServicesApi.ServicesApi()

    def initialize_services_interns(self):

        self.ServicesFramework.init_services_dates(self.ServicesDate)    

    def get_apis_name_endpoints(self):

        return self.ServicesApi.get_apis_name_endpoints()
    
    def set_apis_name_smtp(self):

        return self.ServicesSmtp.set_apis_name(self.get_apis_name_endpoints())

    def initialize_request_data(self):

        self.set_apis_name_smtp()

        return True

    def send_email(self):

        self.initialize_request_data()

        return self.ServicesSmtp.send_notification_email("20250328114400","test")

    async def add_framework(self):

        return await self.ServicesFramework.add()

    async def GetEndPoint(self):

        return await self.add_framework()