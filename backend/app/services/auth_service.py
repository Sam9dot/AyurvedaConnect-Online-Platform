from __future__ import annotations

import os
from datetime import datetime, timedelta, timezone
from typing import Any, Dict, Optional

from jose import jwt
from passlib.context import CryptContext
from sqlalchemy.orm import Session

from ..models.ayurveda_models import Users

# Password hashing using bcrypt
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def hash_password(password: str) -> str:
    return pwd_context.hash(password)


def verify_password(password: str, password_hash: str) -> bool:
    return pwd_context.verify(password, password_hash)


def _get_jwt_settings() -> Dict[str, Any]:
    # Loaded via `python-dotenv` in `app.database`.
    secret_key = os.getenv("JWT_SECRET_KEY", "CHANGE_ME")
    algorithm = os.getenv("JWT_ALGORITHM", "HS256")
    expire_minutes = int(os.getenv("JWT_EXPIRE_MINUTES", "60"))
    return {
        "secret_key": secret_key,
        "algorithm": algorithm,
        "expire_minutes": expire_minutes,
    }


def create_access_token(subject: str, extra_claims: Optional[Dict[str, Any]] = None) -> str:
    settings = _get_jwt_settings()
    now = datetime.now(timezone.utc)
    expire = now + timedelta(minutes=settings["expire_minutes"])

    payload: Dict[str, Any] = {
        "sub": subject,
        "iat": int(now.timestamp()),
        "exp": int(expire.timestamp()),
    }
    if extra_claims:
        payload.update(extra_claims)

    return jwt.encode(payload, settings["secret_key"], algorithm=settings["algorithm"])


def decode_token(token: str) -> Dict[str, Any]:
    settings = _get_jwt_settings()
    return jwt.decode(token, settings["secret_key"], algorithms=[settings["algorithm"]])


def get_user_by_email(db: Session, email: str) -> Optional[Users]:
    return db.query(Users).filter(Users.email == email).first()


def get_user_by_id(db: Session, user_id: int) -> Optional[Users]:
    return db.query(Users).filter(Users.user_id == user_id).first()

