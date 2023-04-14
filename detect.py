import torch
import torchvision
import numpy as np
from PIL import Image

def detect_objects(image_path):
    model = torch.hub.load('ultralytics/yolov5', 'custom', 'C:/Users/dell/OneDrive/Documents/PP2/projectdemo_dup/best.pt')
    img = Image.open(image_path)
    results = model(img)

    # Load the class names
    with open('C:/Users/dell/OneDrive/Documents/PP2/projectdemo_dup/names.txt', 'r') as f:
        class_names = f.read().splitlines()

    # Convert the label indices to class names
    labels = results.xyxy[0][:, 5].numpy().astype(int)
    class_names = [class_names[label] for label in labels]

    # Combine the bounding boxes with the class names
    boxes = results.xyxy[0][:, :5].numpy().tolist()
    predictions = [[class_names[i]] for i, box in enumerate(boxes)]

    return predictions, class_names

