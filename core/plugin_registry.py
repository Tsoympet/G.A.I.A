import os
import importlib
import traceback

# Centralized plugin event registry
PLUGIN_HOOKS = {}

def register_plugin_hook(event_name, callback):
    if event_name not in PLUGIN_HOOKS:
        PLUGIN_HOOKS[event_name] = []
    PLUGIN_HOOKS[event_name].append(callback)

def trigger_plugin_event(event_name, *args, **kwargs):
    for callback in PLUGIN_HOOKS.get(event_name, []):
        try:
            callback(*args, **kwargs)
        except Exception as e:
            print(f"[Plugin Error] while handling '{event_name}': {e}")
            traceback.print_exc()

def load_plugins(plugin_directory="gaia/plugins"):
    """
    Dynamically load all plugins from the specified directory.
    """
    for filename in os.listdir(plugin_directory):
        if filename.endswith(".py") and filename != "__init__.py":
            plugin_name = filename[:-3]
            try:
                importlib.import_module(f"gaia.plugins.{plugin_name}")
                print(f"[Plugin Loaded] {plugin_name}")
            except Exception as e:
                print(f"[Plugin Load Failed] {plugin_name}: {e}")
                traceback.print_exc()

def register_default_plugins():
    """
    Predefined plugins registered manually without dynamic import.
    For example, gambling-related plugin behavior.
    """
    try:
        from gaia.modules.casino.casino_behavior_model import handle_gambling_behavior
        register_plugin_hook('on_dream_generated', handle_gambling_behavior)
        register_plugin_hook('on_gambling_session_detected', handle_gambling_behavior)
        print("[Plugin] Default gambling behavior hooks registered.")
    except ImportError as e:
        print(f"[Plugin Warning] Default gambling behavior module missing: {e}")
