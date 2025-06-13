import random
from datetime import datetime

class MemoryManager:
    def __init__(self):
        self.short_term = []
        self.long_term = []
        self.max_short = 50
        self.listeners = []

    def log_event(self, event):
        timestamped = {"event": event, "timestamp": datetime.now()}
        self.short_term.append(timestamped)
        if len(self.short_term) > self.max_short:
            archived = self.short_term.pop(0)
            self.long_term.append(archived)
            self.trigger_dream_check(archived)
        self._notify(event)

    def _notify(self, event):
        for listener in self.listeners:
            listener(event)

    def register_listener(self, callback):
        self.listeners.append(callback)

    def recall_recent(self, n=5):
        return self.short_term[-n:]

    def recall_significant(self):
        return [m for m in self.long_term if "important" in m["event"].lower()]

    def trigger_dream_check(self, memory):
        if random.random() < 0.15:  # 15% chance
            from gaia.core.dream_state_engine import trigger_dream
            trigger_dream(memory)

    def forget(self):
        self.short_term.clear()
        self.long_term.clear()

