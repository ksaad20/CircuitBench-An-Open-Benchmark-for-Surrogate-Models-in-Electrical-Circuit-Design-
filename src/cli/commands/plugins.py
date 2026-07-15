"""
Plugin commands for the Circuit Bench CLI.
"""

from __future__ import annotations

import typer

app = typer.Typer(help="Plugin management commands.")


@app.command("list")
def plugins() -> None:
    """
    List all installed plugins.
    """
    typer.echo("No plugins installed.")


# Backward compatibility
command = plugins
execute = plugins


def register(cli) -> None:
    """
    Register the plugin commands with the CLI.
    """
    cli.add_typer(app, name="plugins")


if __name__ == "__main__":
    app()
