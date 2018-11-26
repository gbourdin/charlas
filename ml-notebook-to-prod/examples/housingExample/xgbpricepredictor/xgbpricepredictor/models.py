import logging
import pandas as pd
from sklearn.model_selection import GridSearchCV
from xgboost import XGBRegressor

from xgbpricepredictor.base import BaseModel


FEATURES = ['Rooms', 'Distance', 'Postcode', 'Bedroom2', 'Bathroom', 'Car',
            'Landsize', 'BuildingArea', 'YearBuilt', 'Lattitude', 'Longtitude',
            'Propertycount']


class HousePricePredictor(BaseModel):
    def __init__(self):
        self.model = XGBRegressor()

    def predict(self, X):
        X = self._prepare_data(X)
        return self.model.predict(X)

    def _prepare_data(self, X):
        return pd.DataFrame(X, columns=FEATURES)

    def fit(self, X, y):
        model = XGBRegressor()
        clf = GridSearchCV(
            model,
            {
                'max_depth': [6, ],
                'learning_rate': [0.05, ],
                'n_estimators': [450, 470, 475, 480, 485, ]
            },
            n_jobs=4,
            cv=3,
            verbose=1
        )
        clf.fit(X, y)
        logging.info("Best Score: {}".format(clf.best_score_))
        logging.info("Best Params: {}".format(clf.best_params_))
        self.model = clf.best_estimator_

        return self.model

    def dump(self, path):
        self.model.save_model(path)

    @classmethod
    def load(cls, path):
        house_model = HousePricePredictor()
        house_model.model.load_model(path)

        return house_model
