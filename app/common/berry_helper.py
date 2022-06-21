import requests
import os
from cachetools import cached, TTLCache
from datetime import timedelta, datetime

BASE_BERRY_ENDPOINT_URL = os.getenv('BASE_BERRY_ENDPOINT_URL')

cache = TTLCache(maxsize=100, ttl=timedelta(hours=2), timer=datetime.now)

class BerryQueryHelper():

    @staticmethod
    @cached(cache)
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
    @cached(cache)
    def get_berry_by_id(id):
        response = requests.get(
            BASE_BERRY_ENDPOINT_URL + f"{id}/"
        )
        return response.json()
