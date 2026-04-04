from __future__ import annotations

from typing import List

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from ..database import get_db
from ..dependencies.auth import get_current_user
from ..models.ayurveda_models import Appointments, Users
from ..schemas.appointments import AppointmentCreate, AppointmentResponse
from ..services.appointments_service import create_appointment, list_appointments_by_user

router = APIRouter(prefix="/appointments", tags=["appointments"])


@router.post("", response_model=AppointmentResponse, status_code=status.HTTP_201_CREATED)
def create_new_appointment(
    payload: AppointmentCreate,
    db: Session = Depends(get_db),
    current_user: Users = Depends(get_current_user),
) -> Appointments:
    # Admin users cannot book appointments
    if current_user.user_type == "admin":
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Admin users cannot book appointments. Admins can only view appointments.",
        )
    
    if payload.user_id != current_user.user_id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="You can only create appointments for yourself.",
        )

    try:
        return create_appointment(db, payload=payload, user_id=current_user.user_id)
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e)) from e


@router.get("/user", response_model=List[AppointmentResponse])
def get_appointments_for_user(
    db: Session = Depends(get_db),
    current_user: Users = Depends(get_current_user),
) -> List[Appointments]:
    return list_appointments_by_user(db, user_id=current_user.user_id)


@router.get("/all", response_model=List[AppointmentResponse])
def get_all_appointments(
    db: Session = Depends(get_db),
    current_user: Users = Depends(get_current_user),
) -> List[Appointments]:
    # Only admin users can view all appointments
    if current_user.user_type != "admin":
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Admin access required to view all appointments.",
        )
    
    return db.query(Appointments).all()

