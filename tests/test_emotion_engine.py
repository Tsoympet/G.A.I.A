import unittest
from gaia.core.emotion_engine import EmotionEngine

class TestEmotionEngine(unittest.TestCase):
    def setUp(self):
        self.engine = EmotionEngine()

    def test_initial_state_is_neutral(self):
        """Ensure EmotionEngine starts with neutral state."""
        state = self.engine.get_current_emotion()
        self.assertEqual(state['type'], 'neutral')
        self.assertAlmostEqual(state['intensity'], 0.0, delta=0.05)

    def test_setting_valid_emotion(self):
        """Set an emotion and verify internal state."""
        self.engine.set_emotion('inspiration', level=0.8)
        state = self.engine.get_current_emotion()
        self.assertEqual(state['type'], 'inspiration')
        self.assertAlmostEqual(state['intensity'], 0.8)

    def test_emotion_decay_mechanism(self):
        """Simulate emotion fading over time."""
        self.engine.set_emotion('stress', level=0.9)
        self.engine.tick()  # 1 tick of decay
        state = self.engine.get_current_emotion()
        self.assertLess(state['intensity'], 0.9)

    def test_emotion_intensity_clamping(self):
        """Ensure intensity doesn't exceed valid bounds."""
        self.engine.set_emotion('fear', level=1.5)
        state = self.engine.get_current_emotion()
        self.assertLessEqual(state['intensity'], 1.0)

        self.engine.set_emotion('calm', level=-0.5)
        state = self.engine.get_current_emotion()
        self.assertGreaterEqual(state['intensity'], 0.0)

    def test_emotion_spike_trigger(self):
        """Ensure spike threshold logic activates callbacks if defined."""
        triggered = {'spiked': False}
        def fake_callback(emotion_state):
            triggered['spiked'] = True

        self.engine.register_spike_callback(fake_callback, threshold=0.7)
        self.engine.set_emotion('rage', level=0.9)

        self.assertTrue(triggered['spiked'])

    def test_multiple_emotion_transitions(self):
        """Simulate emotional state transitions."""
        sequence = [
            ('stress', 0.6),
            ('curiosity', 0.4),
            ('focus', 0.9),
            ('relief', 0.2)
        ]
        for typ, level in sequence:
            self.engine.set_emotion(typ, level)
            state = self.engine.get_current_emotion()
            self.assertEqual(state['type'], typ)
            self.assertAlmostEqual(state['intensity'], level, delta=0.01)

if __name__ == '__main__':
    unittest.main()
