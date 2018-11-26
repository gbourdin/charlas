import logging

from {{cookiecutter.project_name}}predictor.base import BaseModel


class Predictor(BaseModel):
    def __init__(self):
        self.model = None

    def predict(self, X):
        return self.model.predict(X)

    def fit(self, X, y):
        self.model.fit(X, y)
        return self