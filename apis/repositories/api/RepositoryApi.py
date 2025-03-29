from django.db import connection,DatabaseError

class RepositoryApi():

    cursor_db = None

    def __init__(self):
        
        self.cursor_db = connection.cursor()

    def get_apis(self,data):

        try:

            query = "SELECT samb_apis.id AS id, samb_apis.description AS description FROM samb_apis WHERE samb_apis.condition=%s"

            parameters = [data['condition']]

            self.cursor_db.execute(query, parameters)

            result = self.cursor_db.fetchall()

            column_names = [desc[0] for desc in self.cursor_db.description]

            result_with_columns = [dict(zip(column_names, row)) for row in result]
            
        except DatabaseError:

            return {'status':False,'msj':"Incidencia en la lectura de los datos en la tabla samb_apis"}
                
        return {'status':True,'data':result_with_columns,'msj':'Success'}

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