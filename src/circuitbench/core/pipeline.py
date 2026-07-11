"""
Generic processing pipeline.
"""


class Pipeline:

    def __init__(self, name="Pipeline"):

        self.name = name

        self.steps = []

    def add_step(self, function):

        self.steps.append(function)

    def remove_step(self, function):

        self.steps.remove(function)

    def clear(self):

        self.steps = []

    def execute(self, data):

        output = data

        for step in self.steps:

            output = step(output)

        return output

    def __len__(self):

        return len(self.steps)

    def __repr__(self):

        return f"Pipeline(name={self.name}, steps={len(self.steps)})"
