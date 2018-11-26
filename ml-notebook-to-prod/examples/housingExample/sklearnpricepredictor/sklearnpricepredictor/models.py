import logging
import pandas as pd

from sklearnpricepredictor.base import BaseModel
from sklearn.ensemble import RandomForestRegressor
from sklearn.externals import joblib

FEATURES = ['Rooms', 'Bathroom', 'Landsize', 'BuildingArea', 'YearBuilt', ]


class HousePricePredictor(BaseModel):
    def __init__(self):
        self.model = RandomForestRegressor(random_state=1, n_estimators=100)

    def _prepare_data(self, X):
        return pd.DataFrame(X, columns=FEATURES)

    def predict(self, X):
        X = self._prepare_data(X)
        return self.model.predict(X)

    def fit(self, X, y):
        self.model.fit(X, y)

        return self

    def dump(self, path):
        joblib.dump(self.model, path)

    @classmethod
    def load(cls, path):
        house_model = HousePricePredictor()
        house_model.model = joblib.load(path) 

        return house_model
