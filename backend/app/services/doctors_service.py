from __future__ import annotations

from typing import List, Optional

from sqlalchemy.orm import Session

from ..models.ayurveda_models import Doctors
from ..schemas.doctors import DoctorCreate, DoctorUpdate


def list_doctors(db: Session) -> List[Doctors]:
    return db.query(Doctors).all()


def get_doctor(db: Session, doctor_id: int) -> Optional[Doctors]:
    return db.query(Doctors).filter(Doctors.doctor_id == doctor_id).first()


def create_doctor(db: Session, payload: DoctorCreate, user_id: Optional[int] = None) -> Doctors:
    doctor = Doctors(
        user_id=user_id or payload.user_id,
        name=payload.name,
        specialization=payload.specialization,
        qualification=payload.qualification,
        experience=payload.experience,
        phone=payload.phone,
        location=payload.location,
        image_url=payload.image_url,
        bio=payload.bio,
    )
    db.add(doctor)
    db.commit()
    db.refresh(doctor)
    return doctor


def update_doctor(db: Session, doctor_id: int, payload: DoctorUpdate) -> Doctors:
    doctor = db.query(Doctors).filter(Doctors.doctor_id == doctor_id).first()
    if not doctor:
        return None
    
    update_data = payload.model_dump(exclude_unset=True)
    for key, value in update_data.items():
        setattr(doctor, key, value)
    
    db.commit()
    db.refresh(doctor)
    return doctor
