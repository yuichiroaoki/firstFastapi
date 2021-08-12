from mongodb.core import Mongodb
from pprint import pprint
import pandas as pd

db_url = "mongodb://localhost:27017/"

sample_data = {"name": "John", "address": "Highway 37"}


def test_add_data():
    mongodb_conf = [db_url, "sample", "sample"]
    mongodb = Mongodb(*mongodb_conf)

    mongodb.add_data(sample_data)

    name_John = {"name": "John"}
    result = mongodb.get_data(name_John)
    assert result == sample_data
