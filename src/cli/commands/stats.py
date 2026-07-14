"""
Statistics command for the Circuit Bench CLI.
"""

from __future__ import annotations

import platform
import sys
from pathlib import Path

import click


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


@click.command(name="stats")
@click.argument(
    "path",
    required=False,
    default=".",
    type=click.Path(
        exists=True,
        file_okay=False,
        path_type=Path,
    ),
)
def stats_command(path: Path) -> None:
    """
    Display repository statistics.
    """
    py_files = count_files(path, ".py")
    json_files = count_files(path, ".json")
    yaml_files = count_files(path, ".yaml") + count_files(path, ".yml")
    notebook_files = count_files(path, ".ipynb")

    click.echo("Circuit Bench Statistics")
    click.echo("-" * 40)
    click.echo(f"Root directory : {path.resolve()}")
    click.echo(f"Python files   : {py_files}")
    click.echo(f"JSON files     : {json_files}")
    click.echo(f"YAML files     : {yaml_files}")
    click.echo(f"Notebooks      : {notebook_files}")
    click.echo(f"Repository size: " f"{human_size(directory_size(path))}")
    click.echo()
    click.echo(f"Python     : {platform.python_version()}")
    click.echo(f"Platform   : {platform.platform()}")
    click.echo(f"Executable : {sys.executable}")


__all__ = [
    "count_files",
    "directory_size",
    "human_size",
    "stats_command",
    "command",
    "execute",
    "register",
]

# Compatibility export for the CLI loader.

command = stats_command
execute = stats_command


def register(cli):
    """Register the stats command with a Click group."""
    cli.add_command(stats_command)
