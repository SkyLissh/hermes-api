from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship

from app.core.db.base_class import Base


class Message(Base):
    id = Column(Integer, primary_key=True, index=True)
    text = Column(String, nullable=False)
    datetime = Column(DateTime, nullable=False)
    sender_id = Column(Integer, ForeignKey('members.id'), index=True)

    sender = relationship('Member', back_populates='messages')
