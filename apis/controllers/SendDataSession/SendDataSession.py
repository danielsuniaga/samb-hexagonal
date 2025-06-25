import apis.services.senddatasession.ServicesSendDataSession as ServicesSendDataSession

import apis.services.entrys.ServicesEntrys as ServicesEntrys

import apis.services.indicatorsentrys.ServicesIndicatorsEntrys as ServicesIndicatorsEntrys

import apis.services.sendentrys.ServicesSendEntrys as ServicesSendEntrys

import apis.services.dates.ServicesDates as ServicesDates

class ControllerSendDataSession:

    ServicesDataSession = None

    ServicesEntrys = None

    ServicesIndicatorsEntrys = None

    ServicesSendEntrys = None

    ServicesDates = None

    def __init__(self):

        self.init_services()

        self.init_services_intern()

    def init_services(self):

        self.ServicesDataSession = ServicesSendDataSession.ServicesSendDataSession()

        self.ServicesEntrys = ServicesEntrys.ServicesEntrys()

        self.ServicesIndicatorsEntrys = ServicesIndicatorsEntrys.ServicesIndicatorsEntrys()

        self.ServicesSendEntrys = ServicesSendEntrys.ServicesSendEntrys()

        self.ServicesDates = ServicesDates.ServicesDate()

        return True
    
    def init_services_intern(self):

        self.ServicesSendEntrys.init_services_dates(self.ServicesDates)

        self.ServicesDataSession.init_services_entrys(self.ServicesEntrys)

        self.ServicesDataSession.init_services_indicators_entrys(self.ServicesIndicatorsEntrys)

        self.ServicesDataSession.init_services_send_entrys(self.ServicesSendEntrys)

        return True
    
    def send(self):

        return self.ServicesDataSession.send() 

    def send_data(self):

        return self.send() 