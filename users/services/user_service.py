from users.repositories.user_repository import UserRepository
from users.schemas import UsersSchemaIn, UserSchema


class UserService:
    _repository = UserRepository()

    def create(self, data: UsersSchemaIn):
        """Создание пользователя"""
        user: UserSchema = self._repository.create(data)
        return user
