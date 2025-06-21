import datetime
from gaia.core.memory_manager import MemoryManager
from gaia.core.emotion_engine import EmotionEngine
from gaia.core.intelligence_engine import KnowledgeBase

class SelfReflectionEngine:
    def __init__(self, memory_manager: MemoryManager, emotion_engine: EmotionEngine, knowledge_base: KnowledgeBase):
        self.memory_manager = memory_manager
        self.emotion_engine = emotion_engine
        self.knowledge_base = knowledge_base
        self.journal = []

    def reflect(self):
        current_mood = self.emotion_engine.current_mood()
        recent_memory = self.memory_manager.recent_experiences()
        if recent_memory:
            topic = recent_memory[-1].get('summary', 'an unknown event')
        else:
            topic = 'a vague feeling'

        timestamp = datetime.datetime.now().isoformat()
        insight = f"On {timestamp}, GAIA felt {current_mood} about {topic}."
        self.journal.append(insight)
        return insight

    def summarize_reflections(self, limit=5):
        return self.journal[-limit:] if self.journal else ["No reflections yet."]
