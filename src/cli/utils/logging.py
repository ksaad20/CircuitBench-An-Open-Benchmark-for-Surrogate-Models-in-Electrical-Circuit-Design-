"""
Logging utilities for the Circuit Bench CLI.
"""

from __future__ import annotations

import logging
import sys
from pathlib import Path
from typing import Final

DEFAULT_FORMAT: Final[str] = "%(asctime)s | %(levelname)-8s | %(name)s | %(message)s"

DEFAULT_DATE_FORMAT: Final[str] = "%Y-%m-%d %H:%M:%S"

_CONFIGURED = False


def configure_logging(
    *,
    level: int = logging.INFO,
    log_file: str | Path | None = None,
    console: bool = True,
) -> None:
    """
    Configure the root logger.

    Parameters
    ----------
    level
        Logging level.
    log_file
        Optional path to a log file.
    console
        Enable console logging.
    """
    global _CONFIGURED

    root = logging.getLogger()

    if _CONFIGURED:
        root.handlers.clear()

    root.setLevel(level)

    formatter = logging.Formatter(
        DEFAULT_FORMAT,
        datefmt=DEFAULT_DATE_FORMAT,
    )

    if console:
        console_handler = logging.StreamHandler(sys.stdout)
        console_handler.setFormatter(formatter)
        root.addHandler(console_handler)

    if log_file is not None:
        path = Path(log_file)
        path.parent.mkdir(parents=True, exist_ok=True)

        file_handler = logging.FileHandler(
            path,
            encoding="utf-8",
        )
        file_handler.setFormatter(formatter)
        root.addHandler(file_handler)

    _CONFIGURED = True


def get_logger(name: str) -> logging.Logger:
    """
    Return a configured logger.
    """
    if not _CONFIGURED:
        configure_logging()

    return logging.getLogger(name)


def set_level(level: int) -> None:
    """
    Set the root logging level.
    """
    logging.getLogger().setLevel(level)


def enable_debug() -> None:
    """
    Enable DEBUG logging.
    """
    set_level(logging.DEBUG)


def disable_logging() -> None:
    """
    Disable all logging.
    """
    logging.disable(logging.CRITICAL)


def enable_logging() -> None:
    """
    Re-enable logging.
    """
    logging.disable(logging.NOTSET)


def add_file_handler(
    path: str | Path,
    *,
    level: int | None = None,
) -> logging.FileHandler:
    """
    Add an additional file handler.
    """
    handler = logging.FileHandler(
        Path(path),
        encoding="utf-8",
    )

    handler.setFormatter(
        logging.Formatter(
            DEFAULT_FORMAT,
            datefmt=DEFAULT_DATE_FORMAT,
        )
    )

    if level is not None:
        handler.setLevel(level)

    logging.getLogger().addHandler(handler)

    return handler


def remove_handler(handler: logging.Handler) -> None:
    """
    Remove a logging handler.
    """
    logger = logging.getLogger()
    logger.removeHandler(handler)
    handler.close()


__all__ = [
    "DEFAULT_DATE_FORMAT",
    "DEFAULT_FORMAT",
    "add_file_handler",
    "configure_logging",
    "disable_logging",
    "enable_debug",
    "enable_logging",
    "get_logger",
    "remove_handler",
    "set_level",
]
