import apis.services.dates.ServicesDates as ServicesDate
import apis.services.events.ServicesEvents as ServicesEvents
import apis.services.cronjobs.ServicesCronjobs as ServicesCronjobs
import apis.services.shedule.ServicesShedule as ServicesShedule
import apis.services.api.ServicesApi as ServicesApi
import apis.services.smtp.ServicesSmtp as ServicesSmtp  
import apis.services.checktrendsexpansive.ServicesCheckTrendsExpansive as ServicesCheckTrendsExpansive
import apis.services.deriv.ServicesDeriv as ServicesDeriv
import apis.services.methodologytrendsexpansive.ServicesMethodologyTrendsExpansive as ServicesMethodologyTrendsExpansive

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

        return True
    
    def init_services_intern(self):

        self.ServicesCheckTrendsExpansive.init_services_deriv(self.ServicesDeriv)

        self.ServicesCheckTrendsExpansive.init_services_methodology_trendsExpansive(self.ServicesMethodologyTrendsExpansive)

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
            lambda: self.ServicesCronjobs.add_trends_expansive(id_cronjobs, date)
        ]

        for servicio in servicios_a_verificar:

            resultado = servicio() if callable(servicio) else servicio

            if not resultado['status']:

                self.ServicesSmtp.send_notification_email(date, resultado['message'])
                
                return resultado

        return {'status': True}
    
    async def initialize_deriv_services(self, date):

        self.ServicesEvents.set_events_field('init_endpoint', self.ServicesDates.get_current_date_mil_dynamic())

        result = await self.ServicesCkeckTrends.init()

        if not result['status']:

            return False

        self.ServicesEvents.set_events_field('init_broker', self.ServicesDates.get_current_date_mil_dynamic())

        await self.ServicesCkeckTrends.set_balance(self.ServicesDates.get_day())

        self.ServicesEvents.set_events_field('config_broker', self.ServicesDates.get_current_date_mil_dynamic())

        self.ServicesCkeckTrends.init_services_events(self.ServicesEvents)

        self.ServicesCkeckTrends.init_services_dates(self.ServicesDates)

        return True

    async def GetDataAnalysisDerivExpansive(self, request):

        now, date, hour, id_cronjobs = self.initialize_request_data()

        resultado = self.verify_services(request, hour, date, id_cronjobs)
        
        if not resultado['status']:

            return   

        return True