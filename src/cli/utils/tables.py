"""Table utilities without external dependencies."""

from __future__ import annotations

from typing import Iterable


def print_table(headers: list[str], rows: Iterable[Iterable[object]]) -> None:
    rows = [[str(c) for c in row] for row in rows]
    widths = [len(h) for h in headers]

    for row in rows:
        for i, cell in enumerate(row):
            widths[i] = max(widths[i], len(cell))

    header = " | ".join(
        h.ljust(widths[i]) for i, h in enumerate(headers)
    )
    divider = "-+-".join("-" * w for w in widths)

    print(header)
    print(divider)

    for row in rows:
        print(
            " | ".join(
                row[i].ljust(widths[i])
                for i in range(len(headers))
            )
        )
