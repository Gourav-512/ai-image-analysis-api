from fastapi import APIRouter, UploadFile, File, Query
from fastapi.responses import Response
from app.models.detection import detect_objects
from app.utils.image_utils import draw_bounding_boxes

router = APIRouter()

@router.post("/predict/visualize")
async def predict_and_visualize(file: UploadFile = File(...), conf: float = Query(0.25, gt=0, lt=1)):
    if not file.content_type.startswith('image/'):
        raise HTTPException(400, "Image file required")
    
    contents = await file.read()
    result = detect_objects(contents, conf)
    
    annotated_image = draw_bounding_boxes(contents, result['detections'])
    
    return Response(content=annotated_image, media_type="image/jpeg")