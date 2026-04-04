from __future__ import annotations

import os
from pathlib import Path
from typing import Generator

from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
import logging
from sqlalchemy.exc import OperationalError

# Load environment variables from `backend/.env` (works regardless of CWD).
BASE_DIR = Path(__file__).resolve().parents[1]
load_dotenv(dotenv_path=BASE_DIR / ".env", override=False)

# If `DATABASE_URL` is provided, it takes precedence. Otherwise we build a MySQL DSN
# from individual DB_* variables. Defaults are placeholders so the project boots.
if os.getenv("DATABASE_URL"):
    DATABASE_URL = os.environ["DATABASE_URL"]
else:
    DB_HOST = os.getenv("DB_HOST", "HOST")
    DB_PORT = os.getenv("DB_PORT", "3306")
    DB_NAME = os.getenv("DB_NAME", "DBNAME")
    DB_USER = os.getenv("DB_USER", "USER")
    DB_PASSWORD = os.getenv("DB_PASSWORD", "PASSWORD")
    DATABASE_URL = f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

engine = create_engine(
    DATABASE_URL,
    pool_pre_ping=True,
    pool_recycle=3600,
    future=True,
)

SessionLocal = sessionmaker(
    bind=engine,
    autocommit=False,
    autoflush=False,
    future=True,
)

Base = declarative_base()

logger = logging.getLogger(__name__)


def get_db() -> Generator:
    """
    FastAPI dependency that provides a SQLAlchemy session.

    Usage:
      from fastapi import Depends
      db = Depends(get_db)
    """

    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def init_db() -> None:
    """
    Create database tables based on the registered SQLAlchemy models.

    Note: this relies on importing model modules before calling this function.
    """

    try:
        Base.metadata.create_all(bind=engine)
    except OperationalError as exc:
        # Keep the app bootable even if credentials/DB are not available yet.
        # In production you may want to fail hard instead.
        logger.warning("Skipping DB table creation (MySQL not reachable): %s", exc)
    except Exception:
        # Unexpected errors should still show a stack trace.
        logger.exception("Failed to create DB tables via Base.metadata.create_all()")

