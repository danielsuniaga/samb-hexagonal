from django.db import connection

class RepositoryCronjobs():

    cursor_db = None

    def __init__(self):
        
        self.cursor_db = connection.cursor()

    def add(self,data):
        
        try:

            self.cursor_db.execute("INSERT INTO samb_cronjobs(samb_cronjobs.id,samb_cronjobs.start_date,samb_cronjobs.end_date,samb_cronjobs.condition,samb_cronjobs.id_samb_api_id,samb_cronjobs.id_samb_financial_asset_id,samb_cronjobs.execution_time)VALUES(%s,%s,%s,%s,%s,%s,%s)",[data['id'], data['date'], data['date'], data['condition'],data['id_api'],data['id_financial_asset'],data['default_execute']])

        except Exception as err:

            return {'status': False, 'msj':'No se realizo la escritura en samb_cronjobs'+str(err)}

        return {'status':True,'msj':'Success'}
    
    def set(self,data):

        try:

            self.cursor_db.execute("UPDATE samb_cronjobs SET samb_cronjobs.condition=%s,samb_cronjobs.end_date=%s,samb_cronjobs.execution_time=%s WHERE samb_cronjobs.id=%s",[data['success_condition'],data['end_date'],data['execute_time'],data['id_cronjobs']])

        except Exception as err:

            return {'status': False, 'message':'No se realizo la sobreescritura en samb_cronjobs'+str(err)}

        return {'status':True,'msj':'Success'}
    
    def get_data_cronjobs_curdate(self):

        try:

            self.cursor_db.execute("SELECT * FROM samb_cronjobs WHERE samb_cronjobs.start_date = CURDATE()")

            result = self.cursor_db.fetchall()

        except Exception as err:

            return {'status': False, 'message':'No se realizo la lectura en samb_cronjobs'+str(err),'data':None}

        return {'status':True,'message':'Success','data':result}