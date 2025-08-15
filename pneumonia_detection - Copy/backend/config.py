import os
from pathlib import Path
from dotenv import load_dotenv

# Load environment variables from root .env
env_path = Path(__file__).resolve().parent.parent / '.env'
load_dotenv(env_path)

class Config:
    # ===== CORE =====
    FLASK_ENV = os.getenv('FLASK_ENV', 'production')
    SECRET_KEY = os.getenv('SECRET_KEY')
    DEBUG = os.getenv('DEBUG_MODE', 'false').lower() == 'true'
    
    # ===== DATABASE =====
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    # ===== AUTHENTICATION =====
    JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY')
    JWT_ACCESS_TOKEN_EXPIRES = int(os.getenv('JWT_ACCESS_TOKEN_EXPIRES', 3600))
    
    # ===== ML MODEL =====
    MODEL_PATH = os.getenv('MODEL_PATH')
    
    # ===== FILE UPLOADS =====
    UPLOAD_FOLDER = os.path.join(os.path.dirname(__file__), 'static/uploads')
    ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'dcm'}
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024  # 16MB
    
    # ===== EMAIL =====
    MAIL_SERVER = os.getenv('MAIL_SERVER')
    MAIL_PORT = int(os.getenv('MAIL_PORT', 587))
    MAIL_USE_TLS = os.getenv('MAIL_USE_TLS', 'true').lower() == 'true'
    MAIL_USERNAME = os.getenv('MAIL_USERNAME')
    MAIL_PASSWORD = os.getenv('MAIL_PASSWORD')
    MAIL_DEFAULT_SENDER = os.getenv('MAIL_USERNAME')

    @staticmethod
    def init_app(app):
        # Ensure directories exist
        os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
        model_dir = os.path.dirname(app.config['MODEL_PATH'])
        os.makedirs(model_dir, exist_ok=True)