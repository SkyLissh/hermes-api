from sqlalchemy import Column, Integer, ForeignKey, Boolean, String
from sqlalchemy.orm import relationship

from app.core.db.base_class import Base


class Member(Base):
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('users.id'), index=True, nullable=False)
    chat_id = Column(Integer, ForeignKey('chats.id'), index=True, nullable=False)
    is_admin = Column(Boolean, default=False)
    nickname = Column(String(25))

    chat = relationship('Chat', back_populates='members')
    user = relationship('User', back_populates='chats')
    messages = relationship('Message', back_populates='sender')
