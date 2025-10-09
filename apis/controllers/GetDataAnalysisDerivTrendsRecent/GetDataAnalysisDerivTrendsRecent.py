from django.db import connection

import apis.services.dates.ServicesDates as ServicesDate
import apis.services.events.ServicesEvents as ServicesEvents
import apis.services.cronjobs.ServicesCronjobs as ServicesCronjobs
import apis.services.api.ServicesApi as ServicesApi
import apis.services.smtp.ServicesSmtp as ServicesSmtp
import apis.services.shedule.ServicesShedule as ServicesShedule
import apis.services.checktrendsrecent.ServicesCkeckTrendsRecent as ServicesCkeckTrendsRecent
import apis.services.managerdays.ServicesManagerDays as ServicesManagerDays
import apis.services.methodologytrendsrecent.ServicesMethodologyTrendsRecent as ServicesMethodologyTrendsRecent
import apis.services.indicators.ServicesIndicators as ServicesIndicators
import apis.services.entrysresults.ServicesEntrysResults as ServicesEntrysResults
import apis.services.entrys.ServicesEntrys as ServicesEntrys
import apis.services.cronjobs.ServicesCronjobs as ServicesCronjobs
import apis.services.platform.ServicesPlatform as ServicesPlatform  
import apis.services.indicatorsentrys.ServicesIndicatorsEntrys as ServicesIndicatorsEntrys
import apis.services.movements.ServicesMovements as ServicesMovements
import apis.services.telegram.ServicesTelegram as ServicesTelegram
import apis.services.deriv.ServicesDeriv as ServicesDeriv   

class ControllerGetDataAnalysisDerivTrendRecent: 

    cursor = None

    ServicesDates = None

    ServicesEvents = None

    ServicesCronjobs = None

    ServicesApi = None

    ServicesSmtp = None

    ServicesShedule = None

    ServicesCkeckTrendsRecent = None

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

    ServicesDeriv = None

    def __init__(self):

        self.initialize_services()

        self.initialize_check_trends_services_interns()

    def initialize_services(self):

        self.ServicesDates = ServicesDate.ServicesDate()

        self.ServicesEvents = ServicesEvents.ServicesEvents()

        self.ServicesCronjobs = ServicesCronjobs.ServicesCronjobs()

        self.ServicesApi = ServicesApi.ServicesApi()

        self.ServicesSmtp = ServicesSmtp.ServicesSmtp()

        self.ServicesShedule = ServicesShedule.ServicesShedule()

        self.ServicesCkeckTrendsRecent = ServicesCkeckTrendsRecent.ServicesCkeckTrendsRecent()

        self.ServicesManagerDays = ServicesManagerDays.ServicesManagerDays()

        self.ServicesMethodologyTrendsRecent = ServicesMethodologyTrendsRecent.ServicesMethodologyTrendsRecent()

        self.ServicesIndicators = ServicesIndicators.ServicesIndicators()

        self.ServicesEntrysResults = ServicesEntrysResults.ServicesEntrysResults()

        self.ServicesEntrys = ServicesEntrys.ServicesEntrys()

        self.ServicesPlatform = ServicesPlatform.ServicesPlatform()

        self.ServicesIndicatorsEntrys = ServicesIndicatorsEntrys.ServicesIndicatorsEntrys()

        self.ServicesMovements = ServicesMovements.ServicesMovements()

        self.ServicesTelegram = ServicesTelegram.ServicesTelegram()

        self.ServicesDeriv = ServicesDeriv.ServicesDeriv()

    def initialize_check_trends_services_interns(self):

        self.ServicesEvents.init_services_dates(self.ServicesDates)

        self.ServicesCkeckTrendsRecent.init_services_manager_days(self.ServicesManagerDays)

        self.ServicesCkeckTrendsRecent.init_services_methodology_trends_recent(self.ServicesMethodologyTrendsRecent)

        self.ServicesCkeckTrendsRecent.init_services_indicators(self.ServicesIndicators)

        self.ServicesCkeckTrendsRecent.init_services_entrys_results(self.ServicesEntrysResults)

        self.ServicesCkeckTrendsRecent.init_services_entrys(self.ServicesEntrys)

        self.ServicesCkeckTrendsRecent.init_services_cronjobs(self.ServicesCronjobs)

        self.ServicesCkeckTrendsRecent.init_services_platform(self.ServicesPlatform)

        self.ServicesCkeckTrendsRecent.init_services_indicators_entrys(self.ServicesIndicatorsEntrys)

        self.ServicesCkeckTrendsRecent.init_services_movements(self.ServicesMovements)

        self.ServicesCkeckTrendsRecent.init_services_telegram(self.ServicesTelegram)

        self.ServicesCkeckTrendsRecent.init_services_deriv(self.ServicesDeriv)

    def get_apis_name_trends_recent(self):

        return self.ServicesApi.get_apis_name_trends_recent()

    def set_apis_name_smtp(self):

        return self.ServicesSmtp.set_apis_name(self.get_apis_name_trends_recent())

    async def GetDataAnalysisDerivRecent(self, request):

        now, date, hour, id_cronjobs = self.initialize_request_data()

        resultado = self.verify_services(request, hour, date, id_cronjobs)
        
        if not resultado['status']:
            return resultado       

        resultado_deriv = await self.initialize_deriv_services(date)

        if not resultado_deriv['status']:
            return resultado_deriv  

        await self.process_deriv_services()

        return self.finalize_request(now, id_cronjobs)

    def initialize_request_data(self):

        now = self.ServicesDates.get_current_utc5()

        date = self.ServicesDates.get_current_date(now)

        hour = self.ServicesDates.get_current_hour(now)

        self.ServicesDates.set_start_date()

        self.set_apis_name_smtp()

        self.ServicesEvents.set_events_field('start_endpoint', self.ServicesDates.get_current_date_mil_dynamic())

        id_cronjobs = self.ServicesCronjobs.generate_cronjobs_id()

        return now, date, hour, id_cronjobs
    
    def get_tokens(self):

        return self.ServicesDeriv.get_tokens_orion()
    
    def init_tokens_asignado(self,account):

        self.ServicesDeriv.init_tokens_asignado(account)

        return True

    async def initialize_deriv_services(self, date):

        self.ServicesEvents.set_events_field('init_endpoint', self.ServicesDates.get_current_date_mil_dynamic())

        tokens = self.get_tokens()

        self.init_tokens_asignado(tokens)

        result = await self.ServicesCkeckTrendsRecent.init()

        if not result['status']:

            return result

        self.ServicesEvents.set_events_field('init_broker', self.ServicesDates.get_current_date_mil_dynamic())

        await self.ServicesCkeckTrendsRecent.set_balance(self.ServicesDates.get_day())

        self.ServicesEvents.set_events_field('config_broker', self.ServicesDates.get_current_date_mil_dynamic())

        self.ServicesCkeckTrendsRecent.init_services_events(self.ServicesEvents)

        self.ServicesCkeckTrendsRecent.init_services_dates(self.ServicesDates)

        return {'status': True, 'message': 'Initialization successful'}

    async def process_deriv_services(self):

        await self.ServicesCkeckTrendsRecent.loops()

        await self.ServicesCkeckTrendsRecent.closed()

    def generate_diferences_events(self):

        return self.ServicesEvents.generate_diferences_events()
    
    def get_events(self):

        return self.ServicesEvents.get_events()
    
    def add_events(self, details, differences, id_cronjobs):

        return self.ServicesEvents.add_events(details, differences, id_cronjobs)

    def finalize_request(self, now, id_cronjobs):

        now = self.ServicesDates.get_current_utc5()

        self.ServicesDates.set_end_date()

        self.add_events(self.get_events(), self.generate_diferences_events(), id_cronjobs)
        
        return self.ServicesCronjobs.set_ejecution(self.ServicesDates.get_current_date(now), self.ServicesDates.get_time_execution(), id_cronjobs)

    def verify_services(self, request, hour, date, id_cronjobs):

        servicios_a_verificar = [
            lambda: self.ServicesShedule.get_shedule_result(hour),
            lambda: self.ServicesApi.get_api_result(),
            lambda: self.ServicesCronjobs.add_trends_recent(id_cronjobs, date)
        ]

        for servicio in servicios_a_verificar:

            resultado = servicio() if callable(servicio) else servicio

            if not resultado['status']:

                error_message = resultado.get('message') or resultado.get('msj') or 'Error desconocido en verificación de servicios'               
                self.ServicesSmtp.send_notification_email(date, error_message)
                
                return resultado

        return {'status': True}
