import unittest
from gaia.modules.quantum.quantum_forecaster import QuantumForecaster
import random

class TestQuantumForecaster(unittest.TestCase):
    def setUp(self):
        self.forecaster = QuantumForecaster()
        self.sample_data = [random.uniform(0.8, 1.2) for _ in range(100)]  # Normalized trends

    def test_forecast_output_structure(self):
        """Ensure forecast returns expected keys and structure."""
        result = self.forecaster.predict(self.sample_data)
        self.assertIn('prediction', result)
        self.assertIn('confidence', result)
        self.assertIn('entropy_level', result)
        self.assertIsInstance(result['prediction'], float)
        self.assertIsInstance(result['confidence'], float)
        self.assertIsInstance(result['entropy_level'], float)

    def test_entropy_influences_confidence(self):
        """Inject high entropy and verify confidence drops."""
        noisy_data = [random.uniform(0.0, 2.0) for _ in range(100)]
        result_low_entropy = self.forecaster.predict(self.sample_data)
        result_high_entropy = self.forecaster.predict(noisy_data)

        self.assertLess(result_high_entropy['confidence'], result_low_entropy['confidence'])

    def test_forecaster_with_constant_data(self):
        """Feed constant data and expect high confidence."""
        constant_data = [1.0] * 100
        result = self.forecaster.predict(constant_data)
        self.assertGreater(result['confidence'], 0.95)
        self.assertLess(result['entropy_level'], 0.01)

    def test_prediction_does_not_crash_on_empty_input(self):
        """Ensure it fails gracefully or returns fallback if input is empty."""
        try:
            result = self.forecaster.predict([])
            self.assertIn('prediction', result)
        except Exception as e:
            self.fail(f"Empty input caused failure: {e}")

    def test_prediction_is_reasonable(self):
        """Check output prediction is in expected numerical bounds."""
        result = self.forecaster.predict(self.sample_data)
        self.assertGreater(result['prediction'], 0.5)
        self.assertLess(result['prediction'], 2.0)

if __name__ == '__main__':
    unittest.main()
