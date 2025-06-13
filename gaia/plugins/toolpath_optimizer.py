class ToolpathOptimizer:
    def __init__(self, strategy='greedy'):
        self.strategy = strategy

    def optimize(self, toolpaths):
        if self.strategy == 'greedy':
            return self._greedy_optimize(toolpaths)
        elif self.strategy == 'brute_force':
            return self._brute_force_optimize(toolpaths)
        else:
            raise ValueError(f"Unknown strategy: {self.strategy}")

    def _greedy_optimize(self, toolpaths):
        if not toolpaths:
            return []
        optimized = [toolpaths[0]]
        remaining = toolpaths[1:]
        while remaining:
            last = optimized[-1]
            next_index = min(range(len(remaining)), key=lambda i: self._distance(last, remaining[i]))
            optimized.append(remaining.pop(next_index))
        return optimized

    def _brute_force_optimize(self, toolpaths):
        from itertools import permutations
        if not toolpaths:
            return []
        best = min(permutations(toolpaths), key=self._total_distance)
        return list(best)

    def _distance(self, p1, p2):
        return ((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)**0.5

    def _total_distance(self, path):
        return sum(self._distance(path[i], path[i+1]) for i in range(len(path) - 1))

