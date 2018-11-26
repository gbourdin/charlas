import logging
from datetime import datetime

from flask import request, current_app as app
from flask_restplus import Namespace, Resource, fields

logger = logging.getLogger(__name__)

ns = Namespace(
    'predict', description='{{cookiecutter.project_name}} Prediction API')


ResourceFields = ns.model('{{cookiecutter.project_name}} Predictor Resource', {
    'feature': fields.String(
        description='A feature for your model',
        required=True,
        min_length=1,
        example='Red'
    ),
})

Model = ns.model('{{cookiecutter.project_name}} Predictor', {
    'prediction': fields.String(description='Prediction', required=True),
})


@ns.route('/')
class Predict(Resource):
    @ns.marshal_with(Model, code=200, description='{{cookiecutter.project_name}} Predictor')
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
        return {'prediction': 'Hammer'}
