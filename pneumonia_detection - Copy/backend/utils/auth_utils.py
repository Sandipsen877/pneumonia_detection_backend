from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token
from datetime import timedelta
from models.user import User
from extensions import db

def register_user(username, email, password):
    if User.query.filter_by(email=email).first():
        return None, 'Email already registered'
    
    hashed_password = generate_password_hash(password)
    new_user = User(
        username=username,
        email=email,
        password=hashed_password
    )
    
    db.session.add(new_user)
    db.session.commit()
    
    return new_user, None

def authenticate_user(email, password):
    user = User.query.filter_by(email=email).first()
    if not user or not check_password_hash(user.password, password):
        return None, 'Invalid credentials'
    
    access_token = create_access_token(
        identity=user.id,
        expires_delta=timedelta(hours=1)
    )
    
    return {
        'access_token': access_token,
        'user_id': user.id,
        'username': user.username,
        'email': user.email
    }, None