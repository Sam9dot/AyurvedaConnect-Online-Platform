from __future__ import annotations

from decimal import Decimal
from typing import Optional

from pydantic import BaseModel, ConfigDict, EmailStr, Field


class UserCreate(BaseModel):
    email: EmailStr
    # Stored in DB as `password_hash`. Alias keeps the request payload ergonomic.
    password_hash: str = Field(min_length=8, max_length=255, alias="password")
    user_type: str = Field(default="patient", max_length=20)
    name: Optional[str] = Field(default=None, max_length=255)
    phone: Optional[str] = Field(default=None, max_length=30)


class UserUpdate(BaseModel):
    name: Optional[str] = Field(default=None, min_length=1, max_length=255)
    phone: Optional[str] = Field(default=None, max_length=30)
    password_hash: Optional[str] = Field(default=None, min_length=8, max_length=255, alias="password")


class UserResponse(BaseModel):
    user_id: int
    name: str
    email: EmailStr
    phone: Optional[str] = None
    user_type: str = "patient"

    # Pydantic v2: allow loading from ORM objects.
    # `orm_mode` is kept for compatibility with older FastAPI/Pydantic examples.
    model_config = ConfigDict(from_attributes=True, orm_mode=True)
