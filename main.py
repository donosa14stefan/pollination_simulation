from dronekit import connect
from dronekit_sitl import SITL
import pollinator.connection as connection_handler
import pollinator.vehicle as vehicle_handler
import pollinator.fleet as fleet_handler

def get_connection():
    connection = connection_handler.ConnectionManager()
    connection.start_sim()
    return connection

def main():
    print("Starting simulation...")
    fleet = fleet_handler.Fleet()

    connection_details = get_connection()
    vehicle = connect(connection_details.connection_string, wait_ready=True)
    wrapper = vehicle_handler.VehicleWrapper(vehicle)
    fleet.fleet_add(wrapper)

    # Adaugă logica de simulare aici
    wrapper.routine_preflight()
    wrapper.routine_takeoff(20)
    
    # Simulează un zbor simplu
    wrapper.simple_goto(vehicle.location.global_relative_frame.north(100))
    
    wrapper.land()
    wrapper.close()
    connection_details.stop_sim()

if __name__ == "__main__":
    main()
