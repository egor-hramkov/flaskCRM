from flask_marshmallow.sqla import SQLAlchemySchema

from users.models import User


class UserSchema(SQLAlchemySchema):
    """Общая схема пользователя"""

    class Meta:
        model = User
        exclude = ('password',)


class UsersSchemaIn(SQLAlchemySchema):
    """Схема пользователя для сохранения/обновления данных"""

    class Meta:
        model = User
