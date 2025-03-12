import apis.services.dates.ServicesDates as ServicesDate
import apis.services.events.ServicesEvents as ServicesEvents
import apis.services.cronjobs.ServicesCronjobs as ServicesCronjobs

class ControllerGetDataAnalysisDerivWMA:

    ServicesDates = None

    ServicesEvents = None

    ServicesCronjobs = None

    def __init__(self):

        self.initialize_services()

    def initialize_services(self):

        self.ServicesDates = ServicesDate.ServicesDate()

        self.ServicesEvents = ServicesEvents.ServicesEvents()

        self.ServicesCronjobs = ServicesCronjobs.ServicesCronjobs()

        return True 

    def initialize_request_data(self):

        now = self.ServicesDates.get_current_utc5()

        date = self.ServicesDates.get_current_date(now)

        hour = self.ServicesDates.get_current_hour(now)

        self.ServicesDates.set_start_date()

        self.ServicesEvents.set_events_field('start_endpoint', self.ServicesDates.get_current_date_mil_dynamic())

        id_cronjobs = self.ServicesCronjobs.generate_cronjobs_id()

        return now, date, hour, id_cronjobs

    async def GetDataAnalysisDerivWMA(self, request):

        now, date, hour, id_cronjobs = self.initialize_request_data()

        return True