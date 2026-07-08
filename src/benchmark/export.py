"""
Export utilities.
"""

import json


class Exporter:

    @staticmethod
    def csv(df,path):

        df.to_csv(path,index=False)

    @staticmethod
    def excel(df,path):

        df.to_excel(path,index=False)

    @staticmethod
    def json(results,path):

        with open(path,"w") as f:

            json.dump(results,f,indent=4)
