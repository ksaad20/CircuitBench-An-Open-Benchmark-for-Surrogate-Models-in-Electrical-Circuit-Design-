
"""
Cleaning commands for the Circuit Bench CLI.
"""

from __future__ import annotations

import typer

app = typer.Typer(help="Cleaning commands.")


@app.command("all")
def clean_all() -> None:
    """
    Clean all generated files.
    """
    typer.echo("Clean completed.")


# Backward compatibility
command = clean_all
execute = clean_all


def register(cli) -> None:
    """
    Register the cleaning commands with the CLI.
    """
    cli.add_typer(app, name="clean")


if __name__ == "__main__":
    app()
