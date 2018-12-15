import os
from unittest.mock import patch

import pytest
from click.testing import CliRunner

from apprentice.commands import REQUIREMENTS_CONTENT, main


@pytest.fixture
def runner():
    return CliRunner()


class TestVersion:

    def test_returns_help_message_when_called_with_argument(self, runner):
        result = runner.invoke(main, ['version', '--help'])

        assert result.exit_code == 0
        assert 'Show installed version' in result.output

    def test_returns_version_when_called(self, runner):
        result = runner.invoke(main, ['version'])

        assert result.exit_code == 0
        assert 'Apprentice v' in result.output


class TestDeploy:

    def test_returns_help_message_when_called_with_argument(self, runner):
        result = runner.invoke(main, ['deploy', '--help'])

        assert result.exit_code == 0
        assert 'Generate gcloud deploy command' in result.output

    def test_returns_command_when_short_options_given(self, runner):
        commands = ['deploy', '-f foo', '-s dir_foo',
                    '-e foo_bar', '-r europe-west1']
        result = runner.invoke(main, commands)

        assert 'gcloud functions deploy foo --runtime python37 ' \
               '--trigger-http --source dir_foo ' \
               '--entry-point foo_bar --region europe-west1' in result.output
        assert result.exit_code == 0

    def test_returns_command_when_long_options_declared(self, runner):
        commands = ['deploy', '--func=foo', '--source=dir_foo',
                    '--entry_point=foo_bar', '--region=europe-west1']
        result = runner.invoke(main, commands)

        assert 'gcloud functions deploy foo --runtime python37 ' \
               '--trigger-http --source dir_foo ' \
               '--entry-point foo_bar --region europe-west1' in result.output
        assert result.exit_code == 0

    def test_returns_region_us_central_when_no_region_defined(self, runner):
        commands = ['deploy', '-f foo', '-s dir_foo', '-e foo_bar']
        result = runner.invoke(main, commands)

        assert 'gcloud functions deploy foo --runtime python37 ' \
               '--trigger-http --source dir_foo ' \
               '--entry-point foo_bar --region us-central1' in result.output
        assert result.exit_code == 0

    def test_returns_exit_code_when_source_dir_does_not_exist(self, runner):
        commands = ['deploy', '-f foo', '-s dir_foo', '-e foo_bar']
        result = runner.invoke(main, commands)

        assert 'gcloud functions deploy foo --runtime python37 ' \
               '--trigger-http --source dir_foo ' \
               '--entry-point foo_bar --region us-central1' in result.output
        assert result.exit_code == 0

    @pytest.mark.parametrize('commands', [
        ['-s dir_foo', '-e foo_bar'],
        ['-f foo', '-e foo_bar'],
        ['-f foo', '-s dir_foo']
    ])
    def test_returns_exit_code_2_when_required_arguments_not_defined(
            self, runner, commands):
        result = runner.invoke(main, ['deploy'] + commands)

        assert result.exit_code == 2


class TestInit:

    def test_returns_help_message_when_called_with_argument(self, runner):
        result = runner.invoke(main, ['init', '--help'])

        assert result.exit_code == 0
        assert 'Initialize a project' in result.output

    def test_returns_default_function_name_when_called_without_webhook_arg(
            self, runner):
        with runner.isolated_filesystem():
            runner.invoke(main, ['init'])

            with open('main.py', 'r') as f:
                contents = f.read()

            assert 'def webhook(' in contents

    def test_returns_custom_name_function_when_called_with_webhook_arg(
            self, runner):
        with runner.isolated_filesystem():
            runner.invoke(main, ['init', '--webhook=testing'])

            with open('main.py', 'r') as f:
                contents = f.read()

            assert 'def testing(' in contents

    def test_returns_main_in_source_when_called_with_source_arg(self, runner):
        with runner.isolated_filesystem():
            runner.invoke(main, ['init', '--webhook=testing', '--source=src'])

            with open('src/main.py', 'r') as f:
                contents = f.read()

            assert 'def testing(' in contents

    def test_returns_requirements_file_when_called(self, runner):
        with runner.isolated_filesystem():
            runner.invoke(main, ['init'])

            with open('requirements.txt', 'r') as f:
                contents = f.read()

            assert REQUIREMENTS_CONTENT in contents

    def test_creates_requirements_file_in_srouce_when_called_with_arg(
            self, runner):
        with runner.isolated_filesystem():
            runner.invoke(main, ['init', '--source=some_dir'])

            with open('some_dir/requirements.txt', 'r') as f:
                contents = f.read()

            assert REQUIREMENTS_CONTENT in contents


class TestRun:

    def test_returns_help_message_when_called_with_argument(self, runner):
        result = runner.invoke(main, ['run', '--help'])

        assert result.exit_code == 0
        assert 'Run a test server for local development' in result.output

    @patch('apprentice.commands.run_simple')
    def test_runs_server_when_a_project_location_is_defined(
            self, mock_server, runner):
        os.environ['FLASK_APP'] = 'example/main.py'

        result = runner.invoke(main, ['run'])

        assert result.exit_code == 0
        assert '* Serving Flask app "example/main.py"' in result.output
        mock_server.assert_called()

    @patch('apprentice.commands.run_simple')
    def test_returns_exit_code_when_a_project_location_undefined(
            self, mock_server, runner):
        del os.environ['FLASK_APP']

        result = runner.invoke(main, ['run'])

        assert result.exit_code == 2
        assert 'Usage: main run [OPTIONS]\n\n' \
               'Error: Could not locate a Flask application. ' \
               'You did not provide the "FLASK_APP" environment variable, ' \
               'and a "wsgi.py" or "app.py" module was not found in the ' \
               'current directory.\n' in result.output
        mock_server.assert_not_called()
