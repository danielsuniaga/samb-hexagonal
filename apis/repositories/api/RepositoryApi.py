from django.db import connection

from decouple import config

class RepositoryApi():

    cursor_db = None

    condition = None

    def __init__(self):
        
        self.cursor_db = connection.cursor()

        self.init_condition()

    def init_condition(self):

        self.condition = config("CONDITION")

    def get_condition(self):

        return self.condition

    def get_api_key(self,key,value):

        try:

            self.count=self.cursor_db.execute("SELECT samb_config.id AS id FROM samb_config WHERE samb_config.key=%s AND samb_config.value=%s AND samb_config.condition=%s LIMIT 1",[key,value,self.get_condition()])

        except Exception as err:

            return {'status':False,'msj':"Incidencia en la lectura de key de la API "+str(err)}
        
        return {'status':True,'msj':'Success'} if self.count>0 else {'status':False,'msj': "Origen corrupto"}