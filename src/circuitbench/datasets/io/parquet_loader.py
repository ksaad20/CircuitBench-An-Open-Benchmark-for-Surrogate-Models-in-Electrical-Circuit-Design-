"""
Parquet Loader
"""

from pathlib import Path

import pandas as pd


class ParquetLoader:
    def load(self, filename):

        filename = Path(filename)

        if not filename.exists():
            raise FileNotFoundError(filename)

        return pd.read_parquet(filename)

    def save(self, dataframe, filename):

        dataframe.to_parquet(filename, index=False)
