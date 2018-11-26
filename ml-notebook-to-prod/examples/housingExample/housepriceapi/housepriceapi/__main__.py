import click

from os import cpu_count, environ, execvp
from sys import prefix

from .app import create_app


@click.group()
def cli():
    pass


@cli.command()
def run_uwsgi():
    """ 
    Run API through uwsgi server.
    """
    # avoid fork problems with tensorflow (and other non-serializable objects)
    environ['UWSGI_LAZY_APPS'] = '1'
    # explicit http timeout
    environ['UWSGI_HTTP_TIMEOUT'] = '60'
    # how many uwsgi workers (processes)
    environ['UWSGI_WORKERS'] = '{}'.format(cpu_count())
    # create one thread for every process, since you're probably cpu-bound
    environ['UWSGI_THREADS'] = '1'
    # load the mmanager WSGI handler
    environ['UWSGI_MODULE'] = 'housepriceapi.wsgi:app'
    # bind the http server, DO NOT USE UWSGI_HTTP_SOCKET!!!
    environ['UWSGI_HTTP'] = ':8080'
    # remove sockets/pidfile at exit
    environ['UWSGI_VACUUM'] = '1'
    # retrieve/set the PythonHome
    environ['UWSGI_PYHOME'] = prefix
    # increase buffer size a bit
    environ['UWSGI_BUFFER_SIZE'] = '8192'
    # enable the master process
    environ['UWSGI_MASTER'] = '1'
    # disable ping logging
    environ['UWSGI_ROUTE'] = '^/ping donotlog:'
    # keep connection from balancer alive
    environ['UWSGI_HTTP_KEEPALIVE'] = '1'
    # slower but safe
    environ['UWSGI_THUNDER_LOCK'] = '1'
    # do not log every request, it's slow and verbose
    environ['UWSGI_DISABLE_LOGGING'] = '1'
    # close uwsgi if something goes wrong, otherwise uwsgi starts with no app
    environ['UWSGI_NEED_APP'] = '1'

    # exec the uwsgi binary
    execvp('uwsgi', ('uwsgi',))

@cli.command()
@click.option('-h', '--host', 'host', default='localhost')
def run_server(host):
    app = create_app()
    app.run(debug=True, host=host, port=8080)

if __name__ == '__main__':
    cli()
