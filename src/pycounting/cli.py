"""pycounting CLI"""


import click
from pycounting import __version__ as VERSION


@click.command()
@click.option("--version", is_flag=True, help="Shows the version of pycounting")
def pycounting(version):
    """The main way to engange with pycounting is with this cli"""
    if version:
        click.echo(f"{VERSION}")
