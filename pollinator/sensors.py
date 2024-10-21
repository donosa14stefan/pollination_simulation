import random

class SimulatedSensors:
    def __init__(self):
        self.gps_error = 2.0  # metri
        self.altitude_error = 0.5  # metri

    def get_gps(self, true_position):
        x, y, z = true_position
        return (
            x + random.uniform(-self.gps_error, self.gps_error),
            y + random.uniform(-self.gps_error, self.gps_error),
            z + random.uniform(-self.altitude_error, self.altitude_error)
        )

    def get_battery_level(self):
        return random.uniform(0, 100)

    def get_velocity(self):
        return random.uniform(0, 10)  # m/s
