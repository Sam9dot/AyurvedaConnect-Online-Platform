from __future__ import annotations

from typing import Optional

from pydantic import BaseModel, ConfigDict, Field


class ReviewCreate(BaseModel):
    user_id: int
    target_id: int
    rating: int = Field(ge=1, le=5)
    comments: Optional[str] = None


class ReviewUpdate(BaseModel):
    target_id: Optional[int] = None
    rating: Optional[int] = Field(default=None, ge=1, le=5)
    comments: Optional[str] = None


class ReviewResponse(BaseModel):
    review_id: int
    user_id: int
    target_id: int
    rating: int
    comments: Optional[str] = None

    # Pydantic v2: allow loading from ORM objects.
    # `orm_mode` is kept for compatibility with older FastAPI/Pydantic examples.
    model_config = ConfigDict(from_attributes=True, orm_mode=True)

