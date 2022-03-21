"""pycounting CLI"""


import click
from pycounting import __version__ as VERSION
from pycounting.settings import Settings


@click.command()
@click.option("--version", is_flag=True, help="Shows the version of pycounting")
@click.option("--setup-settings", is_flag=True, help="Interactively add settings")
def pycounting(version, setup_settings):
    """The main way to engange with pycounting is with this cli"""
    if version:
        click.echo(f"{VERSION}")

    if setup_settings:
        Settings.setup_settings()
