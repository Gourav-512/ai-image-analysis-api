from functools import lru_cache
from typing import Optional
import hashlib

class PredictionCache:
    """In-memory cache for model predictions"""
    def __init__(self, max_size: int = 100):
        self.cache = {}
        self.max_size = max_size
    
    def get_key(self, image_bytes: bytes) -> str:
        """Generate cache key from image bytes"""
        return hashlib.md5(image_bytes).hexdigest()
    
    def get(self, key: str) -> Optional[dict]:
        """Get prediction from cache"""
        return self.cache.get(key)
    
    def set(self, key: str, value: dict) -> None:
        """Set prediction in cache with LRU eviction"""
        if len(self.cache) >= self.max_size:
            self.cache.pop(next(iter(self.cache)))
        self.cache[key] = value
    
    def clear(self) -> None:
        """Clear the cache"""
        self.cache.clear()

prediction_cache = PredictionCache()
