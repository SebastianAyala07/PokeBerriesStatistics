import os
import numpy as np
import pytest
from app import create_app
from app.tests.data_helper import BERRIES_LIST
from app.models.berry import Berry, BerryStatistics
from app.common.berry_helper import BerryQueryHelper


@pytest.fixture(scope="module")
def client_testing():
    app_instance = create_app(
        os.getenv('APP_SETTINGS_MODULE')
    )
    with app_instance.test_client() as testing_client:
        with app_instance.app_context():
            yield testing_client

@pytest.fixture(scope="module")
def berries():
    return Berry.create_berries_from_list(BERRIES_LIST)

def test_create_berries_from_list(berries):
    for berry in berries:
        assert isinstance(berry, Berry)

def test_consult_update_growth_time():
    berry_data = BERRIES_LIST[0]
    my_berry_test = Berry(**berry_data)
    assert isinstance(my_berry_test.growth_time, int)
    assert isinstance(
        my_berry_test._consult_update_growth_time(), int
    )

def test_describe_statistics_data(berries):
    my_berry_statistics_test = BerryStatistics(berries)
    data_statistics = my_berry_statistics_test.describe_statistics_data()
    keys_assert = {
        "berries_names": list,
        "min_growth_time": int,
        "median_growth_time": float,
        "max_growth_time": int,
        "variance_growth_time": float,
        "mean_growth_time": float,
        "frequency_growth_time": dict
    }
    for key, data_type in keys_assert.items():
        assert isinstance(data_statistics.get(key, None), data_type)
    list_growth_time = [
        berry.growth_time for berry in my_berry_statistics_test.berries
    ]
    assert data_statistics.get("min_growth_time", None) == int(np.min(list_growth_time))
    assert data_statistics.get("max_growth_time", None) == np.max(list_growth_time)
    assert data_statistics.get("median_growth_time", None) == np.median(list_growth_time)
    assert (
        data_statistics.get("variance_growth_time", None) - np.var(list_growth_time, axis=0) <= 1
    )
    assert data_statistics.get("mean_growth_time", None) == np.mean(list_growth_time)
    (growth_time_expected_list, freq_expected) = np.unique(list_growth_time, return_counts=True)
    growth_time_expected_list = list(growth_time_expected_list)
    freq_expected = list(freq_expected)
    for growth_time, freq in data_statistics.get("frequency_growth_time").items():
        index = growth_time_expected_list.index(growth_time)
        assert freq_expected[index] == freq

def test_query_helper_get_all_berries():
    result = BerryQueryHelper.get_all_berries()
    assert isinstance(result, list)

def test_query_helper_get_berry_by_id():
    result = BerryQueryHelper.get_berry_by_id(1)
    assert isinstance(result, dict)

def test_all_berry_stats_endpoint(client_testing):
    response = client_testing.get('/allBerryStats')
    assert response.status_code == 200
