import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    """Configuration management for the application"""
    # Model settings
    MODEL_NAME = os.getenv("MODEL_NAME", "yolov8n.pt")
    CONFIDENCE_THRESHOLD = float(os.getenv("CONFIDENCE_THRESHOLD", "0.25"))
    
    # Server settings
    HOST = os.getenv("HOST", "0.0.0.0")
    PORT = int(os.getenv("PORT", "8000"))
    WORKERS = int(os.getenv("WORKERS", "4"))
    
    # Performance settings
    MAX_UPLOAD_SIZE = int(os.getenv("MAX_UPLOAD_SIZE", "104857600"))  # 100MB
    ENABLE_GPU = os.getenv("ENABLE_GPU", "true").lower() == "true"

    
    # Cache settings
    ENABLE_MODEL_CACHE = os.getenv("ENABLE_MODEL_CACHE", "true").lower() == "true"
    CACHE_PREDICTIONS = os.getenv("CACHE_PREDICTIONS", "false").lower() == "true"
    
    # Logging
    LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")

config = Config()
