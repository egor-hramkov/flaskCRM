from dotenv import load_dotenv

import os


load_dotenv()
DB_CONFIG = {
    "SQL_DATABASE": os.environ.get("SQL_DATABASE"),
    "SQL_USER": os.environ.get("SQL_USER"),
    "SQL_PASSWORD": os.environ.get("SQL_PASSWORD"),
    "SQL_HOST": os.environ.get("SQL_HOST"),
    "SQL_PORT": os.environ.get("SQL_PORT"),
}
DB_URI = (f"postgresql://{DB_CONFIG['SQL_USER']}:{DB_CONFIG['SQL_PASSWORD']}@{DB_CONFIG['SQL_HOST']}:"
          f"{DB_CONFIG['SQL_PORT']}/{DB_CONFIG['SQL_DATABASE']}"),
