"""
CSV Loader
"""

from pathlib import Path

import pandas as pd


class CSVLoader:
    def __init__(self, encoding="utf-8"):

        self.encoding = encoding

    def load(self, filename):

        filename = Path(filename)

        if not filename.exists():
            raise FileNotFoundError(filename)

        return pd.read_csv(filename, encoding=self.encoding)

    def save(self, dataframe, filename):

        dataframe.to_csv(filename, index=False, encoding=self.encoding)

    def preview(self, filename, rows=5):

        return self.load(filename).head(rows)
