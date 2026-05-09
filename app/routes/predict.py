from fastapi import APIRouter, UploadFile, File, HTTPException
from app.models.detection import detect_objects

router = APIRouter()

@router.post("/predict")
async def predict(file: UploadFile = File(...), conf: float = 0.25):
    if not file.content_type or not file.content_type.startswith("image/"):
        raise HTTPException(status_code=400, detail="File must be an image")
    
    contents = await file.read()
    try:
        result = detect_objects(contents, conf)
        return {
            "filename": file.filename,
            "status": "success",
            **result
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Inference error: {str(e)}")