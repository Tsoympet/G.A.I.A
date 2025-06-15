import random
import time

class CrashSimulator:
    def __init__(self, seed=None):
        self.history = []
        self.seed = seed or int(time.time())
        random.seed(self.seed)

    def simulate_crash(self):
        crash_point = round(random.uniform(1.00, 10.00), 2)
        self.history.append(crash_point)
        return crash_point

    def get_history(self, limit=50):
        return self.history[-limit:]

    def predict_next(self):
        if len(self.history) < 5:
            return "Insufficient data"
        avg = sum(self.history[-5:]) / 5
        variance = random.uniform(-0.25, 0.25)
        prediction = round(avg + variance, 2)
        return max(1.0, min(prediction, 20.0))
