from pymongo import MongoClient
from pprint import pprint


class Mongodb:
    def __init__(self, db_url, db_name, collection_name) -> None:
        client = MongoClient(db_url)
        db = client[db_name]
        self.collection = db[collection_name]

    def add_data(self, data: dict):

        try:

            self.collection.insert_one(data)

        except Exception as e:

            error_message = str(e)

            pprint({
                "error_message": f"{error_message} - failed to add data"
            })

    def get_data(self, filter: dict):

        try:
            result = self.collection.find(filter)
            return [i for i in result]

        except Exception as e:

            error_message = str(e)

            pprint({
                "error_message": f"{error_message} - failed to add data"
            })
