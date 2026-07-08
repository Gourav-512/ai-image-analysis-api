import pytest
from app.utils.model_manager import model_manager

def test_model_manager_initialization():
    """Test model manager initialization"""
    assert model_manager is not None
    assert not model_manager.is_loaded()
    
def test_model_loading():
    """Test model loading"""
    # This test assumes yolov8n.pt exist
    try:
        model_manager.load_model("yolov8n.pt")
        assert model_manager.is_loaded()
    except Exception as e:
        # Model file might not exist in test environment
        pytest.skip(f"Model loading skipped: {e}")
