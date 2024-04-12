from flask_marshmallow.sqla import SQLAlchemySchema
from marshmallow import fields

from users.models import User


class UserSchema(SQLAlchemySchema):
    """Общая схема пользователя"""
    password = fields.Str(required=True, load_only=True)

    class Meta:
        model = User
        #exclude = ('password',)


class UserSchemaIn(SQLAlchemySchema):
    """Схема пользователя для сохранения/обновления данных"""

    class Meta:
        model = User
