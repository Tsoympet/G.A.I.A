import json
import datetime
import os

class EvolutionTracker:
    def __init__(self, log_path="data/evolution_log.json"):
        self.log_path = log_path
        self.evolution_log = []
        self._load_log()

    def _load_log(self):
        if os.path.exists(self.log_path):
            try:
                with open(self.log_path, "r") as f:
                    self.evolution_log = json.load(f)
            except Exception as e:
                print(f"[EvolutionTracker] Failed to load log: {e}")
                self.evolution_log = []

    def log_event(self, category, description, metadata=None):
        event = {
            "timestamp": datetime.datetime.now().isoformat(),
            "category": category,
            "description": description,
            "metadata": metadata or {}
        }
        self.evolution_log.append(event)
        self._save_log()
        print(f"[EvolutionTracker] Logged: {description}")

    def _save_log(self):
        try:
            with open(self.log_path, "w") as f:
                json.dump(self.evolution_log, f, indent=4)
        except Exception as e:
            print(f"[EvolutionTracker] Failed to save log: {e}")

    def get_recent_events(self, category_filter=None, limit=10):
        filtered = [e for e in self.evolution_log if not category_filter or e["category"] == category_filter]
        return filtered[-limit:]

    def export_log(self, out_path="exported_evolution_log.json"):
        try:
            with open(out_path, "w") as f:
                json.dump(self.evolution_log, f, indent=4)
            return out_path
        except Exception as e:
            print(f"[EvolutionTracker] Export failed: {e}")
            return None

