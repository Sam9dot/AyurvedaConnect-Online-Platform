"""Pydantic schemas live here."""

from .appointments import (  # noqa: F401
    AppointmentCreate,
    AppointmentResponse,
    AppointmentUpdate,
)
from .doctors import DoctorCreate, DoctorResponse, DoctorUpdate  # noqa: F401
from .orders import OrderCreate, OrderResponse, OrderUpdate  # noqa: F401
from .products import (  # noqa: F401
    ProductCreate,
    ProductResponse,
    ProductUpdate,
)
from .reviews import ReviewCreate, ReviewResponse, ReviewUpdate  # noqa: F401
from .users import UserCreate, UserResponse, UserUpdate  # noqa: F401
from .auth import LoginRequest, TokenResponse  # noqa: F401

__all__ = [
    "UserCreate",
    "UserUpdate",
    "UserResponse",
    "DoctorCreate",
    "DoctorUpdate",
    "DoctorResponse",
    "AppointmentCreate",
    "AppointmentUpdate",
    "AppointmentResponse",
    "ProductCreate",
    "ProductUpdate",
    "ProductResponse",
    "OrderCreate",
    "OrderUpdate",
    "OrderResponse",
    "ReviewCreate",
    "ReviewUpdate",
    "ReviewResponse",
    "LoginRequest",
    "TokenResponse",
]

