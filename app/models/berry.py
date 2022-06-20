
class Berry():

    def __init__(self, name, url):
        self.name = name
        self.url = url
        self._consult_update_growth_time()

    @staticmethod
    def create_berries_from_list(berries_json):
        pass

    def _consult_update_growth_time(self):
        pass

class BerryStatistics():

    def __init__(self, berries):
        self.berries = berries if isinstance(berries, list) else None

    def describe_statistics_data(self):
        pass
