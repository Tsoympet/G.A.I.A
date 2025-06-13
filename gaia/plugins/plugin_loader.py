import importlib
import os

class PluginLoader:
    def __init__(self, plugin_dir):
        self.plugin_dir = plugin_dir
        self.plugins = {}

    def load_plugins(self):
        for filename in os.listdir(self.plugin_dir):
            if filename.endswith(".py") and filename != "__init__.py":
                module_name = filename[:-3]
                try:
                    module = importlib.import_module(f"{self.plugin_dir.replace('/', '.')}.{module_name}")
                    self.plugins[module_name] = module
                    print(f"[PluginLoader] Loaded: {module_name}")
                except Exception as e:
                    print(f"[PluginLoader] Failed to load {module_name}: {e}")

    def get_plugin(self, name):
        return self.plugins.get(name)

