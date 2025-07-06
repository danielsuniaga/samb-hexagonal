

import apis.entities.senddatasession.EntitySendDataSession as EntitySendDataSession

class ServicesSendDataSession:

    entity = None

    services_entrys = None

    services_indicators_entrys = None

    services_send_entrys = None

    services_indicators = None

    services_telegram = None

    def __init__(self):

        self.init_entity()

    def init_services_telegram(self, value):

        self.services_telegram = value

        return True

    def init_services_indicators(self, value):

        self.services_indicators = value

        return True

    def init_services_send_entrys(self,value):

        self.services_send_entrys = value

        return True

    def init_services_entrys(self,value):

        self.services_entrys = value

        return True
    
    def init_services_indicators_entrys(self,value):

        self.services_indicators_entrys = value

        return True

    def init_entity(self):

        self.entity = EntitySendDataSession.EntitySendDataSession()

        return True
    
    def get_config_container(self, key):

        return self.entity.get_config_container(key)
    
    def get_config(self, key):

        return self.entity.get_config(key)
    
    def get_indicators(self):

        return self.services_indicators.get_indicators()
    
    def generate_indicators(self, entrys):

        indicadors = self.get_indicators()

        result = []

        for name, data in indicadors.items():

            result.append({
                "name": name,
                "id": self.generate_id(),
                "id_indicators": data.get("id", ""),
                "id_container":self.get_config_container("Id"),
                "active": data.get("active", ""),
                "registration_date":entrys.get("registration_date", ""),
                "update_date": entrys.get("update_date", ""),
                "conditions": self.get_config("conditions")
            })

        return result
    
    def init_send_data(self,entry,data_indicators):

        return {
            "Token": self.get_config("Token"),
            "entry": {
                "id": entry.get("id", ""),
                "type_position": entry.get("type_position", ""),
                "type_account": entry.get("type_account", ""),
                "number_candle": entry.get("number_candle", ""),
                "condition_entry": entry.get("condition_entry", ""),
                "amount": entry.get("amount", 0),
                "registration_date": entry.get("registration_date", ""),
                "update_date": entry.get("update_date", ""),
                "conditions": entry.get("conditions", ""),
                "id_samb_cronjobs_id": entry.get("id_samb_cronjobs_id", ""),
                "id_entry_platform": entry.get("id_entry_platform", ""),
                "result_platform": entry.get("result_platform", ""),
                "id_methodology": entry.get("id_methodology", ""),
                "id_send_entrys": entry.get("id_send_entrys", ""),
                "samb_cronjobs_id": entry.get("samb_cronjobs_id", ""),
                "samb_cronjobs_start_date": entry.get("samb_cronjobs_start_date", ""),
                "samb_cronjobs_end_date": entry.get("samb_cronjobs_end_date", ""),
                "samb_cronjobs_condition": entry.get("samb_cronjobs_condition", ""),
                "samb_cronjobs_id_samb_api_id": entry.get("samb_cronjobs_id_samb_api_id", ""),
                "samb_cronjobs_id_samb_financial_asset": entry.get("samb_cronjobs_id_samb_financial_asset", ""),
                "samb_cronjobs_execution_date": entry.get("samb_cronjobs_execution_date", ""),
                "samb_apis_id": entry.get("samb_apis_id", ""),
                "samb_apis_description": entry.get("samb_apis_description", ""),
                "samb_apis_registration_date": entry.get("samb_apis_registration_date", ""),
                "samb_apis_update_date": entry.get("samb_apis_update_date", ""),
                "samb_apis_condition": entry.get("samb_apis_condition", ""),
                "samb_financial_asset_id": entry.get("samb_financial_asset_id", ""),
                "samb_financial_asset_description": entry.get("samb_financial_asset_description", ""),
                "samb_financial_asset_registration_date": entry.get("samb_financial_asset_registration_date", ""),
                "samb_financial_asset_update_date": entry.get("samb_financial_asset_update_date", ""),
                "samb_financial_asset_condition": entry.get("samb_financial_asset_condition", ""),
                "samb_platform_id": entry.get("samb_platform_id", ""),
                "samb_platform_description": entry.get("samb_platform_description", ""),
                "samb_platform_registration_date": entry.get("samb_platform_registration_date", ""),
                "samb_platform_update_date": entry.get("samb_platform_update_date", ""),
                "samb_platform_condition": entry.get("samb_platform_condition", ""),
                "samb_methodologys_id": entry.get("samb_methodologys_id", ""),
                "samb_methodologys_descriptions": entry.get("samb_methodologys_descriptions", ""),
                "samb_methodologys_permission_real": entry.get("samb_methodologys_permission_real", ""),
                "samb_methodologys_registration_date": entry.get("samb_methodologys_registration_date", ""),
                "samb_methodologys_update_date": entry.get("samb_methodologys_update_date", ""),
                "samb_methodologys_conditions": entry.get("samb_methodologys_conditions", ""),
                "samb_entrys_results_id": entry.get("samb_entrys_results_id", ""),
                "samb_entrys_results_result": entry.get("samb_entrys_results_result", ""),
                "samb_entrys_results_registration_date": entry.get("samb_entrys_results_registration_date", ""),
                "samb_entrys_results_update_date": entry.get("samb_entrys_results_update_date", ""),
                "samb_entrys_results_condition": entry.get("samb_entrys_results_condition", ""),
                "samb_indicadors_entrys": data_indicators,
                "samd_container_descripcion": self.get_config_container("Name"),
                "samd_container_id": self.get_config_container("Id"),
                "samb_indicators_container": self.generate_indicators(entry),
            }
        }
    
    def get_entrys_send(self):

        if self.services_entrys is None:

            raise ValueError("ServicesEntrys not initialized")

        return self.services_entrys.get_entrys_send_session()
    
    def init_send_data_entrys_indicators(self, entrys):

        return self.services_indicators_entrys.get_data_indicators_entrys(entrys)
    
    def add_send_entrys(self, entrys,result):

        if self.services_send_entrys is None:

            raise ValueError("ServicesSendEntrys not initialized")

        return self.services_send_entrys.add_send_entrys(entrys,result)

    def send_message_send_data(self, mensaje):

        if self.services_telegram is None:

            raise ValueError("ServicesTelegram not initialized")

        return self.services_telegram.send_message_send_data(mensaje)
    
    def generate_message_send_data(self, entrys,result):

        return self.entity.generate_message(entrys, result)
    
    def check_send_data(self, entrys,result):

        if result["status_code"] != 200:

            self.send_message_send_data(self.generate_message_send_data(entrys, result))
        
        self.add_send_entrys(entrys,result)

        return True
    
    def generate_id(self):

        if self.entity is None:

            raise ValueError("EntitySendDataSession not initialized")

        return self.entity.generate_id()
    
    def send_services(self, entrys):

        for entry in entrys:

            data_indicators = self.init_send_data_entrys_indicators(entry)

            data = self.init_send_data(entry, data_indicators)

            result = self.entity.send_data(data)
            
            self.check_send_data(entry, result)

        return True

    def send(self):

        data_entrys = self.get_entrys_send()

        return self.send_services(data_entrys)

