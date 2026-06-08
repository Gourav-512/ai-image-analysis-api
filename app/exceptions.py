from fastapi import HTTPException
from typing import Optional

class APIError(Exception):
    """Base API error"""
    def __init__(self, status_code: int, detail: str):
        self.status_code = status_code
        self.detail = detail

class ImageValidationError(APIError):
    """Raised when image validation fails"""
    def __init__(self, detail: str = "Invalid image format or size"):
        super().__init__(400, detail)

class ModelNotLoadedError(APIError):
    """Raised when model is not loaded"""
    def __init__(self):
        super().__init__(503, "Model not loaded. Service temporarily unavailable")

class InferenceError(APIError):
    """Raised when inference fails"""
    def __init__(self, detail: str = "Inference failed"):
        super().__init__(500, detail)

def handle_error(error: Exception) -> HTTPException:
    """Convert exceptions to HTTP exceptions"""
    if isinstance(error, APIError):
        return HTTPException(status_code=error.status_code, detail=error.detail)
    return HTTPException(status_code=500, detail=str(error))
