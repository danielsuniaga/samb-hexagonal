from django.db import connection
class RepositoryFramework: 

    cursor_db = None

    def __init__(self):
        self.cursor_db = connection.cursor()

    async def add(self,data):

        try:

            self.cursor_db.execute("INSERT INTO samb_framework(samb_framework.id,samb_framework.description,samb_framework.registration_date,samb_framework.condition)values(%s,%s,%s,%s)",[data['id_framework'],data['description'],data['fecha'],data['condition']])

        except Exception as err:

            return {'status': False, 'message':'No se realizo la escritura en samb_framework: '+str(err)}

        return {'status':True,'message':'Success'}