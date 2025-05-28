from django.db import connection,DatabaseError

class RepositoryCronjobs():

    cursor_db = None

    def __init__(self):
        
        self.cursor_db = connection.cursor()

    def add(self,data):
        
        try:

            self.cursor_db.execute("INSERT INTO samb_cronjobs(samb_cronjobs.id,samb_cronjobs.start_date,samb_cronjobs.end_date,samb_cronjobs.condition,samb_cronjobs.id_samb_api_id,samb_cronjobs.id_samb_financial_asset_id,samb_cronjobs.execution_time)VALUES(%s,%s,%s,%s,%s,%s,%s)",[data['id'], data['date'], data['date'], data['condition'],data['id_api'],data['id_financial_asset'],data['default_execute']])

        except DatabaseError:

            return {'status': False, 'msj':'No se realizo la escritura en samb_cronjobs'}

        return {'status':True,'msj':'Success'}
    
    def set(self,data):

        try:

            self.cursor_db.execute("UPDATE samb_cronjobs SET samb_cronjobs.condition=%s,samb_cronjobs.end_date=%s,samb_cronjobs.execution_time=%s WHERE samb_cronjobs.id=%s",[data['success_condition'],data['end_date'],data['execute_time'],data['id_cronjobs']])

        except DatabaseError:

            return {'status': False, 'message':'No se realizo la sobreescritura en samb_cronjobs'}

        return {'status':True,'msj':'Success'}
    
    def get_data_cronjobs_curdate(self,data):

        try:

            self.cursor_db.execute("SELECT COUNT(samb_cronjobs.id) AS quantities, IFNULL(MAX(samb_cronjobs.execution_time),0) AS max_durations FROM samb_cronjobs WHERE DATE(samb_cronjobs.start_date) = 20250505 AND samb_cronjobs.condition = %s",
            [data['state']])

            rows = self.cursor_db.fetchall()

            columns = [col[0] for col in self.cursor_db.description]

            result = [dict(zip(columns, row)) for row in rows]

            return {'status':True,'message':'Success','result':result[0]}
            
        except DatabaseError:

            return {'status':False,'message':"Incidencia en la lectura de las samb_entrys_results leidas  "}