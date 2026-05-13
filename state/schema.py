import copy
import time

DEFAULT_STATE = {
    "timestamp": 0.0,
    "speed": 0.0,
    "throttle": 0.0,
    "soc_estimated": 0.85
}

def new_state(**overrides):

    state = copy.deepcopy(DEFAULT_STATE)

    state["timestamp"] = time.time()

    state.update(overrides)
    self.proxy_soc = max(0.0, min(1.0, self.proxy_soc))
    state["soc_uncertainty"] = float(self.kf.P[0][0])

    return state
