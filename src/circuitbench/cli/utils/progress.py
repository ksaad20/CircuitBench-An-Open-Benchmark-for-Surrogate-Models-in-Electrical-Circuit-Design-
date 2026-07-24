"""Progress utilities for CircuitBench CLI."""

from __future__ import annotations

from collections.abc import Iterable, Iterator
from dataclasses import dataclass, field
from typing import Any

from typing_extensions import Self


@dataclass
class _Task:
    description: str = ""
    total: int | float | None = None
    completed: int | float = 0
    fields: dict[str, Any] = field(default_factory=dict)


class Progress:
    """Small drop-in replacement for rich.progress.Progress."""

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        self._tasks: dict[int, _Task] = {}
        self._next_task_id = 1

    def __enter__(self) -> Self:
        return self

    def __exit__(self, exc_type, exc, tb) -> bool:
        return False

    def start(self) -> None:
        return None

    def stop(self) -> None:
        return None

    def add_task(
        self,
        description: str = "",
        total: float | None = None,
        completed: float = 0,
        **fields: Any,
    ) -> int:
        task_id = self._next_task_id
        self._next_task_id += 1
        self._tasks[task_id] = _Task(
            description=description,
            total=total,
            completed=completed,
            fields=dict(fields),
        )
        return task_id

    def update(
        self,
        task_id: int,
        advance: float = 0,
        completed: float | None = None,
        description: str | None = None,
        total: float | None = None,
        **fields: Any,
    ) -> None:
        task = self._tasks.setdefault(task_id, _Task())
        if completed is not None:
            task.completed = completed
        else:
            task.completed += advance
        if description is not None:
            task.description = description
        if total is not None:
            task.total = total
        if fields:
            task.fields.update(fields)

    def remove_task(self, task_id: int) -> None:
        self._tasks.pop(task_id, None)

    def track(
        self, iterable: Iterable[Any], *args: Any, **kwargs: Any
    ) -> Iterator[Any]:
        yield from iterable

    def print(self, *args: Any, **kwargs: Any) -> None:
        print(*args, **kwargs)


def track(iterable: Iterable[Any], *args: Any, **kwargs: Any) -> Iterator[Any]:
    """Standalone track helper compatible with rich.progress.track."""
    yield from iterable


__all__ = ["Progress", "track"]
