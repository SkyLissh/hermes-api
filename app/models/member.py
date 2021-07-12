from sqlalchemy import Column, Integer, ForeignKey, Boolean, String
from sqlalchemy.orm import relationship

from app.core.db.base_class import Base


class Member(Base):
    user_id = Column(Integer, ForeignKey('users.id'), primary_key=True)
    chat_id = Column(Integer, ForeignKey('chats.id'), primary_key=True)
    is_admin = Column(Boolean, default=False)
    nickname = Column(String(25))

    chat = relationship('Chat', back_populates='members')
    user = relationship('User', back_populates='chats')
