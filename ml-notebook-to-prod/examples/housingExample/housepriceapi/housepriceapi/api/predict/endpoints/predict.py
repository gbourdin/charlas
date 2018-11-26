import logging
from datetime import datetime

from flask import request, current_app as app
from flask_restplus import Namespace, Resource, fields

logger = logging.getLogger(__name__)

ns = Namespace(
    'predict', description='houseprice Prediction API')


ResourceFields = ns.model('houseprice Predictor Resource', {
    'Rooms': fields.Integer(
        description='Number of rooms in the house',
        required=True,
        example=2
    ),
    'Bathroom': fields.Integer(
        description='Number of bathrooms in the house',
        required=True,
        example=1
    ),
    'Landsize': fields.Float(
        description='Area in square meters of the entire property',
        required=True,
        example=800
    ),
    'BuildingArea': fields.Float(
        description='Area in square meters of the built surface of the house',
        required=True,
        example=150
    ),
    'YearBuilt': fields.Integer(
        description='Year the house was built on',
        required=True,
        example=1990
    ),
})

Model = ns.model('houseprice Predictor', {
    'value': fields.Float(description='Predicted price for this house', required=True),
})


@ns.route('/')
class Predict(Resource):
    @ns.marshal_with(Model, code=200, description='houseprice Predictor')
    @ns.expect(ResourceFields, validate=True)
    def post(self):
        """
        Make a prediction about value!
        """
        data = request.json

        start = datetime.now()
        result = self.get_result(data)
        duration_msec = (datetime.now() - start).total_seconds() * 1000
        app.logger.info('Prediction for: {} was: {} and took {} msec'.format(
            data, result, duration_msec))

        return result, 200

    def get_result(self, data):
        """
        Gets a prediction from our model
        """
        prediction = app.house_price_predictor.predict([data])[0]
        return {'value': prediction}
