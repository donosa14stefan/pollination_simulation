import cv2
import numpy as np

class SimulatedCamera:
    def __init__(self, width=640, height=480):
        self.width = width
        self.height = height

    def capture(self ):
        # Generează o imagine simulată
        frame = np.random.randint(0, 255, (self.height, self.width, 3), dtype=np.uint8)
        return frame
