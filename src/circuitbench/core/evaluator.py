"""
Benchmark evaluation engine.
"""

from statistics import mean


class Evaluator:
    def __init__(self):

        self.results = {}

    def add_metric(self, name, value):

        self.results[name] = value

    def get_metric(self, name):

        return self.results.get(name)

    def summary(self):

        return self.results

    def clear(self):

        self.results.clear()

    def compare(self, first, second):

        comparison = {}

        keys = set(first.keys()) | set(second.keys())

        for key in keys:
            comparison[key] = {"first": first.get(key), "second": second.get(key)}

        return comparison

    def average(self, metrics):

        output = {}

        if not metrics:
            return output

        for key in metrics[0]:
            output[key] = mean(item[key] for item in metrics if key in item)

        return output
