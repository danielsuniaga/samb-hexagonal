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