from typing import Dict, List
import time

class MetricsCollector:
    """Collect and track API metrics"""
    def __init__(self):
        self.metrics = {
            "total_requests": 0,
            "successful_predictions": 0,
            "failed_predictions": 0,
            "avg_inference_time": 0.0,
            "cache_hits": 0,
            "cache_misses": 0,
        }
    
    def record_request(self, success: bool, inference_time: float, cache_hit: bool):
        """Record metrics for a request"""
        self.metrics["total_requests"] += 1
        if success:
            self.metrics["successful_predictions"] += 1
        else:
            self.metrics["failed_predictions"] += 1
        
        if cache_hit:
            self.metrics["cache_hits"] += 1
        else:
            self.metrics["cache_misses"] += 1
    
    def get_metrics(self) -> Dict:
        """Get current metrics"""
        return self.metrics.copy()

metrics_collector = MetricsCollector()
