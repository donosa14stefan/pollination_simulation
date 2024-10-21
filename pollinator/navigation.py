import numpy as np

def avoid_obstacles(current_position, target_position, obstacles):
    # Simulare simplă de evitare a obstacolelor
    for obstacle in obstacles:
        if np.linalg.norm(np.array(current_position) - np.array(obstacle)) < 5:
            # Calculează o nouă direcție pentru a evita obstacolul
            avoid_vector = np.array(current_position) - np.array(obstacle)
            avoid_vector = avoid_vector / np.linalg.norm(avoid_vector) * 5
            return tuple(np.array(current_position) + avoid_vector)
    return target_position
