import logging
import pickle

from abc import ABCMeta, abstractmethod


logger = logging.getLogger(__name__)


class BaseModel(metaclass=ABCMeta):
    """
    Base class for all predictor models.
    """
    def __init__(self):
        self.model = None  # You should define this!

    @abstractmethod
    def predict(self, X):
        """
        Returns a list of predictios for the provided list of features
        """
        return self.model.predict(X)

    @abstractmethod
    def fit(self, X, y):
        """
        Train the model
        """
        return self

    def dump(self, path):
        """
        Dumps the current trained model to path
        """
        logger.debug('Dumping: {}'.format(self.__class__.__name__))
        with open(path, 'wb') as f:
            pickle.dump(self.model, f)

    @classmethod
    def load(cls, path):
        """
        Load saved model from path.
        """
        logger.debug('Loading: {}'.format(cls.__name__))
        with open(path, 'rb') as f:
            model = pickle.load(f)

        self.model = model

        return self
