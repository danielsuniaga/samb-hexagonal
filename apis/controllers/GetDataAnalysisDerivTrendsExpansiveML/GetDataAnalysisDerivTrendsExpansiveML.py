import apis.services.dates.ServicesDates as ServicesDate
import apis.services.events.ServicesEvents as ServicesEvents
import apis.services.cronjobs.ServicesCronjobs as ServicesCronjobs
import apis.services.shedule.ServicesShedule as ServicesShedule
import apis.services.api.ServicesApi as ServicesApi
import apis.services.smtp.ServicesSmtp as ServicesSmtp  
import apis.services.checktrendsexpansiveml.ServicesCheckTrendsExpansiveML as ServicesCheckTrendsExpansiveML
import apis.services.deriv.ServicesDeriv as ServicesDeriv
import apis.services.methodologytrendsexpansiveml.ServicesMethodologyTrendsExpansiveML as ServicesMethodologyTrendsExpansiveML
import apis.services.managerdays.ServicesManagerDays as ServicesManagerDays
import apis.services.indicators.ServicesIndicators as ServicesIndicators
import apis.services.entrysresults.ServicesEntrysResults as ServicesEntrysResults
import apis.services.movements.ServicesMovements as ServicesMovements
import apis.services.platform.ServicesPlatform as ServicesPlatform
import apis.services.entrys.ServicesEntrys as ServicesEntrys
import apis.services.indicatorsentrys.ServicesIndicatorsEntrys as ServicesIndicatorsEntrys
import apis.services.telegram.ServicesTelegram as ServicesTelegram
import apis.services.models.ServicesModels as ServicesModels
import apis.services.methodologys.ServicesMethodologys as ServicesMethodologys
import apis.services.predictmodels.ServicesPredictModels as ServicesPredictModels
import apis.services.entryspredictmodels.ServicesEntrysPredictModels as ServicesEntrysPredictModels

class ControllerGetDataAnalysisDerivTrendsExpansiveML: 

    cursor = None
    ServicesDates = None
    ServicesEvents = None
    ServicesCronjobs = None
    ServicesShedule = None
    ServicesApi = None
    ServicesSmtp = None
    ServicesCheckTrendsExpansiveML = None
    ServicesDeriv = None
    ServicesMethodologyTrendsExpansiveML = None
    ServicesManagerDays = None
    ServicesIndicators = None
    ServicesEntrysResults = None
    ServicesMovements = None
    ServicesPlatform = None
    ServicesEntrys = None
    ServicesIndicatorsEntrys = None
    ServicesTelegram = None
    ServicesModels = None
    ServicesMethodologys = None
    ServicesPredictModels = None
    ServicesEntrysPredictModels = None

    def __init__(self):
        self.initialize_services()
        self.initialize_check_trends_services_interns()

    def initialize_services(self):
        self.ServicesDates = ServicesDate.ServicesDate()
        self.ServicesEvents = ServicesEvents.ServicesEvents()
        self.ServicesCronjobs = ServicesCronjobs.ServicesCronjobs()
        self.ServicesShedule = ServicesShedule.ServicesShedule()
        self.ServicesApi = ServicesApi.ServicesApi()
        self.ServicesSmtp = ServicesSmtp.ServicesSmtp()
        self.ServicesCheckTrendsExpansiveML = ServicesCheckTrendsExpansiveML.ServicesCheckTrendsExpansiveML()
        self.ServicesDeriv = ServicesDeriv.ServicesDeriv()
        self.ServicesMethodologyTrendsExpansiveML = ServicesMethodologyTrendsExpansiveML.ServicesMethodologyTrendsExpansiveML()
        self.ServicesManagerDays = ServicesManagerDays.ServicesManagerDays()
        self.ServicesIndicators = ServicesIndicators.ServicesIndicators()   
        self.ServicesEntrysResults = ServicesEntrysResults.ServicesEntrysResults()
        self.ServicesMovements = ServicesMovements.ServicesMovements()
        self.ServicesPlatform = ServicesPlatform.ServicesPlatform()  
        self.ServicesEntrys = ServicesEntrys.ServicesEntrys()
        self.ServicesIndicatorsEntrys = ServicesIndicatorsEntrys.ServicesIndicatorsEntrys() 
        self.ServicesTelegram = ServicesTelegram.ServicesTelegram()
        self.ServicesModels = ServicesModels.ServicesModels()
        self.ServicesMethodologys = ServicesMethodologys.ServicesMethodologys()
        self.ServicesPredictModels = ServicesPredictModels.ServicesPredictModels()
        self.ServicesEntrysPredictModels = ServicesEntrysPredictModels.ServicesEntrysPredictModels()

    def initialize_check_trends_services_interns(self):
        self.ServicesEvents.init_services_dates(self.ServicesDates)
        self.ServicesEntrysPredictModels.init_services_dates(self.ServicesDates)
        self.ServicesPredictModels.init_services_dates(self.ServicesDates)
        self.ServicesModels.init_services_predict_models(self.ServicesPredictModels)
        
        self.ServicesCheckTrendsExpansiveML.init_services_deriv(self.ServicesDeriv)
        self.ServicesCheckTrendsExpansiveML.init_services_methodology_trends_expansive_ml(self.ServicesMethodologyTrendsExpansiveML)
        self.ServicesCheckTrendsExpansiveML.init_services_manager_days(self.ServicesManagerDays)
        self.ServicesCheckTrendsExpansiveML.init_services_indicators(self.ServicesIndicators)
        self.ServicesCheckTrendsExpansiveML.init_services_entrys_results(self.ServicesEntrysResults)
        self.ServicesCheckTrendsExpansiveML.init_services_movements(self.ServicesMovements)
        self.ServicesCheckTrendsExpansiveML.init_services_platform(self.ServicesPlatform)
        self.ServicesCheckTrendsExpansiveML.init_services_entrys(self.ServicesEntrys)
        self.ServicesCheckTrendsExpansiveML.init_services_indicators_entrys(self.ServicesIndicatorsEntrys)    
        self.ServicesCheckTrendsExpansiveML.init_services_cronjobs(self.ServicesCronjobs)
        self.ServicesCheckTrendsExpansiveML.init_services_telegram(self.ServicesTelegram)
        self.ServicesCheckTrendsExpansiveML.init_services_models(self.ServicesModels)
        self.ServicesCheckTrendsExpansiveML.init_services_methodologys(self.ServicesMethodologys)
        self.ServicesCheckTrendsExpansiveML.init_services_entrys_predict_models(self.ServicesEntrysPredictModels)
    
    def get_apis_name_trends_expansive_ml(self):
        return self.ServicesApi.get_apis_name_trends_expansive_ml()

    def set_apis_name_smtp(self):
        return self.ServicesSmtp.set_apis_name(self.get_apis_name_trends_expansive_ml())

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
        servicios_a_verificar = self.init_verify_services(hour, date, id_cronjobs)
        for servicio_info in servicios_a_verificar:
            resultado = self.execute_service_check(servicio_info)
            if not resultado['status']:
                self.handle_service_error(servicio_info, date, resultado)
                return resultado
        return {'status': True}

    def init_verify_services(self, hour, date, id_cronjobs):
        return [
            {
                'name': 'schedule_service',
                'function': lambda: self.ServicesShedule.get_shedule_result(hour),
                'send_email_on_error': True
            },
            {
                'name': 'api_service',
                'function': lambda: self.ServicesApi.get_api_result(),
                'send_email_on_error': True
            },
            {
                'name': 'cronjobs_service',
                'function': lambda: self.ServicesCronjobs.add_trends_expansive_ml(id_cronjobs, date),
                'send_email_on_error': True
            },
            {
                'name': 'models_service',
                'function': lambda: self.ServicesModels.check_models(),
                'send_email_on_error': False
            }
        ]

    def execute_service_check(self, servicio_info):
        servicio_function = servicio_info['function']
        resultado = servicio_function() if callable(servicio_function) else servicio_function
        return resultado

    def handle_service_error(self, servicio_info, date, resultado):
        if servicio_info.get('send_email_on_error', False):
            self.ServicesSmtp.send_notification_email(date, resultado['message'])
    
    # def get_tokens(self):
    #     return self.ServicesDeriv.get_tokens_ursa_minor()
    
    # def init_tokens_asignado(self, account):
    #     self.ServicesDeriv.init_tokens_asignado(account)
    #     return True
    
    # async def initialize_deriv_services(self, date):
    #     self.ServicesEvents.set_events_field('init_endpoint', self.ServicesDates.get_current_date_mil_dynamic())
    #     tokens = self.get_tokens()
    #     self.init_tokens_asignado(tokens)
    #     result = await self.ServicesCheckTrendsExpansiveML.init()
    #     if not result['status']:
    #         return result
    #     self.ServicesEvents.set_events_field('init_broker', self.ServicesDates.get_current_date_mil_dynamic())
    #     await self.ServicesCheckTrendsExpansiveML.set_balance(self.ServicesDates.get_day())
    #     self.ServicesEvents.set_events_field('config_broker', self.ServicesDates.get_current_date_mil_dynamic())
    #     self.ServicesCheckTrendsExpansiveML.init_services_events(self.ServicesEvents)
    #     self.ServicesCheckTrendsExpansiveML.init_services_dates(self.ServicesDates)
    #     return {'status': True, 'message': 'Initialization successful'}
    
    # async def process_deriv_services(self):
    #     await self.ServicesCheckTrendsExpansiveML.loops()
    #     await self.ServicesCheckTrendsExpansiveML.closed()

    # def generate_diferences_events(self):
    #     return self.ServicesEvents.generate_diferences_events()
    
    # def get_events(self):
    #     return self.ServicesEvents.get_events()
    
    # def add_events(self, details, differences, id_cronjobs):
    #     return self.ServicesEvents.add_events(details, differences, id_cronjobs)

    # def finalize_request(self, now, id_cronjobs):
    #     now = self.ServicesDates.get_current_utc5()
    #     self.ServicesDates.set_end_date()
    #     self.add_events(self.get_events(), self.generate_diferences_events(), id_cronjobs)
    #     return self.ServicesCronjobs.set_ejecution(self.ServicesDates.get_current_date(now), self.ServicesDates.get_time_execution(), id_cronjobs)

    async def GetDataAnalysisDerivExpansiveML(self, request):

        now, date, hour, id_cronjobs = self.initialize_request_data()
        resultado = self.verify_services(request, hour, date, id_cronjobs)
        if not resultado['status']:
            return resultado
        
        return True
        resultado_deriv = await self.initialize_deriv_services(date)
        if not resultado_deriv['status']:
            return self.ServicesSmtp.send_notification_email(date, resultado_deriv['message'])  
        await self.process_deriv_services()
        return self.finalize_request(now, id_cronjobs)
