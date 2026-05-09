# AI Image Analysis API

A fast and simple **FastAPI + YOLOv8** REST API for object detection in images.

## Features
- Object detection using YOLOv8
- FastAPI with Swagger UI
- Easy to deploy (Docker ready)

## Installation

```bash
git clone https://github.com/Gourav-512/ai-image-analysis-api.git
cd ai-image-analysis-api
pip install -r requirements.txt
```

## Running Locally

```bash
uvicorn app.main:app --reload
```

API will be available at `http://127.0.0.1:8000`

Docs → `http://127.0.0.1:8000/docs`

## API Usage

**POST** `/api/predict`

Upload an image file.

## Docker

```bash
docker build -t ai-image-api .
docker run -p 8000:8000 ai-image-api
```
