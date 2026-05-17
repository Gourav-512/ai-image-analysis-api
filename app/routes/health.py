from fastapi import APIRouter
from app.models.detection import model

router = APIRouter()

@router.get("/health")
def health_check():
    return {
        "status": "healthy",
        "model_loaded": model is not None,
        "message": "AI Image Analysis API is running smoothly!"
    }