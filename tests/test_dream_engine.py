import unittest
from unittest.mock import MagicMock
from gaia.core.dream_state_engine import DreamStateEngine
from gaia.core.emotion_engine import EmotionEngine
from gaia.core.intelligence_engine import KnowledgeBase
from gaia.core.memory_manager import MemoryManager
from gaia.core.plugin_registry import trigger_plugin_event

class TestDreamStateEngine(unittest.TestCase):
    def setUp(self):
        self.emotion_engine = EmotionEngine()
        self.knowledge_base = KnowledgeBase()
        self.memory_store = MemoryManager()
        self.dream_engine = DreamStateEngine(
            self.emotion_engine,
            self.knowledge_base,
            self.memory_store
        )

        # Mock plugin system
        self.mock_trigger = MagicMock()
        self.dream_engine.trigger_plugin_event = self.mock_trigger

    def test_generate_dream_structure(self):
        """Check that dream output contains all necessary fields."""
        dream = self.dream_engine.generate_dream()
        for key in ['time', 'mood', 'seed_topic', 'trigger', 'content', 'visual']:
            self.assertIn(key, dream)

    def test_emotion_influence_on_dream(self):
        """Ensure emotion state affects the dream mood."""
        self.emotion_engine.set_emotion("stress", level=0.9)
        dream = self.dream_engine.generate_dream()
        self.assertEqual(dream['mood'], "stress")

    def test_dream_includes_plugin_triggers(self):
        """Simulate plugin interaction and ensure it fires correctly."""
        # Patch plugin call
        trigger_plugin_event_backup = self.dream_engine.trigger_plugin_event
        self.dream_engine.trigger_plugin_event = MagicMock()

        dream = self.dream_engine.generate_dream()
        self.dream_engine.trigger_plugin_event.assert_called()
        self.dream_engine.trigger_plugin_event = trigger_plugin_event_backup

    def test_generate_multiple_dreams_with_memory(self):
        """Check memory store integration with sequential dreams."""
        for _ in range(3):
            dream = self.dream_engine.generate_dream()
            self.memory_store.save_dream(dream)

        self.assertEqual(len(self.memory_store.get_recent_dreams()), 3)

    def test_edge_case_low_emotion_activity(self):
        """Check behavior when emotion is at near-zero."""
        self.emotion_engine.set_emotion("neutral", level=0.01)
        dream = self.dream_engine.generate_dream()
        self.assertEqual(dream['mood'], "neutral")

if __name__ == '__main__':
    unittest.main()
