from __future__ import annotations

from typing import List, Optional

from sqlalchemy.orm import Session

from ..models.ayurveda_models import Orders, Users
from ..schemas.orders import OrderCreate, OrderUpdate


def create_order(db: Session, payload: OrderCreate, user_id: int) -> Orders:
    user = db.query(Users).filter(Users.user_id == user_id).first()
    if user is None:
        raise ValueError("User not found.")

    order = Orders(
        user_id=user_id,
        total_amount=payload.total_amount,
        status=payload.status,
        tracking_status="placed",
    )
    db.add(order)
    db.commit()
    db.refresh(order)
    return order


def list_orders_by_user(db: Session, user_id: int) -> List[Orders]:
    return (
        db.query(Orders)
        .filter(Orders.user_id == user_id)
        .order_by(Orders.order_id.desc())
        .all()
    )


def get_order_by_id(db: Session, order_id: int) -> Optional[Orders]:
    return db.query(Orders).filter(Orders.order_id == order_id).first()


def update_order_status(db: Session, order: Orders, payload: OrderUpdate) -> Orders:
    if payload.status is not None:
        order.status = payload.status
    if payload.tracking_status is not None:
        order.tracking_status = payload.tracking_status
    if payload.estimated_delivery is not None:
        order.estimated_delivery = payload.estimated_delivery
    if payload.total_amount is not None:
        order.total_amount = payload.total_amount
    db.commit()
    db.refresh(order)
    return order
