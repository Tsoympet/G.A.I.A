import json
import os
from datetime import datetime

class MemoryStore:
    def __init__(self, memory_file='emotional_memory.json'):
        self.memory_file = memory_file
        self.memories = self._load()

    def _load(self):
        if os.path.exists(self.memory_file):
            with open(self.memory_file, 'r') as f:
                return json.load(f)
        return []

    def save_dream(self, dream_data):
        self.memories.append({
            'timestamp': dream_data['time'],
            'mood': dream_data['mood'],
            'topic': dream_data['seed_topic'],
            'summary': dream_data['content']
        })
        self._persist()

    def _persist(self):
        with open(self.memory_file, 'w') as f:
            json.dump(self.memories, f, indent=2)

    def recent_experiences(self, limit=5):
        return self.memories[-limit:]

    def get_all(self):
        return self.memories

    def clear_memory(self):
        self.memories = []
        self._persist()

    def add_manual_entry(self, mood, topic, summary):
        self.memories.append({
            'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            'mood': mood,
            'topic': topic,
            'summary': summary
        })
        self._persist()
