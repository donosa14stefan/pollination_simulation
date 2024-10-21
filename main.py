from pollinator.environment import Environment
from pollinator.vehicle import VehicleWrapper

def main():
    env = Environment()
    vehicle = VehicleWrapper(None)  # Nu este necesar un vehicul real

    # Simulează mișcarea vehiculului
    vehicle.move_to(100, 100, 10)
    vehicle.takeoff(20)
    vehicle.move_to(200, 200, 20)
    vehicle.land()

    # Simulează vederea dronei
    view = env.get_drone_view(vehicle.position, (640, 480))
    cv2.imshow("Drone View", view)
    cv2.waitKey(0)

if __name__ == "__main__":
    main()
