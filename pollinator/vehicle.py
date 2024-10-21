import time
import numpy as np

class VehicleWrapper:
    def __init__(self, vehicle):
        self.vehicle = vehicle
        self.position = np.array([0, 0, 20])  # x, y, altitude
        self.path = [self.position.copy()]

    def move_to(self, x, y, altitude):
        new_position = np.array([x, y, altitude])
        self.position = new_position
        self.path.append(self.position.copy())
        time.sleep(0.1)  # Simulează timpul necesar pentru mișcare
        print(f"Moved to position: {self.position}")

    def takeoff(self, target_altitude):
        print(f"Taking off to altitude: {target_altitude}")
        self.position[2] = target_altitude
        self.path.append(self.position.copy())

       def land(self):
        print("Landing...")
        self.position[2] = 0
        self.path.append(self.position.copy())
        print("Landed")

    def get_position(self):
        return self.position

    def get_path(self):
        return self.path
