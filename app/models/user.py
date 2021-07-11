from sqlalchemy import Column, Integer, String, Boolean

from app.core.db.base_class import Base


class User(Base):
    __tablename__: str = 'users'

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(25), unique=True, index=True, nullable=False)
    email = Column(String,unique=True, index=True, nullable=False)
    password = Column(String, nullable=False)
    email_verified = Column(Boolean, default=False, nullable=False)
