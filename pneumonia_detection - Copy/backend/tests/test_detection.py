import pytest
import io
from PIL import Image
import numpy as np
from app import create_app
from extensions import db

@pytest.fixture
def app():
    app = create_app()
    app.config.update({
        "TESTING": True,
        "SQLALCHEMY_DATABASE_URI": "sqlite:///:memory:",
        "UPLOAD_FOLDER": "/tmp/uploads"
    })
    
    with app.app_context():
        db.create_all()
        yield app
        db.drop_all()

@pytest.fixture
def client(app):
    return app.test_client()

def create_test_image():
    file = io.BytesIO()
    image = Image.new('RGB', (100, 100), color='red')
    image.save(file, 'png')
    file.seek(0)
    return file

def test_detect_pneumonia(client):
    # Create a test image
    test_image = create_test_image()
    
    # Test with no file
    response = client.post('/api/analyze')
    assert response.status_code == 400
    
    # Test with valid file
    response = client.post('/api/analyze', data={
        'xray': (test_image, 'test.png'),
        'patient_name': 'Test Patient',
        'patient_age': '30',
        'patient_gender': 'male'
    }, content_type='multipart/form-data')
    
    assert response.status_code == 200
    assert 'has_pneumonia' in response.json
    assert 'confidence' in response.json