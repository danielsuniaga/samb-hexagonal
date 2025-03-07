from django.db import connection,DatabaseError

class RepositoryApi():

    cursor_db = None

    def __init__(self):
        
        self.cursor_db = connection.cursor()

    def get(self,data):

        try:

            self.count=self.cursor_db.execute("SELECT samb_apis.id AS id FROM samb_apis WHERE samb_apis.description=%s AND samb_apis.condition=%s LIMIT 1",[data['api_description'],data['condition']])

        except DatabaseError: 

            return {'status':False,'msj':"Incidencia en la lectura de la API "}
        
        return {'status':True,'msj':'Success'} if self.count>0 else {'status':False,'msj': "API Desactivada"}

    def get_api_key(self,key,value,condition):

        try:

            self.count=self.cursor_db.execute("SELECT samb_config.id AS id FROM samb_config WHERE samb_config.key=%s AND samb_config.value=%s AND samb_config.condition=%s LIMIT 1",[key,value,condition])

        except DatabaseError: 

            return {'status':False,'msj':"Incidencia en la lectura de key de la API "}
        
        return {'status':True,'msj':'Success'} if self.count>0 else {'status':False,'msj': "Origen corrupto"}