import os

import click
from flask.cli import DispatchingApp, pass_script_info, show_server_banner
from flask.helpers import get_env
from werkzeug.serving import run_simple

MAIN_CONTENT = """from apprentice import Apprentice

apr = Apprentice(__name__)


@apr.route('/', methods=['POST'])
def hello_world(*args, **kwargs):
    reply = 'Hello world!'
    return apr.response(reply)

"""

REQUIREMENTS_CONTENT = """apprentice
"""


@click.group()
def main():
    pass


@click.command(help='Show installed version')
def version():
    from .__version__ import __version__
    click.echo(f'Apprentice v{__version__}')


@click.command(help='Initialize a project')
def init():
    dir_name = 'hello_world_agent'
    if os.path.exists(dir_name):
        click.echo(f'{dir_name} already exists.')
        raise click.Abort()

    click.echo(f'Creating a project in {dir_name}')

    os.makedirs(dir_name)
    with open(f'{dir_name}/main.py', 'w') as file:
        file.write(MAIN_CONTENT)
        file.close()

    with open(f'{dir_name}/requirements.txt', 'w') as file:
        file.write(REQUIREMENTS_CONTENT)
        file.close()

    click.echo('Project created')


@click.command(help='Generate gcloud deploy command')
@click.option('--func', '-f', required=True, type=str,
              help='Name of Google Cloud Function')
@click.option('--source', '-s', required=True, type=click.Path(),
              help='Directory path to main.py')
@click.option('--entry_point', '-e', type=str, required=True,
              help='Function to be called in main.py')
@click.option('--region', '-r', type=str, default='us-central1',
              help='Google Cloud Compute Region')
def deploy(func, source, entry_point, region):
    base_command = 'gcloud functions deploy'

    deploy_command = f'{base_command} {func} --runtime python37 ' \
                     f'--trigger-http --source {source} ' \
                     f'--entry-point {entry_point} --region {region}'
    deploy_command = ' '.join(deploy_command.split())
    click.echo(f'Deploy with command: {deploy_command}')


@click.command(help='Run a test server for local development')
@pass_script_info
def run(info):
    debug = True

    # Check that the user has added a proper Flask App
    info.load_app()

    show_server_banner(get_env(), debug, info.app_import_path, None)
    app = DispatchingApp(info.load_app, use_eager_loading=None)
    run_simple('127.0.0.1', 5000, app, use_reloader=debug, use_debugger=debug,
               threaded=True)


main.add_command(version)
main.add_command(init)
main.add_command(deploy)
main.add_command(run)
