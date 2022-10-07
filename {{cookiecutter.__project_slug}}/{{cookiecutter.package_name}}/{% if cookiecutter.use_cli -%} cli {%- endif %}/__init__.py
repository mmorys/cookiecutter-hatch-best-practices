import click

from ..__about__ import __version__


@click.group(
    context_settings={"help_option_names": ["-h", "--help"]},
    invoke_without_command=True,
)
@click.version_option(version=__version__, prog_name="{{ cookiecutter.project_name }}")
@click.pass_context
def {{ cookiecutter.__package_name }}(ctx: click.Context):
    click.echo("Hello world!")
