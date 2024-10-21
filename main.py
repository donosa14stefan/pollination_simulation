import cv2
import numpy as np
from pollinator.environment import Environment
from pollinator.vehicle import VehicleWrapper
from pollinator.sensors import SimulatedSensors
from pollinator.navigation import avoid_obstacles
from pollinator.fleet import Fleet
from pollinator.logger import logger

def main():
    env = Environment(size=(1000, 1000))
    fleet = Fleet()
    sensors = SimulatedSensors()

    # Adaugă două drone la flotă
    for _ in range(2):
        vehicle = VehicleWrapper(None)
        fleet.add_vehicle(vehicle)

    logger.info("Simulation started")

    # Simulează operațiunile flotei
    fleet.takeoff_all(20)
    logger.info("All vehicles took off")

    # Creează ferestre pentru vizualizare
    cv2.namedWindow("Drone View", cv2.WINDOW_NORMAL)
    cv2.namedWindow("Top View", cv2.WINDOW_NORMAL)

    for _ in range(100):  # Simulează 100 pași de mișcare
        for vehicle in fleet.vehicles:
            gps = sensors.get_gps(vehicle.get_position())
            battery = sensors.get_battery_level()
            velocity = sensors.get_velocity()
            logger.info(f"Vehicle at {gps}, battery: {battery}%, velocity: {velocity} m/s")

            # Simulează evitarea obstacolelor
            target_position = (np.random.randint(0, 1000), np.random.randint(0, 1000), 20)
            obstacles = [(150, 150, 20), (250, 250, 20)]
            new_target = avoid_obstacles(vehicle.get_position(), target_position, obstacles)
            vehicle.move_to(*new_target)

            # Renderizează vederea dronei
            drone_view = env.render(vehicle.get_position())
            cv2.imshow("Drone View", drone_view)

        # Renderizează vederea de sus
        top_view = env.terrain.copy()
        for vehicle in fleet.vehicles:
            path = vehicle.get_path()
            for i in range(1, len(path)):
                pt1 = (int(path[i-1][0]), int(path[i-1][1]))
                pt2 = (int(path[i][0]), int(path[i][1]))
                cv2.line(top_view, pt1, pt2, (255, 0, 0), 2)
            cv2.circle(top_view, (int(vehicle.get_position()[0]), int(vehicle.get_position()[1])), 5, (0, 0, 255), -1)

        cv2.imshow("Top View", top_view)
        
        if cv2.waitKey(100) & 0xFF == ord('q'):
            break

    fleet.land_all()
    logger.info("All vehicles landed")
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
