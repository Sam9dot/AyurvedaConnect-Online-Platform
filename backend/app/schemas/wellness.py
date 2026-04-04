from __future__ import annotations

from typing import Optional

from pydantic import BaseModel, ConfigDict, Field


class WellnessCreate(BaseModel):
    name: str = Field(min_length=1, max_length=255)
    location: str = Field(min_length=1, max_length=255)
    center_type: str = "wellness"
    experience: Optional[str] = None
    phone: Optional[str] = None
    services: Optional[str] = None
    image_url: Optional[str] = None
    amenities: Optional[str] = None


class WellnessResponse(BaseModel):
    center_id: int
    name: str
    location: str
    amenities: Optional[str] = None
    center_type: str = "wellness"
    experience: Optional[str] = None
    daily_footfall: Optional[str] = None
    image_url: Optional[str] = None
    phone: Optional[str] = None
    services: Optional[str] = None
    rating: Optional[float] = None

    model_config = ConfigDict(from_attributes=True, orm_mode=True)
