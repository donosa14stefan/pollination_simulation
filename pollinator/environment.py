import numpy as np

class Environment:
    def __init__(self, size=(1000, 1000)):
        self.size = size
        self.flower_positions = self.generate_flower_positions()

    def generate_flower_positions(self, num_flowers=50):
        return [(np.random.randint(0, self.size[0]), 
                 np.random.randint(0, self.size[1])) 
                for _ in range(num_flowers)]

    def get_drone_view(self, drone_position, view_size=(640, 480)):
        # Simulează vederea dronei bazată pe poziția sa
        view = np.zeros((*view_size, 3), dtype=np.uint8)
        for flower in self.flower_positions:
            if self.is_in_view(drone_position, flower, view_size):
                x, y = self.world_to_view_coords(drone_position, flower, view_size)
                cv2.circle(view, (x, y), 5, (0, 255, 0), -1)
        return view

    def is_in_view(self, drone_pos, flower_pos, view_size):
        # Verifică dacă floarea este în câmpul vizual al dronei
        dx = abs(flower_pos[0] - drone_pos[0])
        dy = abs(flower_pos[1] - drone_pos[1])
        return dx < view_size[0] // 2 and dy < view_size[1] // 2

    def world_to_view_coords(self, drone_pos, world_pos, view_size):
        # Convertește coordonatele lumii în coordonate de vizualizare
        x = int((world_pos[0] - drone_pos[0] + view_size[0] // 2) % view_size[0])
        y = int((world_pos[1] - drone_pos[1] + view_size[1] // 2) % view_size[1])
        return x, y
