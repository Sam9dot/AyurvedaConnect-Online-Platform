from __future__ import annotations

import os
from typing import List

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# Importing models registers them with `Base.metadata`.
from . import models  # noqa: F401
from .database import init_db
from .routes.auth import router as auth_router
from .routes.appointments import router as appointments_router
from .routes.doctors import router as doctors_router
from .routes.orders import router as orders_router
from .routes.products import router as products_router
from .routes.reviews import router as reviews_router
from .routes.wellness import router as wellness_router
from .routes.admin import router as admin_router

app = FastAPI(title="AyurvedaConnect", version="0.1.0")


def _parse_csv_env(value: str) -> List[str]:
    return [v.strip() for v in value.split(",") if v.strip()]


allow_origins = os.getenv("CORS_ALLOW_ORIGINS", "*")

app.add_middleware(
    CORSMiddleware,
    allow_origins=_parse_csv_env(allow_origins),
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def root() -> dict:
    return {"message": "AyurvedaConnect backend is running."}


@app.get("/health")
def health() -> dict:
    # Intentionally no DB connectivity test here; the goal is to keep the app boot-safe
    # even when credentials/DB are not configured yet.
    return {"status": "ok"}


@app.on_event("startup")
def on_startup() -> None:
    # Creates tables from `Base.metadata` after model import.
    init_db()


app.include_router(auth_router)
app.include_router(doctors_router)
app.include_router(appointments_router)
app.include_router(products_router)
app.include_router(orders_router)
app.include_router(reviews_router)
app.include_router(wellness_router)
app.include_router(admin_router)

