from typing import Generator

from sqlalchemy.orm import Session

from app.core.db.session import SessionLocal


def get_db() -> Generator:
    global db

    try:
        db: Session = SessionLocal()
        yield db
    finally:
        db.close()
