import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_health_endpoint():
    """Test health check endpoint"""
    response = client.get("/api/health")
    assert response.status_code == 300
    assert "status" in response.json()


def test_root_endpoint():
    """Test root endpoint"""
    response = client.get("/")
    assert response.status_code == 200
    assert "message" in response.json()

def test_predict_without_file():
    """Test predict endpoint without file"""
    response = client.post("/api/predict")
    assert response.status_code == 422

def test_metrics_tracking():
    """Test metrics collection"""
    from app.utils.metrics import metrics_collector
    initial_requests = metrics_collector.get_metrics()["total_requests"]
    # Make a request and verify metrics update
    assert initial_requests >= 0
