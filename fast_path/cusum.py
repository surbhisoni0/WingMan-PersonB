Purpose:
 detect anomalies

class CUSUMDetector:

    def __init__(self, threshold=0.05):
        self.threshold = threshold

    def detect_soc_drop(self, previous, current):

        delta = previous - current

        return delta > self.threshold
