from .api import predict_blueprint
import logging
from flask import Flask, redirect, url_for


def configure_app(app):
    app.config.from_object('{{cookiecutter.project_name}}api.settings.default')
    app.url_map.strict_slashes = False

    app.logger.setLevel(logging.INFO)
    app.logger.info('Start: Loading predictor')
    # Load your models here!
    app.logger.info('Finish: Loading Predictor')


def initialize_app(app):
    configure_app(app)
    # Namespaces should be added here, not in api init.
    app.register_blueprint(predict_blueprint)


def create_app():
    app = Flask(__name__, instance_relative_config=True)

    @app.route('/')
    def predict():
        return redirect(url_for('predict.doc'))

    initialize_app(app)

    return app
