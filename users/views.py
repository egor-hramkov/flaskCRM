from flasgger import swag_from
from flask import Blueprint, request, jsonify
from marshmallow import ValidationError

from swagger.users.register import REGISTER_SWAGGER
from users.schemas import UserSchemaIn, UserSchema
from users.services.user_service import UserService

users_bp = Blueprint('users', __name__)
user_service = UserService()


@swag_from("../swagger/users/register.yml")
@users_bp.route('/register', methods=['POST'])
def register():
    """Регистрация пользователя"""
    try:
        data = UserSchemaIn.load(request.get_json())
    except ValidationError as err:
        return jsonify(err.messages), 400
    user: UserSchema = user_service.create(data)
    return jsonify(user)


@users_bp.route('/<int:user_id>', methods=['GET'])
def get(user_id: int):
    """Получение пользователя"""
    return user_service.get(user_id)


@users_bp.route('/list/', methods=['GET'])
def list(user_id: int):
    """Получение пользователей"""
    pass


@users_bp.route('/<int:user_id>', methods=['PUT'])
def update(user_id: int):
    """Получение пользователя"""
    pass


@users_bp.route('/<int:user_id>', methods=['DELETE'])
def delete(user_id: int):
    """Получение пользователя"""
    user_service.delete(user_id)
    return jsonify({"detail": "OK"})
