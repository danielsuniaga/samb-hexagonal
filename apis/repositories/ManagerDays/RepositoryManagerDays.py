from django.db import connection

class RepositoryManagerDays():

    cursor_db = None

    def __init__(self):
        
        self.cursor_db = connection.cursor()
    
    def get_type_manager_day(self,day):

        try:

            query = "SELECT samb_manager_days.type AS type, samb_manager_days.money AS money, samb_manager_days.profit AS profit, samb_manager_days.loss AS loss FROM samb_manager_days WHERE samb_manager_days.day_number = %s"

            self.cursor_db.execute(query, day)

            result = self.cursor_db.fetchall()

            column_names = [desc[0] for desc in self.cursor_db.description]

            result_with_columns = [dict(zip(column_names, row)) for row in result]
            
        except Exception as err:

            return {'status':False,'msj':"Incidencia en la lectura de las samb_manager_days leidas  "+str(err)}
                
        return {'status':True,'data':result_with_columns[0],'msj':'Success'}