from typing import Optional
from PIL import Image
import io

class ImageProcessor:
    """Utility class for image processing operations"""
    
    @staticmethod
    def resize_image(image: Image.Image, max_size: tuple = (640, 640)) -> Image.Image:
        """Resize image while maintaining aspect ratio"""
        image.thumbnail(max_size, Image.Resampling.LANCZOS)
        return image
    
    @staticmethod
    def normalize_image(image: Image.Image) -> Image.Image:
        """Normalize image for better model performance"""
        return image.convert('RGB')
    
    @staticmethod
    def bytes_to_image(image_bytes: bytes) -> Image.Image:
        """Convert bytes to PIL Image"""
        return Image.open(io.BytesIO(image_bytes))
    
    @staticmethod
    def image_to_bytes(image: Image.Image, format: str = 'PNG') -> bytes:
        """Convert PIL Image to bytes"""
        buffer = io.BytesIO()
        image.save(buffer, format=format)
        return buffer.getvalue()
    
    @staticmethod
    def validate_image(image: Image.Image) -> bool:
        """Validate image format and size"""
        if image.size[0] < 10 or image.size[1] < 10:
            return False
        if image.mode not in ['RGB', 'RGBA', 'L']:
            return False
        return True
