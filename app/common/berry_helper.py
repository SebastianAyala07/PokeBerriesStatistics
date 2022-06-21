import json
import requests
import os

BASE_BERRY_ENDPOINT_URL = os.getenv('BASE_BERRY_ENDPOINT_URL')

class BerryQueryHelper():

    @staticmethod
    def get_all_berries():
        response = requests.get(
            BASE_BERRY_ENDPOINT_URL,
            {
                "offset": 0,
                "limit": 1000
            }
        )
        data_to_return = response.json()
        return data_to_return.get("results")

    @staticmethod
    def get_berry_by_id(id):
        response = requests.get(
            BASE_BERRY_ENDPOINT_URL + f"{id}/"
        )
        return response.json()
