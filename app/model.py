import pandas as pd
from sklearn.metrics import accuracy_score
from sklearn.ensemble import RandomForestClassifier
from typing import Optional
import joblib


class RFModel:
    def __init__(self, base_name: str, target: str):
        self.base_name = base_name
        self.model: Optional[RandomForestClassifier] = None
        self.target = target

    def fit(self, x_train: pd.DataFrame, y_train: pd.DataFrame):
        self.model = RandomForestClassifier(n_estimators=200, max_depth=20, min_samples_leaf=1, min_samples_split=5)
        self.model.fit(x_train, y_train)
        self._save_model()

    def _save_model(self):
        model_name = self.target + '.' + self.base_name
        path = 'saved_models/'
        joblib.dump(self.model, path + model_name, compress=5)

    def _load_model(self):
        model_name = self.target + '.' + self.base_name
        path = 'saved_models/'
        loaded_model = joblib.load(path + model_name)
        return loaded_model

    def predict(self, data_to_predict: pd.DataFrame):
        loaded_model = self._load_model()
        predicts = loaded_model.predict(data_to_predict)
        return predicts

    def get_info(self):
        pass

    def metrics(self, x_test: pd.DataFrame, y_test: pd.DataFrame):
        predicts = self.model.predict(x_test)
        accuracy = accuracy_score(y_test, predicts)
        return print(f'Accuracy: {accuracy}')
