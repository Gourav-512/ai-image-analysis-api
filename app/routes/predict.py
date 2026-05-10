from fastapi import APIRouter, UploadFile, File, HTTPException, Response
import io
from PIL import Image, ImageDraw
from app.models.detection import detect_objects, model

router = APIRouter()

@router.post("/predict")
async def predict(file: UploadFile = File(...), conf: float = 0.25, return_image: bool = False):
    if not file.content_type or not file.content_type.startswith("image/"):
        raise HTTPException(status_code=400, detail="File must be an image")
    
    contents = await file.read()
    try:
        result = detect_objects(contents, conf)
        
        if return_image and result.get("detections"):
            # Draw bounding boxes on image
            image = Image.open(io.BytesIO(contents))
            draw = ImageDraw.Draw(image)
            for det in result["detections"]:
                bbox = det["bbox"]
                draw.rectangle([bbox[0], bbox[1], bbox[2], bbox[3]], outline="red", width=3)
                label = f"{det['class']} {det['confidence']:.2f}"
                draw.text((bbox[0], max(bbox[1]-15, 0)), label, fill="red")
            
            img_byte_arr = io.BytesIO()
            image.save(img_byte_arr, format='JPEG')
            return Response(content=img_byte_arr.getvalue(), media_type="image/jpeg")
        
        return {
            "filename": file.filename,
            "status": "success",
            **result
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Inference error: {str(e)}")

@router.get("/health")
async def health():
    return {"status": "healthy", "model": "yolov8n"}
