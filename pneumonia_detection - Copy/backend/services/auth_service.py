from utils.auth_utils import register_user, authenticate_user
from models.user import User
from extensions import db

def handle_registration(username, email, password):
    # Additional business logic can go here
    return register_user(username, email, password)

def handle_login(email, password):
    # Additional business logic can go here
    return authenticate_user(email, password)

def get_user_by_id(user_id):
    return User.query.get(user_id)