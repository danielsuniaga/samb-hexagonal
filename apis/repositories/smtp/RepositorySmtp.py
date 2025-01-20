from django.db import connection

class RepositorySmtp():

    cursor_db = None

    def __init__(self):

        self.cursor_db = connection.cursor()

    def add_notificacion_exc(self,data):

        try:

            self.cursor_db.execute("INSERT INTO samb_notifications_exceptions_apis_independient(samb_notifications_exceptions_apis_independient.id,samb_notifications_exceptions_apis_independient.description, samb_notifications_exceptions_apis_independient.registration_date,samb_notifications_exceptions_apis_independient.update_date,samb_notifications_exceptions_apis_independient.condition, samb_notifications_exceptions_apis_independient.id_exceptions_api_id)VALUES(%s,%s,%s,%s,%s,%s)",[data['id'], data['mensaje'], data['fecha'], data['fecha'], data['condition'], data['id_exceptions_apis']])

        except Exception as err:

            return {'status': False, 'message':'No se realizo la escritura en samb_framework: '+str(err)}

        return {'status':True,'message':'Success'}