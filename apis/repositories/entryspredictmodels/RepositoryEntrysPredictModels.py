from django.db import connection, DatabaseError

class RepositoryEntrysPredictModels:

    cursor_db = None

    def __init__(self):
        self.cursor_db = connection.cursor()

    def add_entrys_predict_model(self, data):
        try:
            params = [
                data['id'],
                data['id_entrys'],
                data['id_predict_models'],
                data['registration_date'],
                data['update_date'],
                data['state']
            ]
            self.cursor_db.execute("""
                INSERT INTO samb_entrys_predict_models (
                    id,
                    id_entrys,
                    id_predict_models,
                    registration_date,
                    update_date,
                    state
                ) VALUES (
                    %s, %s, %s, %s, %s, %s
                )
            """, params)
        except DatabaseError as e:
            return {
                'status': False,
                'msj': f'No se realizó la escritura en samb_entrys_predict_models. Error: {str(e)}'
            }
        return {'status': True, 'msj': 'Success'}

    def add(self, data):
        return self.add_entrys_predict_model(data)