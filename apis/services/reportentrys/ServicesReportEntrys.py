import apis.entities.reportsentrys.EntityReportEntrys as EntityReportEntrys
import json
import os
from datetime import datetime

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
            
            # NUEVO: Exportar archivos para análisis
            export_tracking = {
                'successful': [],
                'failed': [],
                'successful_count': 0,
                'failed_count': 0,
                'files_created': [],
                'export_folder': None,
                'error': None
            }
            
            try:
                export_data = {
                    'methodologys': methodologys,
                    'day': day
                }
                export_result = self.save_export_files(export_data)
                
                if export_result.get('status'):
                    print(f"✅ Exportación exitosa: {export_result.get('message')}")
                    # Extraer datos de tracking de la exportación
                    details = export_result.get('details', {})
                    tracking = details.get('tracking', {})
                    
                    export_tracking.update({
                        'successful': tracking.get('successful', []),
                        'failed': tracking.get('failed', []),
                        'successful_count': tracking.get('successful_count', 0),
                        'failed_count': tracking.get('failed_count', 0),
                        'files_created': details.get('files', []),
                        'export_folder': details.get('export_folder'),
                        'success_rate': tracking.get('success_rate', '0/0')
                    })
                else:
                    print(f"⚠️ Error en exportación: {export_result.get('message')}")
                    export_tracking['error'] = export_result.get('message')
                    
            except Exception as e:
                error_msg = f"Error crítico en exportación: {str(e)}"
                print(f"⚠️ {error_msg}")
                export_tracking['error'] = error_msg
                # No afectamos el flujo principal por errores de exportación
            
            # Preparar respuesta final
            total_methodologies = len(methodologys)
            successful_count = len(successful_methodologies)
            failed_count = len(failed_methodologies)
            
            # Crear mensaje combinado
            telegram_msg = f"Telegram: {successful_count}/{total_methodologies}"
            export_msg = f"Exportación: {export_tracking['successful_count']}/{total_methodologies}"
            combined_message = f"Reportes procesados. {telegram_msg}, {export_msg}"
            
            if failed_count == 0:
                return {
                    'status': True, 
                    'message': f'{combined_message} - Proceso exitoso',
                    'details': {
                        'telegram': {
                            'successful': successful_methodologies,
                            'failed': failed_methodologies,
                            'successful_count': successful_count,
                            'failed_count': failed_count,
                            'success_rate': f"{successful_count}/{total_methodologies}"
                        },
                        'exports': export_tracking,
                        'total_methodologies': total_methodologies,
                        'overall_status': 'success'
                    }
                }
            else:
                overall_status = 'partial_success' if successful_count > 0 else 'failure'
                return {
                    'status': False if failed_count == total_methodologies else True,
                    'message': f'{combined_message} - Proceso con errores',
                    'details': {
                        'telegram': {
                            'successful': successful_methodologies,
                            'failed': failed_methodologies,
                            'successful_count': successful_count,
                            'failed_count': failed_count,
                            'success_rate': f"{successful_count}/{total_methodologies}"
                        },
                        'exports': export_tracking,
                        'total_methodologies': total_methodologies,
                        'overall_status': overall_status
                    }
                }
                
        except Exception as e:
            return {
                'status': False, 
                'message': f'Error crítico en el proceso de reportes: {str(e)}',
                'details': {
                    'error_type': 'critical', 
                    'error': str(e),
                    'telegram': {'successful': [], 'failed': [], 'successful_count': 0, 'failed_count': 0},
                    'exports': {'successful': [], 'failed': [], 'successful_count': 0, 'failed_count': 0, 'error': str(e)},
                    'overall_status': 'critical_failure'
                }
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

    def save_export_files(self, report_data=None):
        """
        Guarda los reportes en archivos JSON para análisis posterior
        Args:
            report_data: datos del reporte (opcional, se obtienen si no se proporcionan)
        Returns: dict con status y detalles de la exportación
        """
        try:
            # Crear timestamp para la carpeta (año-mes/día)
            now = datetime.now()
            year_month = now.strftime('%Y%m')           # Ejemplo: 202602
            date_day = now.strftime('%Y-%m-%d')         # Ejemplo: 2026-02-21
            timestamp = date_day  # Mantener compatibilidad con código existente
            
            # Crear ruta base con estructura año-mes/día
            base_path = '/export-reporting-sessions'
            export_folder = os.path.join(base_path, year_month, date_day)
            
            # Crear directorio si no existe (creará carpetas intermedias)
            os.makedirs(export_folder, exist_ok=True)
            
            # Obtener datos si no se proporcionaron
            if report_data is None:
                methodologys = self.get_methodologys()
                day = self.get_day()
            else:
                methodologys = report_data.get('methodologys', [])
                day = report_data.get('day', {})
            
            exported_files = []
            export_successful = []
            export_failed = []
            
            # Exportar cada metodología
            for methodology in methodologys:
                methodology_name = methodology.get('descriptions', 'unknown')
                container = methodology.get('container', '')
                
                try:
                    # Generar datos del reporte para esta metodología
                    report_result = self._generate_methodology_data(methodology, day)
                    
                    # Crear nombre de archivo (solo metodología si container está vacío o unknown)
                    if container and container != 'unknown' and container.strip():
                        filename = f"{methodology_name}_{container}.json"
                    else:
                        filename = f"{methodology_name}.json"
                    filepath = os.path.join(export_folder, filename)
                    
                    # Estructura de datos para exportar
                    export_data = {
                        'timestamp': timestamp,
                        'methodology': methodology_name,
                        'container': container,
                        'day_info': day,
                        'report_data': report_result,
                        'metadata': {
                            'export_date': datetime.now().isoformat(),
                            'methodology_id': methodology.get('id'),
                            'version': '1.0'
                        }
                    }
                    
                    # Guardar archivo
                    with open(filepath, 'w', encoding='utf-8') as f:
                        json.dump(export_data, f, indent=2, ensure_ascii=False, default=str)
                    
                    exported_files.append(filename)
                    export_successful.append(methodology_name)
                    
                except Exception as e:
                    error_msg = f"Error exportando metodología {methodology_name}: {str(e)}"
                    print(error_msg)
                    export_failed.append({
                        'methodology': methodology_name,
                        'error': str(e)
                    })
                    continue
            
            # Crear archivo resumen
            summary_data = {
                'export_summary': {
                    'timestamp': timestamp,
                    'total_methodologies': len(methodologys),
                    'exported_files': len(exported_files),
                    'export_folder': export_folder,
                    'files': exported_files,
                    'day_info': day,
                    'metadata': {
                        'export_date': datetime.now().isoformat(),
                        'total_files_expected': len(methodologys),
                        'success_rate': f"{len(exported_files)}/{len(methodologys)}"
                    }
                }
            }
            
            summary_filepath = os.path.join(export_folder, '_export_summary.json')
            with open(summary_filepath, 'w', encoding='utf-8') as f:
                json.dump(summary_data, f, indent=2, ensure_ascii=False, default=str)
            
            return {
                'status': True,
                'message': f'Reportes exportados exitosamente. {len(exported_files)} archivos creados',
                'details': {
                    'export_folder': export_folder,
                    'files_exported': len(exported_files),
                    'total_methodologies': len(methodologys),
                    'timestamp': timestamp,
                    'files': exported_files,
                    'tracking': {
                        'successful': export_successful,
                        'failed': export_failed,
                        'successful_count': len(export_successful),
                        'failed_count': len(export_failed),
                        'success_rate': f"{len(export_successful)}/{len(methodologys)}"
                    }
                }
            }
            
        except Exception as e:
            return {
                'status': False,
                'message': f'Error durante la exportación: {str(e)}',
                'details': {'error': str(e)}
            }

    def _generate_methodology_data(self, methodology, day):
        """
        Genera los datos específicos de una metodología para exportar
        Usa la MISMA lógica que process_methodology_report pero retorna datos estructurados
        """
        methodology_name = methodology.get('descriptions', 'Unknown')
        methodology_id = methodology.get('id', 'Unknown')
        
        try:
            # Usar la MISMA lógica que funciona para Telegram
            
            # 1. Inicializar datos de reportes
            self.init_data_reports()
            
            # 2. Obtener parámetros del día
            data_param = self.get_type_manager_days_reporting(day, methodology_id)
            message_param = self.generate_message_parameters(data_param)
            self.set_message_params(message_param)
            
            # 3. Generar datos del reporte (MISMA lógica que Telegram)
            report_data = self.generate_data_reports_daily(methodology_id)
            
            # 4. Generar mensaje (para tener el texto también)
            telegram_message = self.generate_message(report_data, methodology_name)
            
            # 5. Retornar datos estructurados
            return {
                'methodology_info': {
                    'name': methodology_name,
                    'id': methodology_id,
                    'container': methodology.get('container', ''),
                },
                'day_params': data_param,
                'message_params': message_param,
                'report_data': report_data,
                'telegram_message': telegram_message,
                'status': 'success'
            }
            
        except Exception as e:
            return {
                'error': str(e), 
                'methodology': methodology_name,
                'status': 'error',
                'error_details': {
                    'methodology_id': methodology_id,
                    'day': day
                }
            }
