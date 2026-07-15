"""
Leaderboard commands for the Circuit Bench CLI.
"""

from __future__ import annotations

import typer

app = typer.Typer(help="Leaderboard commands.")


@app.command("show")
def show() -> None:
    """
    Display the benchmark leaderboard.
    """
    typer.echo("Leaderboard is empty.")


# Backward compatibility
command = show
execute = show


def register(cli) -> None:
    """
    Register the leaderboard commands with the CLI.
    """
    cli.add_typer(app, name="leaderboard")


if __name__ == "__main__":
    app()
