from pycounting import __version__ as VERSION
from pycounting.cli import pycounting


def test_version(runner):
    with runner.isolated_filesystem():
        result = runner.invoke(pycounting, ["--version"])
        assert not result.exception
        assert result.output == f"{VERSION}\n"


def test_pycounting(runner):
    with runner.isolated_filesystem():
        result = runner.invoke(pycounting, ["--setup-settings"], input="test\n")
        assert not result.exception
        with open("settings.txt", "r") as file:
            assert file.read() == "test=test\n"
