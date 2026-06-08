from typing import Optional, List
from app.schemas import Detection, BoundingBox

class ResultProcessor:
    """Process YOLOv8 model results"""
    
    @staticmethod
    def process_detections(yolo_results) -> List[Detection]:
        """Convert YOLOv8 results to standardized format"""
        detections = []
        for result in yolo_results:
            for box in result.boxes:
                x1, y1, x2, y2 = box.xyxy[0].tolist()
                conf = float(box.conf[0])
                cls = int(box.cls[0])
                name = result.names[cls]
                
                detection = Detection(
                    class_name=name,
                    confidence=round(conf, 4),
                    bbox=BoundingBox(x1=round(x1, 2), y1=round(y1, 2), x2=round(x2, 2), y2=round(y2, 2))
                )
                detections.append(detection)
        return detections
    
    @staticmethod
    def filter_by_confidence(detections: List[Detection], threshold: float) -> List[Detection]:
        """Filter detections by confidence threshold"""
        return [d for d in detections if d.confidence >= threshold]
