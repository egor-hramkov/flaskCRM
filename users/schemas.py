from typing import Optional

from pydantic import BaseModel


class UserSchema(BaseModel):
    """Общая схема пользователя"""
    id: Optional[int] = None
    username: str
    name: str
    surname: str
    photo: Optional[str] = None
    about: str
    social_media: Optional[dict] = None
    address: str
    company: str


class UserSchemaIn(UserSchema):
    """Схема пользователя для сохранения/обновления данных"""
    password: str
