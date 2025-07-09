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
    
    def get_movements_by_entry(self, data):

        try:

            sql=" SELECT samb_movements.id AS id, samb_movements.registration_date AS registration_date, samb_movements.update_date AS update_date, samb_movements.condition AS conditions, samb_movements.open_candle AS open_candle, samb_movements.close_candle AS close_candle, samb_movements.high_candle AS high_candle, samb_movements.low_candle AS low_candle, samb_movements.epoch AS epoch, samb_movements.id_entry_id AS id_entry_id FROM samb_movements WHERE samb_movements.id_entry_id=%s"

            self.cursor_db.execute(
                sql,
                [data['id']]
            )
            rows = self.cursor_db.fetchall()
            column_names = [desc[0] for desc in self.cursor_db.description]
            result_with_columns = [dict(zip(column_names, row)) for row in rows]

        except DatabaseError:
            return {'status': False, 'message': 'No se pudo obtener los movimientos por la entrada'}

        return {'status': True, 'data': result_with_columns, 'msj': 'Success'}