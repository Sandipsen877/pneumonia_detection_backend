from flask import Blueprint, request, jsonify
from utils.auth_utils import register_user, authenticate_user

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/api/auth/register', methods=['POST'])
def register():
    data = request.get_json()
    if not data or not all(key in data for key in ['username', 'email', 'password']):
        return jsonify({'error': 'Missing required fields'}), 400
    
    user, error = register_user(
        data['username'],
        data['email'],
        data['password']
    )
    
    if error:
        return jsonify({'error': error}), 400
    
    return jsonify({
        'message': 'User registered successfully',
        'user_id': user.id
    }), 201

@auth_bp.route('/api/auth/login', methods=['POST'])
def login():
    data = request.get_json()
    if not data or not all(key in data for key in ['email', 'password']):
        return jsonify({'error': 'Missing email or password'}), 400
    
    result, error = authenticate_user(data['email'], data['password'])
    
    if error:
        return jsonify({'error': error}), 401
    
    return jsonify(result), 200

@auth_bp.route('/api/auth/forgot-password', methods=['POST'])
def forgot_password():
    # Implement password reset logic here
    return jsonify({'message': 'Password reset link sent'}), 200