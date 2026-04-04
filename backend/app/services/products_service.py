from __future__ import annotations

from typing import List, Optional

from sqlalchemy.orm import Session

from ..models.ayurveda_models import Products


def list_products(db: Session) -> List[Products]:
    return db.query(Products).all()


def get_product(db: Session, product_id: int) -> Optional[Products]:
    return db.query(Products).filter(Products.product_id == product_id).first()

