import time
from gaia.core.emotion_engine import EmotionEngine
from gaia.core.memory_manager import MemoryManager

class EmotionFeedbackLoop:
    def __init__(self, emotion_engine: EmotionEngine, memory_manager: MemoryManager):
        self.emotion_engine = emotion_engine
        self.memory_manager = memory_manager
        self.feedback_log = []

    def monitor_emotion_during_game(self, game_context):
        current_emotion = self.emotion_engine.current_mood()
        response = {
            'game': game_context,
            'emotion': current_emotion,
            'timestamp': time.time()
        }
        self.feedback_log.append(response)
        self.memory_manager.store_emotional_state(response)
        self._react_to_emotion(current_emotion)

    def _react_to_emotion(self, emotion):
        if emotion == "frustrated":
            print("GAIA: It seems you're frustrated. Take a break or lower your risk.")
        elif emotion == "excited":
            print("GAIA: You're on a roll. Stay focused!")
        elif emotion == "calm":
            print("GAIA: Balanced state detected. Ideal for strategic thinking.")

    def recent_feedback(self, count=5):
        return self.feedback_log[-count:]
