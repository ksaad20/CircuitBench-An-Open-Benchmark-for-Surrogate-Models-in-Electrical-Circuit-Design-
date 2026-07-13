"""
General helper utilities for the Circuit Bench CLI.
"""

from __future__ import annotations

from collections.abc import Iterable
from pathlib import Path
from typing import Any, TypeVar

T = TypeVar("T")


def ensure_directory(path: str | Path) -> Path:
    """
    Create a directory if it does not already exist.

    Parameters
    ----------
    path
        Directory path.

    Returns
    -------
    Path
        The created (or existing) directory.
    """
    directory = Path(path)
    directory.mkdir(parents=True, exist_ok=True)
    return directory


def flatten(items: Iterable[Iterable[T]]) -> list[T]:
    """
    Flatten a nested iterable.
    """
    return [item for group in items for item in group]


def unique(items: Iterable[T]) -> list[T]:
    """
    Return unique items while preserving order.
    """
    return list(dict.fromkeys(items))


def chunked(items: list[T], size: int) -> list[list[T]]:
    """
    Split a list into chunks.

    Parameters
    ----------
    items
        Input list.
    size
        Chunk size.

    Returns
    -------
    list[list[T]]
    """
    if size <= 0:
        raise ValueError("size must be greater than zero")

    return [items[index : index + size] for index in range(0, len(items), size)]


def safe_get(mapping: dict[str, Any], key: str, default: Any = None) -> Any:
    """
    Safely retrieve a value from a dictionary.
    """
    return mapping.get(key, default)


def is_empty(value: Any) -> bool:
    """
    Check whether a value is considered empty.
    """
    return value is None or value == ""


def pluralize(word: str, count: int) -> str:
    """
    Return a simple pluralized word.
    """
    return word if count == 1 else f"{word}s"


def human_readable_size(size: int) -> str:
    """
    Convert bytes into a human-readable string.
    """
    units = ["B", "KB", "MB", "GB", "TB"]

    value = float(size)

    for unit in units:
        if value < 1024 or unit == units[-1]:
            return f"{value:.2f} {unit}"
        value /= 1024

    return f"{value:.2f} TB"


def elapsed_time(seconds: float) -> str:
    """
    Format elapsed time.
    """
    if seconds < 1:
        return f"{seconds * 1000:.2f} ms"

    if seconds < 60:
        return f"{seconds:.2f} s"

    minutes, remaining = divmod(seconds, 60)
    return f"{int(minutes)} min {remaining:.2f} s"


__all__ = [
    "chunked",
    "elapsed_time",
    "ensure_directory",
    "flatten",
    "human_readable_size",
    "is_empty",
    "pluralize",
    "safe_get",
    "unique",
]
