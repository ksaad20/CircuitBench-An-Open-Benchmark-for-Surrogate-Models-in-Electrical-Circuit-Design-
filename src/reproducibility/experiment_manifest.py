"""
CircuitBench Experiment Manifest
================================

Generate reproducibility manifests.

Author
------
CircuitBench Development Team
"""

from __future__ import annotations

import json
import os
import platform
import random
import subprocess
import sys
from datetime import datetime

import numpy as np


class ExperimentManifest:
    @staticmethod
    def git_commit():

        try:
            return (
                subprocess.check_output(
                    ["git", "rev-parse", "HEAD"],
                    stderr=subprocess.DEVNULL,
                )
                .decode()
                .strip()
            )

        except Exception:
            return "Unavailable"

    @staticmethod
    def installed_packages():

        try:
            import pkg_resources

            packages = {}

            for pkg in pkg_resources.working_set:
                packages[pkg.project_name] = pkg.version

            return dict(sorted(packages.items()))

        except Exception:
            return {}

    @staticmethod
    def hardware():

        return {
            "machine": platform.machine(),
            "processor": platform.processor(),
            "cpu_count": os.cpu_count(),
        }

    @staticmethod
    def system():

        return {
            "platform": platform.platform(),
            "system": platform.system(),
            "release": platform.release(),
            "python": sys.version,
        }

    @staticmethod
    def seed(seed=42):

        random.seed(seed)

        np.random.seed(seed)

        try:
            import torch

            torch.manual_seed(seed)

            if torch.cuda.is_available():
                torch.cuda.manual_seed_all(seed)

        except Exception:
            pass

        return seed

    @staticmethod
    def create(seed=42):

        ExperimentManifest.seed(seed)

        return {
            "timestamp": datetime.now().isoformat(),
            "seed": seed,
            "git_commit": ExperimentManifest.git_commit(),
            "system": ExperimentManifest.system(),
            "hardware": ExperimentManifest.hardware(),
            "packages": ExperimentManifest.installed_packages(),
        }

    @staticmethod
    def save(filename, seed=42):

        manifest = ExperimentManifest.create(seed)

        with open(
            filename,
            "w",
            encoding="utf-8",
        ) as f:
            json.dump(
                manifest,
                f,
                indent=4,
            )
