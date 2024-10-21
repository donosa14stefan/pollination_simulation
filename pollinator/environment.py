import numpy as np
import cv2

class Environment:
    def __init__(self, size=(1000, 1000)):
        self.size = size
        self.objects = self.generate_objects()
        self.terrain = self.generate_terrain()

    def generate_objects(self, num_objects=50):
        objects = []
        for _ in range(num_objects):
            obj_type = np.random.choice(["flower", "tree", "rock"])
            x = np.random.randint(0, self.size[0])
            y = np.random.randint(0, self.size[1])
            objects.append({"type": obj_type, "position": (x, y, 0)})
        return objects

    def generate_terrain(self):
        terrain = np.zeros((self.size[1], self.size[0], 3), dtype=np.uint8)
        terrain[:, :, 1] = 100  # Green base color
        # Add some texture
        noise = np.random.randint(0, 30, (self.size[1], self.size[0]), dtype=np.uint8)
        terrain[:, :, 1] += noise
        return terrain

    def render(self, drone_position):
        view = self.terrain.copy()
        for obj in self.objects:
            if self.is_in_view(drone_position, obj["position"]):
                x, y = self.world_to_view_coords(drone_position, obj["position"])
                color = (0, 255, 0) if obj["type"] == "flower" else (0, 100, 0) if obj["type"] == "tree" else (100, 100, 100)
                cv2.circle(view, (x, y), 5, color, -1)
        
        # Render drone
        drone_x, drone_y = self.size[0] // 2, self.size[1] // 2
        cv2.circle(view, (drone_x, drone_y), 10, (255, 0, 0), -1)
        
        return view

    def is_in_view(self, drone_pos, obj_pos):
        dx = abs(obj_pos[0] - drone_pos[0])
        dy = abs(obj_pos[1] - drone_pos[1])
        return dx < self.size[0] // 2 and dy < self.size[1] // 2

    def world_to_view_coords(self, drone_pos, world_pos):
        x = int((world_pos[0] - drone_pos[0] + self.size[0] // 2) % self.size[0])
        y = int((world_pos[1] - drone_pos[1] + self.size[1] // 2) % self.size[1])
        return x, y
