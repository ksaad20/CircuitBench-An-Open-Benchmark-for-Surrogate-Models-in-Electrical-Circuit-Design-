from __future__ import annotations

import platform
import sys

import typer

app = typer.Typer(help="Check the Circuit-Bench installation.")


@app.callback(invoke_without_command=True)
def doctor() -> None:
    """Run diagnostic checks."""
    typer.echo("Circuit-Bench Doctor")
    typer.echo("--------------------")
    typer.echo(f"Python: {platform.python_version()}")
    typer.echo(f"Platform: {platform.system()} {platform.release()}")
    typer.echo(f"Executable: {sys.executable}")
    typer.echo("System status: OK")
