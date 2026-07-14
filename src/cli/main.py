"""Circuit-Bench command-line entry point."""

from __future__ import annotations

import typer
import sys
from src.cli.commands.create import app as create_app
from src.cli.commands.version import app as version_app

app = typer.Typer(
    name="circuitbench",
    help="Circuit-Bench command line interface.",
    no_args_is_help=True,
)

app.add_typer(create_app, name="create")
app.add_typer(version_app, name="version")

app = typer.Typer(
    name="circuitbench",
    help="Circuit-Bench command line interface.",
    no_args_is_help=True,
)

app.add_typer(create_app, name="create")
app.add_typer(version_app, name="version")


def main() -> None:
    """Run the CLI application."""

    if len(sys.argv) == 1:
        typer.echo(app.get_help())
        raise SystemExit(0)

    app()


if __name__ == "__main__":
    main()
