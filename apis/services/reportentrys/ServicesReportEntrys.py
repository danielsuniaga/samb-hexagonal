import apis.entities.reportsentrys.EntityReportEntrys as EntityReportEntrys

class ServicesReportEntrys():

    entity = None

    ServicesReports = None

    ServicesDates = None

    ServicesTelegram = None

    ServicesEntrysResults = None

    ServicesMethodologys = None

    ServicesManagerDays = None

    def __init__(self):

        self.entity = EntityReportEntrys.EntityReportEntrys()

    def init_services_manager_days(self,value):

        self.ServicesManagerDays = value

        return True

    def init_data_reports(self):    

        self.entity.init_data_reports()

        return True

    def init_services_methodologys(self, value):

        self.ServicesMethodologys = value

        return True

    def init_services_reportsentrys(self, value):   

        self.ServicesEntrysResults = value

        return True

    def init_services_telegram(self, value):    

        self.ServicesTelegram = value

        return True

    def get_current_date_hour(self):

        return self.ServicesDates.get_current_date_hour()

    def init_services_reports(self, value):

        self.ServicesReports = value

        return True
    
    def init_services_dates(self, value):

        self.ServicesDates = value

        return True
    
    def get_max_attempts_reports_entrys(self):

        return self.entity.get_max_attempts_reports_entrys()
    
    def get_types_reports_daily(self):

        return self.entity.get_types_reports_daily()
    
    def add_persistence_daily_reports_entrys(self):

        type_reports = self.get_types_reports_daily()

        return self.ServicesReports.add_persistence(type_reports,self.get_current_date_hour())
    
    def generate_message(self,data,name_methodology):

        return self.entity.generate_message(data,name_methodology)
    
    def generate_message_parameters(self,data):
            
        return self.entity.generate_message_parameters(data)
    
    def send_message(self,mensaje):

        return self.ServicesTelegram.send_message_report(mensaje)
    
    def generate_data_report_cur(self,data,id_methodology):

        return self.ServicesEntrysResults.get_data_entrys_results_curdate(data,id_methodology)
    
    def generate_data_report_cur_complete(self,data):

        return self.ServicesEntrysResults.get_data_entrys_results_curdate_complete(data)
    
    def generate_data_report_tot(self,data,id_methodology):

        return self.ServicesEntrysResults.get_data_entrys_results_total(data,id_methodology)
    
    def generate_data_report_tot_complete(self,data):

        return self.ServicesEntrysResults.get_data_entrys_results_total_complete(data)
    
    def generate_data_report_nom(self,data,id_methodology):

        return self.ServicesEntrysResults.get_data_entrys_results_nom(data,id_methodology)
    
    def generate_data_report_nom_complete(self,data):

        return self.ServicesEntrysResults.get_data_entrys_results_nom_complete(data)
    
    def check_data_reports(self,data,id_methodology):

        if data['name'] == 'CUR':

            return self.generate_data_report_cur(data['data'],id_methodology)

        if data['name'] == 'TOT':   

            return self.generate_data_report_tot(data['data'],id_methodology)

        return self.generate_data_report_nom(data['data'],id_methodology)
    
    def check_data_reports_complete(self,data):

        if data['name'] == 'CUR':

            return self.generate_data_report_cur_complete(data['data'])

        if data['name'] == 'TOT':   

            return self.generate_data_report_tot_complete(data['data'])

        return self.generate_data_report_nom_complete(data['data'])
    
    def generate_data_reports_daily(self,id_methodology):

        data = self.entity.get_data_reports()

        for item in data:

            item = self.check_data_reports(item,id_methodology)
            
        return data
    
    def get_methodologys(self):

        return self.ServicesMethodologys.get_methodologys()
    
    def generate_data_reports_daily_complete(self):

        data = self.entity.get_data_reports()

        for item in data:

            item = self.check_data_reports_complete(item)
            
        return data
    
    def get_titles_reports_daily_complete_complement(self):

        return self.entity.get_titles_reports_daily_complete_complement()
    
    def init_message_params(self):

        return self.entity.init_message_params()
    
    def get_daily_report_entrys_complete(self):

        self.init_data_reports()

        self.init_message_params()

        data = self.generate_data_reports_daily_complete()

        message = self.generate_message(data,self.get_titles_reports_daily_complete_complement())

        result = self.send_message(message)

        return True
    
    def get_day(self):

        return self.ServicesDates.get_day()
    
    def get_type_manager_days_reporting(self,day,id_methodology):

        return self.ServicesManagerDays.get_type_manager_days_reporting(day,id_methodology)
    
    def set_message_params(self,message):
           
        return self.entity.set_message_params(message)

    def get_daily_report_entrys(self):
        """
        Procesa y envía reportes diarios para todas las metodologías
        Returns: dict con status y message
        """
        try:
            # Verificar persistencia
            result_persistence = self.add_persistence_daily_reports_entrys()
            if not result_persistence['status']:
                return result_persistence
            
            # Obtener datos necesarios
            try:
                methodologys = self.get_methodologys()
                day = self.get_day()
            except Exception as e:
                return {'status': False, 'message': f'Error obteniendo datos iniciales: {str(e)}'}
            
            # Procesar cada metodología
            failed_methodologies = []
            successful_methodologies = []
            
            for methodology in methodologys:
                try:
                    result = self.process_methodology_report(methodology, day)
                    
                    if result and result.get('status', True):
                        successful_methodologies.append(methodology.get('descriptions', 'Unknown'))
                    else:
                        failed_methodologies.append(methodology.get('descriptions', 'Unknown'))
                        
                except Exception as e:
                    methodology_name = methodology.get('descriptions', 'Unknown')
                    failed_methodologies.append(methodology_name)
            
            # Enviar reporte completo
            try:
                complete_result = self._send_complete_report_with_retry()
            except Exception as e:
                # No retornamos error aquí porque las metodologías individuales ya se procesaron
                pass
            
            # Preparar respuesta final
            total_methodologies = len(methodologys)
            successful_count = len(successful_methodologies)
            failed_count = len(failed_methodologies)
            
            if failed_count == 0:
                return {
                    'status': True, 
                    'message': f'Reportes procesados exitosamente. {successful_count}/{total_methodologies} metodologías completadas',
                    'details': {
                        'successful': successful_methodologies,
                        'failed': failed_methodologies,
                        'total': total_methodologies
                    }
                }
            else:
                return {
                    'status': False if failed_count == total_methodologies else True,
                    'message': f'Proceso completado con errores. {successful_count}/{total_methodologies} metodologías exitosas',
                    'details': {
                        'successful': successful_methodologies,
                        'failed': failed_methodologies,
                        'total': total_methodologies
                    }
                }
                
        except Exception as e:
            return {
                'status': False, 
                'message': f'Error crítico en el proceso de reportes: {str(e)}',
                'details': {'error_type': 'critical', 'error': str(e)}
            }

    def process_methodology_report(self, methodology, day):
        """
        Procesa y envía reporte para una metodología específica
        Args:
            methodology: dict con información de la metodología
            day: día actual para el reporte
        Returns:
            dict con status y message
        """
        methodology_name = methodology.get('descriptions', 'Unknown')
        methodology_id = methodology.get('id', 'Unknown')
        
        try:
            # Inicializar datos de reportes
            try:
                self.init_data_reports()
            except Exception as e:
                return {'status': False, 'message': f'Error inicializando datos: {str(e)}'}
            
            # Obtener parámetros del día
            try:
                data_param = self.get_type_manager_days_reporting(day, methodology_id)
                message_param = self.generate_message_parameters(data_param)
                self.set_message_params(message_param)
            except Exception as e:
                return {'status': False, 'message': f'Error configurando parámetros: {str(e)}'}
            
            # Generar datos del reporte
            try:
                data = self.generate_data_reports_daily(methodology_id)
            except Exception as e:
                return {'status': False, 'message': f'Error generando datos: {str(e)}'}
            
            # Generar mensaje
            try:
                message = self.generate_message(data, methodology_name)
            except Exception as e:
                return {'status': False, 'message': f'Error generando mensaje: {str(e)}'}
            
            # Enviar mensaje con reintentos
            try:
                result = self.send_message_with_retry(message, f"methodology {methodology_name}")
                
                if result.get('status', False):
                    return {'status': True, 'message': f'Reporte de {methodology_name} enviado exitosamente'}
                else:
                    return {'status': False, 'message': f'Error enviando mensaje: {result.get("message", "Unknown error")}'}
                    
            except Exception as e:
                return {'status': False, 'message': f'Error crítico enviando mensaje: {str(e)}'}
                
        except Exception as e:
            return {'status': False, 'message': f'Error crítico en procesamiento: {str(e)}'}

    def send_message_with_retry(self, message, context="message"):
        """
        Envía mensaje con lógica de reintentos
        Args:
            message: mensaje a enviar
            context: contexto del mensaje
        Returns:
            dict con status y message
        """
        max_attempts = self.get_max_attempts_reports_entrys()
        last_error = None
        
        for attempt in range(1, max_attempts + 1):
            try:
                result = self.send_message(message)
                
                if result and result.get('status', False):
                    return result
                else:
                    error_msg = result.get('message', 'Unknown error') if result else 'No result returned'
                    last_error = error_msg
                    
            except Exception as e:
                error_msg = str(e)
                last_error = error_msg
        
        error_message = f'Failed to send {context} after {max_attempts} attempts. Last error: {last_error}'
        return {'status': False, 'message': error_message}

    def _send_complete_report_with_retry(self):
        """
        Envía reporte completo con lógica de reintentos
        Returns:
            dict con status y message
        """
        max_attempts = self.get_max_attempts_reports_entrys()
        last_error = None
        
        for attempt in range(1, max_attempts + 1):
            try:
                complete_result = self.get_daily_report_entrys_complete()
                
                if complete_result:
                    return {'status': True, 'message': 'Complete report sent successfully'}
                else:
                    last_error = "Method returned False/None"
                    
            except Exception as e:
                error_msg = str(e)
                last_error = error_msg
        
        error_message = f'Failed to send complete report after {max_attempts} attempts. Last error: {last_error}'
        return {'status': False, 'message': error_message}
