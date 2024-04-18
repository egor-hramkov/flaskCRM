from flasgger import swag_from
from flask import Blueprint, request, jsonify
from flask_pydantic import validate
from marshmallow import ValidationError

from users.schemas import UserSchemaIn, UserSchema
from users.services.user_service import UserService

users_bp = Blueprint('users', __name__, url_prefix='/users')
user_service = UserService()


@users_bp.route('/register', methods=['POST'])
@validate()
@swag_from("../swagger/users/register.yml")
def register(body: UserSchemaIn):
    """Регистрация пользователя"""
    user: UserSchema = user_service.create(body)
    return jsonify(user)


@users_bp.route('/<int:user_id>', methods=['GET'])
def get(user_id: int):
    """Получение пользователя"""
    return user_service.get(user_id)


@users_bp.route('/list/', methods=['GET'])
def list():
    """Получение пользователей"""
    users = user_service.list()
    return users


@users_bp.route('/<int:user_id>', methods=['PUT'])
def update(user_id: int):
    """Получение пользователя"""
    pass


@users_bp.route('/<int:user_id>', methods=['DELETE'])
def delete(user_id: int):
    """Получение пользователя"""
    user_service.delete(user_id)
    return jsonify({"detail": "OK"})
