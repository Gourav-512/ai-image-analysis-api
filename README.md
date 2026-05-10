# AI Image Analysis API

🚀 **FastAPI + YOLOv8** Object Detection API with **bounding box visualization**.

## ✨ Today's Update
- New: Return image with red bounding boxes drawn (`return_image=true`)
- Added `/api/health` endpoint
- Improved documentation

## Features
- Real-time object detection (YOLOv8n)
- JSON results or annotated image response
- FastAPI + Swagger UI
- CORS enabled
- Docker support

## Quick Start
```bash
git clone https://github.com/Gourav-512/ai-image-analysis-api.git
cd ai-image-analysis-api
pip install -r requirements.txt
uvicorn app.main:app --reload
```

Test the new feature at `/docs` → set `return_image=true`

**Contributions & improvements added daily for better learning & portfolio**

— Gourav Salunkhe