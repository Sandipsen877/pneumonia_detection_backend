from extensions import db, jwt

def create_app():
    app = Flask(__name__)
    CORS(app)
    
    # Initialize extensions
    db.init_app(app)
    jwt.init_app(app)

from flask import Flask
from flask_cors import CORS
from routes.auth import auth_bp
from routes.detection import detection_bp
from routes.main import main_bp

def create_app():
    app = Flask(__name__)
    CORS(app)
    
    # Load configuration
    app.config.from_pyfile('config.py')
    
    # Register blueprints
    app.register_blueprint(auth_bp)
    app.register_blueprint(detection_bp)
    app.register_blueprint(main_bp)
    
    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)