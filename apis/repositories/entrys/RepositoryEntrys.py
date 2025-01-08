from django.db import connection

class RepositoryEntrys():

    cursor_db = None

    def __init__(self):
        
        self.cursor_db = connection.cursor()

    def add(self,data):

        try:

            self.cursor_db.execute("INSERT INTO samb_entrys(samb_entrys.id,samb_entrys.type,samb_entrys.type_account,samb_entrys.number_candle,samb_entrys.condition_entry,samb_entrys.amount,samb_entrys.registration_date,samb_entrys.update_date,samb_entrys.condition,samb_entrys.id_samb_cronjobs_id,samb_entrys.id_entry_platform,samb_entrys.result_platform)VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",[self.data['id_entry'],data['type_operations'],data['mode'],data['candle_analized'],data['condition_entry'],data['amount'],data['current_date'],data['current_date'],data['condition'],data['id_cronjobs'],data['id_entry_platform'],data['rd_entry_platform']])

        except Exception as err:

            return {'status': False, 'message':'No se realizo la escritura en samb_entrys'+str(err)}

        return {'status':True,'msj':'Success'}