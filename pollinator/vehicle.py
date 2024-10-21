import time
from dronekit import VehicleMode, LocationGlobalRelative

class VehicleWrapper:
    def __init__(self):
        self.mode = "STABILIZE"
        self.armed = False
        self.location = LocationGlobalRelative(0, 0, 0)
        self.position = [0, 0, 0]  # x, y, altitude

    def set_mode(self, mode):
        self.mode = mode
        print(f"Mode changed to {mode}")

    def arm(self):
        self.armed = True
        print("Vehicle armed")

    def simple_takeoff(self, altitude):
        print(f"Taking off to {altitude}m")
        for i in range(10):
            self.location.alt = altitude * (i+1) / 10
            self.position[2] = self.location.alt
            print(f"Altitude: {self.location.alt}")
            time.sleep(0.5)

    def move_to(self, x, y, altitude):
        self.position = [x, y, altitude]
        self.location.alt = altitude
        print(f"Moved to position: {self.position}")
        time.sleep(2)  # Simulează timpul necesar pentru mișcare

    def takeoff(self, target_altitude):
        print(f"Taking off to altitude: {target_altitude}")
        self.set_mode("GUIDED")
        self.arm()
        self.simple_takeoff(target_altitude)
        while True:
            print(f"Altitude: {self.location.alt}")
            if self.location.alt >= target_altitude * 0.95:
                print("Reached target altitude")
                break
            time.sleep(0.5)

    def land(self):
        print("Landing...")
        self.set_mode("LAND")
        while self.location.alt > 0:
            self.location.alt -= 1
            self.position[2] = self.location.alt
            print(f"Altitude: {self.location.alt}")
            time.sleep(0.5)
        self.armed = False
        print("Landed")
