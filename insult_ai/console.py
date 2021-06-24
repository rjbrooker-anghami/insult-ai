"""Command-line interface. A command line tool for using Detoxify.py"""
import click
from . import __version__
from detoxify import Detoxify
import pandas as pd 

@click.command()
@click.option('--message', default="", help='A message to send to insult-ai.')
@click.version_option(version=__version__)
def insult_me(
        message : str 
    ):
    """
    A command line tool for .
    
    Calls Detoxify.py 'original' model and returns the results. 
    
    Args:
        message: A message to be sent to the sentiment analysis model.
    
    Returns:
        None
    
    Example:
        >>> import click.testing
        >>> runner = click.testing.CliRunner()
        >>> result = runner.invoke(insult_me, ['--message="You look nice."'])
        >>> print(result.exit_code)
        0
    """
    
    #load model
    model = Detoxify('original')
    
    #predict toxicity
    results = model.predict(message)
    
    #echo results
    click.echo(pd.Series(results))
