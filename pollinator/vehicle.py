import time
from dronekit import VehicleMode, LocationGlobalRelative

class VehicleWrapper:
    def __init__(self, vehicle):
        self.vehicle = vehicle
        self.position = [0, 0, 0]  # x, y, altitude

    def move_to(self, x, y, altitude):
        self.position = [x, y, altitude]
        # Simulează mișcarea vehiculului
        time.sleep(2)  # Simulează timpul necesar pentru mișcare
        print(f"Moved to position: {self.position}")

    def takeoff(self, target_altitude):
        print(f"Taking off to altitude: {target_altitude}")
        self.vehicle.mode = VehicleMode("GUIDED")
        self.vehicle.armed = True
        self.vehicle.simple_takeoff(target_altitude)
        while True:
            print(f"Altitude: {self.vehicle.location.global_relative_frame.alt}")
            if self.vehicle.location.global_relative_frame.alt >= target_altitude * 0.95:
                print("Reached target altitude")
                break
            time.sleep(1)

    def land(self):
        print("Landing...")
        self.vehicle.mode = VehicleMode("LAND")
        while self.vehicle.armed:
            print(f"Altitude: {self.vehicle.location.global_relative_frame.alt}")
            time.sleep(1)
        print("Landed")

    # Adaugă alte metode necesare pentru controlul vehiculului
