class BatterySOCEstimator:

    def __init__(self):
        self.soc = 0.85

    def update(self, throttle, brake):

        if throttle > 0.8:
            self.soc -= 0.01

        if brake:
            self.soc += 0.005

        return self.soc
