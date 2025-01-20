
import apis.services.framework.ServicesFramework as ServicesFramework
import apis.services.dates.ServicesDates as ServicesDate

class ControllerGetEndPoint:

    ServicesFramework = None

    ServicesDates = None

    def __init__(self):

        self.initialize_services()

        self.initialize_services_interns()

    def initialize_services(self):
        
        self.ServicesFramework = ServicesFramework.ServicesFramework()

        self.ServicesDate = ServicesDate.ServicesDate()

    def initialize_services_interns(self):

        self.ServicesFramework.init_services_dates(self.ServicesDate)    

    async def add_framework(self):

        return await self.ServicesFramework.add()

    async def GetEndPoint(self):

        return await self.add_framework()