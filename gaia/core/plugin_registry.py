import importlib
import os
import traceback

PLUGIN_HOOKS = {}

def register_plugin_hook(event_name, callback):
    if event_name not in PLUGIN_HOOKS:
        PLUGIN_HOOKS[event_name] = []
    PLUGIN_HOOKS[event_name].append(callback)

def trigger_plugin_event(event_name, *args, **kwargs):
    if event_name in PLUGIN_HOOKS:
        for callback in PLUGIN_HOOKS[event_name]:
            try:
                callback(*args, **kwargs)
            except Exception as e:
                print(f"[Plugin Error] {e}")
                traceback.print_exc()

def load_plugins(plugin_directory="gaia/plugins"):
    for filename in os.listdir(plugin_directory):
        if filename.endswith(".py") and filename != "__init__.py":
            plugin_name = filename[:-3]
            try:
                importlib.import_module(f"gaia.plugins.{plugin_name}")
                print(f"[Plugin Loaded] {plugin_name}")
            except Exception as e:
                print(f"[Plugin Load Failed] {plugin_name}: {e}")
                traceback.print_exc()
