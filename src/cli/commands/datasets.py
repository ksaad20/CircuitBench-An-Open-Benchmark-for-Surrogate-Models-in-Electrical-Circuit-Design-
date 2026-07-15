
"""
Dataset management commands for the Circuit Bench CLI.
"""

from __future__ import annotations

import typer

app = typer.Typer(help="Dataset management commands.")


@app.command("list")
def list_datasets() -> None:
    """
    List all registered datasets.
    """
    typer.echo("No datasets registered.")


# Backward compatibility
command = list_datasets
execute = list_datasets


def register(cli) -> None:
    """
    Register the dataset commands with the CLI.
    """
    cli.add_typer(app, name="datasets")


if __name__ == "__main__":
    app()
