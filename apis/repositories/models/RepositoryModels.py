from django.db import connection, DatabaseError

class RepositoryModels():

    def get_best_model(self):
        try:
            query = """
                SELECT sm.id AS id,
                       sm.descriptions AS descriptions,
                       sm.registration_date AS registration_date,
                       sm.state AS state,
                       best_model.accuracy AS accuracy
                FROM samb_models sm
                INNER JOIN (
                    SELECT id_models, accuracy
                    FROM samb_metrics_evaluations_models
                    ORDER BY registration_date DESC, accuracy DESC
                    LIMIT 1
                ) best_model ON sm.id = best_model.id_models
            """
            with connection.cursor() as cursor:
                cursor.execute(query)
                result = cursor.fetchall()
                column_names = [desc[0] for desc in cursor.description]
                result_with_columns = [dict(zip(column_names, row)) for row in result]
        except DatabaseError:
            return {'status': False, 'msj': "Incidencia en la lectura del mejor modelo"}
        return {'status': True, 'data': result_with_columns, 'msj': 'Success'}