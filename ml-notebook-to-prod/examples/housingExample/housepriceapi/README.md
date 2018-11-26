# houseprice

Simple Flask + Flask-RESTPlus api to serve a house pricing predictor model that will
from a set of pre-defined features predict the selling price of a house.

## Usage
### Install, compile and run
In a virtualenv:
First, install the xbgpricepredictor:

```bash
$ pip install -e ../xgbpricepredictor
```

Second, install this api
```bash
$ pip install -e .
```

Now, run the server in development mode
```bash
$ housepriceapi run-server
```

Alternatively, run the server in production mode:
```bash
$ housepriceapi run-uwsgi
```
