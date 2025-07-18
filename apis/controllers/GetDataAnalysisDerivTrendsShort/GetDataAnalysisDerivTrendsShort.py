import apis.services.dates.ServicesDates as ServicesDate
import apis.services.smtp.ServicesSmtp as ServicesSmtp
import apis.services.events.ServicesEvents as ServicesEvents
import apis.services.cronjobs.ServicesCronjobs as ServicesCronjobs
import apis.services.shedule.ServicesShedule as ServicesShedule
import apis.services.api.ServicesApi as ServicesApi

class ControllerGetDataAnalysisDerivTrendsShort:

    ServicesDates = None

    ServicesSmtp = None

    ServicesEvents = None

    ServicesCronjobs = None

    ServicesShedule = None

    ServicesApi = None

    def __init__(self):

        self.init_services()

        # self.init_services_intern()

    def init_services(self):

        self.ServicesDates = ServicesDate.ServicesDate()

        self.ServicesEvents = ServicesEvents.ServicesEvents()

        self.ServicesCronjobs = ServicesCronjobs.ServicesCronjobs()

        self.ServicesShedule = ServicesShedule.ServicesShedule()

        self.ServicesApi = ServicesApi.ServicesApi()

        self.ServicesSmtp = ServicesSmtp.ServicesSmtp()

        # self.ServicesCheckTrendsExpansive = ServicesCheckTrendsExpansive.ServicesCheckTrendsExpansive()

        # self.ServicesDeriv = ServicesDeriv.ServicesDeriv()

        # self.ServicesMethodologyTrendsExpansive = ServicesMethodologyTrendsExpansive.ServicesMethodologyTrendsExpansive()

        # self.ServicesManagerDays = ServicesManagerDays.ServicesManagerDays()

        # self.ServicesIndicators = ServicesIndicators.ServicesIndicators()   

        # self.ServicesEntrysResults = ServicesEntrysResults.ServicesEntrysResults()

        # self.ServicesMovements = ServicesMovements.ServicesMovements()

        # self.ServicesPlatform = ServicesPlatform.ServicesPlatform()  

        # self.ServicesEntrys = ServicesEntrys.ServicesEntrys()

        # self.ServicesIndicatorsEntrys = ServicesIndicatorsEntrys.ServicesIndicatorsEntrys() 

        # self.ServicesTelegram = ServicesTelegram.ServicesTelegram()

        return True
    
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

    async def GetDataAnalysisDerivShort(self, request):

        now, date, hour, id_cronjobs = self.initialize_request_data()

        resultado = self.verify_services(request, hour, date, id_cronjobs)

        return False
