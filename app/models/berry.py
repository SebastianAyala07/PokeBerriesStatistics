from app.common.berry_helper import BerryQueryHelper
import pandas as pd

class Berry():

    def __init__(self, name, url):
        self.name = name
        self.url = url
        self.__set_id()
        self._consult_update_growth_time()

    @staticmethod
    def create_berries_from_list(berries_json):
        berries_to_return = []
        for berry_data in berries_json:
            temp_berry_obj = Berry(**berry_data)
            berries_to_return.append(temp_berry_obj)
        return berries_to_return

    def __set_id(self):
        self.id = int(self.url.split("berry/")[1][:-1])

    def _consult_update_growth_time(self):
        response = BerryQueryHelper.get_berry_by_id(self.id)
        self.growth_time = response.get("growth_time")
        return self.growth_time

class BerryStatistics():

    def __init__(self, berries):
        self.berries = berries if isinstance(berries, list) else None

    def describe_statistics_data(self):
        names = []
        growth_time_list = []
        for berry in self.berries:
            names.append(berry.name)
            growth_time_list.append(berry.growth_time)

        growth_time_series = pd.Series(growth_time_list)
        frequency_time = dict(growth_time_series.value_counts())
        for key, value in frequency_time.items():
            frequency_time[key] = int(value)
        data_to_return = {
            "berries_names": names,
            "min_growth_time": int(growth_time_series.min()),
            "median_growth_time": float(growth_time_series.median()),
            "max_growth_time": int(growth_time_series.max()),
            "variance_growth_time": float(growth_time_series.var()),
            "mean_growth_time": float(growth_time_series.mean()),
            "frequency_growth_time": frequency_time
        }
        return data_to_return
