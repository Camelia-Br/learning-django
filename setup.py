from setuptools import setup
import distutils.cmd
import subprocess
from typing import List


def create_command(text: str, commands: List[List[str]]):
    class CustomCommand(distutils.cmd.Command):
        user_options: List[str] = []
        description = text

        def initialize_options(self):
            pass

        def finalize_options(self):
            pass

        def run(self):
            for cmd in commands:
                subprocess.check_call(cmd)

    return CustomCommand


setup(
    name="some-project",
    version="1.0.0",
    author="Some Author",
    author_email="some@mail.soon",
    description="Some description",
    license="MIT",
    packages=[],
    cmdclass=dict(
        format=create_command("Auto-formats code", [["black", "-S", "--config", "./pyproject.toml", "."]]),
        verify_format=create_command(
            "Verifies that code is properly formatted",
            [["black", "-S", "--check", "--config", "./pyproject.toml", "."]],
        ),
        lint=create_command("Lints the code", [["flake8", "."]]),
        fix=create_command(
            "Auto-fixes and lints code",
            [
                ["python", "setup.py", "format"],
                ["python", "setup.py", "lint"],
            ],
        ),
        verify=create_command(
            "Verifies that code is valid",
            [
                ["python", "setup.py", "verify_format"],
                ["python", "setup.py", "lint"],
            ],
        ),
        test=create_command("Runs tests", [["docker-compose", "run", "web", "python", "manage.py", "test"]]),
    ),
)
