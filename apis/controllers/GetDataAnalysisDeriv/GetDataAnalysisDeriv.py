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

    def __init__(self):

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

        self.ServicesDeriv.init_services_manager_days(self.ServicesManagerDays)

        self.ServicesDeriv.init_services_methodology_trends(self.ServicesMethodologyTrends)

        self.ServicesDeriv.init_services_indicators(self.ServicesIndicators)

        self.ServicesDeriv.init_services_entrys_results(self.ServicesEntrysResults)

    async def GetDataAnalysisDeriv(self,request):

        self.ServicesEvents.set_events_field('start_endpoint',self.ServicesDates.get_current_date_mil_dynamic())

        id_cronjobs = self.ServicesCronjobs.generate_cronjobs_id()

        now = self.ServicesDates.get_current_utc5()

        date = self.ServicesDates.get_current_date(now)

        hour = self.ServicesDates.get_current_hour(now)
        
        servicios_a_verificar = [
            lambda: self.ServicesApi.get_api_key(request),  
            lambda: self.ServicesShedule.get_shedule_result(hour),  
            lambda: self.ServicesApi.get_api_result(),
            lambda: self.ServicesCronjobs.add(id_cronjobs,date)
        ]

        resultado = None

        for servicio in servicios_a_verificar:
 
            resultado = servicio() if callable(servicio) else servicio

            if not resultado['status']:

                self.ServicesSmtp.send_notification_email(date, resultado['msj'])

                return resultado
            
        self.ServicesEvents.set_events_field('init_endpoint',self.ServicesDates.get_current_date_mil_dynamic())

        result = await self.ServicesDeriv.init()

        if not result['status']:

            return self.ServicesSmtp.send_notification_email(date, result['msj'])
        
        self.ServicesEvents.set_events_field('init_broker',self.ServicesDates.get_current_date_mil_dynamic())

        await self.ServicesDeriv.set_balance(self.ServicesDates.get_day())

        self.ServicesEvents.set_events_field('config_broker',self.ServicesDates.get_current_date_mil_dynamic())

        self.ServicesDeriv.init_services_events(self.ServicesEvents)

        self.ServicesDeriv.init_services_dates(self.ServicesDates)

        result = await self.ServicesDeriv.loops()

        print("result_loops",result)

        result = await self.ServicesDeriv.closed()

        if not result['status']:

            return self.ServicesSmtp.send_notification_email(date, result['msj'])

        return result