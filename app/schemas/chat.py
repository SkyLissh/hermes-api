from typing import Optional
from pydantic import BaseModel, HttpUrl

from app.schemas.member import Member


# Shared properties
class ChatBase(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    picture: Optional[HttpUrl] = None
    invitation_link: Optional[HttpUrl] = None


# Properties to receive via API on creation
class ChatCreate(ChatBase):
    name: str


# Properties to have on db
class ChatInDBBase(ChatBase):
    id: Optional[int] = None

    class Config:
        orm_mode = True


# Additional properties stored in DB
class ChatInDB(ChatInDBBase):
    pass


# Additional properties to return via API
class Chat(ChatBase):
    members: Optional[list[Member]]
