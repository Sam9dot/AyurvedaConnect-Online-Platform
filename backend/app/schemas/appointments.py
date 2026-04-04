from __future__ import annotations

from datetime import datetime
from typing import Optional

from pydantic import BaseModel, ConfigDict, Field


class AppointmentCreate(BaseModel):
    user_id: int
    doctor_id: int
    center_id: int
    appointment_date: datetime


class AppointmentUpdate(BaseModel):
    user_id: Optional[int] = None
    doctor_id: Optional[int] = None
    center_id: Optional[int] = None
    appointment_date: Optional[datetime] = None


class AppointmentResponse(BaseModel):
    appointment_id: int
    user_id: int
    doctor_id: int
    center_id: int
    appointment_date: datetime

    # Pydantic v2: allow loading from ORM objects.
    # `orm_mode` is kept for compatibility with older FastAPI/Pydantic examples.
    model_config = ConfigDict(from_attributes=True, orm_mode=True)

