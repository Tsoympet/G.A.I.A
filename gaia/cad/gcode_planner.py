import math

class GCodePlanner:
    def __init__(self):
        self.commands = []
        self.position = (0, 0, 0)
        self.feed_rate = 1500

    def move_to(self, x, y, z=None):
        command = f"G1 X{x:.3f} Y{y:.3f}"
        if z is not None:
            command += f" Z{z:.3f}"
        command += f" F{self.feed_rate}"
        self.commands.append(command)
        self.position = (x, y, z if z is not None else self.position[2])

    def set_feed_rate(self, rate):
        self.feed_rate = rate

    def generate_circle(self, cx, cy, radius, segments=100):
        for i in range(segments + 1):
            angle = 2 * math.pi * i / segments
            x = cx + radius * math.cos(angle)
            y = cy + radius * math.sin(angle)
            self.move_to(x, y)

    def get_gcode(self):
        return "\n".join(self.commands)

    def save_to_file(self, filepath):
        with open(filepath, 'w') as f:
            f.write(self.get_gcode())

