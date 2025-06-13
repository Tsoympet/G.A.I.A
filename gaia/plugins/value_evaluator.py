class ValueEvaluator:
    def __init__(self, criteria=None):
        self.criteria = criteria or {
            "efficiency": 0.3,
            "reliability": 0.3,
            "innovation": 0.4
        }

    def evaluate(self, candidate):
        """
        Evaluates a candidate (e.g., a project, decision, or plugin)
        based on predefined weighted criteria.
        :param candidate: dict of scores (0 to 1) for each criterion
        :return: weighted score
        """
        score = 0.0
        for k, weight in self.criteria.items():
            score += candidate.get(k, 0) * weight
        return round(score, 4)

    def set_criteria(self, new_criteria):
        """
        Update the evaluation criteria and weights.
        """
        total = sum(new_criteria.values())
        if not 0.99 <= total <= 1.01:
            raise ValueError("Total weights must sum to approximately 1.0")
        self.criteria = new_criteria

