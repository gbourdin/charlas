# sklearnpricepredictor
This is a wrapper class around a scikit-learn Random Forest Regressor configured
to predict housing prices. It's intended to be trained used the Melbourne Housing
data from kaggle's tutorials.


The performance achieved by training this model with the selected features and no
additional work is very poor, however, the main purpose of this is not to demonstrate
how to do feature selection, model specification or training and validation, instead
the focus of this project is on wrapping models around a standard interface to make it
easier to use different implementations.

Methods to dump and load trained models are provided to make it easier to use in production
environments where re-training the model before each use is not expected.

A command line interface to train the model and create a dump of the training model is
provided as an example of something that could be used in environments with automated
regular training.

## Installation instructions
In a clean python 3.6 virtualenv run:
```bash
$ pip install -e .
```

## Usage instructions
```python
>>> from sklearnpricepredictor.models import HousePricePredictor
>>> model = HousePricePredictor.load('../models/melbourne_model.joblib')  # Or a path to your model!
>>> predictions = model.predict([{'Rooms': 4,'Bathroom': 1,'Landsize': 800,'BuildingArea': 150,'YearBuilt': 1990}])
>>> print(predictions[0])
643630.0
```

## Training instructions
```bash
$ sklearnpricepredictor train path-to-your-dataset output-path
```

## Training instructions (using the provided dataset)
```bash
$ sklearnpricepredictor train ../../input/melbourne-housing-snapshot/melb_data.csv ../models/melbourne_model.joblib
```
