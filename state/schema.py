It Stores:
speed
throttle
SOC
telemetry system realistic


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
    DEFAULT_STATE = {
    "timestamp": 0.0,
    "speed": 0.0,
    "throttle": 0.0,
    "brake": False,
    "steering": 0.0,
    "rpm": 0,
    "gear": 0,
    "drs": False,
    "ers_deployment": 0.0,
    "soc_estimated": 0.85,
    "soc_uncertainty": 0.05,
    "tire_temp_fl": 0.0,
    "tire_temp_fr": 0.0,
    "tire_temp_rl": 0.0,
    "tire_temp_rr": 0.0,
    "understeer_flag": False,
    "oversteer_flag": False
}

    return state
