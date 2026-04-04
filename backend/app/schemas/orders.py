from __future__ import annotations

from datetime import datetime
from decimal import Decimal
from typing import Optional

from pydantic import BaseModel, ConfigDict, Field


class OrderCreate(BaseModel):
    user_id: int
    total_amount: Decimal = Field(ge=0)
    status: str = Field(default="pending", min_length=1, max_length=50)


class OrderUpdate(BaseModel):
    total_amount: Optional[Decimal] = Field(default=None, ge=0)
    status: Optional[str] = Field(default=None, min_length=1, max_length=50)
    tracking_status: Optional[str] = Field(default=None, max_length=50)
    estimated_delivery: Optional[str] = Field(default=None, max_length=100)


class OrderResponse(BaseModel):
    order_id: int
    user_id: int
    total_amount: Decimal
    status: str
    tracking_status: str = "placed"
    estimated_delivery: Optional[str] = None
    created_at: Optional[datetime] = None

    # Pydantic v2: allow loading from ORM objects.
    # `orm_mode` is kept for compatibility with older FastAPI/Pydantic examples.
    model_config = ConfigDict(from_attributes=True, orm_mode=True)
