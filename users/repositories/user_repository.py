from users.models import User
from users.schemas import UserSchemaIn, UserSchema


class UserRepository:
    """Репозиторий для работы с пользователем"""

    def create(self, data: UserSchemaIn) -> UserSchema:
        """Создание пользователя"""
        user = User(**data.dict())
        user.create()
        return UserSchema.dump(user)

    def get(self, user_id: int) -> UserSchema:
        """Получение пользователя"""
        user = User.query.get_or_404(user_id)
        return UserSchema.dump(user)

    def list(self, data: UserSchemaIn) -> UserSchema:
        """Создание пользователя"""
        user = User(**data.dict())
        user.create()
        return UserSchema.dump(user)

    def update(self, data: UserSchemaIn) -> UserSchema:
        """Создание пользователя"""
        user = User(**data.dict())
        user.create()
        return UserSchema.dump(user)

    def delete(self, user_id: int) -> None:
        """Создание пользователя"""
        user = User.query.get_or_404(user_id)
        user.delete()
