"""
Version command for the Circuit Bench CLI.
"""

from __future__ import annotations

import platform
import sys
from importlib.metadata import PackageNotFoundError, version

import click

PACKAGE_NAME = "circuitbench"


def get_version() -> str:
    """Return the installed package version."""
    try:
        return version(PACKAGE_NAME)
    except PackageNotFoundError:
        return "development"


@click.command(name="version")
@click.option(
    "--verbose",
    is_flag=True,
    help="Display detailed version information.",
)
def version_command(verbose: bool) -> None:
    """
    Display Circuit Bench version information.
    """
    click.echo(f"Circuit Bench {get_version()}")

    if verbose:
        click.echo(f"Python : {platform.python_version()}")
        click.echo(f"Platform : {platform.platform()}")
        click.echo(f"Executable : {sys.executable}")


__all__ = [
    "get_version",
    "version_command",
]
