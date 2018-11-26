import logging
from flask import Flask, redirect, url_for, current_app

from .api import predict_blueprint
from mnistpredictor.models import MnistPredictor

def configure_app(flask_app):
    flask_app.config.from_object('mnistapi.settings.default')
    flask_app.url_map.strict_slashes = False

    flask_app.logger.setLevel(logging.INFO)
    flask_app.logger.info('Start: Loading predictor')
    with flask_app.app_context():
        path = current_app.config['MNIST_MODEL_PATH']
        current_app.mnist_predictor = MnistPredictor.load(path) 
    flask_app.logger.info('Finish: Loading Predictor')


def initialize_app(flask_app):
    configure_app(flask_app)
    # Namespaces should be added here, not in api init.
    flask_app.register_blueprint(predict_blueprint)


def create_app():
    app = Flask(__name__, instance_relative_config=True)

    @app.route('/')
    def predict():
        return redirect(url_for('predict.doc'))

    initialize_app(app)

    return app
