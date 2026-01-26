import apis.services.dates.ServicesDates as ServicesDate
from apis.services.managerdays.ServicesManagerDays import ServicesManagerDays
import apis.services.smtp.ServicesSmtp as ServicesSmtp
import apis.services.events.ServicesEvents as ServicesEvents
import apis.services.cronjobs.ServicesCronjobs as ServicesCronjobs
import apis.services.shedule.ServicesShedule as ServicesShedule
import apis.services.api.ServicesApi as ServicesApi
import apis.services.checktrendsminusrecent.ServicesCheckTrendsMinusRecent as ServicesCheckTrendsMinusRecent
import apis.services.deriv.ServicesDeriv as ServicesDeriv
import apis.services.managerdays.ServicesManagerDays as ServicesManagerDays
import apis.services.indicators.ServicesIndicators as ServicesIndicators
import apis.services.entrysresults.ServicesEntrysResults as ServicesEntrysResults
import apis.services.movements.ServicesMovements as ServicesMovements
import apis.services.platform.ServicesPlatform as ServicesPlatform
import apis.services.entrys.ServicesEntrys as ServicesEntrys
import apis.services.indicatorsentrys.ServicesIndicatorsEntrys as ServicesIndicatorsEntrys
import apis.services.telegram.ServicesTelegram as ServicesTelegram
import apis.services.methodologytrendsminusrecent.ServicesMethodologyTrendsMinusRecent as ServicesMethodologyTrendsMinusRecent

class ControllerGetDataAnalysisDerivTrendsMinusRecent:

    ServicesDates = None

    ServicesSmtp = None

    ServicesEvents = None

    ServicesCronjobs = None

    ServicesShedule = None

    ServicesApi = None

    ServicesCheckTrendsMinusRecent = None

    ServicesMethodologyTrendsMinusRecent = None

    ServicesDeriv = None

    ServicesManagerDays = None

    ServicesIndicators = None

    ServicesEntrysResults = None

    ServicesMovements = None

    ServicesPlatform = None

    ServicesEntrys = None

    ServicesIndicatorsEntrys = None

    ServicesTelegram = None

    def __init__(self):

        self.init_services()

        self.init_services_intern()

    def init_services(self):

        self.ServicesDates = ServicesDate.ServicesDate()

        self.ServicesEvents = ServicesEvents.ServicesEvents()

        self.ServicesCronjobs = ServicesCronjobs.ServicesCronjobs()

        self.ServicesShedule = ServicesShedule.ServicesShedule()

        self.ServicesApi = ServicesApi.ServicesApi()

        self.ServicesSmtp = ServicesSmtp.ServicesSmtp()

        self.ServicesCheckTrendsMinusRecent = ServicesCheckTrendsMinusRecent.ServicesCheckTrendsMinusRecent()

        self.ServicesDeriv = ServicesDeriv.ServicesDeriv()

        self.ServicesMethodologyTrendsMinusRecent = ServicesMethodologyTrendsMinusRecent.ServicesMethodologyTrendsMinusRecent()

        self.ServicesManagerDays = ServicesManagerDays.ServicesManagerDays()

        self.ServicesIndicators = ServicesIndicators.ServicesIndicators()   

        self.ServicesEntrysResults = ServicesEntrysResults.ServicesEntrysResults()

        self.ServicesMovements = ServicesMovements.ServicesMovements()

        self.ServicesPlatform = ServicesPlatform.ServicesPlatform()  

        self.ServicesEntrys = ServicesEntrys.ServicesEntrys()

        self.ServicesIndicatorsEntrys = ServicesIndicatorsEntrys.ServicesIndicatorsEntrys() 

        self.ServicesTelegram = ServicesTelegram.ServicesTelegram()

        return True
    
    def init_services_intern(self):

        self.ServicesEvents.init_services_dates(self.ServicesDates)

        self.ServicesCheckTrendsMinusRecent.init_services_deriv(self.ServicesDeriv)

        self.ServicesCheckTrendsMinusRecent.init_services_methodology_trends_minus_recent(self.ServicesMethodologyTrendsMinusRecent)

        self.ServicesCheckTrendsMinusRecent.init_services_manager_days(self.ServicesManagerDays)

        self.ServicesCheckTrendsMinusRecent.init_services_indicators(self.ServicesIndicators)

        self.ServicesCheckTrendsMinusRecent.init_services_entrys_results(self.ServicesEntrysResults)

        self.ServicesCheckTrendsMinusRecent.init_services_movements(self.ServicesMovements)

        self.ServicesCheckTrendsMinusRecent.init_services_platform(self.ServicesPlatform)

        self.ServicesCheckTrendsMinusRecent.init_services_entrys(self.ServicesEntrys)

        self.ServicesCheckTrendsMinusRecent.init_services_indicators_entrys(self.ServicesIndicatorsEntrys)

        self.ServicesCheckTrendsMinusRecent.init_services_cronjobs(self.ServicesCronjobs)

        self.ServicesCheckTrendsMinusRecent.init_services_telegram(self.ServicesTelegram)

        return True
    
    def generate_diferences_events(self):

        return self.ServicesEvents.generate_diferences_events()
    
    def get_events(self):

        return self.ServicesEvents.get_events()

    def get_apis_name_trends_minus_recent(self):

        return self.ServicesApi.get_apis_name_trends_minus_recent()

    def set_apis_name_smtp(self):

        return self.ServicesSmtp.set_apis_name(self.get_apis_name_trends_minus_recent())

    def initialize_request_data(self):

        now = self.ServicesDates.get_current_utc5()

        date = self.ServicesDates.get_current_date(now)

        hour = self.ServicesDates.get_current_hour(now)

        self.ServicesDates.set_start_date()

        self.set_apis_name_smtp()

        self.ServicesEvents.set_events_field('start_endpoint', self.ServicesDates.get_current_date_mil_dynamic())

        id_cronjobs = self.ServicesCronjobs.generate_cronjobs_id()

        return now, date, hour, id_cronjobs
    
    def verify_services(self, request, hour, date, id_cronjobs):

        servicios_a_verificar = [
            lambda: self.ServicesShedule.get_shedule_result(hour),
            lambda: self.ServicesApi.get_api_result(),
            lambda: self.ServicesCronjobs.add_trends_minus_recent(id_cronjobs, date)
        ]

        for servicio in servicios_a_verificar:

            resultado = servicio() if callable(servicio) else servicio

            if not resultado['status']:

                error_message = resultado.get('message') or resultado.get('msj') or 'Error desconocido en verificación de servicios'               
                self.ServicesSmtp.send_notification_email(date, error_message)
                
                return resultado

        return {'status': True}
    
    def get_tokens(self):

        return self.ServicesDeriv.get_tokens_ursa_minor()
    
    def init_tokens_asignado(self,account):

        self.ServicesDeriv.init_tokens_asignado(account)

        return True
    
    async def initialize_deriv_services(self, date):

        self.ServicesEvents.set_events_field('init_endpoint', self.ServicesDates.get_current_date_mil_dynamic())

        tokens = self.get_tokens()

        self.init_tokens_asignado(tokens)

        result = await self.ServicesCheckTrendsMinusRecent.init()

        if not result['status']:

            return result

        self.ServicesEvents.set_events_field('init_broker', self.ServicesDates.get_current_date_mil_dynamic())

        await self.ServicesCheckTrendsMinusRecent.set_balance(self.ServicesDates.get_day())

        self.ServicesEvents.set_events_field('config_broker', self.ServicesDates.get_current_date_mil_dynamic())

        self.ServicesCheckTrendsMinusRecent.init_services_events(self.ServicesEvents)

        self.ServicesCheckTrendsMinusRecent.init_services_dates(self.ServicesDates)

        return {'status': True, 'message': 'Initialization successful'}

    async def process_deriv_services(self):

        await self.ServicesCheckTrendsMinusRecent.loops()

        await self.ServicesCheckTrendsMinusRecent.closed()

    def finalize_request(self, now, id_cronjobs):

        now = self.ServicesDates.get_current_utc5()

        self.ServicesDates.set_end_date()

        self.add_events(self.get_events(), self.generate_diferences_events(), id_cronjobs)

        return self.ServicesCronjobs.set_ejecution(self.ServicesDates.get_current_date(now), self.ServicesDates.get_time_execution(), id_cronjobs)
    
    def add_events(self, details, differences, id_cronjobs):

        return self.ServicesEvents.add_events(details, differences, id_cronjobs)

    async def GetDataAnalysisDerivMinusRecent(self, request):
    
        now, date, hour, id_cronjobs = self.initialize_request_data()

        resultado = self.verify_services(request, hour, date, id_cronjobs)

        if not resultado['status']:
            self.ServicesSmtp.send_notification_email(date, resultado['message'])  # ← añade esto si lo deseas
            return resultado
        
        resultado_deriv = await self.initialize_deriv_services(date)
        if not resultado_deriv['status']:
            self.ServicesSmtp.send_notification_email(date, resultado_deriv.get('message', 'Error al inicializar Deriv'))
            return resultado_deriv

        await self.process_deriv_services()

        return self.finalize_request(now, id_cronjobs)

