from flask import Blueprint, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from models.user import User

main_bp = Blueprint('main', __name__)

@main_bp.route('/api/status')
def status():
    return jsonify({'status': 'OK'})

@main_bp.route('/api/protected')
@jwt_required()
def protected():
    current_user_id = get_jwt_identity()
    user = User.query.get(current_user_id)
    return jsonify({
        'message': f'Hello {user.username}!',
        'user': {
            'id': user.id,
            'username': user.username,
            'email': user.email
        }
    })