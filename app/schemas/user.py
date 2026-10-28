from datetime import datetime
from typing import Optional
from uuid import UUID
from pydantic import BaseModel, EmailStr, Field

class UserBase(BaseModel):
    name: str = Field(..., max_length=255)
    email: EmailStr
    role: str = Field(..., pattern="^(officer|admin)$")
    is_active: bool = True

class UserCreate(UserBase):
    password: str = Field(..., min_length=8)

class UserUpdate(BaseModel):
    name: Optional[str] = None
    role: Optional[str] = Field(None, pattern="^(officer|admin)$")
    is_active: Optional[bool] = None

class UserResponse(UserBase):
    id: UUID