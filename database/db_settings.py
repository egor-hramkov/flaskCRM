from flask_sqlalchemy import SQLAlchemy

from app import app
from database.config import DB_URI

app.config.update(
    SQLALCHEMY_DATABASE_URI=DB_URI,
)
db = SQLAlchemy(app)
