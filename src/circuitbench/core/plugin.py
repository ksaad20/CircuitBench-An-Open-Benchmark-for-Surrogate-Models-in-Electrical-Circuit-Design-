"""
Plugin system for CircuitBench.
"""

from abc import ABC, abstractmethod


class Plugin(ABC):
    """
    Base plugin interface.
    """

    def __init__(self, name: str):
        self.name = name

    @abstractmethod
    def initialize(self):
        """Initialize plugin."""

    @abstractmethod
    def execute(self, *args, **kwargs):
        """Execute plugin."""

    @abstractmethod
    def shutdown(self):
        """Cleanup plugin resources."""


class PluginManager:
    def __init__(self):
        self.plugins = {}

    def register(self, plugin: Plugin):

        self.plugins[plugin.name] = plugin
        plugin.initialize()

    def unregister(self, name):

        if name in self.plugins:
            self.plugins[name].shutdown()
            del self.plugins[name]

    def get(self, name):

        return self.plugins.get(name)

    def execute(self, name, *args, **kwargs):

        plugin = self.get(name)

        if plugin is None:
            raise KeyError(f"Plugin '{name}' not found.")

        return plugin.execute(*args, **kwargs)

    def list_plugins(self):

        return sorted(self.plugins.keys())

    def clear(self):

        for plugin in self.plugins.values():
            plugin.shutdown()

        self.plugins.clear()
