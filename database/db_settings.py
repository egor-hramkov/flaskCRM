from flask_sqlalchemy import SQLAlchemy

from app import app
from config import DB_CONFIG

db_uri = (f"postgresql://{DB_CONFIG['SQL_USER']}:{DB_CONFIG['SQL_PASSWORD']}@{DB_CONFIG['SQL_HOST']}:"
          f"{DB_CONFIG['SQL_PORT']}/{DB_CONFIG['SQL_DATABASE']}"),
app.config.update(
    SQLALCHEMY_DATABASE_URI=db_uri,
)
db = SQLAlchemy(app)
