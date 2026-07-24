"""
CircuitBench Experiment Logger
==============================

Experiment logging and artifact management.

Author
------
CircuitBench Development Team
"""

from __future__ import annotations

import json
import shutil
from dataclasses import asdict, dataclass
from datetime import datetime
from pathlib import Path


@dataclass
class ExperimentRecord:
    experiment_name: str

    run_id: str

    timestamp: str

    output_directory: str

    notes: str = ""


class ExperimentLogger:
    def __init__(
        self,
        root="experiments",
    ):

        self.root = Path(root)

        self.root.mkdir(
            parents=True,
            exist_ok=True,
        )

    def create_run(
        self,
        experiment_name,
        notes="",
    ):

        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

        run_id = f"{experiment_name}_{timestamp}"

        output = self.root / run_id

        output.mkdir(
            parents=True,
            exist_ok=True,
        )

        record = ExperimentRecord(
            experiment_name=experiment_name,
            run_id=run_id,
            timestamp=datetime.now().isoformat(),
            output_directory=str(output),
            notes=notes,
        )

        self.save_record(record)

        return record

    @staticmethod
    def save_record(
        record,
    ):

        path = Path(record.output_directory)

        with open(
            path / "run.json",
            "w",
            encoding="utf-8",
        ) as f:
            json.dump(
                asdict(record),
                f,
                indent=4,
            )

    @staticmethod
    def save_metrics(
        metrics,
        output_directory,
    ):

        with open(
            Path(output_directory) / "metrics.json",
            "w",
            encoding="utf-8",
        ) as f:
            json.dump(
                metrics,
                f,
                indent=4,
            )

    @staticmethod
    def copy_artifact(
        source,
        output_directory,
    ):

        source = Path(source)

        destination = Path(output_directory)

        destination.mkdir(
            parents=True,
            exist_ok=True,
        )

        shutil.copy2(
            source,
            destination / source.name,
        )

    def history(self):

        runs = []

        for folder in sorted(self.root.iterdir()):
            file = folder / "run.json"

            if file.exists():
                with open(
                    file,
                    encoding="utf-8",
                ) as f:
                    runs.append(json.load(f))

        return runs
