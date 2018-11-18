import os

import pytest
from click.testing import CliRunner

from apprentice.cli import (
    MAIN_CONTENT,
    REQUIREMENTS_CONTENT,
    base_cli,
    deploy,
    init
)


@pytest.fixture
def runner():
    return CliRunner()


def test_version(runner):
    result = runner.invoke(base_cli, ['version'])

    assert result.exit_code == 0
    assert 'Apprentice v' in result.output


class TestDeploy:

    def test_returns_command_when_short_options_given(self, runner):
        commands = ['-f foo', '-s dir_foo',
                    '-e foo_bar', '-r europe-west1']
        result = runner.invoke(deploy, commands)

        assert 'gcloud functions deploy foo --runtime python37 ' \
               '--trigger-http --source dir_foo ' \
               '--entry-point foo_bar --region europe-west1' in result.output
        assert result.exit_code == 0

    def test_returns_command_when_long_options_declared(self, runner):
        commands = ['--func=foo', '--source=dir_foo',
                    '--entry_point=foo_bar', '--region=europe-west1']
        result = runner.invoke(deploy, commands)

        assert 'gcloud functions deploy foo --runtime python37 ' \
               '--trigger-http --source dir_foo ' \
               '--entry-point foo_bar --region europe-west1' in result.output
        assert result.exit_code == 0

    def test_returns_region_us_central_when_no_region_defined(self, runner):
        commands = ['-f foo', '-s dir_foo',
                    '-e foo_bar']
        result = runner.invoke(deploy, commands)

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
        result = runner.invoke(deploy, commands)

        assert result.exit_code == 2


class TestInit:

    def test_returns_main_py_file_when_called(self, runner):
        with runner.isolated_filesystem():
            result = runner.invoke(init)

            assert result.exit_code == 0
            assert 'Project created' in result.output

            with open('hello_world_agent/main.py', 'r') as f:
                contents = f.read()

            assert MAIN_CONTENT in contents

    def test_returns_requirements_file_when_called(self, runner):
        with runner.isolated_filesystem():
            result = runner.invoke(init)

            assert result.exit_code == 0
            assert 'Project created' in result.output

            with open('hello_world_agent/requirements.txt', 'r') as f:
                contents = f.read()

            assert REQUIREMENTS_CONTENT in contents

    def test_returns_exit_code_2_when_directory_already_exists(self, runner):
        dir_name = 'hello_world_agent'
        with runner.isolated_filesystem():

            os.makedirs(dir_name)

            result = runner.invoke(init)

            assert result.exit_code == 1
            assert f'{dir_name} already exists.' in result.output
            assert 'Aborted!' in result.output
