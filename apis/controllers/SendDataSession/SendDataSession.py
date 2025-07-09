import apis.services.senddatasession.ServicesSendDataSession as ServicesSendDataSession

import apis.services.entrys.ServicesEntrys as ServicesEntrys

import apis.services.indicatorsentrys.ServicesIndicatorsEntrys as ServicesIndicatorsEntrys

import apis.services.sendentrys.ServicesSendEntrys as ServicesSendEntrys

import apis.services.dates.ServicesDates as ServicesDates

import apis.services.indicators.ServicesIndicators as ServicesIndicators

import apis.services.telegram.ServicesTelegram as ServicesTelegram

import apis.services.movements.ServicesMovements as ServicesMovements

class ControllerSendDataSession:

    ServicesDataSession = None

    ServicesEntrys = None

    ServicesIndicatorsEntrys = None

    ServicesSendEntrys = None

    ServicesDates = None

    ServicesIndicators = None

    ServicesTelegram = None

    ServicesMovements = None

    def __init__(self):

        self.init_services()

        self.init_services_intern()

    def init_services(self):

        self.ServicesDataSession = ServicesSendDataSession.ServicesSendDataSession()

        self.ServicesEntrys = ServicesEntrys.ServicesEntrys()

        self.ServicesIndicatorsEntrys = ServicesIndicatorsEntrys.ServicesIndicatorsEntrys()

        self.ServicesSendEntrys = ServicesSendEntrys.ServicesSendEntrys()

        self.ServicesDates = ServicesDates.ServicesDate()

        self.ServicesIndicators = ServicesIndicators.ServicesIndicators()

        self.ServicesTelegram = ServicesTelegram.ServicesTelegram()

        self.ServicesMovements = ServicesMovements.ServicesMovements()

        return True
    
    def init_services_intern(self):

        self.ServicesSendEntrys.init_services_dates(self.ServicesDates)

        self.ServicesDataSession.init_services_entrys(self.ServicesEntrys)

        self.ServicesDataSession.init_services_indicators_entrys(self.ServicesIndicatorsEntrys)

        self.ServicesDataSession.init_services_send_entrys(self.ServicesSendEntrys)

        self.ServicesDataSession.init_services_indicators(self.ServicesIndicators)

        self.ServicesDataSession.init_services_telegram(self.ServicesTelegram)

        self.ServicesDataSession.init_services_movements(self.ServicesMovements)

        return True
    
    def send(self):

        return self.ServicesDataSession.send() 

    def send_data(self):

        return self.send() 