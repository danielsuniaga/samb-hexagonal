import apis.services.dates.ServicesDates as ServicesDate
import apis.services.events.ServicesEvents as ServicesEvents
import apis.services.cronjobs.ServicesCronjobs as ServicesCronjobs
import apis.services.shedule.ServicesShedule as ServicesShedule
import apis.services.api.ServicesApi as ServicesApi
import apis.services.smtp.ServicesSmtp as ServicesSmtp  
import apis.services.checktrendsexpansive.ServicesCheckTrendsExpansive as ServicesCheckTrendsExpansive
import apis.services.deriv.ServicesDeriv as ServicesDeriv
import apis.services.methodologytrendsexpansive.ServicesMethodologyTrendsExpansive as ServicesMethodologyTrendsExpansive
import apis.services.managerdays.ServicesManagerDays as ServicesManagerDays
import apis.services.indicators.ServicesIndicators as ServicesIndicators
import apis.services.entrysresults.ServicesEntrysResults as ServicesEntrysResults
import apis.services.movements.ServicesMovements as ServicesMovements
import apis.services.platform.ServicesPlatform as ServicesPlatform
import apis.services.entrys.ServicesEntrys as ServicesEntrys
import apis.services.indicatorsentrys.ServicesIndicatorsEntrys as ServicesIndicatorsEntrys
import apis.services.telegram.ServicesTelegram as ServicesTelegram

class ControllerGetDataAnalysisDerivTrendsExpansive: 

    ServicesDates = None

    ServicesEvents = None

    ServicesCronjobs = None

    ServicesShedule = None

    ServicesApi = None

    ServicesSmtp = None

    ServicesCheckTrendsExpansive = None

    ServicesDeriv = None

    ServicesMethodologyTrendsExpansive = None

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

        self.ServicesCheckTrendsExpansive = ServicesCheckTrendsExpansive.ServicesCheckTrendsExpansive()

        self.ServicesDeriv = ServicesDeriv.ServicesDeriv()

        self.ServicesMethodologyTrendsExpansive = ServicesMethodologyTrendsExpansive.ServicesMethodologyTrendsExpansive()

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

        self.ServicesCheckTrendsExpansive.init_services_deriv(self.ServicesDeriv)

        self.ServicesCheckTrendsExpansive.init_services_methodology_trendsExpansive(self.ServicesMethodologyTrendsExpansive)

        self.ServicesCheckTrendsExpansive.init_services_manager_days(self.ServicesManagerDays)

        self.ServicesCheckTrendsExpansive.init_services_indicators(self.ServicesIndicators)

        self.ServicesCheckTrendsExpansive.init_services_entrys_results(self.ServicesEntrysResults)

        self.ServicesCheckTrendsExpansive.init_services_movements(self.ServicesMovements)

        self.ServicesCheckTrendsExpansive.init_services_platform(self.ServicesPlatform)

        self.ServicesCheckTrendsExpansive.init_services_entrys(self.ServicesEntrys)

        self.ServicesCheckTrendsExpansive.init_services_indicators_entrys(self.ServicesIndicatorsEntrys)    

        self.ServicesCheckTrendsExpansive.init_services_cronjobs(self.ServicesCronjobs)

        self.ServicesCheckTrendsExpansive.init_services_telegram(self.ServicesTelegram)

        return True
    
    def get_apis_name_trends_expansive(self):

        return self.ServicesApi.get_apis_name_trends_expansive()

    def set_apis_name_smtp(self):

        return self.ServicesSmtp.set_apis_name(self.get_apis_name_trends_expansive())


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
            lambda: self.ServicesCronjobs.add_trends_expansive(id_cronjobs, date)
        ]

        for servicio in servicios_a_verificar:

            resultado = servicio() if callable(servicio) else servicio

            if not resultado['status']:

                self.ServicesSmtp.send_notification_email(date, resultado['message'])
                
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

        result = await self.ServicesCheckTrendsExpansive.init()

        if not result['status']:

            return result

        self.ServicesEvents.set_events_field('init_broker', self.ServicesDates.get_current_date_mil_dynamic())

        await self.ServicesCheckTrendsExpansive.set_balance(self.ServicesDates.get_day())

        self.ServicesEvents.set_events_field('config_broker', self.ServicesDates.get_current_date_mil_dynamic())

        self.ServicesCheckTrendsExpansive.init_services_events(self.ServicesEvents)

        self.ServicesCheckTrendsExpansive.init_services_dates(self.ServicesDates)

        return {'status': True, 'message': 'Initialization successful'}
    
    async def process_deriv_services(self):

        await self.ServicesCheckTrendsExpansive.loops()

        await self.ServicesCheckTrendsExpansive.closed()

    def finalize_request(self, now, id_cronjobs):

        now = self.ServicesDates.get_current_utc5()

        self.ServicesDates.set_end_date()

        return self.ServicesCronjobs.set_ejecution(self.ServicesDates.get_current_date(now), self.ServicesDates.get_time_execution(), id_cronjobs)

    async def GetDataAnalysisDerivExpansive(self, request):

        now, date, hour, id_cronjobs = self.initialize_request_data()

        resultado = self.verify_services(request, hour, date, id_cronjobs)
        
        if not resultado['status']:

            return 
        
        resultado_deriv = await self.initialize_deriv_services(date)

        if not resultado_deriv['status']:

            return self.ServicesSmtp.send_notification_email(date, resultado_deriv['message'])  
        
        await self.process_deriv_services()

        return self.finalize_request(now, id_cronjobs)