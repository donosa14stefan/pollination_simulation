from dronekit_sitl import SITL

class ConnectionManager:
    def __init__(self):
        self.sitl = None
        self.connection_string = None

    def start_sim(self):
        print("Starting SITL simulation...")
        self.sitl = SITL()
        self.sitl.download('copter', '3.3', verbose=True)
        sitl_args = ['-I0', '--model', 'quad', '--home=-35.363261,149.165230,584,353']
        self.sitl.launch(sitl_args, await_ready=True, restart=True)
        self.connection_string = 'tcp:127.0.0.1:5760'

    def stop_sim(self):
        if self.sitl:
            self.sitl.stop()
