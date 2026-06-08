from typing import Optional, Dict, Any
import threading

class ThreadSafeModelManager:
    """Thread-safe model loading and management"""
    def __init__(self):
        self._lock = threading.RLock()
        self._model = None
        self._model_name = None
    
    def load_model(self, model_name: str):
        """Load model in thread-safe manner"""
        with self._lock:
            if self._model_name != model_name:
                from ultralytics import YOLO
                self._model = YOLO(model_name)
                self._model_name = model_name
    
    def get_model(self):
        """Get loaded model"""
        with self._lock:
            return self._model
    
    def is_loaded(self) -> bool:
        """Check if model is loaded"""
        with self._lock:
            return self._model is not None

model_manager = ThreadSafeModelManager()
