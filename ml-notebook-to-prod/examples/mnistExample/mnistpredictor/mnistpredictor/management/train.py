import click
import tensorflow as tf

from mnistpredictor.models import MnistPredictor


TF_MODEL_EXTENSION = ".hdf5"

@click.command(name='train')
@click.option('--epochs', default=5, help='Number of epochs to train')
@click.argument('out-file', type=click.Path(writable=True, resolve_path=True))
def cli(epochs, out_file):
    """Train a new model.

    This will train a new model using the provided dataset, trained model
    will be dumped to OUT file.
    """
    mnist = tf.keras.datasets.mnist
    (x_train, y_train),(x_test, y_test) = mnist.load_data()

    # Transform the values from int to float, values remain the same
    x_train, x_test = x_train / 255.0, x_test / 255.0

    model = MnistPredictor()
    model.fit(x_train, y_train, epochs=epochs)
    
    # I wan't outfiles to have the right extension
    if not out_file.endswith(TF_MODEL_EXTENSION):
        out_file = out_file + TF_MODEL_EXTENSION
    model.dump(out_file)

    # Print metrics
    loss, accuracy = model.evaluate(x_test, y_test)
    print(
        "Validation Loss: {}, Validation Accuracy: {}".format(loss, accuracy)
    )

    print("Trained model was saved to {}".format(out_file))
