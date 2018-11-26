import os

PROJECT_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))

MODELS_BASE_PATH = os.path.join(PROJECT_PATH, 'models')
XGB_HOUSE_MODEL_NAME = 'melbourne_model.xgb'
XGB_HOUSE_MODEL_PATH = os.path.join(MODELS_BASE_PATH, XGB_HOUSE_MODEL_NAME)
SKLEARN_HOUSE_MODEL_NAME = 'melbourne_model.joblib'
SKLEARN_HOUSE_MODEL_PATH = os.path.join(MODELS_BASE_PATH, 
    SKLEARN_HOUSE_MODEL_NAME)

SWAGGER_UI_JSONEDITOR = True
