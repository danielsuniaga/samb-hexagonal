from django.db import connection, DatabaseError

class RepositoryMethodologys():

    cursor_db = None

    def __init__(self):
        
        self.cursor_db = connection.cursor()
    
    def get_methodologys(self, data):

        try:

            query = "SELECT samb_methodologys.id AS id, samb_methodologys.descriptions AS descriptions FROM samb_methodologys WHERE samb_methodologys.conditions=%s"

            self.cursor_db.execute(query, data['condition_success'])

            result = self.cursor_db.fetchall()

            column_names = [desc[0] for desc in self.cursor_db.description]

            result_with_columns = [dict(zip(column_names, row)) for row in result]
            
        except DatabaseError:

            return {'status': False, 'msj': "Incidencia en la lectura de las samb_metododolgys: "}
                
        return {'status': True, 'data': result_with_columns, 'msj': 'Success'}
    
    def get_methodology_description_number_by_id(self, data):

        try:

            query = "SELECT samb_methodologys.description_number AS description_number FROM samb_methodologys WHERE samb_methodologys.id=%s LIMIT 1"

            self.cursor_db.execute(query, [data['id_methodology']])

            result = self.cursor_db.fetchall()

            column_names = [desc[0] for desc in self.cursor_db.description]

            result_with_columns = [dict(zip(column_names, row)) for row in result]

        except DatabaseError:

            return {'status': False, 'msj': "Incidencia en la lectura de las samb_metododolgys: "}

        return {'status': True, 'data': result_with_columns, 'msj': 'Success'}
