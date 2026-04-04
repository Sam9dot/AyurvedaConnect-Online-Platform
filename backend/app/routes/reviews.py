from __future__ import annotations

from typing import List

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from ..database import get_db
from ..dependencies.auth import get_current_user
from ..models.ayurveda_models import Reviews, Users
from ..schemas.reviews import ReviewCreate, ReviewResponse
from ..services.reviews_service import create_review, list_reviews_by_target

router = APIRouter(prefix="/reviews", tags=["reviews"])


@router.post("", response_model=ReviewResponse, status_code=status.HTTP_201_CREATED)
def create_new_review(
    payload: ReviewCreate,
    db: Session = Depends(get_db),
    current_user: Users = Depends(get_current_user),
) -> Reviews:
    if payload.user_id != current_user.user_id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="You can only create reviews for yourself.",
        )

    try:
        return create_review(db, payload=payload, user_id=current_user.user_id)
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e)) from e


@router.get("/{target_id}", response_model=List[ReviewResponse])
def get_reviews_for_target(
    target_id: int,
    db: Session = Depends(get_db),
) -> List[Reviews]:
    return list_reviews_by_target(db, target_id=target_id)

