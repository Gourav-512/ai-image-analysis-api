from pydantic import BaseModel
from typing import List, Optional

class BoundingBox(BaseModel):
    x1: float
    y1: float
    x2: float
    y2: float
    class Config:
        json_schema_extra = {
            "example": {"x1": 10.5, "y1": 20.3, "x2": 100.8, "y2": 150.2}
        }

class Detection(BaseModel):
    class_name: str
    confidence: float
    bbox: BoundingBox

class PredictionResponse(BaseModel):
    success: bool
    filename: Optional[str] = None
    detections: List[Detection]
    inference_time: Optional[float] = None

class HealthResponse(BaseModel):
    status: str
    model_loaded: bool
    version: str = "1.0.0"
