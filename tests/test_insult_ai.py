
import click.testing
import pytest
from insult_ai import console

@pytest.fixture
def runner():
    """Reusable helper function."""
    return click.testing.CliRunner()

def test_insult_me_succeeds(runner):
    result = runner.invoke(console.insult_me, ['--message="You look nice."'])
    assert result.exit_code == 0
