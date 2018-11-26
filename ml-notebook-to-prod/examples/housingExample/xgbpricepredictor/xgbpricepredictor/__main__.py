import logging

import click
from click_repl import register_repl

from xgbpricepredictor.management import train_cli


@click.group()
@click.option('--verbose', is_flag=True, help="Enable debug logging.")
@click.version_option()
def cli(verbose):
    if verbose:
        logging.basicConfig(level=logging.DEBUG)
    else:
        logging.basicConfig(level=logging.INFO)


cli.add_command(train_cli)


register_repl(cli)

if __name__ == '__main__':
    cli()
