import os
from werkzeug.utils import secure_filename
from config import Config
from PIL import Image
import io

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in Config.ALLOWED_EXTENSIONS

def save_file(file):
    if not file or file.filename == '':
        return None
    
    if allowed_file(file.filename):
        filename = secure_filename(file.filename)
        filepath = os.path.join(Config.UPLOAD_FOLDER, filename)
        file.save(filepath)
        return filepath
    
    return None

def convert_to_png(image_bytes):
    try:
        image = Image.open(io.BytesIO(image_bytes))
        if image.mode != 'RGB':
            image = image.convert('RGB')
        
        output = io.BytesIO()
        image.save(output, format='PNG')
        return output.getvalue()
    except Exception as e:
        raise Exception(f"Image conversion failed: {str(e)}")