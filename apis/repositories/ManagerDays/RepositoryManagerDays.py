from django.db import connection, DatabaseError

class RepositoryManagerDays():

    cursor_db = None

    def __init__(self):
        
        self.cursor_db = connection.cursor()
    
    def get_type_manager_day(self,day,id_methodology):

        try:

            query = """SELECT samb_manager_days.type AS type, samb_manager_days.money AS money, samb_manager_days.profit AS profit, samb_manager_days.loss AS loss, samb_methodologys.permission_real AS permision_real FROM samb_manager_days INNER JOIN samb_methodologys ON samb_manager_days.id_methodology=samb_methodologys.id WHERE samb_manager_days.day_number = %s AND samb_manager_days.id_methodology = %s"""

            self.cursor_db.execute(query, [day, id_methodology])

            result = self.cursor_db.fetchall()

            column_names = [desc[0] for desc in self.cursor_db.description]

            result_with_columns = [dict(zip(column_names, row)) for row in result]
            
        except DatabaseError:

            return {'status':False,'msj':"Incidencia en la lectura de las samb_manager_days leidas"}
                
        return {'status':True,'data':result_with_columns[0],'msj':'Success'}