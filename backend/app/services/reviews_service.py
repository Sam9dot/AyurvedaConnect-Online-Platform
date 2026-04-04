from __future__ import annotations

from typing import List

from sqlalchemy.orm import Session

from ..models.ayurveda_models import Reviews, Users
from ..schemas.reviews import ReviewCreate


def create_review(db: Session, payload: ReviewCreate, user_id: int) -> Reviews:
    user = db.query(Users).filter(Users.user_id == user_id).first()
    if user is None:
        raise ValueError("User not found.")

    review = Reviews(
        user_id=user_id,
        target_id=payload.target_id,
        rating=payload.rating,
        comments=payload.comments,
    )
    db.add(review)
    db.commit()
    db.refresh(review)
    return review


def list_reviews_by_target(db: Session, target_id: int) -> List[Reviews]:
    return (
        db.query(Reviews)
        .filter(Reviews.target_id == target_id)
        .order_by(Reviews.review_id.desc())
        .all()
    )

