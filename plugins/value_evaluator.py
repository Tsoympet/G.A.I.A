class ValueEvaluator:
    def __init__(self):
        self.weights = {
            'performance': 0.4,
            'efficiency': 0.3,
            'cost': 0.2,
            'risk': 0.1
        }

    def evaluate(self, metrics):
        score = 0.0
        for key, weight in self.weights.items():
            score += weight * metrics.get(key, 0)
        return round(score, 2)

    def explain(self, metrics):
        explanation = []
        for key, weight in self.weights.items():
            value = metrics.get(key, 0)
            contribution = weight * value
            explanation.append(f"{key.capitalize()}: {value} * {weight} = {contribution}")
        return "\n".join(explanation)
