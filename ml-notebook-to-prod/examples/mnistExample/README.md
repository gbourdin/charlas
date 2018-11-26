# mnist handwritten digit recognition production ready example

This intends to be a full example of how a predictor for the mnist problem can be served in production environments.

There's four things made available in this directory:
- A machine learning model wrapper based on the mnist example from tensorflow's documentation
- An api wrapper around the tensorflow model that will load and expose an enpoint to serve predictions
- A very simple frontend that's intended to show how final users would interact in the real world with the underlying model through a web service where they can draw a number and get a prediction of what that number is.

Installation and detailed instructions for each application can be found in their
directories, but below you can find an overview on how to get this application up and
running.

## Installation Instructions
In a clean python 3.6 virtualenv:

### Install the predictor
```
$ pip install -e mnistpredictor
```

### Install the api
```
$ pip install -e mnistapi
```

### Install the frontend compilation tools
```
$ pip install nodeenv
$ nodeenv -p
$ cd frontend
$ npm install
```

## Usage instructions

### Start the backend API
```
$ mnistapi run-server
```

### Compile and serve the frontend
```
$ cd frontend
$ npm start
```

### Open a browser and point it to the frontend app
Go to http://localhost:4444/
Profit!


