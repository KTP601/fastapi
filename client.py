import requests

def predict(image_path):
    with open(image_path, "rb") as f:
        res = requests.post("http://localhost:8000/predict", files={"image": f})
    print("Result: ", res.json()["result"])

predict("test.png")
