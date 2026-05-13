from state.kalman import BatterySOCEstimator

estimator = BatterySOCEstimator()

soc = estimator.update(
    throttle=0.9,
    brake=False
)

print(soc)

Connect everything together:
window manager
rules engine
anomaly detector
