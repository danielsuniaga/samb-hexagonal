from django.db import connection

import apis.services.dates.ServicesDates as ServicesDate
import apis.services.events.ServicesEvents as ServicesEvents
import apis.services.cronjobs.ServicesCronjobs as ServicesCronjobs
import apis.services.api.ServicesApi as ServicesApi
import apis.services.smtp.ServicesSmtp as ServicesSmtp
import apis.services.shedule.ServicesShedule as ServicesShedule
import apis.services.deriv.ServicesDeriv as ServicesDeriv
import apis.services.managerdays.ServicesManagerDays as ServicesManagerDays
import apis.services.methodologytrends.ServicesMethodologyTrends as ServicesMethodologyTrends
import apis.services.indicators.ServicesIndicators as ServicesIndicators
import apis.services.entrysresults.ServicesEntrysResults as ServicesEntrysResults
import apis.services.entrys.ServicesEntrys as ServicesEntrys
import apis.services.cronjobs.ServicesCronjobs as ServicesCronjobs
import apis.services.platform.ServicesPlatform as ServicesPlatform  
import apis.services.indicatorsentrys.ServicesIndicatorsEntrys as ServicesIndicatorsEntrys
import apis.services.movements.ServicesMovements as ServicesMovements
import apis.services.telegram.ServicesTelegram as ServicesTelegram
class ControllerGetDataAnalysisDeriv: 

    cursor = None

    ServicesDates = None

    ServicesEvents = None

    ServicesCronjobs = None

    ServicesApi = None

    ServicesSmtp = None

    ServicesShedule = None

    ServicesDeriv = None

    ServicesManagerDays = None

    ServicesMethodologyTrends = None

    ServicesIndicators = None

    ServicesEntrysResults = None

    ServicesEntrys = None

    ServicesCronjobs = None

    ServicesPlatform = None

    ServicesIndicatorsEntrys = None

    ServicesMovements = None

    ServicesTelegram = None

    def __init__(self):

        self.initialize_services()

        self.initialize_deriv_services_interns()

    def initialize_services(self):

        self.ServicesDates = ServicesDate.ServicesDate()

        self.ServicesEvents = ServicesEvents.ServicesEvents()

        self.ServicesCronjobs = ServicesCronjobs.ServicesCronjobs()

        self.ServicesApi = ServicesApi.ServicesApi()

        self.ServicesSmtp = ServicesSmtp.ServicesSmtp()

        self.ServicesShedule = ServicesShedule.ServicesShedule()

        self.ServicesDeriv = ServicesDeriv.ServicesDeriv()

        self.ServicesManagerDays = ServicesManagerDays.ServicesManagerDays()

        self.ServicesMethodologyTrends = ServicesMethodologyTrends.ServicesMethodologyTrends()

        self.ServicesIndicators = ServicesIndicators.ServicesIndicators()

        self.ServicesEntrysResults = ServicesEntrysResults.ServicesEntrysResults()

        self.ServicesEntrys = ServicesEntrys.ServicesEntrys()

        self.ServicesPlatform = ServicesPlatform.ServicesPlatform()

        self.ServicesIndicatorsEntrys = ServicesIndicatorsEntrys.ServicesIndicatorsEntrys()

        self.ServicesMovements = ServicesMovements.ServicesMovements()

        self.ServicesTelegram = ServicesTelegram.ServicesTelegram()

    def initialize_deriv_services_interns(self):

        self.ServicesDeriv.init_services_manager_days(self.ServicesManagerDays)

        self.ServicesDeriv.init_services_methodology_trends(self.ServicesMethodologyTrends)

        self.ServicesDeriv.init_services_indicators(self.ServicesIndicators)

        self.ServicesDeriv.init_services_entrys_results(self.ServicesEntrysResults)

        self.ServicesDeriv.init_services_entrys(self.ServicesEntrys)

        self.ServicesDeriv.init_services_cronjobs(self.ServicesCronjobs)

        self.ServicesDeriv.init_services_platform(self.ServicesPlatform)

        self.ServicesDeriv.init_services_indicators_entrys(self.ServicesIndicatorsEntrys)

        self.ServicesDeriv.init_services_movements(self.ServicesMovements)

        self.ServicesDeriv.init_services_telegram(self.ServicesTelegram)

    async def GetDataAnalysisDeriv(self, request):

        now, date, hour, id_cronjobs = self.initialize_request_data()

        resultado = self.verify_services(request, hour, date, id_cronjobs)
        
        if not resultado['status']:

            return resultado

        if not await self.initialize_deriv_services(date):

            return self.ServicesSmtp.send_notification_email(date, "Initialization failed")

        await self.process_deriv_services()

        return self.finalize_request(now, id_cronjobs)

    def initialize_request_data(self):

        now = self.ServicesDates.get_current_utc5()

        date = self.ServicesDates.get_current_date(now)

        hour = self.ServicesDates.get_current_hour(now)

        self.ServicesDates.set_start_date()

        self.ServicesEvents.set_events_field('start_endpoint', self.ServicesDates.get_current_date_mil_dynamic())

        id_cronjobs = self.ServicesCronjobs.generate_cronjobs_id()

        return now, date, hour, id_cronjobs

    async def initialize_deriv_services(self, date):

        self.ServicesEvents.set_events_field('init_endpoint', self.ServicesDates.get_current_date_mil_dynamic())

        result = await self.ServicesDeriv.init()

        if not result['status']:

            return False

        self.ServicesEvents.set_events_field('init_broker', self.ServicesDates.get_current_date_mil_dynamic())

        await self.ServicesDeriv.set_balance(self.ServicesDates.get_day())

        self.ServicesEvents.set_events_field('config_broker', self.ServicesDates.get_current_date_mil_dynamic())

        self.ServicesDeriv.init_services_events(self.ServicesEvents)

        self.ServicesDeriv.init_services_dates(self.ServicesDates)

        return True

    async def process_deriv_services(self):

        await self.ServicesDeriv.loops()

        await self.ServicesDeriv.closed()

    def finalize_request(self, now, id_cronjobs):

        now = self.ServicesDates.get_current_utc5()

        self.ServicesDates.set_end_date()

        return self.ServicesCronjobs.set_ejecution(self.ServicesDates.get_current_date(now), self.ServicesDates.get_time_execution(), id_cronjobs)

    def verify_services(self, request, hour, date, id_cronjobs):

        servicios_a_verificar = [
            lambda: self.ServicesApi.get_api_key(request),
            lambda: self.ServicesShedule.get_shedule_result(hour),
            lambda: self.ServicesApi.get_api_result(),
            lambda: self.ServicesCronjobs.add(id_cronjobs, date)
        ]

        for servicio in servicios_a_verificar:

            resultado = servicio() if callable(servicio) else servicio

            if not resultado['status']:

                self.ServicesSmtp.send_notification_email(date, resultado['message'])
                
                return resultado

        return {'status': True}
