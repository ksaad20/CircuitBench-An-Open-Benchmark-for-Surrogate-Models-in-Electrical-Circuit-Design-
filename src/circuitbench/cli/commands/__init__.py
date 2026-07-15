from __future__ import annotations

from .base import app
from .benchmarks import app as benchmarks_app
from .cache import app as cache_app
from .clean import app as clean_app
from .config import app as config_app
from .create import app as create_app
from .datasets import app as datasets_app
from .doctor import app as doctor_app
from .evaluate import app as evaluate_app
from .export import app as export_app
from .info import app as info_app
from .leaderboard import app as leaderboard_app
from .list import app as list_app
from .plugins import app as plugins_app
from .report import app as report_app
from .run import app as run_app
from .shall import app as shall_app
from .stats import app as stats_app
from .validate import app as validate_app
from .version import app as version_app

__all__ = [
    "app",
    "benchmarks_app",
    "cache_app",
    "clean_app",
    "config_app",
    "create_app",
    "datasets_app",
    "doctor_app",
    "evaluate_app",
    "export_app",
    "info_app",
    "leaderboard_app",
    "list_app",
    "plugins_app",
    "report_app",
    "run_app",
    "shall_app",
    "stats_app",
    "validate_app",
    "version_app",
]
