from typing_extensions import Self

from sqlalchemy import JSON

from database.db_settings import db


class User(db.Model):
    """Модель пользователя"""
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(60), unique=True, nullable=False)
    password = db.Column(db.String(), nullable=False)
    name = db.Column(db.String(60))
    surname = db.Column(db.String(60))
    photo = db.Column(db.String())
    about = db.Column(db.String())
    social_media = db.Column(JSON)
    address = db.Column(db.String())
    company = db.Column(db.String())

    def __str__(self):
        return f"<User {self.id}: {self.username}>"

    def create(self) -> Self:
        db.session.add(self)
        db.session.commit()
        return self

    def delete(self):
        db.session.delete(self)
        db.session.commit()
