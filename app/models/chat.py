from sqlalchemy import Column, Integer, String, Text
from sqlalchemy.orm import relationship

from app.core.db.base_class import Base


class Chat(Base):
    id = Column(Integer, primary_key=True, index=True)
    picture = Column(String, nullable=True)
    name = Column(String(25), nullable=False, index=True)
    description = Column(Text, nullable=True)
    invitation_link = Column(String, index=True)

    members = relationship('Member', back_populates='chat')
    messages = relationship('Message')
