from gaia.core.emotion_engine import EmotionEngine
from gaia.core.dream_state_engine import DreamStateEngine
import time

class EmotionFeedbackLoop:
    def __init__(self, emotion_engine: EmotionEngine, dream_engine: DreamStateEngine):
        self.emotion_engine = emotion_engine
        self.dream_engine = dream_engine
        self.reinforcement_log = []

    def evaluate_event(self, context: str, result: str, intensity: float = 0.5):
        """
        Evaluate a user event (e.g., casino win/loss) and log an emotional response.
        """
        emotion_map = {
            "win": "satisfaction",
            "loss": "frustration",
            "tie": "neutral",
            "streak": "excitement",
            "risk": "anticipation",
            "error": "confusion"
        }

        emotion = emotion_map.get(result, "neutral")
        self.emotion_engine.log_emotion(emotion, intensity)
        self._reinforce(context, emotion, intensity)

    def _reinforce(self, context, emotion, intensity):
        timestamp = time.time()
        entry = {
            "context": context,
            "emotion": emotion,
            "intensity": intensity,
            "time": timestamp
        }
        self.reinforcement_log.append(entry)

        # Boost memory or dream priority if emotion is strong
        if intensity > 0.7:
            self.dream_engine.set_priority(context, level="high", reason=emotion)

    def summarize_feedback(self):
        summary = {}
        for entry in self.reinforcement_log:
            emotion = entry["emotion"]
            summary[emotion] = summary.get(emotion, 0) + 1
        return summary

    def inject_dream_reflection(self):
        """
        Feed summary into dream engine as reflection seed.
        """
        summary = self.summarize_feedback()
        self.dream_engine.store_memory("emotional_feedback", summary)
