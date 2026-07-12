"""
CircuitBench Reporting Engine
=============================

Central reporting engine for benchmark experiments.

Produces publication-ready statistical summaries and exports.

Author
------
CircuitBench Development Team
"""

from __future__ import annotations

import json
from datetime import datetime
from pathlib import Path
from typing import Any, Dict

import pandas as pd


class BenchmarkReport:
    """
    Central benchmark reporting class.
    """

    def __init__(self, title: str):

        self.title = title

        self.created = datetime.utcnow().isoformat()

        self.sections = []

        self.tables = {}

        self.figures = {}

        self.statistics = {}

        self.metadata = {}

    # -----------------------------------------------------

    def add_section(
        self,
        title: str,
        content: str,
    ):

        self.sections.append({

            "title": title,

            "content": content,

        })

    # -----------------------------------------------------

    def add_statistics(
        self,
        name: str,
        results: Dict,
    ):

        self.statistics[name] = results

    # -----------------------------------------------------

    def add_table(
        self,
        name: str,
        dataframe,
    ):

        if not isinstance(dataframe, pd.DataFrame):

            dataframe = pd.DataFrame(dataframe)

        self.tables[name] = dataframe

    # -----------------------------------------------------

    def add_figure(
        self,
        name: str,
        path: str,
    ):

        self.figures[name] = path

    # -----------------------------------------------------

    def set_metadata(
        self,
        **kwargs,
    ):

        self.metadata.update(kwargs)

    # -----------------------------------------------------

    def summary(self):

        return {

            "title": self.title,

            "created": self.created,

            "sections": len(self.sections),

            "tables": len(self.tables),

            "figures": len(self.figures),

            "statistics": len(self.statistics),

        }

    # -----------------------------------------------------

    def export_json(
        self,
        filename="benchmark_report.json",
    ):

        output = {

            "title": self.title,

            "created": self.created,

            "metadata": self.metadata,

            "sections": self.sections,

            "statistics": self.statistics,

            "tables": {

                k: v.to_dict()

                for k, v in self.tables.items()

            },

            "figures": self.figures,

        }

        with open(

            filename,

            "w",

            encoding="utf-8",

        ) as f:

            json.dump(

                output,

                f,

                indent=4,

            )

    # -----------------------------------------------------

    def export_markdown(

        self,

        filename="benchmark_report.md",

    ):

        with open(

            filename,

            "w",

            encoding="utf-8",

        ) as f:

            f.write(

                f"# {self.title}\n\n"

            )

            f.write(

                f"Generated: {self.created}\n\n"

            )

            for section in self.sections:

                f.write(

                    f"## {section['title']}\n\n"

                )

                f.write(

                    section["content"]

                )

                f.write("\n\n")

            if self.statistics:

                f.write(

                    "# Statistical Results\n\n"

                )

                for name, value in self.statistics.items():

                    f.write(

                        f"## {name}\n"

                    )

                    f.write("```json\n")

                    f.write(

                        json.dumps(

                            value,

                            indent=4,

                        )

                    )

                    f.write("\n```\n\n")

            for name, table in self.tables.items():

                f.write(

                    f"## {name}\n\n"

                )

                f.write(

                    table.to_markdown(

                        index=False

                    )

                )

                f.write("\n\n")

    # -----------------------------------------------------

    def export_csv(

        self,

        directory="tables",

    ):

        directory = Path(directory)

        directory.mkdir(

            parents=True,

            exist_ok=True,

        )

        for name, table in self.tables.items():

            table.to_csv(

                directory / f"{name}.csv",

                index=False,

            )

    # -----------------------------------------------------

    def print_summary(self):

        print("=" * 70)

        print("CircuitBench Report")

        print("=" * 70)

        for k, v in self.summary().items():

            print(f"{k:15}: {v}")

        print("=" * 70)


__all__ = [

    "BenchmarkReport",

]

