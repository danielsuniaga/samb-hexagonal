from django.db import connection

class RepositoryShedule():

    cursor_db = None

    def __init__(self):

        self.cursor_db = connection.cursor()

    def get(self,data):

        try:

            self.count=self.cursor_db.execute("SELECT samb_shedule.id AS id FROM samb_shedule WHERE samb_shedule.start_date<=%s AND samb_shedule.end_date>=%s AND samb_shedule.description=%s AND samb_shedule.CONDITION=%s LIMIT 1",[int(data['hour']),int(data['hour']),data['shedule_permission'],data['condition']])

        except Exception as err:

            return {'status':False,'message':"Incidencia en la lectura de Shedule "+str(err)}
        
        return {'status':True,'message':'Success'} if self.count>0 else {'status':False,'message': "Horario no contemplado"}