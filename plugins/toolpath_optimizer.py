import math

class ToolpathOptimizer:
    def __init__(self, tool_diameter=1.0, safe_height=5.0):
        self.tool_diameter = tool_diameter
        self.safe_height = safe_height

    def optimize_path(self, toolpath):
        optimized = []
        visited = set()

        def distance(p1, p2):
            return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

        current = toolpath[0]
        optimized.append(current)
        visited.add(0)

        while len(visited) < len(toolpath):
            nearest = None
            nearest_dist = float('inf')
            for i, point in enumerate(toolpath):
                if i in visited:
                    continue
                d = distance(current, point)
                if d < nearest_dist:
                    nearest = i
                    nearest_dist = d
            current = toolpath[nearest]
            optimized.append(current)
            visited.add(nearest)

        return optimized

    def add_safe_movements(self, toolpath):
        safe_toolpath = []
        for i, point in enumerate(toolpath):
            if i == 0:
                safe_toolpath.append((point[0], point[1], self.safe_height))
            safe_toolpath.append((point[0], point[1], 0))
            safe_toolpath.append((point[0], point[1], self.safe_height))
        return safe_toolpath
