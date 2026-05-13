Purpose:
rolling telemetry history
recent state memory

from collections import deque

class TelemetryWindow:

    def __init__(self, size=20):
        self.window = deque(maxlen=size)

    def add(self, state):
        self.window.append(state)

    def latest(self):
        return self.window[-1]

    def average_speed(self):

        if not self.window:
            return 0

        return sum(
            s["speed"] for s in self.window
        ) / len(self.window)


