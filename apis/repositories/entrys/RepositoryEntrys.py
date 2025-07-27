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

            query = """WITH Last30Movements AS( 
                SELECT 
                    samb_movements.id_entry_id, 
                    samb_movements.open_candle, 
                    samb_movements.close_candle, 
                    samb_movements.high_candle, 
                    samb_movements.low_candle, 
                    ROW_NUMBER() OVER ( PARTITION BY samb_movements.id_entry_id ORDER BY samb_movements.epoch DESC) AS candle_position 
                FROM samb_movements 
            ), 
            PivotedCandles AS (
                SELECT 
                    id_entry_id,
                    MAX(CASE WHEN candle_position = 1 THEN open_candle END) AS candle_1_open,
                    MAX(CASE WHEN candle_position = 1 THEN high_candle END) AS candle_1_high,
                    MAX(CASE WHEN candle_position = 1 THEN low_candle END) AS candle_1_low,
                    MAX(CASE WHEN candle_position = 1 THEN close_candle END) AS candle_1_close,
                    MAX(CASE WHEN candle_position = 2 THEN open_candle END) AS candle_2_open,
                    MAX(CASE WHEN candle_position = 2 THEN high_candle END) AS candle_2_high,
                    MAX(CASE WHEN candle_position = 2 THEN low_candle END) AS candle_2_low,
                    MAX(CASE WHEN candle_position = 2 THEN close_candle END) AS candle_2_close,
                    MAX(CASE WHEN candle_position = 3 THEN open_candle END) AS candle_3_open,
                    MAX(CASE WHEN candle_position = 3 THEN high_candle END) AS candle_3_high,
                    MAX(CASE WHEN candle_position = 3 THEN low_candle END) AS candle_3_low,
                    MAX(CASE WHEN candle_position = 3 THEN close_candle END) AS candle_3_close,
                    MAX(CASE WHEN candle_position = 4 THEN open_candle END) AS candle_4_open,
                    MAX(CASE WHEN candle_position = 4 THEN high_candle END) AS candle_4_high,
                    MAX(CASE WHEN candle_position = 4 THEN low_candle END) AS candle_4_low,
                    MAX(CASE WHEN candle_position = 4 THEN close_candle END) AS candle_4_close,
                    MAX(CASE WHEN candle_position = 5 THEN open_candle END) AS candle_5_open,
                    MAX(CASE WHEN candle_position = 5 THEN high_candle END) AS candle_5_high,
                    MAX(CASE WHEN candle_position = 5 THEN low_candle END) AS candle_5_low,
                    MAX(CASE WHEN candle_position = 5 THEN close_candle END) AS candle_5_close,
                    MAX(CASE WHEN candle_position = 6 THEN open_candle END) AS candle_6_open,
                    MAX(CASE WHEN candle_position = 6 THEN high_candle END) AS candle_6_high,
                    MAX(CASE WHEN candle_position = 6 THEN low_candle END) AS candle_6_low,
                    MAX(CASE WHEN candle_position = 6 THEN close_candle END) AS candle_6_close,
                    MAX(CASE WHEN candle_position = 7 THEN open_candle END) AS candle_7_open,
                    MAX(CASE WHEN candle_position = 7 THEN high_candle END) AS candle_7_high,
                    MAX(CASE WHEN candle_position = 7 THEN low_candle END) AS candle_7_low,
                    MAX(CASE WHEN candle_position = 7 THEN close_candle END) AS candle_7_close,
                    MAX(CASE WHEN candle_position = 8 THEN open_candle END) AS candle_8_open,
                    MAX(CASE WHEN candle_position = 8 THEN high_candle END) AS candle_8_high,
                    MAX(CASE WHEN candle_position = 8 THEN low_candle END) AS candle_8_low,
                    MAX(CASE WHEN candle_position = 8 THEN close_candle END) AS candle_8_close,
                    MAX(CASE WHEN candle_position = 9 THEN open_candle END) AS candle_9_open,
                    MAX(CASE WHEN candle_position = 9 THEN high_candle END) AS candle_9_high,
                    MAX(CASE WHEN candle_position = 9 THEN low_candle END) AS candle_9_low,
                    MAX(CASE WHEN candle_position = 9 THEN close_candle END) AS candle_9_close,
                    MAX(CASE WHEN candle_position = 10 THEN open_candle END) AS candle_10_open,
                    MAX(CASE WHEN candle_position = 10 THEN high_candle END) AS candle_10_high,
                    MAX(CASE WHEN candle_position = 10 THEN low_candle END) AS candle_10_low,
                    MAX(CASE WHEN candle_position = 10 THEN close_candle END) AS candle_10_close,
                    MAX(CASE WHEN candle_position = 11 THEN open_candle END) AS candle_11_open,
                    MAX(CASE WHEN candle_position = 11 THEN high_candle END) AS candle_11_high,
                    MAX(CASE WHEN candle_position = 11 THEN low_candle END) AS candle_11_low,
                    MAX(CASE WHEN candle_position = 11 THEN close_candle END) AS candle_11_close,
                    MAX(CASE WHEN candle_position = 12 THEN open_candle END) AS candle_12_open,
                    MAX(CASE WHEN candle_position = 12 THEN high_candle END) AS candle_12_high,
                    MAX(CASE WHEN candle_position = 12 THEN low_candle END) AS candle_12_low,
                    MAX(CASE WHEN candle_position = 12 THEN close_candle END) AS candle_12_close,
                    MAX(CASE WHEN candle_position = 13 THEN open_candle END) AS candle_13_open,
                    MAX(CASE WHEN candle_position = 13 THEN high_candle END) AS candle_13_high,
                    MAX(CASE WHEN candle_position = 13 THEN low_candle END) AS candle_13_low,
                    MAX(CASE WHEN candle_position = 13 THEN close_candle END) AS candle_13_close,
                    MAX(CASE WHEN candle_position = 14 THEN open_candle END) AS candle_14_open,
                    MAX(CASE WHEN candle_position = 14 THEN high_candle END) AS candle_14_high,
                    MAX(CASE WHEN candle_position = 14 THEN low_candle END) AS candle_14_low,
                    MAX(CASE WHEN candle_position = 14 THEN close_candle END) AS candle_14_close,
                    MAX(CASE WHEN candle_position = 15 THEN open_candle END) AS candle_15_open,
                    MAX(CASE WHEN candle_position = 15 THEN high_candle END) AS candle_15_high,
                    MAX(CASE WHEN candle_position = 15 THEN low_candle END) AS candle_15_low,
                    MAX(CASE WHEN candle_position = 15 THEN close_candle END) AS candle_15_close,
                    MAX(CASE WHEN candle_position = 16 THEN open_candle END) AS candle_16_open,
                    MAX(CASE WHEN candle_position = 16 THEN high_candle END) AS candle_16_high,
                    MAX(CASE WHEN candle_position = 16 THEN low_candle END) AS candle_16_low,
                    MAX(CASE WHEN candle_position = 16 THEN close_candle END) AS candle_16_close,
                    MAX(CASE WHEN candle_position = 17 THEN open_candle END) AS candle_17_open,
                    MAX(CASE WHEN candle_position = 17 THEN high_candle END) AS candle_17_high,
                    MAX(CASE WHEN candle_position = 17 THEN low_candle END) AS candle_17_low,
                    MAX(CASE WHEN candle_position = 17 THEN close_candle END) AS candle_17_close,
                    MAX(CASE WHEN candle_position = 18 THEN open_candle END) AS candle_18_open,
                    MAX(CASE WHEN candle_position = 18 THEN high_candle END) AS candle_18_high,
                    MAX(CASE WHEN candle_position = 18 THEN low_candle END) AS candle_18_low,
                    MAX(CASE WHEN candle_position = 18 THEN close_candle END) AS candle_18_close,
                    MAX(CASE WHEN candle_position = 19 THEN open_candle END) AS candle_19_open,
                    MAX(CASE WHEN candle_position = 19 THEN high_candle END) AS candle_19_high,
                    MAX(CASE WHEN candle_position = 19 THEN low_candle END) AS candle_19_low,
                    MAX(CASE WHEN candle_position = 19 THEN close_candle END) AS candle_19_close,
                    MAX(CASE WHEN candle_position = 20 THEN open_candle END) AS candle_20_open,
                    MAX(CASE WHEN candle_position = 20 THEN high_candle END) AS candle_20_high,
                    MAX(CASE WHEN candle_position = 20 THEN low_candle END) AS candle_20_low,
                    MAX(CASE WHEN candle_position = 20 THEN close_candle END) AS candle_20_close,
                    MAX(CASE WHEN candle_position = 21 THEN open_candle END) AS candle_21_open,
                    MAX(CASE WHEN candle_position = 21 THEN high_candle END) AS candle_21_high,
                    MAX(CASE WHEN candle_position = 21 THEN low_candle END) AS candle_21_low,
                    MAX(CASE WHEN candle_position = 21 THEN close_candle END) AS candle_21_close,
                    MAX(CASE WHEN candle_position = 22 THEN open_candle END) AS candle_22_open,
                    MAX(CASE WHEN candle_position = 22 THEN high_candle END) AS candle_22_high,
                    MAX(CASE WHEN candle_position = 22 THEN low_candle END) AS candle_22_low,
                    MAX(CASE WHEN candle_position = 22 THEN close_candle END) AS candle_22_close,
                    MAX(CASE WHEN candle_position = 23 THEN open_candle END) AS candle_23_open,
                    MAX(CASE WHEN candle_position = 23 THEN high_candle END) AS candle_23_high,
                    MAX(CASE WHEN candle_position = 23 THEN low_candle END) AS candle_23_low,
                    MAX(CASE WHEN candle_position = 23 THEN close_candle END) AS candle_23_close,
                    MAX(CASE WHEN candle_position = 24 THEN open_candle END) AS candle_24_open,
                    MAX(CASE WHEN candle_position = 24 THEN high_candle END) AS candle_24_high,
                    MAX(CASE WHEN candle_position = 24 THEN low_candle END) AS candle_24_low,
                    MAX(CASE WHEN candle_position = 24 THEN close_candle END) AS candle_24_close,
                    MAX(CASE WHEN candle_position = 25 THEN open_candle END) AS candle_25_open,
                    MAX(CASE WHEN candle_position = 25 THEN high_candle END) AS candle_25_high,
                    MAX(CASE WHEN candle_position = 25 THEN low_candle END) AS candle_25_low,
                    MAX(CASE WHEN candle_position = 25 THEN close_candle END) AS candle_25_close,
                    MAX(CASE WHEN candle_position = 26 THEN open_candle END) AS candle_26_open,
                    MAX(CASE WHEN candle_position = 26 THEN high_candle END) AS candle_26_high,
                    MAX(CASE WHEN candle_position = 26 THEN low_candle END) AS candle_26_low,
                    MAX(CASE WHEN candle_position = 26 THEN close_candle END) AS candle_26_close,
                    MAX(CASE WHEN candle_position = 27 THEN open_candle END) AS candle_27_open,
                    MAX(CASE WHEN candle_position = 27 THEN high_candle END) AS candle_27_high,
                    MAX(CASE WHEN candle_position = 27 THEN low_candle END) AS candle_27_low,
                    MAX(CASE WHEN candle_position = 27 THEN close_candle END) AS candle_27_close,
                    MAX(CASE WHEN candle_position = 28 THEN open_candle END) AS candle_28_open,
                    MAX(CASE WHEN candle_position = 28 THEN high_candle END) AS candle_28_high,
                    MAX(CASE WHEN candle_position = 28 THEN low_candle END) AS candle_28_low,
                    MAX(CASE WHEN candle_position = 28 THEN close_candle END) AS candle_28_close,
                    MAX(CASE WHEN candle_position = 29 THEN open_candle END) AS candle_29_open,
                    MAX(CASE WHEN candle_position = 29 THEN high_candle END) AS candle_29_high,
                    MAX(CASE WHEN candle_position = 29 THEN low_candle END) AS candle_29_low,
                    MAX(CASE WHEN candle_position = 29 THEN close_candle END) AS candle_29_close,
                    MAX(CASE WHEN candle_position = 30 THEN open_candle END) AS candle_30_open,
                    MAX(CASE WHEN candle_position = 30 THEN high_candle END) AS candle_30_high,
                    MAX(CASE WHEN candle_position = 30 THEN low_candle END) AS candle_30_low,
                    MAX(CASE WHEN candle_position = 30 THEN close_candle END) AS candle_30_close
                FROM Last30Movements 
                WHERE candle_position <= 30 
                GROUP BY id_entry_id
            )
            SELECT 
                PivotedCandles.id_entry_id AS id_entry_id,
                CASE WHEN samb_entrys.type = 'CALL' THEN 1 WHEN samb_entrys.type = 'PUT' THEN 0 ELSE NULL END AS entry_type,
                CASE WHEN samb_entrys.condition_entry = 'CLOSE' THEN 1 ELSE NULL END AS entry_condition,
                samb_entrys.amount AS entry_amount,
                samb_entrys.registration_date AS entry_registration_date,
                CASE WHEN samb_entrys_results.result > 0 THEN 1 WHEN samb_entrys_results.result < 0 THEN 0 ELSE samb_entrys_results.result END AS entry_result,
                sma_30.value AS sma_30_value,
                sma_10.value AS sma_10_value,
                rsi.value AS rsi_value,
                -- Las 120 nuevas columnas OHLC de las 30 velas
                PivotedCandles.candle_1_open, PivotedCandles.candle_1_high, PivotedCandles.candle_1_low, PivotedCandles.candle_1_close,
                PivotedCandles.candle_2_open, PivotedCandles.candle_2_high, PivotedCandles.candle_2_low, PivotedCandles.candle_2_close,
                PivotedCandles.candle_3_open, PivotedCandles.candle_3_high, PivotedCandles.candle_3_low, PivotedCandles.candle_3_close,
                PivotedCandles.candle_4_open, PivotedCandles.candle_4_high, PivotedCandles.candle_4_low, PivotedCandles.candle_4_close,
                PivotedCandles.candle_5_open, PivotedCandles.candle_5_high, PivotedCandles.candle_5_low, PivotedCandles.candle_5_close,
                PivotedCandles.candle_6_open, PivotedCandles.candle_6_high, PivotedCandles.candle_6_low, PivotedCandles.candle_6_close,
                PivotedCandles.candle_7_open, PivotedCandles.candle_7_high, PivotedCandles.candle_7_low, PivotedCandles.candle_7_close,
                PivotedCandles.candle_8_open, PivotedCandles.candle_8_high, PivotedCandles.candle_8_low, PivotedCandles.candle_8_close,
                PivotedCandles.candle_9_open, PivotedCandles.candle_9_high, PivotedCandles.candle_9_low, PivotedCandles.candle_9_close,
                PivotedCandles.candle_10_open, PivotedCandles.candle_10_high, PivotedCandles.candle_10_low, PivotedCandles.candle_10_close,
                PivotedCandles.candle_11_open, PivotedCandles.candle_11_high, PivotedCandles.candle_11_low, PivotedCandles.candle_11_close,
                PivotedCandles.candle_12_open, PivotedCandles.candle_12_high, PivotedCandles.candle_12_low, PivotedCandles.candle_12_close,
                PivotedCandles.candle_13_open, PivotedCandles.candle_13_high, PivotedCandles.candle_13_low, PivotedCandles.candle_13_close,
                PivotedCandles.candle_14_open, PivotedCandles.candle_14_high, PivotedCandles.candle_14_low, PivotedCandles.candle_14_close,
                PivotedCandles.candle_15_open, PivotedCandles.candle_15_high, PivotedCandles.candle_15_low, PivotedCandles.candle_15_close,
                PivotedCandles.candle_16_open, PivotedCandles.candle_16_high, PivotedCandles.candle_16_low, PivotedCandles.candle_16_close,
                PivotedCandles.candle_17_open, PivotedCandles.candle_17_high, PivotedCandles.candle_17_low, PivotedCandles.candle_17_close,
                PivotedCandles.candle_18_open, PivotedCandles.candle_18_high, PivotedCandles.candle_18_low, PivotedCandles.candle_18_close,
                PivotedCandles.candle_19_open, PivotedCandles.candle_19_high, PivotedCandles.candle_19_low, PivotedCandles.candle_19_close,
                PivotedCandles.candle_20_open, PivotedCandles.candle_20_high, PivotedCandles.candle_20_low, PivotedCandles.candle_20_close,
                PivotedCandles.candle_21_open, PivotedCandles.candle_21_high, PivotedCandles.candle_21_low, PivotedCandles.candle_21_close,
                PivotedCandles.candle_22_open, PivotedCandles.candle_22_high, PivotedCandles.candle_22_low, PivotedCandles.candle_22_close,
                PivotedCandles.candle_23_open, PivotedCandles.candle_23_high, PivotedCandles.candle_23_low, PivotedCandles.candle_23_close,
                PivotedCandles.candle_24_open, PivotedCandles.candle_24_high, PivotedCandles.candle_24_low, PivotedCandles.candle_24_close,
                PivotedCandles.candle_25_open, PivotedCandles.candle_25_high, PivotedCandles.candle_25_low, PivotedCandles.candle_25_close,
                PivotedCandles.candle_26_open, PivotedCandles.candle_26_high, PivotedCandles.candle_26_low, PivotedCandles.candle_26_close,
                PivotedCandles.candle_27_open, PivotedCandles.candle_27_high, PivotedCandles.candle_27_low, PivotedCandles.candle_27_close,
                PivotedCandles.candle_28_open, PivotedCandles.candle_28_high, PivotedCandles.candle_28_low, PivotedCandles.candle_28_close,
                PivotedCandles.candle_29_open, PivotedCandles.candle_29_high, PivotedCandles.candle_29_low, PivotedCandles.candle_29_close,
                PivotedCandles.candle_30_open, PivotedCandles.candle_30_high, PivotedCandles.candle_30_low, PivotedCandles.candle_30_close
            FROM samb_entrys 
            INNER JOIN samb_entrys_results ON samb_entrys.id = samb_entrys_results.id_entrys_id 
            INNER JOIN PivotedCandles ON samb_entrys.id = PivotedCandles.id_entry_id 
            LEFT JOIN samb_indicators_entrys sma_30 ON sma_30.id_entry_id = samb_entrys.id AND sma_30.id_indicators_id = %s 
            LEFT JOIN samb_indicators_entrys sma_10 ON sma_10.id_entry_id = samb_entrys.id AND sma_10.id_indicators_id = %s 
            LEFT JOIN samb_indicators_entrys rsi ON rsi.id_entry_id = samb_entrys.id AND rsi.id_indicators_id = %s 
            WHERE samb_entrys_results.registration_date = ( SELECT MAX(registration_date) FROM samb_entrys_results AS ser WHERE ser.id_entrys_id = samb_entrys.id ) 
            ORDER BY samb_entrys.registration_date DESC"""

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

            query = "SELECT samb_entrys.id AS id, samb_entrys.type AS type_position, samb_entrys.type_account AS type_account, samb_entrys.number_candle AS number_candle, samb_entrys.condition_entry AS condition_entry, samb_entrys.amount AS amount, samb_entrys.registration_date AS registration_date, samb_entrys.update_date AS update_date, samb_entrys.condition AS conditions, samb_entrys.id_samb_cronjobs_id AS id_samb_cronjobs_id, samb_entrys.id_entry_platform AS id_entry_platform, samb_entrys.result_platform AS result_platform, samb_entrys.id_methodology AS id_methodology, samb_send_entrys.id AS id_send_entrys, samb_cronjobs.id AS samb_cronjobs_id, samb_cronjobs.start_date AS samb_cronjobs_start_date, samb_cronjobs.end_date AS samb_cronjobs_end_date, samb_cronjobs.condition AS samb_cronjobs_condition, samb_cronjobs.id_samb_api_id AS samb_cronjobs_id_samb_api_id, samb_cronjobs.id_samb_financial_asset_id AS samb_cronjobs_id_samb_financial_asset, samb_cronjobs.execution_time AS samb_cronjobs_execution_date, samb_apis.id AS samb_apis_id, samb_apis.description AS samb_apis_description, samb_apis.registration_date AS samb_apis_registration_date, samb_apis.update_date AS samb_apis_update_date, samb_apis.condition AS samb_apis_condition, samb_financial_asset.id AS samb_financial_asset_id, samb_financial_asset.description AS samb_financial_asset_description, samb_financial_asset.registration_date AS samb_financial_asset_registration_date, samb_financial_asset.update_date AS samb_financial_asset_update_date, samb_financial_asset.condition AS samb_financial_asset_condition, samb_platform.id AS samb_platform_id, samb_platform.description AS samb_platform_description, samb_platform.registration_date AS samb_platform_registration_date, samb_platform.update_date AS samb_platform_update_date, samb_platform.condition AS samb_platform_condition, samb_methodologys.id AS samb_methodologys_id, samb_methodologys.descriptions AS samb_methodologys_descriptions, samb_methodologys.permission_real AS samb_methodologys_permission_real, samb_methodologys.registration_date AS samb_methodologys_registration_date, samb_methodologys.update_date AS samb_methodologys_update_date, samb_methodologys.conditions AS samb_methodologys_conditions, samb_entrys_results.id AS samb_entrys_results_id, samb_entrys_results.result AS samb_entrys_results_result, samb_entrys_results.registration_date AS samb_entrys_results_registration_date, samb_entrys_results.update_date AS samb_entrys_results_update_date, samb_entrys_results.condition AS samb_entrys_results_condition FROM samb_entrys INNER JOIN samb_cronjobs ON samb_cronjobs.id = samb_entrys.id_samb_cronjobs_id INNER JOIN samb_apis ON samb_apis.id = samb_cronjobs.id_samb_api_id INNER JOIN samb_financial_asset ON samb_financial_asset.id = samb_cronjobs.id_samb_financial_asset_id INNER JOIN samb_platform ON samb_platform.id = samb_financial_asset.id_samb_platform_id INNER JOIN samb_methodologys ON samb_methodologys.id = samb_entrys.id_methodology INNER JOIN samb_entrys_results ON samb_entrys_results.id_entrys_id = samb_entrys.id LEFT JOIN samb_send_entrys ON samb_send_entrys.id_entrys = samb_entrys.id WHERE samb_entrys.condition = %s AND samb_send_entrys.id is null LIMIT 1000"

            parameters = (data['condition'])

            self.cursor_db.execute(query,parameters)

            result = self.cursor_db.fetchall()

            column_names = [desc[0] for desc in self.cursor_db.description]

            result_with_columns = [dict(zip(column_names, row)) for row in result]
            
        except DatabaseError:

            return {'status':False,'msj':"Incidencia en la lectura de los datos necesarios para las entradas de la sesion "}
                
        return {'status':True,'data':result_with_columns,'msj':'Success'}