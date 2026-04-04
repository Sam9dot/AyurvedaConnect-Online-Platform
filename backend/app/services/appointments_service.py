from __future__ import annotations

from typing import List, Optional

from sqlalchemy.orm import Session

from ..models.ayurveda_models import Appointments, Doctors, Users, WellnessCenters
from ..schemas.appointments import AppointmentCreate


def _require_exists(obj: Optional[object], entity_name: str) -> None:
    if obj is None:
        raise ValueError(f"{entity_name} not found.")


def create_appointment(db: Session, payload: AppointmentCreate, user_id: int) -> Appointments:
    # `user_id` is derived from the JWT (prevents user spoofing).
    _require_exists(db.query(Users).filter(Users.user_id == user_id).first(), "User")
    _require_exists(db.query(Doctors).filter(Doctors.doctor_id == payload.doctor_id).first(), "Doctor")
    _require_exists(
        db.query(WellnessCenters).filter(WellnessCenters.center_id == payload.center_id).first(),
        "Wellness center",
    )

    appointment = Appointments(
        user_id=user_id,
        doctor_id=payload.doctor_id,
        center_id=payload.center_id,
        appointment_date=payload.appointment_date,
    )
    db.add(appointment)
    db.commit()
    db.refresh(appointment)
    return appointment


def list_appointments_by_user(db: Session, user_id: int) -> List[Appointments]:
    return (
        db.query(Appointments)
        .filter(Appointments.user_id == user_id)
        .order_by(Appointments.appointment_date.desc())
        .all()
    )

