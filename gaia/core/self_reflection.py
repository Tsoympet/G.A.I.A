import datetime
from gaia.core.emotion_engine import EmotionEngine
from gaia.core.memory_manager import MemoryManager

class SelfReflection:
    def __init__(self, emotion_engine: EmotionEngine, memory_manager: MemoryManager):
        self.emotion_engine = emotion_engine
        self.memory_manager = memory_manager
        self.daily_log = []

    def reflect(self):
        mood = self.emotion_engine.current_mood()
        recent_memories = self.memory_manager.get_recent_entries(limit=10)
        summary = self.generate_summary(mood, recent_memories)
        self.daily_log.append({
            "date": datetime.datetime.now().isoformat(),
            "mood": mood,
            "summary": summary
        })
        return summary

    def generate_summary(self, mood, memories):
        summary = f"Today I felt {mood}.
"
        if memories:
            summary += "Notable memories include:
"
            for m in memories:
                summary += f" - {m}\n"
        else:
            summary += "I experienced little memorable activity."
        return summary

    def get_log(self):
        return self.daily_log

