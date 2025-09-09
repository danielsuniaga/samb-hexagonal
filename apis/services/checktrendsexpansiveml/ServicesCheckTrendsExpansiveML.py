class ServicesCheckTrendsExpansiveML:
    # --- Servicios base de CheckTrendsExpansive ---
    ServicesDeriv = None
    ServicesMethodologyTrendsExpansiveML = None
    ServicesManagerDays = None
    ServicesEvents = None
    ServicesDates = None    
    ServicesIndicators = None
    ServicesEntrysResults = None
    ServicesMovements = None
    ServicesCronjobs = None
    ServicesPlatform = None
    ServicesEntrys = None
    ServicesIndicatorsEntrys = None
    ServicesTelegram = None 
    # --- Servicios ML (heredados de MinusML) ---
    ServicesModels = None
    ServicesMethodologys = None
    ServicesEntrysPredictModels = None

    # --- Métodos de inicialización de servicios base ---
    def init_services_telegram(self, value):
        self.ServicesTelegram = value
        return True

    def init_services_indicators_entrys(self, value):
        self.ServicesIndicatorsEntrys = value
        return True

    def init_services_entrys(self, value):
        self.ServicesEntrys = value
        return True

    def init_services_platform(self, value):
        self.ServicesPlatform = value
        return True

    def init_services_cronjobs(self, value):
        self.ServicesCronjobs = value
        return True

    def init_services_movements(self, value):
        self.ServicesMovements = value
        return True

    def init_services_entrys_results(self, value):
        self.ServicesEntrysResults = value
        return True

    def init_services_indicators(self, value):
        self.ServicesIndicators = value
        return True

    def init_services_events(self, value):
        self.ServicesEvents = value
        return True
    
    def init_services_dates(self, value):
        self.ServicesDates = value
        return True

    def init_services_manager_days(self, value):
        self.ServicesManagerDays = value
        return True

    def init_services_methodology_trends_expansive_ml(self, value):
        self.ServicesMethodologyTrendsExpansiveML = value
        return True

    def init_services_deriv(self, value):
        self.ServicesDeriv = value
        return True

    # --- Métodos de inicialización de servicios ML ---
    def init_services_models(self, value):
        self.ServicesModels = value
        return True

    def init_services_methodologys(self, value):
        self.ServicesMethodologys = value
        return True

    def init_services_entrys_predict_models(self, value):
        self.ServicesEntrysPredictModels = value
        return True

    # --- Métodos base (async, get, set, check, add, etc.) ---
    async def init(self):
        return await self.ServicesDeriv.init()
    
    def get_id_methodology(self):
        return self.ServicesMethodologyTrendsExpansiveML.get_id()
    
    def get_type_manager_days(self, day):
        id_methodology = self.get_id_methodology()
        return self.ServicesManagerDays.get_type_manager_days(day, id_methodology)
    
    def check_mode(self, day):
        return self.get_type_manager_days(day)
    
    async def check_broker(self, mode):
        return await self.ServicesDeriv.check(mode)
    
    async def set_balance(self, day):
        result = self.check_mode(day)
        if result:
            return await self.check_broker(result)
        return True
    
    async def closed(self):
        return await self.ServicesDeriv.closed()
    
    def get_current_date_mil_dynamic(self):
        return self.ServicesDates.get_current_date_mil_dynamic()
    
    def init_data_set_events_field_result(self, date, result=0):
        return date + " Result: " + str(result) + " "
    
    def set_events_field(self, field, value):
        return self.ServicesEvents.set_events_field(field, value)
    
    async def get_candles(self):
        return await self.ServicesDeriv.get_candles()
    
    def check_candles(self, candles):
        return self.ServicesMethodologyTrendsExpansiveML.check_candles(candles)
    
    def get_rsi(self, candles):
        return self.ServicesIndicators.generate_rsi(candles)
    
    def get_sma_short_services(self):
        return self.ServicesIndicators.get_sma_short()
    
    def get_sma_short(self, candles):
        indicators = self.get_sma_short_services()
        return self.ServicesIndicators.generate_sma(candles, indicators)
    
    def get_sma_long(self, candles):
        indicators = self.ServicesIndicators.get_sma_long()
        return self.ServicesIndicators.generate_sma(candles, indicators)
    
    def get_candle_last(self, candle):
        return self.ServicesIndicators.get_candles_last(candle)
    
    def init_data_indicators(self, candles):
        return {
            'rsi': self.get_rsi(candles),
            'sma_short': self.get_sma_short(candles),
            'sma_long': self.get_sma_long(candles),
            'last_candle': self.get_candle_last(candles),
        }
    
    def check_rsi(self, rsi):
        return self.ServicesMethodologyTrendsExpansiveML.check_rsi(rsi)
    
    def check_sma(self, sma, last_candle):
        return self.ServicesMethodologyTrendsExpansiveML.check_sma(sma, last_candle)
    
    def init_result_indicators(self, indicators):
        return {
            'rsi': self.check_rsi(indicators['rsi']),
            'sma_short': self.check_sma(indicators['sma_short'], indicators['last_candle']),
            'sma_long': self.check_sma(indicators['sma_long'], indicators['last_candle']),
        }

    def add_result_indicators(self, result_indicators):
        return self.ServicesMethodologyTrendsExpansiveML.add_indicator(result_indicators)  

    def check_result_indicators(self, result_indicators):
        return self.ServicesMethodologyTrendsExpansiveML.check_result_indicators(result_indicators)  
    
    def check_indicators(self, result, candles):
        if not result:
            return False
        
        data_indicators = self.init_data_indicators(candles)
        result_indicators = self.init_result_indicators(data_indicators)
        self.add_result_indicators(data_indicators)
        
        return self.check_result_indicators(result_indicators)
    
    def check_monetary_filter_services(self, result):
        return self.ServicesMethodologyTrendsExpansiveML.check_monetary_filters(result)
    
    def get_current_date_only(self):
        return self.ServicesDates.get_current_date_only()
    
    def sum_entrys_dates(self):
        id_methodology = self.get_id_methodology()
        return self.ServicesEntrysResults.get_sums_entrys_date(self.get_current_date_only(), id_methodology)
    
    def get_profit(self):
        return self.ServicesManagerDays.get_profit()
    
    def get_loss(self): 
        return self.ServicesManagerDays.get_loss()
    
    def init_data_monetary_filter(self):
        return {
            'sum_entrys_dates': self.sum_entrys_dates(),
            'profit': self.get_profit(),
            'loss': self.get_loss(),
        }
    
    def check_monetary_filter(self, result):
        if not result:
            return False
        
        data = self.init_data_monetary_filter()
        return self.check_monetary_filter_services(data)
    
    def get_money(self):
        return self.ServicesManagerDays.get_money()
    
    def get_type_entry(self):
        return self.ServicesMethodologyTrendsExpansiveML.get_type_entry_positions()
    
    def get_duration(self):
        return self.ServicesDeriv.get_duration()
    
    def get_duration_unit(self):    
        return self.ServicesDeriv.get_duration_unit()
    
    def get_par(self):
        return self.ServicesDeriv.get_par()
    
    def init_data_add_entry(self):
        return {
            'amount': int(self.get_money()),
            'contract_type': self.get_type_entry(),
            'duration': int(self.get_duration()),
            'duration_unit': self.get_duration_unit(),
            'symbol': self.get_par()
        }
    
    async def add_entry_broker(self, result):
        if not result:
            return False
        
        return await self.ServicesDeriv.add_entry(self.init_data_add_entry())
    
    def set_candles_movements(self, candles):
        return self.ServicesMovements.set_candles(candles)
    
    def set_candles_positions(self, candles):
        return self.ServicesMethodologyTrendsExpansiveML.set_result_candles(candles)
    
    def add_result_positions_mode(self, data, mode):
        return self.ServicesDeriv.add_result_positions_mode(data, mode)
    
    def get_mode(self):
        return self.ServicesManagerDays.get_mode()
    
    def add_result_positions_candle_analisys(self, data, candle):
        return self.ServicesDeriv.add_result_positions_candle_analisys(data, candle)
    
    def get_candle_removed(self):
        return self.ServicesMethodologyTrendsExpansiveML.get_candle_removed()
    
    def add_result_positions_condition_entry(self, data, condition):
        return self.ServicesDeriv.add_result_positions_condition_entry(data, condition)
    
    def get_condition_entry(self):
        return self.ServicesMethodologyTrendsExpansiveML.get_condition_entry()
    
    def add_result_positions_amount(self, data, amount):
        return self.ServicesDeriv.add_result_positions_amount(data, amount)
    
    def add_result_positions_current_date(self, data, date):
        return self.ServicesDeriv.add_result_positions_current_date(data, date)
    
    def get_current_date_hour(self):
        return self.ServicesDates.get_current_date_hour()
    
    def add_result_positions_id_cronjobs(self, data, id_cronjobs):
        return self.ServicesDeriv.add_result_positions_id_cronjobs(data, id_cronjobs)
    
    def get_id_cronjobs(self):
        return self.ServicesCronjobs.get_id_cronjobs()
    
    def add_result_positions_re_platform(self, data, re_platform):    
        return self.ServicesDeriv.add_result_positions_re_platform(data, re_platform)
    
    def get_re_platform(self):
        return self.ServicesPlatform.get_re_platform_deriv()
    
    def add_result_positions_id_methodology(self, data, id_methodology):
        return self.ServicesDeriv.add_result_positions_id_methodology(data, id_methodology) 
    
    def init_set_result_positions(self, result):
        return [
            (self.add_result_positions_mode, self.get_mode()),
            (self.add_result_positions_candle_analisys, self.get_candle_removed()),
            (self.add_result_positions_condition_entry, self.get_condition_entry()),
            (self.add_result_positions_amount, self.get_money()),
            (self.add_result_positions_current_date, self.get_current_date_hour()),
            (self.add_result_positions_id_cronjobs, self.get_id_cronjobs()),
            (self.add_result_positions_re_platform, self.get_re_platform()),
            (self.add_result_positions_id_methodology, self.get_id_methodology()),
        ]
    
    def set_result_positions(self, result):
        result_positions_methods = self.init_set_result_positions(result)
        for method, value in result_positions_methods:
            result = method(result, value)
        return result
    
    def set_result_positions_entity(self, result):
        return self.ServicesMethodologyTrendsExpansiveML.set_result_entrys(result)
    
    def add_entrys(self, result):
        return self.ServicesEntrys.add_entrys(result)
    
    def get_indicators(self):
        return self.ServicesMethodologyTrendsExpansiveML.get_indicators()
    
    def get_data_entrys(self):
        return self.ServicesEntrys.get_data_entity()
    
    def add_result_positions_data_entrys(self, result, data):
        return self.ServicesDeriv.add_result_positions_data_entrys(result, data)
    
    def set_result_indicators(self, result):
        result = self.add_result_positions_current_date(result, self.get_current_date_hour())
        result = self.add_result_positions_data_entrys(result, self.get_data_entrys())
        return result
    
    def get_result_entrys_result(self):
        return self.ServicesMethodologyTrendsExpansiveML.get_result_entrys_result()
    
    def add_entrys_results_persistence(self):
        data = self.get_result_entrys_result()
        data_indicators = self.set_result_indicators(self.get_indicators())
        result = self.ServicesEntrysResults.add_persistence(data, data_indicators)
        if not result['status']:
            return False
        return self.add_entrys_predict_models(data_indicators)
    
    def add_movements_persistence(self, data):
        result = self.ServicesMovements.add_persistence(data)
        if not result['status']:
            return False
        return self.add_entrys_results_persistence()
    
    def add_indicators_entrys_persistence(self):
        data = self.set_result_indicators(self.get_indicators())
        result = self.ServicesIndicatorsEntrys.add_persistence(data)
        if not result['status']:
            return False
        return self.add_movements_persistence(data)
    
    def get_name_methodology(self):
        return self.ServicesMethodologyTrendsExpansiveML.get_name()
    
    def generate_message_add_entry(self):
        name_methodology = self.get_name_methodology()
        return self.ServicesTelegram.generate_message_add_entry(name_methodology)
    
    def send_report_management(self, result):
        if not result:
            return False
        
        mensaje = self.generate_message_add_entry()
        return self.ServicesTelegram.send_message(mensaje, self.get_current_date_hour())
    
    def add_data_entrys_results_reports(self, data):
        return self.ServicesTelegram.add_data_entrys(data)

    # --- Métodos ML (heredados de ServicesCheckTrendsMinusML) ---
    def get_config_id_predict_models(self):
        return self.ServicesModels.get_config_id_predict_models()
    
    def add_entrys_predict_models(self, data_indicators):
        data_indicators['id_predict_models'] = self.get_config_id_predict_models()
        result = self.ServicesEntrysPredictModels.add(data_indicators)
        if not result['status']:
            return False
        return True
    
    def get_methodology_description_number_by_id(self, id_methodology):
        return self.ServicesMethodologys.get_methodology_description_number_by_id(id_methodology)
    
    def generate_entry_type_value(self, entry_type):
        if entry_type == 'CALL':
            return 1
        elif entry_type == 'PUT':
            return 0
        else:
            return None
    
    def generate_entry_condition_value(self, condition):
        if condition == 'CLOSE':
            return 1
        else:
            return None
    
    def init_check_predict_models(self, candles):
        data_indicators = self.get_indicators()
        return {
            'description_methodology': self.get_methodology_description_number_by_id(self.get_id_methodology()),
            'entry_type': self.generate_entry_type_value(self.get_type_entry()),
            'entry_condition': self.generate_entry_condition_value(self.get_condition_entry()),
            'entry_amount': self.get_money(),
            'sma_30_value': data_indicators['sma_long'],
            'sma_10_value': data_indicators['sma_short'],
            'rsi_value': data_indicators['rsi'],
            'candles': candles
        }
    
    def check_predict_models(self, result, candles):
        if not result:
            return False
        data_services = self.init_check_predict_models(candles)
        return self.ServicesModels.check_predict_models(data_services)
    
    def add_entry_persistence(self, result, candles):
        if not result:
            return False
        
        self.set_candles_movements(candles)
        result = self.set_result_positions(result)
        self.set_result_positions_entity(result)
        self.set_candles_positions(candles)
        result = self.add_entrys(result)
        
        if not result['status']:
            return False
        
        return self.add_indicators_entrys_persistence()
    
    # --- Método principal loops (combinando ambas metodologías) ---
    async def loops(self):
        self.set_events_field('init_loop', self.get_current_date_mil_dynamic())
        
        result_candles = await self.get_candles()
        self.set_events_field('get_candles', self.get_current_date_mil_dynamic())
        
        result = self.check_candles(result_candles)
        self.set_events_field('check_candles', self.get_current_date_mil_dynamic())
        
        result = self.check_indicators(result, result_candles)
        self.set_events_field('generate_indicators', self.get_current_date_mil_dynamic())

        result = self.check_monetary_filter(result)
        self.set_events_field('get_filter_monetary', self.get_current_date_mil_dynamic())

        # Integración ML - verificación de modelos predictivos
        result = self.check_predict_models(result, result_candles)
        self.set_events_field('get_model_ml', self.get_current_date_mil_dynamic())

        result = await self.add_entry_broker(result)
        self.add_data_entrys_results_reports(result)
        self.set_events_field('add_positions_brokers', self.get_current_date_mil_dynamic())

        result = self.add_entry_persistence(result, result_candles)
        self.set_events_field('add_persistence', self.get_current_date_mil_dynamic())

        self.send_report_management(result)

        return True
