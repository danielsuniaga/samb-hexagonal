from django.db import connection,DatabaseError

class RepositorySendEntrys():

    cursor_db = None

    def __init__(self):
        
        self.cursor_db = connection.cursor()

    def add(self, data):
        
        try:

            self.cursor_db.execute(
                "INSERT INTO samb_send_entrys (id, registration_date, conditions, id_entrys, response, message) VALUES (%s, %s, %s, %s, %s, %s)",
                [
                    data['id'],
                    data['registration_date'],
                    data['conditions'],
                    data['id_entrys'],
                    data['response'],
                    data['message']
                ]
            )

        except DatabaseError:

            return {'status': False, 'msj': 'No se realizo la escritura en samb_send_entrys'}

        return {'status': True, 'msj': 'Success'}