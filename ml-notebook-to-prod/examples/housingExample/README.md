# Melbourne housing problem production ready example

This intends to be a full example of how a set of machine learning models trained
to predict housing prices can be served and connected to a frontend for end users to
be able to predict the price of their house.

There's four things made available in this directory:
- Two machine learning model wrappers configured to train with the melboure data from
kaggle and equipped to dump and load their trained models (one based on xgboost and one
based on random forest)
- An api wrapper around the machine learning models that will load the models and expose
an enpoint to serve predictions
- A very simple frontend that's intended to show how final users would interact in the
real world with the underlying models through a web service.

Installation and detailed instructions for each application can be found in their
directories, but below you can find an overview on how to get this application up and
running.

## Installation Instructions
In a clean python 3.6 virtualenv:

### Install the predictors
```
$ pip install -e xgbpricepredictor
$ pip install -e sklearnpricepredictor
```

### Install the api
```
$ pip install -e housepriceapi
```

### Install the frontend compilation tools
```
$ pip install nodeenv
$ nodeenv -p
$ cd frontend
$ npm install yarn
$ node_modules/yarn/bin/yarn install
```

## Usage instructions
By default the API will use the xgboost based model, in order to switch predictors
you will have to edit housepriceapi/housepriceapi/app.py to load the sklearn model.

### Start the backend API
```
$ housepriceapi run-server
```

### Compile and serve the frontend
```
$ cd frontend
$ node_modules/yarn/bin/yarn run watch
```

### Open a browser and point it to the frontend app
Go to http://localhost:8000/
Profit!

## Caveats
None of these models is very good, a lot of precission is lost by ignoring some features
that would either be impossible for users to provide or would have been complicated
to code the demo frontend for (example latitud and longitude).

However the objective of this is to demonstrate how machine learning models are served
and used rather than provide an example of perfect models.

