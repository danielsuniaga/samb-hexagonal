from django.db import connection

class RepositoryMetricsEvaluationsModels():

    cursor_db = None

    def __init__(self):
        
        self.cursor_db = connection.cursor()

    def add(self,data):
        
        try:

            self.cursor_db.execute("INSERT INTO samb_metrics_evaluations_models(samb_metrics_evaluations_models.id, samb_metrics_evaluations_models.id_models, samb_metrics_evaluations_models.accuracy, samb_metrics_evaluations_models.precisions, samb_metrics_evaluations_models.recall, samb_metrics_evaluations_models.f1_score, samb_metrics_evaluations_models.registration_date, samb_metrics_evaluations_models.update_date, samb_metrics_evaluations_models.state) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s)", [data['id'], data['id_models'], data['accuracy'], data['precisions'], data['recall'], data['f1_score'], data['registration_date'], data['update_date'], data['state']])

        except Exception as err:

            return {'status': False, 'msj':'No se realizo la escritura en samb_metrics_evaluations_models: '+str(err)}

        return {'status':True,'msj':'Success'}