from django.db import connection,DatabaseError

import json

class RepositoryEvents():

    cursor_db = None

    def __init__(self):
        
        self.cursor_db = connection.cursor()

    def add(self,data):

        try:

            self.cursor_db.execute("INSERT INTO samb_events(id, details, difference, registration_date, update_cate, state, id_samb_cronjobs_id) VALUES (%s, %s, %s, %s, %s, %s, %s)", [data['id'], json.dumps(data['details']), json.dumps(data['difference']), data['registration_date'], data['update_cate'], data['state'], data['id_samb_cronjobs_id']])

        except DatabaseError as e:

            return {'status': False, 'msj': f'No se realizo la escritura en samb_cronjobs. Error: {str(e)}'}

        return {'status':True,'msj':'Success'}
    
    def get_events_daily_crons(self):

        try:

            self.cursor_db.execute("SELECT samb_events.id AS id, samb_events.difference AS difference, samb_cronjobs.execution_time AS execution_time, samb_cronjobs.condition AS cond FROM samb_events INNER JOIN samb_cronjobs ON samb_cronjobs.id = samb_events.id_samb_cronjobs_id WHERE samb_cronjobs.start_date >= CURDATE() AND samb_cronjobs.start_date < DATE_ADD(CURDATE(), INTERVAL 1 DAY) ORDER BY samb_cronjobs.execution_time DESC LIMIT 1;")

            rows = self.cursor_db.fetchall()

            columns = [col[0] for col in self.cursor_db.description]

            result = [dict(zip(columns, row)) for row in rows]

            if result:

                return {'status':True,'message':'Success','result':result[0]}
            
            else:
                
                return {'status':False,'message':'No events found for today','result':None}
        
        except DatabaseError:

            return {'status':False,'message':"Incidencia en la lectura de las samb_events leidas "}
        