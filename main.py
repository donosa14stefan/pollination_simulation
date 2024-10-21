from pollinator.environment import Environment
from pollinator.vehicle import VehicleWrapper
from pollinator.sensors import SimulatedSensors
from pollinator.navigation import avoid_obstacles
from pollinator.fleet import Fleet
from pollinator.logger import logger
import cv2

def main():
    env = Environment()
    fleet = Fleet()
    sensors = SimulatedSensors()

    # Adaugă două drone la flotă
    for _ in range(2):
        vehicle = VehicleWrapper()  # Eliminați parametrul None
        fleet.add_vehicle(vehicle)

    logger.info("Simulation started")

    # Simulează operațiunile flotei
    fleet.takeoff_all(20)
    logger.info("All vehicles took off")

    for _ in range(10):  # Simulează 10 pași de mișcare
        for vehicle in fleet.vehicles:
            gps = sensors.get_gps(vehicle.position)
            battery = sensors.get_battery_level()
            velocity = sensors.get_velocity()
            logger.info(f"Vehicle at {gps}, battery: {battery}%, velocity: {velocity} m/s")

            # Simulează evitarea obstacolelor
            target_position = (200, 200, 20)
            obstacles = [(150, 150, 20), (250, 250, 20)]
            new_target = avoid_obstacles(vehicle.position, target_position, obstacles)
            vehicle.move_to(*new_target)

        # Simulează vederea dronei
        view = env.get_drone_view(vehicle.position, (640, 480))
        cv2.imshow("Drone View", view)
        cv2. waitKey(1)

    # Simulează aterizarea flotei
    fleet.land_all()
    logger.info("All vehicles landed")

if __name__ == "__main__":
    main()
