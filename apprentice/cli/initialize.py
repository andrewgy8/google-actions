import click

MAIN_CONTENT = """from flask import Flask

from apprentice import format_response, generate_intent_response

app = Flask(__name__)


@app.route('/', methods=['POST'])
def cool_fact_generator(*args, **kwargs):
    phrase = "Hello there! I'm your Hello World Agent"
    formatted_data = generate_intent_response(phrase)
    return format_response(formatted_data)
"""

REQUIREMENTS_CONTENT = """apprentice
"""


@click.command()
def init():
    directory = 'hello_world_agent'
    import os
    if os.path.exists(directory):
        click.echo(f'The {directory} already exists.')
        return

    click.echo(f'Creating a project in {directory}')

    os.makedirs(directory)
    with open(f'{directory}/main.py', 'w') as file:
        file.write(MAIN_CONTENT)
        file.close()

    with open(f'{directory}/requirements.txt', 'w') as file:
        file.write(REQUIREMENTS_CONTENT)
        file.close()

    click.echo('Project created')
