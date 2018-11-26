import logging
import numpy as np
import tensorflow as tf

from mnistpredictor.base import BaseModel


logger = logging.getLogger(__name__)


class MnistPredictor(BaseModel):
    def __init__(self):
        self.model = None

    def predict(self, X):
        predictions = self.model.predict(X)
        return predictions

    def fit(self, X, y, epochs=5, validation_data=None):
        if not self.model:
            self.model = self._build_model()
        
        self.model.fit(X, y, epochs=epochs, validation_data=validation_data)
        return self

    def _build_model(self):
        model = tf.keras.models.Sequential([
            tf.keras.layers.Flatten(),
            tf.keras.layers.Dense(512, activation=tf.nn.relu),
            tf.keras.layers.Dropout(0.2),
            tf.keras.layers.Dense(10, activation=tf.nn.softmax)
        ])

        model.compile(optimizer='adam',
            loss='sparse_categorical_crossentropy',
            metrics=['accuracy'])

        return model

    def evaluate(self, X, y):
        return self.model.evaluate(X, y)

    def dump(self, path):
        """
        Dumps the current trained model to path
        """
        logger.debug('Dumping: {}'.format(self.__class__.__name__))
        tf.keras.models.save_model(self.model, path)

    @classmethod
    def load(cls, path):
        """
        Load saved model from path.
        """
        logger.debug('Loading: {}'.format(cls.__name__))

        mnist_model = MnistPredictor()
        mnist_model.model = tf.keras.models.load_model(path, compile=False)

        return mnist_model
