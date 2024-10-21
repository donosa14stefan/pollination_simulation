from pollinator.vehicle import VehicleWrapper

class Fleet:
    def __init__(self):
        self.vehicles = []

    def add_vehicle(self, vehicle):
        self.vehicles.append(vehicle)

    def move_all(self, targets):
        for vehicle, target in zip(self.vehicles, targets):
            vehicle.move_to(*target)

    def takeoff_all(self, altitude):
        for vehicle in self.vehicles:
            vehicle.takeoff(altitude)

    def land_all( self ):
        for vehicle in self.vehicles:
            vehicle.land()
