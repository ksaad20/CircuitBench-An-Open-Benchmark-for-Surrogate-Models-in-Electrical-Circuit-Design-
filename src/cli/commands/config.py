"""
Configuration commands for the Circuit Bench CLI.
"""

from __future__ import annotations

import typer

app = typer.Typer(help="Configuration commands.")


@app.command("show")
def show() -> None:
    """
    Display the current configuration.
    """
    typer.echo("Configuration loaded.")


@app.command("reset")
def reset() -> None:
    """
    Reset the configuration to its default values.
    """
    typer.echo("Configuration reset.")


# Backward compatibility
command = show
execute = show


def register(cli) -> None:
    """
    Register the configuration commands with the CLI.
    """
    cli.add_typer(app, name="config")


if __name__ == "__main__":
    app()
