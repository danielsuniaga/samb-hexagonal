from django.db import connection

class RepositoryIndicatorsEntrys():

    cursor_db = None

    def __init__(self):
        
        self.cursor_db = connection.cursor()

    def add(self,data):
        
        try:

            self.cursor_db.execute("INSERT INTO samb_indicators_entrys(samb_indicators_entrys.id,samb_indicators_entrys.registration_date,samb_indicators_entrys.condition,samb_indicators_entrys.id_entry_id,samb_indicators_entrys.id_indicators_id,samb_indicators_entrys.value)VALUES(%s,%s,%s,%s,%s,%s)",[data['id'],data['current_date'],data['condition'],data['id_entry'],data['id_indicators'],data['value_indicators']])

        except Exception as err:

            return {'status': False, 'msj':'No se realizo la escritura en samb_indicators_entrys'+str(err)}

        return {'status':True,'msj':'Success'}