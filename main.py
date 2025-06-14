from fastapi import FastAPI, UploadFile, File
from fastapi.responses import JSONResponse
from ultralytics import YOLO
from PIL import Image
import numpy as np
import io

app = FastAPI()

model = YOLO("best.pt") 

@app.post("/predict")
async def predict(image: UploadFile = File(...)):
    contents = await image.read()
    img = Image.open(io.BytesIO(contents)).convert("RGB")
    img_array = np.array(img)
    
    results = model.predict(img_array, conf=0.4)

    labels = results[0].names
    boxes = results[0].boxes
    detected = any(labels[int(cls)] == "samdasoo" for cls in boxes.cls)

    result_msg = "Detected Samdasoo" if detected else "Samdasoo Not Detected"
    return JSONResponse(content={"result": result_msg})
