"""
Statistics command for the Circuit Bench CLI.
"""

from __future__ import annotations

import platform
import sys
from pathlib import Path

import typer

app = typer.Typer(help="Repository statistics commands.")


def count_files(directory: Path, suffix: str) -> int:
    """
    Count files with a given suffix recursively.
    """
    return sum(1 for file in directory.rglob(f"*{suffix}") if file.is_file())


def directory_size(directory: Path) -> int:
    """
    Calculate total directory size in bytes.
    """
    total = 0

    for file in directory.rglob("*"):
        if file.is_file():
            total += file.stat().st_size

    return total


def human_size(size: int) -> str:
    """
    Convert bytes to a human-readable string.
    """
    units = ("B", "KB", "MB", "GB", "TB")
    value = float(size)

    for unit in units:
        if value < 1024 or unit == units[-1]:
            return f"{value:.2f} {unit}"
        value /= 1024

    return f"{value:.2f} TB"


@app.command("show")
def stats_command(
    path: Path = typer.Argument(
        Path("."),
        exists=True,
        file_okay=False,
        dir_okay=True,
        resolve_path=True,
    ),
) -> None:
    """
    Display repository statistics.
    """
    py_files = count_files(path, ".py")
    json_files = count_files(path, ".json")
    yaml_files = count_files(path, ".yaml") + count_files(path, ".yml")
    notebook_files = count_files(path, ".ipynb")

    typer.echo("Circuit Bench Statistics")
    typer.echo("-" * 40)
    typer.echo(f"Root directory : {path.resolve()}")
    typer.echo(f"Python files   : {py_files}")
    typer.echo(f"JSON files     : {json_files}")
    typer.echo(f"YAML files     : {yaml_files}")
    typer.echo(f"Notebooks      : {notebook_files}")
    typer.echo(f"Repository size: {human_size(directory_size(path))}")
    typer.echo()
    typer.echo(f"Python     : {platform.python_version()}")
    typer.echo(f"Platform   : {platform.platform()}")
    typer.echo(f"Executable : {sys.executable}")


__all__ = [
    "app",
    "count_files",
    "directory_size",
    "human_size",
    "stats_command",
]

command = stats_command
execute = stats_command


def register(cli) -> None:
    """Register the Typer application with another Typer app."""
    cli.add_typer(app, name="stats")


if __name__ == "__main__":
    app()
