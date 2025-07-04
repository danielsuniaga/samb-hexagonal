from decouple import config

import requests

import json

class EntitySendDataSession():

    config = None

    def __init__(self):

        self.init_config()

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