from pycounting import __version__ as VERSION
from pycounting.cli import pycounting


def test_pycounting(runner):
    with runner.isolated_filesystem():
        result = runner.invoke(pycounting, ["--version"])
        assert not result.exception
        assert result.output == f"{VERSION}\n"
