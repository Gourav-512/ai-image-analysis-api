def format_confidence(conf: float) -> str:
    return f"{conf:.2%}" 

def get_model_info():
    return {
        "model": "YOLOv8n",
        "task": "Object Detection",
        "framework": "Ultralytics"
    }
