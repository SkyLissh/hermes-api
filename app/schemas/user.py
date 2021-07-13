from typing import Optional

from pydantic import BaseModel, EmailStr

from app.schemas.member import Member


# Shared properties
class UserBase(BaseModel):
    username: Optional[str] = None
    picture: Optional[str] = None
    email: Optional[EmailStr] = None
    email_verified: bool = False


# Properties to receive via API on creation
class UserCreate(UserBase):
    username: str
    email: EmailStr
    password: str


# Properties to receive via API on update
class UserUpdate(UserBase):
    password: Optional[str] = None


# Properties stored in DB
class UserInDBBase(UserBase):
    id: Optional[int] = None

    class Config:
        orm_mode = True


# Additional properties to return via API
class User(UserBase):
    chats: Optional[list[Member]] = None


# Additional properties stored in DB
class UserInDB(UserInDBBase):
    password: str
