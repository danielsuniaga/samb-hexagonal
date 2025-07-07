from django.db import connection, DatabaseError

class RepositoryIndicatorsEntrys():

    cursor_db = None

    def __init__(self):
        
        self.cursor_db = connection.cursor()

    def add(self,data):
        
        try:

            self.cursor_db.execute("INSERT INTO samb_indicators_entrys(samb_indicators_entrys.id,samb_indicators_entrys.registration_date,samb_indicators_entrys.condition,samb_indicators_entrys.id_entry_id,samb_indicators_entrys.id_indicators_id,samb_indicators_entrys.value)VALUES(%s,%s,%s,%s,%s,%s)",[data['id'],data['current_date'],data['condition'],data['id_entry'],data['id_indicators'],data['value_indicators']])

        except DatabaseError:

            return {'status': False, 'msj':'No se realizo la escritura en samb_indicators_entrys'}

        return {'status':True,'msj':'Success'}
    
    def get_entrys(self, data):

        try:
            self.cursor_db.execute(
                "SELECT samb_indicators_entrys.id AS id, "
                "samb_indicators_entrys.registration_date AS registration_date, "
                "samb_indicators_entrys.condition AS conditions, "
                "samb_indicators_entrys.id_entry_id AS id_entry_id, "
                "samb_indicators_entrys.id_indicators_id AS id_indicators_id, "
                "samb_indicators_entrys.value AS value, "
                "samb_indicators.id AS samb_indicators_id, "
                "samb_indicators.description AS samb_indicators_description, "
                "samb_indicators.registration_date AS samb_indicators_registration_date, "
                "samb_indicators.condition AS samb_indicators_condition "
                "FROM samb_indicators_entrys "
                "INNER JOIN samb_indicators ON samb_indicators.id=samb_indicators_entrys.id_indicators_id "
                "WHERE samb_indicators_entrys.condition=%s AND samb_indicators_entrys.id_entry_id=%s",
                [data['condition'], data['id_entry']]
            )

            result = self.cursor_db.fetchall()
            column_names = [desc[0] for desc in self.cursor_db.description]
            result_with_columns = [dict(zip(column_names, row)) for row in result]

        except DatabaseError:
            return {'status': False, 'msj': 'No se realizo la lectura en samb_indicators_entrys'}

        return {'status': True, 'msj': 'Success', 'data': result_with_columns}