import click
import pandas as pd
from sklearn.metrics import (
    explained_variance_score, r2_score, mean_absolute_error)
from sklearn.model_selection import train_test_split

from sklearnpricepredictor.models import HousePricePredictor, FEATURES


@click.command(name='train')
@click.argument('dataset-path', 
    type=click.Path(exists=True, resolve_path=True))
@click.argument('out-file', type=click.Path(writable=True, resolve_path=True))
def cli(dataset_path, out_file):
    """Train a new model.

    This will train a new model using the provided dataset, trained model
    will be dumped to OUT file.
    """
    data = pd.read_csv(dataset_path)
    data = data.dropna(axis=0)  # Just drop empty values
    X = data[FEATURES]
    y = data['Price']

    train_X, test_X, train_y, test_y = train_test_split(
        X, y, test_size=0.2, random_state=1
    )

    model = HousePricePredictor()
    model.fit(train_X, train_y)
    model.dump(out_file)

    predictions = model.predict(test_X)
    print("Mean Absolute Error : " + str(
        mean_absolute_error(predictions, test_y)))
    print("Explained Variance Score :" + str(
        explained_variance_score(predictions, test_y)))
    print("R2 Score :" + str(r2_score(predictions, test_y)))
