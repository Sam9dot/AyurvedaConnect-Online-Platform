from __future__ import annotations

from typing import List

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from ..database import get_db
from ..models.ayurveda_models import Users, Doctors, WellnessCenters, Products, Orders, Appointments
from ..dependencies.auth import get_current_user
from ..schemas.users import UserResponse
from ..schemas.appointments import AppointmentResponse

router = APIRouter(prefix="/admin", tags=["admin"])


def require_admin(current_user: Users = Depends(get_current_user)) -> Users:
    if current_user.user_type != "admin":
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Admin access required"
        )
    return current_user


@router.get("/users", response_model=List[UserResponse])
def get_all_users(
    db: Session = Depends(get_db),
    admin: Users = Depends(require_admin)
):
    return db.query(Users).all()


@router.get("/stats")
def get_dashboard_stats(
    db: Session = Depends(get_db),
    admin: Users = Depends(require_admin)
):
    total_users = db.query(Users).count()
    total_doctors = db.query(Doctors).count()
    total_centres = db.query(WellnessCenters).count()
    total_products = db.query(Products).count()
    total_orders = db.query(Orders).count()
    total_appointments = db.query(Appointments).count()
    
    users_by_type = {}
    for user_type in ["patient", "doctor", "seller", "wellness", "admin"]:
        count = db.query(Users).filter(Users.user_type == user_type).count()
        users_by_type[user_type] = count
    
    return {
        "total_users": total_users,
        "total_doctors": total_doctors,
        "total_centres": total_centres,
        "total_products": total_products,
        "total_orders": total_orders,
        "total_appointments": total_appointments,
        "users_by_type": users_by_type
    }


@router.delete("/users/{user_id}")
def delete_user(
    user_id: int,
    db: Session = Depends(get_db),
    admin: Users = Depends(require_admin)
):
    user = db.query(Users).filter(Users.user_id == user_id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    
    db.delete(user)
    db.commit()
    return {"message": "User deleted successfully"}


@router.delete("/doctors/{doctor_id}")
def delete_doctor(
    doctor_id: int,
    db: Session = Depends(get_db),
    admin: Users = Depends(require_admin)
):
    doctor = db.query(Doctors).filter(Doctors.doctor_id == doctor_id).first()
    if not doctor:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Doctor not found")
    
    db.delete(doctor)
    db.commit()
    return {"message": "Doctor deleted successfully"}


@router.delete("/wellness/{center_id}")
def delete_wellness_centre(
    center_id: int,
    db: Session = Depends(get_db),
    admin: Users = Depends(require_admin)
):
    centre = db.query(WellnessCenters).filter(WellnessCenters.center_id == center_id).first()
    if not centre:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Centre not found")
    
    db.delete(centre)
    db.commit()
    return {"message": "Wellness centre deleted successfully"}


@router.get("/appointments", response_model=List[AppointmentResponse])
def get_all_appointments(
    db: Session = Depends(get_db),
    admin: Users = Depends(require_admin)
):
    """Admin endpoint to view all appointments in the system"""
    return db.query(Appointments).all()
