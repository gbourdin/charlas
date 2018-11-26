# mnistpredictor
This is a wrapper class around a keras+tensorflow model trained to classify handwritten digits based on the mnist dataset


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

## Training instructions
```bash
$ mnistpredictor train ../models/mnist_tensorflow.hdf5
```

## Training instructions (customizing the number of epochs)
```bash
$ mnistpredictor train ../models/mnist_tensorflow.hdf5 --epochs 10
```
