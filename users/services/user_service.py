from users.repositories.user_repository import UserRepository
from users.schemas import UserSchemaIn, UserSchema


class UserService:
    _repository = UserRepository()

    def create(self, data: UserSchemaIn):
        """Создание пользователя"""
        user: UserSchema = self._repository.create(data)
        return user

    def get(self, user_id: int):
        """Создание пользователя"""
        user: UserSchema = self._repository.get(user_id)
        return user

    def list(self, data: UserSchemaIn):
        """Создание пользователя"""
        user: UserSchema = self._repository.create(data)
        return user

    def update(self, data: UserSchemaIn):
        """Создание пользователя"""
        user: UserSchema = self._repository.create(data)
        return user

    def delete(self, user_id: int) -> None:
        """Создание пользователя"""
        self._repository.delete(user_id)
