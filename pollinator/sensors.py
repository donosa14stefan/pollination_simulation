import numpy as np

class SimulatedSensors:
    def __init__(self):
        pass

    def get_gps(self, position):
        return position

    def get_battery_level(self):
        return np.random.randint(20, 100)

    def get_velocity(self):
        return np.random.randint(1, 10)
