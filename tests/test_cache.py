import pytest
from app.utils.cache import prediction_cache

def test_cache_set_get():
    """Test cache set and get operations"""
    prediction_cache.clear()
    key = "test_key"
    value = {"class": "person", "confidence": 0.95}
    
    prediction_cache.set(key, value)
    result = prediction_cache.get(key)
    
    assert result == value

def test_cache_miss():
    """Test cache miss scenario"""
    prediction_cache.clear()
    result = prediction_cache.get("nonexistent_key")
    assert result is None

def test_cache_lru_eviction():
    """Test LRU cache eviction"""
    from app.utils.cache import PredictionCache
    small_cache = PredictionCache(max_size=2)
    
    small_cache.set("key1", {"data": 1})
    small_cache.set("key2", {"data": 2})
    small_cache.set("key3", {"data": 3})
    
    # key1 should be evicted
    assert small_cache.get("key1") is None
    assert small_cache.get("key2") is not None
    assert small_cache.get("key3") is not None
