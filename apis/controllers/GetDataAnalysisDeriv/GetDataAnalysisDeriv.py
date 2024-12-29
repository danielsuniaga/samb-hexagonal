from django.db import connection

import apis.services.dates.ServicesDates as ServicesDate
import apis.services.events.ServicesEvents as ServicesEvents
import apis.services.cronjobs.ServicesCronjobs as ServicesCronjobs
import apis.services.api.ServicesApi as ServicesApi
import apis.services.smtp.ServicesSmtp as ServicesSmtp

class ControllerGetDataAnalysisDeriv: 

    cursor = None

    ServicesDates = None

    ServicesEvents = None

    ServicesCronjobs = None

    ServicesApi = None

    ServicesSmtp = None

    def __init__(self):

        self.ServicesDates = ServicesDate.ServicesDate()

        self.ServicesEvents = ServicesEvents.ServicesEvents()

        self.ServicesCronjobs = ServicesCronjobs.ServicesCronjobs()

        self.ServicesApi = ServicesApi.ServicesApi()

        self.ServicesSmtp = ServicesSmtp.ServicesSmtp()

    def GetDataAnalysisDeriv(self,request):

        self.ServicesEvents.set_events_field('start_endpoint',self.ServicesDates.get_current_date_mil_dynamic())

        id_cronjobs = self.ServicesCronjobs.generate_cronjobs_id()

        now = self.ServicesDates.get_current_utc5()

        date = self.ServicesDates.get_current_date(now)

        hour = self.ServicesDates.get_current_hour(now)

        result = self.ServicesApi.get_api_key(request)

        return result