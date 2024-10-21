import numpy as np

def avoid_obstacles(current_position, target_position, obstacles):
    # Simulează evitarea obstacolelor
    for obstacle in obstacles:
        dx = abs(obstacle[0] - target_position[0])
        dy = abs(obstacle[1] - target_position[1])
        if dx < 50 and dy < 50:
            new_target_x = target_position[0] + np.random.randint(-50, 50)
            new_target_y = target_position[1] + np.random.randint(-50, 50)
            return new_target_x, new_target_y, target_position[2]
    return target_position
