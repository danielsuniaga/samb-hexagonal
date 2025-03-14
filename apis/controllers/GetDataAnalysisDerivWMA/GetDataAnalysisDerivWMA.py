import apis.services.dates.ServicesDates as ServicesDate
import apis.services.events.ServicesEvents as ServicesEvents
import apis.services.cronjobs.ServicesCronjobs as ServicesCronjobs
import apis.services.shedule.ServicesShedule as ServicesShedule
import apis.services.api.ServicesApi as ServicesApi
import apis.services.smtp.ServicesSmtp as ServicesSmtp
import apis.services.deriv.ServicesDeriv as ServicesDeriv
import apis.services.checkwma.ServicesCheckWMA as ServicesCheckWMA
import apis.services.methodologywma.ServicesMethodologyWMA as ServicesMethodologyWMA
import apis.services.managerdays.ServicesManagerDays as ServicesManagerDays
import apis.services.indicators.ServicesIndicators as ServicesIndicators

class ControllerGetDataAnalysisDerivWMA:

    ServicesDates = None

    ServicesEvents = None

    ServicesCronjobs = None

    ServicesShedule = None

    ServicesApi = None

    ServicesSmtp = None

    ServicesDeriv = None

    ServicesCheckWMA = None

    ServicesMethodologyWMA = None

    ServicesManagerDays = None

    ServicesIndicators = None

    def __init__(self):

        self.initialize_services()

        self.initialize_services_internal()

    def initialize_services(self):

        self.ServicesDates = ServicesDate.ServicesDate()

        self.ServicesEvents = ServicesEvents.ServicesEvents()

        self.ServicesCronjobs = ServicesCronjobs.ServicesCronjobs()

        self.ServicesShedule = ServicesShedule.ServicesShedule()

        self.ServicesApi = ServicesApi.ServicesApi()

        self.ServicesSmtp = ServicesSmtp.ServicesSmtp()

        self.ServicesDeriv = ServicesDeriv.ServicesDeriv() 

        self.ServicesCheckWMA = ServicesCheckWMA.ServicesCheckWMA() 

        self.ServicesMethodologyWMA = ServicesMethodologyWMA.ServicesMethodologyWMA()   

        self.ServicesManagerDays = ServicesManagerDays.ServicesManagerDays()

        self.ServicesIndicators = ServicesIndicators.ServicesIndicators()

        return True 
    
    def initialize_services_internal(self):

        self.ServicesCheckWMA.init_services_deriv(self.ServicesDeriv)

        self.ServicesCheckWMA.init_services_methodology_wma(self.ServicesMethodologyWMA)

        self.ServicesCheckWMA.init_services_manager_days(self.ServicesManagerDays)

        self.ServicesCheckWMA.init_services_indicators(self.ServicesIndicators)

        return True

    def initialize_request_data(self):

        now = self.ServicesDates.get_current_utc5()

        date = self.ServicesDates.get_current_date(now)

        hour = self.ServicesDates.get_current_hour(now)

        self.ServicesDates.set_start_date()

        self.ServicesEvents.set_events_field('start_endpoint', self.ServicesDates.get_current_date_mil_dynamic())

        id_cronjobs = self.ServicesCronjobs.generate_cronjobs_id()

        return now, date, hour, id_cronjobs
    
    def verify_services(self, request, hour, date, id_cronjobs):

        servicios_a_verificar = [
            lambda: self.ServicesShedule.get_shedule_result(hour),
            lambda: self.ServicesApi.get_api_result(),
            lambda: self.ServicesCronjobs.add_wma(id_cronjobs, date)
        ]

        for servicio in servicios_a_verificar:

            resultado = servicio() if callable(servicio) else servicio

            if not resultado['status']:

                self.ServicesSmtp.send_notification_email(date, resultado['message'])
                
                return resultado

        return {'status': True}
    
    async def initialize_deriv_services(self, date):

        self.ServicesEvents.set_events_field('init_endpoint', self.ServicesDates.get_current_date_mil_dynamic())

        result = await self.ServicesCheckWMA.init()

        if not result['status']:

            return False

        self.ServicesEvents.set_events_field('init_broker', self.ServicesDates.get_current_date_mil_dynamic())

        await self.ServicesCheckWMA.set_balance(self.ServicesDates.get_day())

        self.ServicesEvents.set_events_field('config_broker', self.ServicesDates.get_current_date_mil_dynamic())

        self.ServicesCheckWMA.init_services_events(self.ServicesEvents)

        self.ServicesCheckWMA.init_services_dates(self.ServicesDates)

        return True
    
    async def process_deriv_services(self):

        await self.ServicesCheckWMA.loops()

        await self.ServicesCheckWMA.closed()

    def finalize_request(self, now, id_cronjobs):

        now = self.ServicesDates.get_current_utc5()

        self.ServicesDates.set_end_date()

        return self.ServicesCronjobs.set_ejecution(self.ServicesDates.get_current_date(now), self.ServicesDates.get_time_execution(), id_cronjobs)

    async def GetDataAnalysisDerivWMA(self, request):

        now, date, hour, id_cronjobs = self.initialize_request_data()

        resultado = self.verify_services(request, hour, date, id_cronjobs)
        
        if not resultado['status']:

            return 
        
        if not await self.initialize_deriv_services(date):

            return self.ServicesSmtp.send_notification_email(date, "Initialization failed")
        
        await self.process_deriv_services()

        return self.finalize_request(now, id_cronjobs)