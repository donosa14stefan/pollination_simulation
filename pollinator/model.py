import cv2
import numpy as np
from ultralytics import YOLO

class Model:
    def __init__(self, model_name: str):
        self.model_name = model_name
        self.model = None

    def start(self):
        self.model = YOLO(self.model_name)

    def simulate_camera_frame(self):
        # Generează o imagine simulată
        frame = np.random.randint(0, 255, (480, 640, 3), dtype=np.uint8)
        return frame

    def on(self, frame=None):
        if frame is None:
            frame = self.simulate_camera_frame()
        results = self.model(frame)[0]
        return results

    # ... restul metodelor rămân neschimbate

    def parse_detections(self, results):
        detections = []
        for result in results:
            print(f"Result")
            for box in result.boxes:
                print(f"    Box:")
                print(f"        Confidence: {box.conf}")
                print(f"        Type ID: {box.cls}")
                print(f"        Type: {result.names[box.cls[0].item()]}")
                print(f"        Bounds: {box.xyxy}")
                print(f"    Box end")

                # draw details on frame over
                bounds = box.xyxy[0]
                x1, y1 = (int(bounds[0].item()), int(bounds[1].item()))
                x2, y2 = (int(bounds[2].item()), int(bounds[3].item()))

                detections.append(
                    [result.names[box.cls[0].item()], box.conf[0].item(), (x1, y1), (x2, y2), (255, 0, 0), 1])
                # name, confidence, p1, p2, color, thick
            print(f"Result end")
        print(f"Detections: {len(detections)}")
        return detections

    def show_results(self, results):
        cv2.imshow('processing', results.plot())
        cv2.waitKey(1)
