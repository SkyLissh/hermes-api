from typing import Optional
from pydantic import BaseModel

from datetime import datetime

from app.schemas.member import Member


# Shared Properties


class MessageBase(BaseModel):
    text: Optional[str] = None
    datetime: Optional[datetime] = None


# Properties to receive via API on creation
class MessageCreate(MessageBase):
    text: str
    datetime: datetime
    sender_id: int


# Properties to receive via API on update
class MessageUpdate(MessageBase):
    sender_id: Optional[int] = None


# Properties stored in DB
class MessageInDBBase(MessageBase):
    id: Optional[int] = None

    class Config:
        orm_mode = True


# Additional properties stored in DB
class MessageInDB(MessageInDBBase):
    sender_id: int = None


# Additional properties to return via API
class Message(MessageBase):
    sender: Optional[Member] = None
