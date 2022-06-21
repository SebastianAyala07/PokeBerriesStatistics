from flask import jsonify
from flask_restful import Resource

from app.common.berry_helper import BerryQueryHelper
from app.models.berry import Berry, BerryStatistics as BStatisticsModel

class BerryStatistics(Resource):
    def get(self):
        berries_json = BerryQueryHelper.get_all_berries()
        berries = Berry.create_berries_from_list(berries_json)
        statistics_berries = BStatisticsModel(berries)
        return jsonify(statistics_berries.describe_statistics_data())

