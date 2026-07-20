import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from config import config
from logger import setup_logging
from app.utils.model_manager import model_manager
from routes_predict import router as predict_router


# Setup logging
logger = setup_logging(config.LOG_LEVEL)

# Initialize FastAPI app
app = FastAPI(
    title="AI Image Analysis API",
    description="YOLOv8 Object Detection API with Performance Optimizations",
    version="1.0.0"
)

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=[""],
)

# Load model on startup
@app.on_event("startup")
async def startup_event():
    """Initialize model on application startup"""
    logger.info("Loading YOLO model...")
    model_manager.load_model(config.MODEL_NAME)
    logger.info(f"Model {config.MODEL_NAME} loaded successfully")

@app.on_event("shutdown")
async def shutdown_event():
    """Cleanup on shutdown"""
    logger.info("Shutting down API")

# Include routers
app.include_router(predict_router, prefix="/api", tags=["predictions"])

@app.get("/")
async def root():
    """Root endpoint"""
    return {"message": "AI Image Analysis API is running! Visit /docs for API documentation"}

if __name__ == "__main__":
    uvicorn.run(
        app,
        host=config.HOST,
        port=config.PORT,
        workers=config.WORKERS,
        log_level=config.LOG_LEVEL.lower()
    )
