"""Version command."""

from __future__ import annotations

import typer

app = typer.Typer(help="Display version information.")


@app.command()
def main() -> None:
    """Show the Circuit-Bench version."""
    typer.echo("Circuit-Bench 0.1.0")
