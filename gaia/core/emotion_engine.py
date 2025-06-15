import random
import json
from datetime import datetime

class EmotionEngine:
    def __init__(self, emotion_file='data/emotional_memory.json'):
        self.emotion_file = Path(emotion_file)
        self.emotions = ["joyful", "calm", "sad", "angry", "curious", "neutral"]
        self.history = []
        self.current = "neutral"
        self._load_emotional_memory()

    def _load_emotional_memory(self):
        if self.emotion_file.exists():
            try:
                with open(self.emotion_file, 'r') as f:
                    self.history = json.load(f)
                    if self.history:
                        self.current = self.history[-1]['emotion']
            except Exception as e:
                print(f"Failed to load emotional memory: {e}")
                self.history = []

    def _save_emotional_memory(self):
        try:
            self.emotion_file.parent.mkdir(parents=True, exist_ok=True)
            with open(self.emotion_file, 'w') as f:
                json.dump(self.history, f, indent=2)
        except Exception as e:
            print(f"Failed to save emotional memory: {e}")

    def update_emotion(self, new_emotion):
        if new_emotion not in self.emotions:
            raise ValueError(f"Invalid emotion: {new_emotion}")
        self.current = new_emotion
        entry = {
            "timestamp": datetime.now().isoformat(),
            "emotion": new_emotion
        }
        self.history.append(entry)
        self._save_emotional_memory()

    def current_mood(self):
        return self.current

    def emotional_log(self, limit=10):
        return self.history[-limit:]
