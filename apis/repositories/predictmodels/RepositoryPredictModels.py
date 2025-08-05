from django.db import connection, DatabaseError

class RepositoryPredictModels:

    cursor_db = None

    def __init__(self):
        self.cursor_db = connection.cursor()

    def add_predict_model(self, data):
        try:
            self.cursor_db.execute("""
                INSERT INTO samb_predict_models (
                    id,
                    id_models,
                    accuracy_min,
                    probability_min,
                    model_name,
                    prediction,
                    prediction_label,
                    probability_loss,
                    probability_win,
                    confidence,
                    confidence_percentage,
                    data_shape,
                    features_count,
                    registration_date,
                    udpate_date,
                    state
                ) VALUES (
                    %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s
                )
            """, [
                data['id'],
                data['id_models'],
                data['accuracy_min'],
                data['probability_min'],
                data['model_name'],
                data['prediction'],
                data['prediction_label'],
                data['probability_loss'],
                data['probability_win'],
                data['confidence'],
                data['confidence_percentage'],
                data['data_shape'],
                data['features_count'],
                data['registration_date'],
                data['udpate_date'],
                data['state']
            ])
        except DatabaseError as e:
            return {
                'status': False,
                'msj': f'No se realizó la escritura en samb_predict_models. Error: {str(e)}'
            }
        
        return {'status': True, 'msj': 'Success'}

    def add_predict_model_data(self, data):
        try:
            self.cursor_db.execute("""
                INSERT INTO samb_predict_models_data (
                    id, id_samb_predict_models, dictionary, registration_date, update_date, state
                ) VALUES (%s, %s, %s, %s, %s, %s)
            """, [
                data['id'], data['id_samb_predict_models'], data['dictionary'],
                data['registration_date'], data['update_date'], data['state']
            ])
        except DatabaseError:
            return {'status': False, 'msj': 'No se realizó la escritura en samb_predict_models_data'}
        
        return {'status': True, 'msj': 'Success'}

    def add(self, data):
        
        # Primera inserción
        result_model = self.add_predict_model(data['samb_predict_models'])
        if not result_model['status']:
            return result_model
        
        # # Segunda inserción
        # result_data = self.add_predict_model_data(data['samb_predict_models_data'])
        # if not result_data['status']:
        #     return result_data
        
        return {'status': True, 'msj': 'Success'}
