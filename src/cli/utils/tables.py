"""
Rich table helpers.
"""

from __future__ import annotations

from rich.console import Console
from rich.table import Table

console = Console()


def display_table(title: str, columns, rows):

    table = Table(title=title)

    for column in columns:
        table.add_column(column)

    for row in rows:
        table.add_row(*[str(x) for x in row])

    console.print(table)
