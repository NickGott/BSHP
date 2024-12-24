import pandas as pd
from ..Model_BSHP.prepare_data import encode_objects_fit, prepare_to_train, prepare_to_predict, decode_objects
from connector import Connector
from model import RFModel


class Processor:
    def __init__(self, base_name: str, data: pd.DataFrame):
        self.base_name = base_name
        self.data = data
        self.target_list = ['article_cash_flow', 'details_cash_flow', 'with_without_count', 'unit_of_count', 'year']

    def fit_process(self):
        try:
            df, target_dict = encode_objects_fit(self.data)
            connector = Connector(self.base_name)
            connector.add_dict_to_db(target_dict)
            connector.set_model_status('Model is fitting')
            for target in self.target_list:
                x_train, x_test, y_train, y_test = prepare_to_train(df, target)
                model = RFModel(self.base_name, target)
                model.fit(x_train, y_train)
            connector.set_model_status('Model has been fit')
            return "Model has been fit"
        except Exception as ex:
            print(f'Error: {ex}')
            Connector(self.base_name).set_model_status('Error fit')

    def predict_process(self):
        try:
            result_df = pd.DataFrame(self.data).copy()
            df = prepare_to_predict(self.data)
            for target in self.target_list:
                model = RFModel(self.base_name, target)
                predicts = model.predict(df)
                target_dict = {}
                target_dict = Connector(self.base_name).read_dict_from_db(target)
                decoded_predicts = decode_objects(predicts, target_dict)
                result_df[target] = decoded_predicts
                df[target] = predicts
            result_json = result_df.to_json(orient="records")
            return result_json
        except Exception as ex:
            print(f'Error: {ex}')

    def get_status(self):
        pass
