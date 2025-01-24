from django.db import connection

class RepositoryReports():

    cursor_db = None

    def __init__(self):

        self.cursor_db = connection.cursor()

    def add(self,data):

        try:

            self.cursor_db.execute("INSERT INTO samb_reports(samb_reports.id,samb_reports.description,samb_reports.registration_date,samb_reports.update_date,samb_reports.state)VALUES(%s,%s,%s,%s,%s)",[data['id'], data['description'], data['fecha'], data['fecha'], data['condition']])

        except Exception as err:

            return {'status': False, 'msj':'No se realizo la escritura en samb_reports'+str(err)}

        return {'status':True,'msj':'Success'}