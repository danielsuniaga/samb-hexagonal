from django.db import connection, DatabaseError

class RepositoryPredictModels:

    def __init__(self):
        self.cursor_db = connection.cursor()

    def add_predict_model(self, data):
        print("Adding predict model to the database")
        sql = """
            INSERT INTO samb_predict_models (
                id, id_models, id_cronjobs, accuracy_min, probability_min, model_name,
                prediction, prediction_label, probability_loss, probability_win,
                confidence, confidence_percentage, data_shape, features_count,
                registration_date, udpate_date, state
            ) VALUES (
                %s, %s, %s, %s, %s, %s,
                %s, %s, %s, %s,
                %s, %s, %s, %s,
                %s, %s, %s
            )
        """
        params = [
            data['id'],
            data['id_models'],
            data['id_cronjobs'],
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
        ]
        self.cursor_db.execute(sql, params)
        return self.cursor_db.lastrowid if hasattr(self.cursor_db, 'lastrowid') else data['id']

    def add_predict_model_data(self, data, predict_model_id):
        sql = """
            INSERT INTO samb_predict_models_data (
                id, id_samb_predict_models, dictionary, registration_date, update_date, state
            ) VALUES (
                %s, %s, %s, %s, %s, %s
            )
        """
        params = [
            data['id'],
            predict_model_id,
            data['dictionary'],
            data['registration_date'],
            data['update_date'],
            data['state']
        ]
        self.cursor_db.execute(sql, params)
        return self.cursor_db.lastrowid if hasattr(self.cursor_db, 'lastrowid') else data['id']

    def add(self, data):
        try:
            print("repository predict models add    ")
            # # Insert into samb_predict_models
            # predict_model_id = self.add_predict_model(data['samb_predict_models'])
            # # Insert into samb_predict_models_data
            # self.add_predict_model_data(data['samb_predict_models_data'], predict_model_id)
            return {'status': True, 'msj': 'Success'}
        except DatabaseError as e:
            return {'status': False, 'msj': f'Error: {str(e)}'}
