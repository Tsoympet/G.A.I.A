import random
from datetime import datetime

class EmotionEngine:
    def __init__(self):
        self.current_emotion = "neutral"
        self.emotion_history = []
        self.visual_feedback = None
        self.listeners = []

    def set_emotion(self, emotion, reason=""):
        timestamp = datetime.now().isoformat()
        self.current_emotion = emotion
        self.emotion_history.append((timestamp, emotion, reason))
        self.trigger_feedback()
        self.notify_listeners(emotion)

    def get_emotion(self):
        return self.current_emotion

    def get_emotion_log(self, n=10):
        return self.emotion_history[-n:]

    def trigger_feedback(self):
        if self.visual_feedback:
            self.visual_feedback.show_emotion(self.current_emotion)

    def register_visual_feedback(self, feedback):
        self.visual_feedback = feedback

    def register_listener(self, callback):
        self.listeners.append(callback)

    def notify_listeners(self, emotion):
        for callback in self.listeners:
            callback(emotion)

    def random_emotion_shift(self):
        emotions = ["happy", "focused", "calm", "curious", "tired", "frustrated", "neutral"]
        selected = random.choice(emotions)
        self.set_emotion(selected, reason="Random shift based on session time or system metrics.")
