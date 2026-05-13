class RulesEngine:

    def evaluate(self, state):

        alerts = []

        if state["soc_estimated"] < 0.2:
            alerts.append("Critical battery level")

        if state["understeer_flag"]:
            alerts.append("Understeer detected")

        if state["tire_temp_fl"] > 120:
            alerts.append("Front-left tire overheating")

        return alerts
This becomes AI alert system.
