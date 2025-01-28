from django.db import connection

class RepositoryEntrys():

    cursor_db = None

    def __init__(self):
        
        self.cursor_db = connection.cursor()

    def add(self,data):

        try:

            self.cursor_db.execute("INSERT INTO samb_entrys(samb_entrys.id,samb_entrys.type,samb_entrys.type_account,samb_entrys.number_candle,samb_entrys.condition_entry,samb_entrys.amount,samb_entrys.registration_date,samb_entrys.update_date,samb_entrys.condition,samb_entrys.id_samb_cronjobs_id,samb_entrys.id_entry_platform,samb_entrys.result_platform)VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",[data['id_entry'],data['type_operations'],data['mode'],data['candle_analized'],data['condition_entry'],data['amount'],data['current_date'],data['current_date'],data['condition'],data['id_cronjobs'],data['id_entry_platform'],data['re_entry_platform']])

        except Exception as err:

            return {'status': False, 'message':'No se realizo la escritura en samb_entrys'+str(err)}

        return {'status':True,'msj':'Success'}
    
    def get_entrys_dataset(self,data):

        try:

            query = "WITH Last30Movements AS( SELECT samb_movements.id_entry_id, samb_movements.registration_date AS movement_registration_date, samb_movements.open_candle AS movement_open_candle, samb_movements.close_candle AS movement_close_candle, samb_movements.high_candle AS movement_high_candle, samb_movements.low_candle AS movement_low_candle, ROW_NUMBER() OVER ( PARTITION BY samb_movements.id_entry_id ORDER BY samb_movements.epoch DESC) AS rn FROM samb_movements ) SELECT Last30Movements.id_entry_id AS id_entry_id, CASE WHEN samb_entrys.type = 'CALL' THEN 1 WHEN samb_entrys.type = 'PUT' THEN 0 ELSE NULL END AS entry_type, CASE WHEN samb_entrys.type_account = 'PRACTICE' THEN 0 WHEN samb_entrys.type_account = 'REAL' THEN 1 ELSE NULL END AS entry_type_account, samb_entrys.number_candle AS entry_number_candle, CASE WHEN samb_entrys.condition_entry = 'CLOSE' THEN 1 ELSE NULL END AS entry_condition, samb_entrys.amount AS entry_amount, samb_entrys.registration_date AS entry_registration_date, CASE WHEN samb_entrys_results.result > 0 THEN 1 WHEN samb_entrys_results.result < 0 THEN 0 ELSE samb_entrys_results.result END AS entry_result, sma_30.value AS sma_30_value, sma_10.value AS sma_10_value, rsi.value AS rsi_value, Last30Movements.movement_open_candle, Last30Movements.movement_close_candle, Last30Movements.movement_high_candle, Last30Movements.movement_low_candle FROM samb_entrys INNER JOIN samb_entrys_results ON samb_entrys.id = samb_entrys_results.id_entrys_id INNER JOIN Last30Movements ON samb_entrys.id = Last30Movements.id_entry_id LEFT JOIN samb_indicators_entrys sma_30 ON sma_30.id_entry_id = samb_entrys.id AND sma_30.id_indicators_id = %s LEFT JOIN samb_indicators_entrys sma_10 ON sma_10.id_entry_id = samb_entrys.id AND sma_10.id_indicators_id = %s LEFT JOIN samb_indicators_entrys rsi ON rsi.id_entry_id = samb_entrys.id AND rsi.id_indicators_id = %s WHERE Last30Movements.rn <= 1 AND samb_entrys_results.registration_date = ( SELECT MAX(registration_date) FROM samb_entrys_results AS ser WHERE ser.id_entrys_id = samb_entrys.id ) ORDER BY samb_entrys.registration_date DESC;"

            parameters = (data['sma30'],data['sma10'],data['rsi10'])

            self.cursor_db.execute(query,parameters)

            result = self.cursor_db.fetchall()

            column_names = [desc[0] for desc in self.cursor_db.description]

            result_with_columns = [dict(zip(column_names, row)) for row in result]
            
        except Exception as err:

            return {'status':False,'msj':"Incidencia en la lectura de los datos necesarios para crear el dataset  "+str(err)}
                
        return {'status':True,'data':result_with_columns,'msj':'Success'}