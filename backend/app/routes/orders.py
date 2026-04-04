from __future__ import annotations

from typing import List

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from ..database import get_db
from ..dependencies.auth import get_current_user
from ..models.ayurveda_models import Orders, Users
from ..schemas.orders import OrderCreate, OrderResponse, OrderUpdate
from ..services.orders_service import create_order, get_order_by_id, list_orders_by_user, update_order_status

router = APIRouter(prefix="/orders", tags=["orders"])


@router.post("", response_model=OrderResponse, status_code=status.HTTP_201_CREATED)
def create_new_order(
    payload: OrderCreate,
    db: Session = Depends(get_db),
    current_user: Users = Depends(get_current_user),
) -> Orders:
    if payload.user_id != current_user.user_id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="You can only create orders for yourself.",
        )

    try:
        return create_order(db, payload=payload, user_id=current_user.user_id)
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e)) from e


@router.get("/user", response_model=List[OrderResponse])
def get_orders_for_user(
    db: Session = Depends(get_db),
    current_user: Users = Depends(get_current_user),
) -> List[Orders]:
    return list_orders_by_user(db, user_id=current_user.user_id)


@router.get("/{order_id}", response_model=OrderResponse)
def get_order_detail(
    order_id: int,
    db: Session = Depends(get_db),
    current_user: Users = Depends(get_current_user),
) -> Orders:
    order = get_order_by_id(db, order_id=order_id)
    if not order:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Order not found.")
    if order.user_id != current_user.user_id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Not your order.")
    return order


@router.patch("/{order_id}/status", response_model=OrderResponse)
def update_order(
    order_id: int,
    payload: OrderUpdate,
    db: Session = Depends(get_db),
    current_user: Users = Depends(get_current_user),
) -> Orders:
    order = get_order_by_id(db, order_id=order_id)
    if not order:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Order not found.")
    if order.user_id != current_user.user_id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Not your order.")
    return update_order_status(db, order=order, payload=payload)
