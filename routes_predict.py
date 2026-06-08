from fastapi import APIRouter, File, UploadFile, HTTPException
import time
from app.schemas import PredictionResponse
from app.utils.model_manager import model_manager
from app.utils.image_processor import ImageProcessor
from app.utils.result_processor import ResultProcessor
from app.utils.cache import prediction_cache


router = APIRouter()

@router.post("/predict", response_model=PredictionResponse)
async def predict(file: UploadFile = File(...)):
    """Predict objects in uploaded image"""
    try:
        start_time = time.time()
        contents = await file.read()
        
        # Check cache
        cache_key = prediction_cache.get_key(contents)
        cached_result = prediction_cache.get(cache_key)
        if cached_result:
            return cached_result
        
        # Process image
        image = ImageProcessor.bytes_to_image(contents)
        if not ImageProcessor.validate_image(image):
            raise HTTPException(status_code=400, detail="Invalid image format")
        
        image = ImageProcessor.normalize_image(image)
        
        # Get model and run inference
        model = model_manager.get_model()
        if not model:
            raise HTTPException(status_code=500, detail="Model not loaded")
        
        results = model(image)
        detections = ResultProcessor.process_detections(results)
        
        inference_time = time.time() - start_time
        
        response = PredictionResponse(
            success=True,
            filename=file.filename,
            detections=detections,
            inference_time=round(inference_time, 4)
        )
        
        # Cache result
        prediction_cache.set(cache_key, response)
        return response
        
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/health")
async def health():
    """Health check endpoint"""
    return {
        "status": "healthy",
        "model_loaded": model_manager.is_loaded(),
        "version": "1.0.0"
    }
