from sqlalchemy import create_engine
import pandas

from config import (
    DB_USER,
    DB_PASSWORD,
    DB_NAME,
    DB_HOST,
)


def connect_to_db():
    engine = create_engine(
        f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}"
    )
    return engine