from __future__ import annotations

from typing import Literal, Optional

from pydantic import BaseModel, EmailStr, Field


class LoginRequest(BaseModel):
    email: EmailStr
    password: str = Field(min_length=8, max_length=255)


class OTPRequest(BaseModel):
    email: EmailStr
    phone: str = Field(min_length=10, max_length=15, description="Mobile number for OTP")

class Login2FAResponse(BaseModel):
    status: Literal["otp_required"]
    email: EmailStr
    message: str


class OTPVerify(BaseModel):
    email: EmailStr
    otp: str = Field(min_length=4, max_length=6)


class TokenResponse(BaseModel):
    access_token: str
    token_type: Literal["bearer"] = "bearer"
    user_type: str = "patient"
    user_name: str = ""
