from __future__ import annotations

from decimal import Decimal
from typing import Optional

from pydantic import BaseModel, ConfigDict, Field


class ProductCreate(BaseModel):
    name: str = Field(min_length=1, max_length=255)
    brand_id: int
    category_id: int
    price: Decimal = Field(ge=0)


class ProductUpdate(BaseModel):
    name: Optional[str] = Field(default=None, min_length=1, max_length=255)
    brand_id: Optional[int] = None
    category_id: Optional[int] = None
    price: Optional[Decimal] = Field(default=None, ge=0)


class ProductResponse(BaseModel):
    product_id: int
    name: str
    brand_id: int
    category_id: int
    price: Decimal

    # Pydantic v2: allow loading from ORM objects.
    # `orm_mode` is kept for compatibility with older FastAPI/Pydantic examples.
    model_config = ConfigDict(from_attributes=True, orm_mode=True)

