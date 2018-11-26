import os

PROJECT_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
MODELS_BASE_PATH = os.path.join(PROJECT_PATH, 'models')
MNIST_MODEL_NAME = 'mnist_tensorflow10.hdf5'
MNIST_MODEL_PATH = os.path.join(MODELS_BASE_PATH, MNIST_MODEL_NAME)

SWAGGER_UI_JSONEDITOR = True
