import logging
import numpy as np
from datetime import datetime

from flask import request, current_app as app
from flask_restplus import Namespace, Resource, fields

logger = logging.getLogger(__name__)

ns = Namespace(
    'predict', description='mnist Prediction API')


ResourceFields = ns.model('mnist Predictor Resource', {
    'image': fields.List(
        fields.Integer, 
        description='List of pixel intensities for image',
        required=True,
        min_length=1,
    ),
})

Model = ns.model('mnist Predictor', {
    'predictions': fields.List(
        fields.Raw, 
        description='Probabilities for each number',
        required=True,
        min_length=1,
    ),
})


@ns.route('/')
class Predict(Resource):
    @ns.marshal_with(Model, code=200, description='mnist Predictor')
    @ns.expect(ResourceFields, validate=True)
    def post(self):
        """
        Make a prediction about value!
        """
        data = request.json

        start = datetime.now()
        result = self.get_result(data)
        duration_msec = (datetime.now() - start).total_seconds() * 1000
        predictions = result['predictions']
        predicted_numer = np.argmax(predictions, 0)
        app.logger.info(
            'Predicted number was: {}, with probabilities: '
            '{} and took {} msec'.format(
                predicted_numer, predictions, duration_msec))

        return result, 200

    def get_result(self, data):
        """
        Gets a prediction from our model
        """
        image = data.get('image')
        app.logger.info("Types: {} {} {}".format(type(data), type(image), type(image[0])))
        image = ((255 - np.array(image, dtype=np.uint8)) / 255.0).reshape(1, 784)
        prediction = app.mnist_predictor.predict(np.array([image, ]))[0]
        return {'predictions': prediction.tolist()}
