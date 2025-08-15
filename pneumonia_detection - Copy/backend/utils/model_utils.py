import torch
import torch.nn as nn
from torchvision import transforms
from PIL import Image
import io

# Define the model architecture (should match training)
class PneumoniaModel(nn.Module):
    def __init__(self):
        super(PneumoniaModel, self).__init__()
        # Define your model layers here
        pass

# Load the trained model
def load_model(model_path):
    model = PneumoniaModel()
    model.load_state_dict(torch.load(model_path, map_location=torch.device('cpu')))
    model.eval()
    return model

# Preprocess the image
def preprocess_image(image_bytes):
    transform = transforms.Compose([
        transforms.Resize((256, 256)),
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
    ])
    
    image = Image.open(io.BytesIO(image_bytes)).convert('RGB')
    return transform(image).unsqueeze(0)

# Make prediction
def predict(image_bytes, model):
    tensor = preprocess_image(image_bytes)
    with torch.no_grad():
        outputs = model(tensor)
        _, preds = torch.max(outputs, 1)
        prob = torch.nn.functional.softmax(outputs, dim=1)[0] * 100
    return preds.item(), prob[preds.item()].item()