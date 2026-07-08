import pytest
from app.utils.image_processor import ImageProcessor
from PIL import Image
import io

def test_image_normalization():
    """Test image normalization"""
    img = Image.new('RGB', (640, 640))
    normalized = ImageProcessor.normalize_image(img)
    assert normalized.mode == 'RGB'

def test_image_validation():
    """Test image validation"""
    valid_img = Image.new('RGB', (640, 640))
    assert ImageProcessor.validate_image(valid_img) == True
    
    invalid_img = Image.new('RGB', (5, 5))
    assert ImageProcessor.validate_image(invalid_img) == False


def test_bytes_conversion():
    """Test image bytes conversion"""
    img = Image.new('RGB', (100, 100))
    img_bytes = ImageProcessor.image_to_bytes(img)
    assert isinstance(img_bytes, bytes)
    assert len(img_bytes) > 0
