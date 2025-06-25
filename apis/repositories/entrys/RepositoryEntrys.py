from django.db import connection,DatabaseError

class RepositoryEntrys():

    cursor_db = None

    def __init__(self):
        
        self.cursor_db = connection.cursor()

    def add(self,data):

        try:

            self.cursor_db.execute("INSERT INTO samb_entrys(samb_entrys.id,samb_entrys.type,samb_entrys.type_account,samb_entrys.number_candle,samb_entrys.condition_entry,samb_entrys.amount,samb_entrys.registration_date,samb_entrys.update_date,samb_entrys.condition,samb_entrys.id_samb_cronjobs_id,samb_entrys.id_entry_platform,samb_entrys.id_methodology,samb_entrys.result_platform)VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",[data['id_entry'],data['type_operations'],data['mode'],data['candle_analized'],data['condition_entry'],data['amount'],data['current_date'],data['current_date'],data['condition'],data['id_cronjobs'],data['id_entry_platform'],data['id_methodology'],data['re_entry_platform']])

        except DatabaseError:

            return {'status': False, 'message':'No se realizo la escritura en samb_entrys'}

        return {'status':True,'msj':'Success'}
    

    def get_entrys_dataset_min(self,data):

        try:

            query = "WITH Last30Movements AS( SELECT samb_movements.id_entry_id, samb_movements.registration_date AS movement_registration_date, samb_movements.open_candle AS movement_open_candle, samb_movements.close_candle AS movement_close_candle, samb_movements.high_candle AS movement_high_candle, samb_movements.low_candle AS movement_low_candle, ROW_NUMBER() OVER ( PARTITION BY samb_movements.id_entry_id ORDER BY samb_movements.epoch DESC) AS rn FROM samb_movements ) SELECT Last30Movements.id_entry_id AS id_entry_id, CASE WHEN samb_entrys.type = 'CALL' THEN 1 WHEN samb_entrys.type = 'PUT' THEN 0 ELSE NULL END AS entry_type, CASE WHEN samb_entrys.condition_entry = 'CLOSE' THEN 1 ELSE NULL END AS entry_condition, samb_entrys.amount AS entry_amount, samb_entrys.registration_date AS entry_registration_date, CASE WHEN samb_entrys_results.result > 0 THEN 1 WHEN samb_entrys_results.result < 0 THEN 0 ELSE samb_entrys_results.result END AS entry_result, sma_30.value AS sma_30_value, sma_10.value AS sma_10_value, rsi.value AS rsi_value, Last30Movements.movement_open_candle, Last30Movements.movement_close_candle, Last30Movements.movement_high_candle, Last30Movements.movement_low_candle FROM samb_entrys INNER JOIN samb_entrys_results ON samb_entrys.id = samb_entrys_results.id_entrys_id INNER JOIN Last30Movements ON samb_entrys.id = Last30Movements.id_entry_id LEFT JOIN samb_indicators_entrys sma_30 ON sma_30.id_entry_id = samb_entrys.id AND sma_30.id_indicators_id = %s LEFT JOIN samb_indicators_entrys sma_10 ON sma_10.id_entry_id = samb_entrys.id AND sma_10.id_indicators_id = %s LEFT JOIN samb_indicators_entrys rsi ON rsi.id_entry_id = samb_entrys.id AND rsi.id_indicators_id = %s WHERE Last30Movements.rn <= 1 AND samb_entrys_results.registration_date = ( SELECT MAX(registration_date) FROM samb_entrys_results AS ser WHERE ser.id_entrys_id = samb_entrys.id ) ORDER BY samb_entrys.registration_date DESC;"

            parameters = (data['sma30'],data['sma10'],data['rsi10'])

            self.cursor_db.execute(query,parameters)

            result = self.cursor_db.fetchall()

            column_names = [desc[0] for desc in self.cursor_db.description]

            result_with_columns = [dict(zip(column_names, row)) for row in result]
            
        except DatabaseError:

            return {'status':False,'msj':"Incidencia en la lectura de los datos necesarios para crear el dataset  "}
                
        return {'status':True,'data':result_with_columns,'msj':'Success'}
    
    def get_entrys_dataset(self,data):

        try:

            query = "WITH Last30Movements AS( SELECT samb_movements.id_entry_id, samb_movements.registration_date AS movement_registration_date, samb_movements.open_candle AS movement_open_candle, samb_movements.close_candle AS movement_close_candle, samb_movements.high_candle AS movement_high_candle, samb_movements.low_candle AS movement_low_candle, ROW_NUMBER() OVER ( PARTITION BY samb_movements.id_entry_id ORDER BY samb_movements.epoch DESC) AS rn FROM samb_movements ) SELECT Last30Movements.id_entry_id AS id_entry_id, CASE WHEN samb_entrys.type = 'CALL' THEN 1 WHEN samb_entrys.type = 'PUT' THEN 0 ELSE NULL END AS entry_type, CASE WHEN samb_entrys.type_account = 'PRACTICE' THEN 0 WHEN samb_entrys.type_account = 'REAL' THEN 1 ELSE NULL END AS entry_type_account, samb_entrys.number_candle AS entry_number_candle, samb_entrys.registration_date AS entry_registration_date, CASE WHEN samb_entrys_results.result > 0 THEN 1 WHEN samb_entrys_results.result < 0 THEN 0 ELSE samb_entrys_results.result END AS entry_result, sma_30.value AS sma_30_value, sma_10.value AS sma_10_value, rsi.value AS rsi_value, Last30Movements.movement_open_candle, Last30Movements.movement_close_candle, Last30Movements.movement_high_candle, Last30Movements.movement_low_candle FROM samb_entrys INNER JOIN samb_entrys_results ON samb_entrys.id = samb_entrys_results.id_entrys_id INNER JOIN Last30Movements ON samb_entrys.id = Last30Movements.id_entry_id LEFT JOIN samb_indicators_entrys sma_30 ON sma_30.id_entry_id = samb_entrys.id AND sma_30.id_indicators_id = %s LEFT JOIN samb_indicators_entrys sma_10 ON sma_10.id_entry_id = samb_entrys.id AND sma_10.id_indicators_id = %s LEFT JOIN samb_indicators_entrys rsi ON rsi.id_entry_id = samb_entrys.id AND rsi.id_indicators_id = %s WHERE Last30Movements.rn <= 1 AND samb_entrys_results.registration_date = ( SELECT MAX(registration_date) FROM samb_entrys_results AS ser WHERE ser.id_entrys_id = samb_entrys.id ) ORDER BY samb_entrys.registration_date DESC;"

            parameters = (data['sma30'],data['sma10'],data['rsi10'])

            self.cursor_db.execute(query,parameters)

            result = self.cursor_db.fetchall()

            column_names = [desc[0] for desc in self.cursor_db.description]

            result_with_columns = [dict(zip(column_names, row)) for row in result]
            
        except DatabaseError:

            return {'status':False,'msj':"Incidencia en la lectura de los datos necesarios para crear el dataset  "}
                
        return {'status':True,'data':result_with_columns,'msj':'Success'}
    
    def get_entrys_send_session(self,data):

        try:

            query = "SELECT samb_entrys.id AS id, samb_entrys.type AS type_position, samb_entrys.type_account AS type_account, samb_entrys.number_candle AS number_candle, samb_entrys.condition_entry AS condition_entry, samb_entrys.amount AS amount, samb_entrys.registration_date AS registration_date, samb_entrys.update_date AS update_date, samb_entrys.condition AS conditions, samb_entrys.id_samb_cronjobs_id AS id_samb_cronjobs_id, samb_entrys.id_entry_platform AS id_entry_platform, samb_entrys.result_platform AS result_platform, samb_entrys.id_methodology AS id_methodology, samb_send_entrys.id AS id_send_entrys, samb_cronjobs.id AS samb_cronjobs_id, samb_cronjobs.start_date AS samb_cronjobs_start_date, samb_cronjobs.end_date AS samb_cronjobs_end_date, samb_cronjobs.condition AS samb_cronjobs_condition, samb_cronjobs.id_samb_api_id AS samb_cronjobs_id_samb_api_id, samb_cronjobs.id_samb_financial_asset_id AS samb_cronjobs_id_samb_financial_asset, samb_cronjobs.execution_time AS samb_cronjobs_execution_date, samb_apis.id AS samb_apis_id, samb_apis.description AS samb_apis_description, samb_apis.registration_date AS samb_apis_registration_date, samb_apis.update_date AS samb_apis_update_date, samb_apis.condition AS samb_apis_condition, samb_financial_asset.id AS samb_financial_asset_id, samb_financial_asset.description AS samb_financial_asset_description, samb_financial_asset.registration_date AS samb_financial_asset_registration_date, samb_financial_asset.update_date AS samb_financial_asset_update_date, samb_financial_asset.condition AS samb_financial_asset_condition, samb_platform.id AS samb_platform_id, samb_platform.description AS samb_platform_description, samb_platform.registration_date AS samb_platform_registration_date, samb_platform.update_date AS samb_platform_update_date, samb_platform.condition AS samb_platform_condition, samb_methodologys.id AS samb_methodologys_id, samb_methodologys.descriptions AS samb_methodologys_descriptions, samb_methodologys.permission_real AS samb_methodologys_permission_real, samb_methodologys.registration_date AS samb_methodologys_registration_date, samb_methodologys.update_date AS samb_methodologys_update_date, samb_methodologys.conditions AS samb_methodologys_conditions, samb_entrys_results.id AS samb_entrys_results_id, samb_entrys_results.result AS samb_entrys_results_result, samb_entrys_results.registration_date AS samb_entrys_results_registration_date, samb_entrys_results.update_date AS samb_entrys_results_update_date, samb_entrys_results.condition AS samb_entrys_results_condition FROM samb_entrys INNER JOIN samb_cronjobs ON samb_cronjobs.id = samb_entrys.id_samb_cronjobs_id INNER JOIN samb_apis ON samb_apis.id = samb_cronjobs.id_samb_api_id INNER JOIN samb_financial_asset ON samb_financial_asset.id = samb_cronjobs.id_samb_financial_asset_id INNER JOIN samb_platform ON samb_platform.id = samb_financial_asset.id_samb_platform_id INNER JOIN samb_methodologys ON samb_methodologys.id = samb_entrys.id_methodology INNER JOIN samb_entrys_results ON samb_entrys_results.id_entrys_id = samb_entrys.id LEFT JOIN samb_send_entrys ON samb_send_entrys.id_entrys = samb_entrys.id WHERE samb_entrys.condition = %s AND samb_send_entrys.id is null "

            parameters = (data['condition'])

            self.cursor_db.execute(query,parameters)

            result = self.cursor_db.fetchall()

            column_names = [desc[0] for desc in self.cursor_db.description]

            result_with_columns = [dict(zip(column_names, row)) for row in result]
            
        except DatabaseError:

            return {'status':False,'msj':"Incidencia en la lectura de los datos necesarios para las entradas de la sesion "}
                
        return {'status':True,'data':result_with_columns,'msj':'Success'}