"""
Experiment management for CircuitBench.
"""

from datetime import datetime
import uuid


class Experiment:

    def __init__(self, name, description=""):

        self.id = str(uuid.uuid4())

        self.name = name

        self.description = description

        self.created = datetime.now()

        self.metrics = {}

        self.parameters = {}

        self.tags = []

        self.status = "initialized"

    def add_parameter(self, key, value):

        self.parameters[key] = value

    def add_metric(self, key, value):

        self.metrics[key] = value

    def add_tag(self, tag):

        if tag not in self.tags:

            self.tags.append(tag)

    def start(self):

        self.status = "running"

    def finish(self):

        self.status = "completed"

    def fail(self):

        self.status = "failed"

    def summary(self):

        return {

            "id": self.id,

            "name": self.name,

            "status": self.status,

            "created": str(self.created),

            "parameters": self.parameters,

            "metrics": self.metrics,

            "tags": self.tags

        }
