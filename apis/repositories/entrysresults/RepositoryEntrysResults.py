from queue import Full
from django.db import connection,DatabaseError

class RepositoryEntrysResults():

    cursor_db = None

    def __init__(self):
        
        self.cursor_db = connection.cursor()

    def get_sums_entrys_date(self,date,id_methodology):

        try:

            query = "SELECT IFNULL(SUM(samb_entrys_results.result), 0) AS result FROM samb_entrys_results INNER JOIN samb_entrys ON samb_entrys.id=samb_entrys_results.id_entrys_id WHERE DATE_FORMAT(samb_entrys_results.registration_date, %s) = %s AND samb_entrys.id_methodology=%s"

            self.cursor_db.execute(query, ('%Y%m%d', date, id_methodology))

            result = self.cursor_db.fetchone() 
            
        except DatabaseError:

            return {'status':False,'msj':"Incidencia en la lectura de las samb_entrys_results leidas"}
        
        return {'status':True,'data':result[0],'msj':'Success'}
    
    def add(self,data):

        try:

            self.cursor_db.execute("INSERT INTO samb_entrys_results(samb_entrys_results.id,samb_entrys_results.result,samb_entrys_results.registration_date,samb_entrys_results.update_date,samb_entrys_results.condition,samb_entrys_results.id_entrys_id)VALUES(%s,%s,%s,%s,%s,%s)",[data['id_entry_result'],data['result_entry'],data['current_date'],data['current_date'],data['condition'],data['id_entry']])

        except DatabaseError:

            return {'status': False, 'message':'No se realizo la escritura en samb_entrys_results '}
        
        return {'status':True,'msj':'Success'}
    
    def get_entrys_results_curdate(self,id_methodology):

        try:

            query = "SELECT samb_entrys.type_account AS type_account, count(samb_entrys.id) AS total, SUM(CASE WHEN samb_entrys_results.result > 0 THEN 1 ELSE 0 END) AS positive_count, SUM(CASE WHEN samb_entrys_results.result < 0 THEN 1 ELSE 0 END) AS negative_count, IFNULL(SUM(samb_entrys_results.result), 0) AS result,(SUM(CASE WHEN samb_entrys_results.result > 0 THEN 1 ELSE 0 END) - SUM(CASE WHEN samb_entrys_results.result < 0 THEN 1 ELSE 0 END)) AS quantities FROM samb_entrys_results INNER JOIN samb_entrys ON samb_entrys.id = samb_entrys_results.id_entrys_id WHERE DATE(samb_entrys_results.registration_date) = CURDATE() AND samb_entrys.id_methodology=%s GROUP BY samb_entrys.type_account;"

            self.cursor_db.execute(query,id_methodology)

            rows = self.cursor_db.fetchall()

            columns = [col[0] for col in self.cursor_db.description]

            result = [dict(zip(columns, row)) for row in rows]

            return {'status':True,'message':'Success','result':result}
            
        except DatabaseError:

            return {'status':False,'message':'No se realizo la lectura de samb_entrys_results','result':'data not found'}
    
    def get_entrys_results_curdate_complete(self):

        try:

            query = "SELECT samb_entrys.type_account AS type_account, COUNT(samb_entrys.id) AS total, SUM(CASE WHEN samb_entrys_results.result > 0 THEN 1 ELSE 0 END) AS positive_count, SUM(CASE WHEN samb_entrys_results.result < 0 THEN 1 ELSE 0 END) AS negative_count, IFNULL(SUM(samb_entrys_results.result), 0) AS result,(SUM(CASE WHEN samb_entrys_results.result > 0 THEN 1 ELSE 0 END) - SUM(CASE WHEN samb_entrys_results.result < 0 THEN 1 ELSE 0 END)) AS quantities FROM samb_entrys_results INNER JOIN samb_entrys ON samb_entrys.id = samb_entrys_results.id_entrys_id WHERE DATE(samb_entrys_results.registration_date) = CURDATE() GROUP BY samb_entrys.type_account;"

            self.cursor_db.execute(query)

            rows = self.cursor_db.fetchall()

            columns = [col[0] for col in self.cursor_db.description]

            result = [dict(zip(columns, row)) for row in rows]

            return {'status':True,'message':'Success','result':result}
            
        except DatabaseError:

            return {'status':False,'message':'No se realizo la lectura de samb_entrys_results','result':'data not found'}
        
    def get_entrys_results_total(self,id_methodology):

        try:

            query = "SELECT samb_entrys.type_account AS type_account, COUNT(samb_entrys.id) AS total, SUM(CASE WHEN samb_entrys_results.result > 0 THEN 1 ELSE 0 END) AS positive_count, SUM(CASE WHEN samb_entrys_results.result < 0 THEN 1 ELSE 0 END) AS negative_count, IFNULL(SUM(samb_entrys_results.result), 0) AS result,(SUM(CASE WHEN samb_entrys_results.result > 0 THEN 1 ELSE 0 END) - SUM(CASE WHEN samb_entrys_results.result < 0 THEN 1 ELSE 0 END)) AS quantities FROM samb_entrys_results INNER JOIN samb_entrys ON samb_entrys.id = samb_entrys_results.id_entrys_id WHERE samb_entrys.id_methodology=%s GROUP BY samb_entrys.type_account"

            self.cursor_db.execute(query,id_methodology)

            rows = self.cursor_db.fetchall()

            columns = [col[0] for col in self.cursor_db.description]

            result = [dict(zip(columns, row)) for row in rows]

            return {'status':True,'message':'Success','result':result}
            
        except DatabaseError:

            return {'status':False,'message':'No se realizo la lectura en samb_entrys_results','result':'data not found'}
        
    def get_entrys_results_total_complete(self):

        try:

            query = "SELECT samb_entrys.type_account AS type_account, COUNT(samb_entrys.id) AS total, SUM(CASE WHEN samb_entrys_results.result > 0 THEN 1 ELSE 0 END) AS positive_count, SUM(CASE WHEN samb_entrys_results.result < 0 THEN 1 ELSE 0 END) AS negative_count, IFNULL(SUM(samb_entrys_results.result), 0) AS result,(SUM(CASE WHEN samb_entrys_results.result > 0 THEN 1 ELSE 0 END) - SUM(CASE WHEN samb_entrys_results.result < 0 THEN 1 ELSE 0 END)) AS quantities FROM samb_entrys_results INNER JOIN samb_entrys ON samb_entrys.id = samb_entrys_results.id_entrys_id GROUP BY samb_entrys.type_account"

            self.cursor_db.execute(query)

            rows = self.cursor_db.fetchall()

            columns = [col[0] for col in self.cursor_db.description]

            result = [dict(zip(columns, row)) for row in rows]

            return {'status':True,'message':'Success','result':result}
            
        except DatabaseError:

            return {'status':False,'message':'No se realizo la lectura en samb_entrys_results','result':'data not found'}
        
    def get_entrys_results_nom(self,day,id_methodology):

        try:

            query = "SELECT samb_entrys.type_account AS type_account, count(samb_entrys.id) AS total, SUM(CASE WHEN samb_entrys_results.result > 0 THEN 1 ELSE 0 END) AS positive_count, SUM(CASE WHEN samb_entrys_results.result < 0 THEN 1 ELSE 0 END) AS negative_count, IFNULL(SUM(samb_entrys_results.result), 0) AS result,(SUM(CASE WHEN samb_entrys_results.result > 0 THEN 1 ELSE 0 END) - SUM(CASE WHEN samb_entrys_results.result < 0 THEN 1 ELSE 0 END)) AS quantities FROM samb_entrys_results INNER JOIN samb_entrys ON samb_entrys.id = samb_entrys_results.id_entrys_id WHERE DAYOFWEEK(samb_entrys_results.registration_date) = %s AND samb_entrys.id_methodology=%s GROUP BY samb_entrys.type_account"

            self.cursor_db.execute(query,[day,id_methodology])

            rows = self.cursor_db.fetchall()

            columns = [col[0] for col in self.cursor_db.description]

            result = [dict(zip(columns, row)) for row in rows]

            return {'status':True,'message':'Success','result':result}
            
        except DatabaseError:

            return {'status':False,'message':'No se realizo la lectura en samb_entrys_results','result':'data not found'}
        
    def get_entrys_results_nom_complete(self,day):

        try:

            query = "SELECT samb_entrys.type_account AS type_account, COUNT(samb_entrys.id) AS total, SUM(CASE WHEN samb_entrys_results.result > 0 THEN 1 ELSE 0 END) AS positive_count, SUM(CASE WHEN samb_entrys_results.result < 0 THEN 1 ELSE 0 END) AS negative_count, IFNULL(SUM(samb_entrys_results.result), 0) AS result,(SUM(CASE WHEN samb_entrys_results.result > 0 THEN 1 ELSE 0 END) - SUM(CASE WHEN samb_entrys_results.result < 0 THEN 1 ELSE 0 END)) AS quantities FROM samb_entrys_results INNER JOIN samb_entrys ON samb_entrys.id = samb_entrys_results.id_entrys_id WHERE DAYOFWEEK(samb_entrys_results.registration_date) = %s GROUP BY samb_entrys.type_account;"

            self.cursor_db.execute(query,day)

            rows = self.cursor_db.fetchall()

            columns = [col[0] for col in self.cursor_db.description]

            result = [dict(zip(columns, row)) for row in rows]

            return {'status':True,'message':'Success','result':result}
            
        except DatabaseError:

            return {'status':False,'message':'No se realizo la lectura en samb_entrys_results','result':'data not found'}