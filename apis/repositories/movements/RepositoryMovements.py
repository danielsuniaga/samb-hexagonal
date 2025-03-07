from django.db import connection, DatabaseError

class RepositoryMovements():

    cursor_db = None

    def __init__(self):
        
        self.cursor_db = connection.cursor()

    def add(self,candles):

        try:

            self.cursor_db.executemany("INSERT INTO samb_movements(samb_movements.id,samb_movements.registration_date,samb_movements.update_date,samb_movements.condition,samb_movements.open_candle,samb_movements.close_candle,samb_movements.high_candle,samb_movements.low_candle,samb_movements.epoch,samb_movements.id_entry_id)VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",candles)

        except DatabaseError:

            return {'status': False, 'message':'No se realizo la escritura en samb_movements'}

        return {'status':True,'msj':'Success'}