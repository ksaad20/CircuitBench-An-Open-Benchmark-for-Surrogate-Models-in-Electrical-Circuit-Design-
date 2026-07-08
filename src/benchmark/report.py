"""
Benchmark reports.
"""

class Report:

    @staticmethod
    def markdown(results):

        text="# CircuitBench Report\n\n"

        for k,v in results.items():

            text+=f"- **{k}** : {v}\n"

        return text
