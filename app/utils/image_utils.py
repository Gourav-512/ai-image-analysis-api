from PIL import Image, ImageDraw, ImageFont
import io

def draw_bounding_boxes(image_bytes: bytes, detections: list) -> bytes:
    image = Image.open(io.BytesIO(image_bytes))
    draw = ImageDraw.Draw(image)
    
    for det in detections:
        bbox = det['bbox']
        label = f"{det['class']} {det['confidence']:.2f}"
        draw.rectangle(bbox, outline='red', width=3)
        draw.text((bbox[0], bbox[1]-15), label, fill='red')
    
    output = io.BytesIO()
    image.save(output, format='JPEG')
    return output.getvalue()