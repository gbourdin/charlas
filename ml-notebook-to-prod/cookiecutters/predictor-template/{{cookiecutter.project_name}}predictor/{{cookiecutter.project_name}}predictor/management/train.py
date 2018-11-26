import click
import pandas as pd
from sklearn.model_selection import train_test_split

from {{cookiecutter.project_name}}predictor.models import Predictor


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
    train_X, test_X, train_y, test_y = train_test_split(
        X, y, test_size=0.2, random_state=1
    )

    model = Predictor()
    model.fit(train_X, train_y)
    model.dump(out_file)
