import os
import sys
from decimal import Decimal
from pathlib import Path
from passlib.context import CryptContext

# Adjust path to import backend modules
BASE_DIR = Path(__file__).resolve().parent
sys.path.append(str(BASE_DIR))

from app.database import SessionLocal, init_db
from app.models.ayurveda_models import Users, ProductCategories, Brands, Products

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

FALLBACK_PRODUCTS = [
    { "name": "Ashwagandha Capsules", "price": "899", "category": "Supplements" },
    { "name": "Triphala Powder", "price": "549", "category": "Powders" },
    { "name": "Brahmi Hair Oil", "price": "649", "category": "Oils" },
    { "name": "Turmeric Golden Milk Mix", "price": "450", "category": "Drinks" },
    { "name": "Neem Face Wash", "price": "350", "category": "Skincare" },
    { "name": "Amla Vitamin C Tablets", "price": "299", "category": "Supplements" },
    { "name": "Chyawanprash (500g)", "price": "599", "category": "Tonics" },
    { "name": "Kumkumadi Face Oil", "price": "1299", "category": "Skincare" },
    { "name": "Shatavari Capsules", "price": "799", "category": "Supplements" },
    { "name": "Moringa Leaf Powder", "price": "399", "category": "Powders" },
]

def seed_db():
    print("Connecting to NeonDB explicitly...")
    db = SessionLocal()
    
    # 1. Seed brand
    brand = db.query(Brands).first()
    if not brand:
        brand = Brands(brand_name="AyurvedaConnect Essentials")
        db.add(brand)
        db.commit()
        db.refresh(brand)
        
    # 2. Seed Categories
    category_map = {}
    for p in FALLBACK_PRODUCTS:
        cat_name = p["category"]
        if cat_name not in category_map:
            cat = db.query(ProductCategories).filter_by(category_name=cat_name).first()
            if not cat:
                cat = ProductCategories(category_name=cat_name)
                db.add(cat)
                db.commit()
                db.refresh(cat)
            category_map[cat_name] = cat.category_id
            
    # 3. Seed Products
    existing_products = db.query(Products).count()
    if existing_products == 0:
        for p in FALLBACK_PRODUCTS:
            prod = Products(
                name=p["name"],
                brand_id=brand.brand_id,
                category_id=category_map[p["category"]],
                price=Decimal(p["price"])
            )
            db.add(prod)
        db.commit()
        print(f"✅ inserted {len(FALLBACK_PRODUCTS)} classic Ayurveda products!")
    else:
        print("✅ Products already seeded.")
        
    # 4. Seed Test Base Users
    users_to_create = [
        {"name": "Admin Panel", "email": "admin@example.com", "role": "admin"},
        {"name": "Seller Demo", "email": "seller@example.com", "role": "seller"},
        {"name": "OTP Tester", "email": "otp_tester@example.com", "role": "patient"}
    ]
    for u in users_to_create:
        if not db.query(Users).filter_by(email=u["email"]).first():
            new_user = Users(
                name=u["name"],
                email=u["email"],
                phone="9876543210",
                user_type=u["role"],
                password_hash=pwd_context.hash("password123")
            )
            db.add(new_user)
    db.commit()
    print("✅ Seeded default test accounts (admin@example.com, seller@example.com, otp_tester@example.com | password123)")
    db.close()

if __name__ == "__main__":
    seed_db()
