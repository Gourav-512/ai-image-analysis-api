# AI Image Analysis API

✅ Updated on May 23, 2026

FastAPI + YOLOv8 based object detection API.

## Features
- Object Detection using YOLOv8
- Bounding Box Visualization (return annotated image)
- Health Check Endpoint
- Fast & Lightweight

## How to Run

```bash
git clone https://github.com/Gourav-512/ai-image-analysis-api.git
cd ai-image-analysis-api
pip install -r requirements.txt
uvicorn app.main:app --reload
```

## API Endpoints
- `POST /api/predict` - Detect objects
- `POST /api/predict?return_image=true` - Get image with boxes
- `GET /api/health` - Health check

**Updated today with better documentation.**