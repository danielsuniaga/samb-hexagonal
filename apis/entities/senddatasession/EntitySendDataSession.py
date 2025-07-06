from decouple import config

import requests

import json

import uuid

class EntitySendDataSession():

    config = None

    def __init__(self):

        self.init_config()

    def generate_id(self):

        return uuid.uuid4().hex

    def init_config(self):

        self.config = {
            "api_url": config("API_CLOUD"),
            "headers": {
                "Content-Type": "application/json"
            },
            "Token": config("TOKEN_CONTAINERS", default=""),
            "Container": 
            {
                "Id": config("PROJECT_ID", default=""),
                "Name":config("PROJECT_NAME", default="")
            },
            "conditions":"1"
        }

        return True

    def get_config(self,key):

        return self.config.get(key, None)
    
    def get_config_container(self, key):
        result = self.get_config("Container")
        if result and key:
            for k, v in result.items():
                if k.lower() == key.lower():
                    return v
        return None

    def generate_message(self, entrys, result):
        container_name = self.get_config_container('Name')
        entry_id = self._get_entry_id(entrys)
        status_code = self._get_status_code(result)
        error_message = self._get_error_message(result)

        message = (
            f"REPORTS SEND TRUNCATED ({container_name})\n"
            f"Entry ID: {entry_id}\n"
            f"Response Status Code: {status_code}\n"
            f"Response Data: {error_message}\n"
        )
        return message

    def _get_entry_id(self, entrys):
        return entrys.get('id', 'N/A')

    def _get_status_code(self, result):
        return result.get('status_code', 'N/A')

    def _get_error_message(self, result):
        return result.get('error', 'N/A')

    
    def send_data(self, data):

        url = self.get_config("api_url") 

        headers =self.get_config("headers")

        try:

            response = requests.post(url, headers=headers, data=json.dumps(data))

            response.raise_for_status()

            try:

                return {
                    "status_code": response.status_code,
                    "data": response.json()
                }
            
            except ValueError:

                return {
                    "status_code": response.status_code,
                    "data": response.text,
                    "error": "Invalid JSON response"
                }
            
        except requests.RequestException as e:
            
            return {
                "status_code": response.status_code if 'response' in locals() else None,
                "data": response.text if 'response' in locals() else None,
                "error": str(e)
            }