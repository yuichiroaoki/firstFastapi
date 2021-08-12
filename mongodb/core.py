from pymongo import MongoClient
from pprint import pprint
import pandas as pd


class Mongodb:
    def __init__(self, db_url, db_name, collection_name) -> None:
        client = MongoClient(db_url)
        db = client[db_name]
        self.collection = db[collection_name]

    def get_data(self):

        try:
            filter_data = {"sample": 1}
            data = [i for i in self.collection.find(filter_data)]
            names = [i["name"] for i in data]

            return names

        except Exception as e:

            error_message = str(e)

            pprint({
                "error_message": f"{error_message} - failed to add data"
            })
