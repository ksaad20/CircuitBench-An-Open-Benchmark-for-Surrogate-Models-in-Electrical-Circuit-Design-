"""
Ranking Engine.
"""

import pandas as pd


class RankingEngine:

    def rank(self,dataframe):

        df=dataframe.copy()

        df=df.sort_values(
            by="Score",
            ascending=False
        )

        df["Rank"]=range(1,len(df)+1)

        return df
