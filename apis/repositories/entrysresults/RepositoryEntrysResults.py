from django.db import connection

class RepositoryEntrysResults():

    cursor_db = None

    def __init__(self):
        
        self.cursor_db = connection.cursor()

    def get_sums_entrys_date(self,date):

        try:

            query = "SELECT IFNULL(SUM(samb_entrys_results.result), 0) as result FROM samb_entrys_results WHERE date_format(samb_entrys_results.registration_date, %s) = %s"

            self.cursor_db.execute(query, ('%Y%m%d', date))

            result = self.cursor_db.fetchone() 
            
        except Exception as err:

            return {'status':False,'msj':"Incidencia en la lectura de las samb_entrys_results leidas  "+str(err)}
        
        return {'status':True,'data':result[0],'msj':'Success'}
    
    def add(self,data):

        try:

            self.cursor_db.execute("INSERT INTO samb_entrys_results(samb_entrys_results.id,samb_entrys_results.result,samb_entrys_results.registration_date,samb_entrys_results.update_date,samb_entrys_results.condition,samb_entrys_results.id_entrys_id)VALUES(%s,%s,%s,%s,%s,%s)",[data['id_entry_result'],data['result_entry'],data['current_date'],data['current_date'],data['condition'],data['id_entry']])

        except Exception as err:

            return {'status': False, 'message':'No se realizo la escritura en samb_entrys_results '+str(err)}
        
        return {'status':True,'msj':'Success'}