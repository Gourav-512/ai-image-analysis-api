from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from ultralytics import YOLO
from PIL import Image
import io

app = FastAPI(title="AI Image Analysis API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

model = YOLO("yolov8n.pt")


@app.get("/")
def read_root():
    return {"message": "✅ AI Image Analysis API is running >>"}

@app.get("/health")
def health():
    return {"status": "healthy"}

@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    try:
        contents = await file.read()
        image = Image.open(io.BytesIO(contents))
        results = model(image)
        
        detections = []
        for result in results:
            for box in result.boxes:
                x1, y1, x2, y2 = box.xyxy[0].tolist()
                conf = float(box.conf[0])
                cls = int(box.cls[0])
                name = result.names[cls]
                detections.append({
                    "class": name,
                    "confidence": round(conf, 4),
                    "bbox": [round(x,2) for x in [x1,y1,x2,y2]]
                })

        
        return {
            "success": True,
            "filename": file.filename,
            "detections": detections
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
