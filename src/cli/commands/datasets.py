"""Datasets CLI command."""

from __future__ import annotations

import click


@click.command(name="datasets")
def datasets() -> None:
    """Manage Circuit Bench datasets."""
    click.echo("Datasets command is not yet implemented.")
