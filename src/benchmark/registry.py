"""
Benchmark registry.
"""

class Registry:

    def __init__(self):

        self.datasets={}

    def register(self,name,dataset):

        self.datasets[name]=dataset

    def list(self):

        return list(self.datasets.keys())

    def get(self,name):

        return self.datasets[name]
