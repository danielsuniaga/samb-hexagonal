
import apis.services.framework.ServicesFramework as ServicesFramework

class ControllerGetEndPoint:

    ServicesFramework = None

    def __init__(self):

        self.initialize_services()

    def initialize_services(self):
        
        self.ServicesFramework = ServicesFramework.ServicesFramework()

    def add_framework(self):

        return self.ServicesFramework.add()

    def GetEndPoint(self):

        return self.add_framework()