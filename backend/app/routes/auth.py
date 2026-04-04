from __future__ import annotations

from typing import Optional

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from ..database import get_db
from ..models.ayurveda_models import Users
from ..schemas.auth import LoginRequest, TokenResponse, OTPVerify, Login2FAResponse, OTPRequest
from ..schemas.users import UserCreate, UserResponse
from ..dependencies.auth import get_current_user
from ..services.auth_service import (
    create_access_token,
    get_user_by_email,
    get_user_by_id,
    hash_password,
    verify_password,
)

import random
from datetime import datetime, timedelta

router = APIRouter(prefix="/auth", tags=["auth"])

# Simulated OTP Store: mapping phone number -> {"otp": "123456", "expires_at": datetime}
# In a real production app, this would be Redis or a database table.
otp_store = {}


@router.post("/register", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
def register(payload: UserCreate, db: Session = Depends(get_db)) -> Users:
    existing = get_user_by_email(db, payload.email)
    if existing:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="A user with this email already exists.",
        )

    hashed_password = hash_password(payload.password_hash)
    # Derive name from email prefix if not provided
    name = payload.name if payload.name else payload.email.split("@")[0].title()
    user = Users(
        name=name,
        email=payload.email,
        phone=payload.phone,
        password_hash=hashed_password,
        user_type=payload.user_type,
    )
    db.add(user)
    db.commit()
    db.refresh(user)
    return user


@router.post("/login")
def login(payload: LoginRequest, db: Session = Depends(get_db)):
    user = get_user_by_email(db, payload.email)
    if not user or not verify_password(payload.password, user.password_hash):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid email or password.",
            headers={"WWW-Authenticate": "Bearer"},
        )
        
    return Login2FAResponse(
        status="otp_required",
        email=user.email,
        message="Please provide your mobile number for 2FA."
    )

@router.post("/send-otp")
def send_otp(payload: OTPRequest, db: Session = Depends(get_db)):
    user = get_user_by_email(db, payload.email)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
        
    # Update phone if empty or different (we trust it since they already passed password check)
    if not user.phone or user.phone != payload.phone:
        user.phone = payload.phone
        db.commit()

    # Generate a random 6-digit OTP
    otp_code = f"{random.randint(100000, 999999)}"
    
    # Store OTP with a 5-minute expiration mapped to email
    expires_at = datetime.utcnow() + timedelta(minutes=5)
    otp_store[user.email] = {"otp": otp_code, "expires_at": expires_at}
    
    # SIMULATE SMS SENDING 
    print("=" * 50)
    print(f"📠 [SIMULATED SMS] To: {user.phone} (User: {user.email})")
    print(f"💬 Message: Your AyurvedaConnect 2FA login OTP is {otp_code}. Valid for 5 minutes.")
    print("=" * 50)
    return {"message": f"OTP sent to {user.phone}"}

@router.post("/verify-otp", response_model=TokenResponse)
def verify_otp(payload: OTPVerify, db: Session = Depends(get_db)) -> TokenResponse:
    stored_data = otp_store.get(payload.email)
    
    # Validate OTP exists and is correct
    if not stored_data or stored_data["otp"] != payload.otp:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or expired OTP."
        )
    
    # Validate expiration
    if datetime.utcnow() > stored_data["expires_at"]:
        del otp_store[payload.email] # clean up
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="OTP has expired. Please log in again."
        )
    
    # Valid! Find user to issue token
    user = get_user_by_email(db, payload.email)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
        
    # Clear the OTP to prevent reuse
    del otp_store[payload.email]
    
    token = create_access_token(subject=str(user.user_id))
    return TokenResponse(
        access_token=token,
        user_type=user.user_type or "patient",
        user_name=user.name or "",
    )


@router.get("/me", response_model=UserResponse)
def me(current_user: Users = Depends(get_current_user)) -> Users:
    # Private route example protected by JWT dependency.
    return current_user
