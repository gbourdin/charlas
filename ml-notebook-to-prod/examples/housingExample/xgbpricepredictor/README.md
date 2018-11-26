# xgbpricepredictor
This is a wrapper class around an xgboost regressor configured to predict housing
prices. It's intended to be trained used the Melbourne Housing data from kaggle's tutorials.

This model, when trained and used with the selected features achieves a reasonable
mean absolute error and R2 score, however, the main purpose of this is not to demonstrate
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
>>> from xgbpricepredictor.models import HousePricePredictor
>>> model = HousePricePredictor.load('../models/melbourne_model.xgb)
>>> predictions = model.predict([{'Rooms': 4,'Bathroom': 1,'Landsize': 800,'BuildingArea': 150,'YearBuilt': 1990}])
>>> print(predictions[0])
2684097.8
```

## Training instructions
```bash 
$ xgbpricepredictor train path-to-your-dataset output-path 
```

## Training instructions (using the provided dataset)
```bash 
$ xgbpricepredictor train ../../input/melbourne-housing-snapshot/melb_data.csv ../models/melbourne_model.xgb 
```
