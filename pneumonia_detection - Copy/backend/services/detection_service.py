from utils.model_utils import load_model, predict
import os

# Initialize model
model_path = os.path.join(os.path.dirname(__file__), '../static/models/pneumonia_model.pth')
model = load_model(model_path)

def analyze_xray(file):
    try:
        # Read file bytes
        image_bytes = file.read()
        
        # Make prediction
        prediction, confidence = predict(image_bytes, model)
        
        # Return results (assuming 1 is pneumonia, 0 is normal)
        return {
            'has_pneumonia': bool(prediction),
            'confidence': round(confidence, 2)
        }
    except Exception as e:
        raise Exception(f"Error analyzing image: {str(e)}")