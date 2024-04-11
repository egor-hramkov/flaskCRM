from flask import Blueprint, request, jsonify
from marshmallow import ValidationError

from users.schemas import UsersSchemaIn, UserSchema
from users.services.user_service import UserService

users_bp = Blueprint('users', __name__)
user_service = UserService()


@users_bp.route('/register', methods=['POST'])
def register():
    """Регистрация пользователя"""
    try:
        data = UsersSchemaIn.load(request.get_json())
    except ValidationError as err:
        return jsonify(err.messages), 400
    user: UserSchema = user_service.create(data)
    return jsonify(user)
