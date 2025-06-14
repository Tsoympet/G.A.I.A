import time
import random
from collections import deque
from gaia.core.emotion_engine import EmotionEngine
from gaia.core.dream_state_engine import DreamStateEngine

class CasinoBehaviorModel:
    def __init__(self, emotion: EmotionEngine, dream: DreamStateEngine):
        self.session_data = []
        self.live_patterns = deque(maxlen=100)
        self.trend_tracker = {}
        self.emotion = emotion
        self.dream = dream
        self.last_prediction = None

    def log_session(self, game_type: str, result: str, multiplier=None, bet_amount=None):
        timestamp = time.time()
        entry = {
            "time": timestamp,
            "game": game_type,
            "result": result,
            "multiplier": multiplier,
            "bet_amount": bet_amount
        }
        self.session_data.append(entry)
        self.live_patterns.append(entry)
        self._update_trend(game_type, result)
        self._emotional_reaction(result)
        self.last_prediction = self._predict_behavior(game_type)

    def _update_trend(self, game_type, result):
        if game_type not in self.trend_tracker:
            self.trend_tracker[game_type] = {"win": 0, "loss": 0, "tie": 0}
        self.trend_tracker[game_type][result] += 1

    def _emotional_reaction(self, result):
        if result == "win":
            self.emotion.log_emotion("confidence", 0.7)
        elif result == "loss":
            self.emotion.log_emotion("frustration", 0.6)
        else:
            self.emotion.log_emotion("confusion", 0.3)

    def _predict_behavior(self, game_type):
        trend = self.trend_tracker.get(game_type, {})
        win_ratio = trend.get("win", 0) / max(1, sum(trend.values()))
        if win_ratio > 0.6:
            return "High win rate trend detected"
        elif trend.get("loss", 0) > trend.get("win", 0):
            return "Loss trend - consider stopping"
        else:
            return "Stable behavior"

    def export_trends(self):
        return {
            "summary": self.trend_tracker,
            "latest_prediction": self.last_prediction,
            "live_entries": list(self.live_patterns)[-10:]
        }

    def push_to_dream(self):
        summary = self.export_trends()
        self.dream.store_memory("casino_behavior_tracking", summary)
