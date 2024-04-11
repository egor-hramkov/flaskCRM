from users.models import User
from users.schemas import UsersSchemaIn, UserSchema


class UserRepository:
    """Репозиторий для работы с пользователем"""

    def create(self, data: UsersSchemaIn) -> UserSchema:
        """Создание пользователя"""
        user = User(**data.dict())
        user.create()
        return UserSchema.dump(user)
