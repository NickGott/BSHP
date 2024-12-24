from pymongo import MongoClient

URL = "mongodb://localhost:27017"


class Connector:

    def __init__(self, base_name):
        self.base_name = base_name
        self.db = None
        self._connect()

    def _connect(self):
        client = MongoClient(URL)
        self.db = client[self.base_name]

    def add_dict_to_db(self, dict_to_db: dict):
        client = MongoClient(URL)
        self.db = client[self.base_name]
        if len(self.db.list_collection_names()) != 0:
            client.drop_database(self.db)
        for key in dict_to_db.keys():
            self.db[key].insert_one(dict_to_db[key])

    def read_dict_from_db(self, target: str):
        target_dict = self.db[target].find_one()
        return target_dict

    def get_model_status(self):
        if 'Model_status' not in self.db.list_collection_names():
            self.db['Model_status'].insert_one({'Model_status': 'No_model'})
        return print(self.db['Model_status'].find_one()['Model_status'])

    def set_model_status(self, model_status: str):
        if 'Model_status' not in self.db.list_collection_names():
            self.db['Model_status'].insert_one({'Model_status': 'No_model'})
        previous_status = self.db['Model_status'].find_one()['Model_status']
        self.db['Model_status'].replace_one({'Model_status': previous_status}, {'Model_status': model_status})
