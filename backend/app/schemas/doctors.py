from __future__ import annotations

from typing import Optional

from pydantic import BaseModel, ConfigDict, Field


class DoctorCreate(BaseModel):
    user_id: Optional[int] = None
    name: str = Field(min_length=1, max_length=255)
    specialization: str = Field(min_length=1, max_length=255)
    qualification: Optional[str] = None
    experience: Optional[str] = None
    phone: Optional[str] = None
    location: Optional[str] = None
    image_url: Optional[str] = None
    bio: Optional[str] = None


class DoctorUpdate(BaseModel):
    name: Optional[str] = Field(default=None, min_length=1, max_length=255)
    specialization: Optional[str] = Field(default=None, min_length=1, max_length=255)
    qualification: Optional[str] = None
    experience: Optional[str] = None
    phone: Optional[str] = None
    location: Optional[str] = None
    image_url: Optional[str] = None
    bio: Optional[str] = None


class DoctorResponse(BaseModel):
    doctor_id: int
    user_id: Optional[int] = None
    name: str = ""
    specialization: str
    qualification: Optional[str] = None
    experience: Optional[str] = None
    phone: Optional[str] = None
    location: Optional[str] = None
    image_url: Optional[str] = None
    daily_footfall: Optional[str] = None
    bio: Optional[str] = None
    rating: Optional[float] = None

    model_config = ConfigDict(from_attributes=True, orm_mode=True)
