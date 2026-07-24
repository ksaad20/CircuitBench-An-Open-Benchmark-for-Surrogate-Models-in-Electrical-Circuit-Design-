"""
Formatting utilities for the Circuit Bench CLI.
"""

from __future__ import annotations

import textwrap
from collections.abc import Iterable
from typing import Any


def indent(text: str, spaces: int = 4) -> str:
    """Indent each line of text by the specified number of spaces."""
    prefix = " " * spaces
    return "\n".join(f"{prefix}{line}" for line in text.splitlines())


def banner(title: str, width: int = 80, fill: str = "=") -> str:
    """Create a banner with a centered title."""
    width = max(width, len(title) + 4)
    line = fill * width
    return f"{line}\n{title.center(width)}\n{line}"


def section(title: str, width: int = 80) -> str:
    """Create a section heading."""
    underline = "-" * min(width, max(len(title), 1))
    return f"{title}\n{underline}"


def separator(width: int = 80, char: str = "-") -> str:
    """Return a separator line."""
    return char * width


def bullet_list(items: Iterable[Any], bullet: str = "-") -> str:
    """Format an iterable as a bulleted list."""
    return "\n".join(f"{bullet} {item}" for item in items)


def numbered_list(items: Iterable[Any]) -> str:
    """Format an iterable as a numbered list."""
    return "\n".join(f"{index}. {item}" for index, item in enumerate(items, start=1))


def key_value(key: str, value: Any) -> str:
    """Format a key-value pair."""
    return f"{key}: {value}"


def pad(text: str, width: int) -> str:
    """Pad text to the given width."""
    return text.ljust(width)


def center(text: str, width: int) -> str:
    """Center text within the specified width."""
    return text.center(width)


def truncate(text: str, length: int = 80) -> str:
    """Truncate text to the specified length."""
    if len(text) <= length:
        return text

    if length <= 3:
        return text[:length]

    return text[: length - 3] + "..."


def wrap(text: str, width: int = 80) -> str:
    """Wrap text to the specified width."""
    return textwrap.fill(text, width=width)


def blank() -> str:
    """Return a blank string."""
    return ""


__all__ = [
    "banner",
    "blank",
    "bullet_list",
    "center",
    "indent",
    "key_value",
    "numbered_list",
    "pad",
    "section",
    "separator",
    "truncate",
    "wrap",
]
