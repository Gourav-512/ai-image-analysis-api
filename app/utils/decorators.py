import time
from functools import wraps
from typing import Callable
import asyncio

def timing_decorator(func: Callable):
    """Decorator to measure function execution time"""
    @wraps(func)
    async def async_wrapper(*args, **kwargs):
        start = time.time()
        result = await func(*args, **kwargs)
        duration = time.time() - start
        return result, duration
    
    @wraps(func)
    def sync_wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        duration = time.time() - start
        return result, duration
    
    return async_wrapper if asyncio.iscoroutinefunction(func) else sync_wrapper
