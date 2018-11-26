from flask import Blueprint
from flask_restplus import Api

from .endpoints import predict_ns

blueprint = Blueprint('predict', __name__, url_prefix='/api/v1.0')
# v1_0 = Blueprint('v1_0', __name__, url_prefix='/api/v1.0')
api = Api(
    blueprint, version='1.0', title='houseprice',
    description='houseprice Prediction API', doc='/doc/')

api.namespaces.clear()
api.add_namespace(predict_ns)
