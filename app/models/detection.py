from ultralytics import YOLO
from PIL import Image
import io

# Load YOLOv8 nano model (fast & lightweight)
model = YOLO("yolov8n.pt")

def detect_objects(image_bytes: bytes, conf: float = 0.25):
    image = Image.open(io.BytesIO(image_bytes))
    results = model(image, conf=conf)[0]
    
    detections = []
    for box in results.boxes:
        detections.append({
            "class": results.names[int(box.cls)],
            "confidence": float(box.conf),
            "bbox": [float(x) for x in box.xyxy[0]]  # x1, y1, x2, y2
        })
    
    return {
        "detections": detections,
        "total_objects": len(detections),
        "image_size": image.size
    }