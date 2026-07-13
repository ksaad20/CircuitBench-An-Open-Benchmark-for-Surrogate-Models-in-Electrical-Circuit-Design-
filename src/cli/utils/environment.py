"""
Environment utilities.
"""

from __future__ import annotations

import os
import platform
import sys


def python_version():
    return platform.python_version()


def operating_system():
    return platform.system()


def executable():
    return sys.executable


def environment_variables():
    return dict(os.environ)


def get_env(name: str, default=None):
    return os.getenv(name, default)
