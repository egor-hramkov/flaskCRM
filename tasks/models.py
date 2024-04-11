from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

from database.db_settings import db


class Task(db.Model):
    """Модель задачи"""
    __tablename__ = 'tasks'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(2000))
    author = db.Column(ForeignKey('users.id'), nullable=False)

    author_rel = relationship('User', backref='tasks')

    def __str__(self):
        return f"<Task {self.author.name}: {self.title}>"
