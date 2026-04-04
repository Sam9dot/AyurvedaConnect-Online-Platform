"""
Migration helper — adds new columns to existing doctors and wellness_centers tables.
Safe to run multiple times.
"""
from __future__ import annotations
import os
from pathlib import Path
from dotenv import load_dotenv
from sqlalchemy import create_engine, text

BASE_DIR = Path(__file__).resolve().parent
load_dotenv(dotenv_path=BASE_DIR / ".env", override=False)

if os.getenv("DATABASE_URL"):
    DATABASE_URL = os.environ["DATABASE_URL"]
else:
    DB_HOST = os.getenv("DB_HOST", "localhost")
    DB_PORT = os.getenv("DB_PORT", "3306")
    DB_NAME = os.getenv("DB_NAME", "ayurvedaconnect")
    DB_USER = os.getenv("DB_USER", "USER")
    DB_PASSWORD = os.getenv("DB_PASSWORD", "PASSWORD")
    DATABASE_URL = f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

engine = create_engine(DATABASE_URL)

MIGRATIONS = [
    # Doctors table — new columns
    "ALTER TABLE doctors ADD COLUMN name VARCHAR(255) NOT NULL DEFAULT ''",
    "ALTER TABLE doctors ADD COLUMN experience VARCHAR(50)",
    "ALTER TABLE doctors ADD COLUMN phone VARCHAR(30)",
    "ALTER TABLE doctors ADD COLUMN location VARCHAR(255)",
    "ALTER TABLE doctors ADD COLUMN image_url TEXT",
    "ALTER TABLE doctors ADD COLUMN daily_footfall VARCHAR(20)",
    "ALTER TABLE doctors ADD COLUMN bio TEXT",
    "ALTER TABLE doctors ADD COLUMN rating DECIMAL(3,1) DEFAULT 4.5",
    "ALTER TABLE doctors MODIFY COLUMN user_id INTEGER NULL",
    # Wellness centers table — new columns
    "ALTER TABLE wellness_centers ADD COLUMN center_type VARCHAR(30) NOT NULL DEFAULT 'wellness'",
    "ALTER TABLE wellness_centers ADD COLUMN experience VARCHAR(50)",
    "ALTER TABLE wellness_centers ADD COLUMN daily_footfall VARCHAR(20)",
    "ALTER TABLE wellness_centers ADD COLUMN image_url TEXT",
    "ALTER TABLE wellness_centers ADD COLUMN phone VARCHAR(30)",
    "ALTER TABLE wellness_centers ADD COLUMN services TEXT",
    "ALTER TABLE wellness_centers ADD COLUMN rating DECIMAL(3,1) DEFAULT 4.5",
    # Make center_id nullable on appointments
    "ALTER TABLE appointments MODIFY COLUMN center_id INTEGER NULL",
]

def main():
    print(f"Connecting to: {DATABASE_URL.split('@')[-1]}")
    with engine.connect() as conn:
        for sql in MIGRATIONS:
            try:
                conn.execute(text(sql))
                conn.commit()
                print(f"  OK  {sql[:70]}...")
            except Exception as exc:
                msg = str(exc).lower()
                if "duplicate column" in msg or "already exists" in msg:
                    print(f"  --  already exists, skip")
                else:
                    print(f"  !!  {exc}")
    print("Migration complete.")

if __name__ == "__main__":
    main()
