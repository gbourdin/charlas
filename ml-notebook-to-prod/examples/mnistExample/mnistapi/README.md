# mnist

Simple Flask + Flask-RESTPlus api to serve a classifier model for the mnist problem.

## Usage

### Install, compile and run
In a virtualenv:

First, install the mnistpredictor:
```bash
$ pip install -e ../mnistpredictor
```

Second, install this api
```bash
$ pip install -e .
```

Now, run the server in development mode
``` bash
$ mnistapi run-server
```

Alternatively, run the server in production mode:
```bash
    $ mnistapi run-uwsgi
```
