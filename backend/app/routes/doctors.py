from __future__ import annotations

from typing import List, Optional

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from ..database import get_db
from ..models.ayurveda_models import Doctors, Users
from ..schemas.doctors import DoctorCreate, DoctorResponse, DoctorUpdate
from ..services.doctors_service import get_doctor, list_doctors, create_doctor, update_doctor
from ..dependencies.auth import get_current_user

router = APIRouter(prefix="/doctors", tags=["doctors"])


@router.get("", response_model=List[DoctorResponse])
def get_all_doctors(db: Session = Depends(get_db)) -> List[Doctors]:
    return list_doctors(db)


@router.get("/{doctor_id}", response_model=DoctorResponse)
def get_doctor_by_id(doctor_id: int, db: Session = Depends(get_db)) -> Doctors:
    doctor = get_doctor(db, doctor_id)
    if not doctor:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Doctor not found.")
    return doctor


@router.post("", response_model=DoctorResponse, status_code=status.HTTP_201_CREATED)
def create_doctor_profile(
    payload: DoctorCreate, 
    db: Session = Depends(get_db),
    current_user: Users = Depends(get_current_user)
) -> Doctors:
    # Check if doctor profile already exists for this user
    existing = db.query(Doctors).filter(Doctors.user_id == current_user.user_id).first()
    if existing:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Doctor profile already exists for this user."
        )
    return create_doctor(db, payload, current_user.user_id)


@router.put("/{doctor_id}", response_model=DoctorResponse)
def update_doctor_profile(
    doctor_id: int,
    payload: DoctorUpdate,
    db: Session = Depends(get_db),
    current_user: Users = Depends(get_current_user)
) -> Doctors:
    doctor = get_doctor(db, doctor_id)
    if not doctor:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Doctor not found.")
    
    # Only allow doctor to update their own profile or admin
    if doctor.user_id != current_user.user_id and current_user.user_type != "admin":
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Not authorized.")
    
    return update_doctor(db, doctor_id, payload)


@router.get("/my/profile", response_model=DoctorResponse)
def get_my_doctor_profile(
    db: Session = Depends(get_db),
    current_user: Users = Depends(get_current_user)
) -> Doctors:
    doctor = db.query(Doctors).filter(Doctors.user_id == current_user.user_id).first()
    if not doctor:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Doctor profile not found.")
    return doctor
