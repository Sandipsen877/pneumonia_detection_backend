from flask import Blueprint, request, jsonify
from werkzeug.utils import secure_filename
import os
from datetime import datetime
from services.detection_service import analyze_xray
from utils.file_utils import allowed_file

detection_bp = Blueprint('detection', __name__)

@detection_bp.route('/api/analyze', methods=['POST'])
def detect_pneumonia():
    if 'xray' not in request.files:
        return jsonify({'error': 'No file uploaded'}), 400
    
    file = request.files['xray']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400
    
    if file and allowed_file(file.filename):
        # Get patient info
        patient_name = request.form.get('patient_name', 'Anonymous')
        patient_age = request.form.get('patient_age', 'Unknown')
        patient_gender = request.form.get('patient_gender', 'Unknown')
        
        try:
            # Analyze the image
            result = analyze_xray(file)
            
            return jsonify({
                'status': 'success',
                'has_pneumonia': result['has_pneumonia'],
                'confidence': result['confidence'],
                'patient_info': {
                    'name': patient_name,
                    'age': patient_age,
                    'gender': patient_gender
                }
            })
        except Exception as e:
            return jsonify({'error': str(e)}), 500
    
    return jsonify({'error': 'Invalid file type'}), 400