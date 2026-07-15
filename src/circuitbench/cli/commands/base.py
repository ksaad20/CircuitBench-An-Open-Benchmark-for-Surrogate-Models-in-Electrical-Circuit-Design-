"""
Base CLI module for Circuit-Bench.
Defines the main application entry point.
"""

import click


@click.group()
@click.version_option()
def app():
    """
    Circuit-Bench: A tool for physics-based trade arbitrage.
    """
    pass


# Example command to verify functionality
@app.command()
def info():
    """Display project information."""
    click.echo("Circuit-Bench: Computational physics for trade arbitrage.")
