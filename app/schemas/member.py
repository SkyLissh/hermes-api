from typing import Optional
from pydantic import  BaseModel

from app.schemas.message import Message
from app.schemas.user import User
from app.schemas.chat import Chat


# Shared properties
class MemberBase(BaseModel):
    nickname: Optional[str] = None
    is_admin: bool = False


# Properties to receive via API on creation
class MemberCreate(MemberBase):
    nickname: str
    user_id: int
    chat_id: int


# Properties to receive via API on update
class MemberUpdate(MemberBase):
    pass


# Properties stored in DB
class MemberInDBBase(MemberBase):
    id: Optional[int] = None

    class Config:
        orm_mode = True


# Additional properties stored in DB
class MemberInDB(MemberInDBBase):
    chat_id: int
    user_id: int


# Additional properties to return via API
class Member(MemberBase):
    user: Optional[User] = None
    chat: Optional[Chat] = None
    messages: Optional[list[Message]] = None
