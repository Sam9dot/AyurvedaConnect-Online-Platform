from __future__ import annotations

from typing import List

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from pydantic import BaseModel
from typing import Optional
from decimal import Decimal

from ..database import get_db
from ..models.ayurveda_models import Products, Brands, ProductCategories
from ..schemas.products import ProductResponse
from ..services.products_service import get_product, list_products
from ..dependencies.auth import get_current_user
from ..models.ayurveda_models import Users

router = APIRouter(prefix="/products", tags=["products"])


class ProductSimpleResponse(BaseModel):
    product_id: int
    name: str
    price: Decimal
    desc: Optional[str] = None
    image_url: Optional[str] = None
    category: Optional[str] = None

    class Config:
        from_attributes = True


class ProductCreateSimple(BaseModel):
    name: str
    desc: Optional[str] = ""
    price: Decimal
    image_url: Optional[str] = ""
    category: Optional[str] = "General"


@router.get("", response_model=List[ProductSimpleResponse])
def get_all_products(db: Session = Depends(get_db)):
    rows = db.query(
        Products.product_id,
        Products.name,
        Products.price,
    ).all()
    # Enrich with category name
    results = []
    for row in rows:
        cat = db.query(ProductCategories).filter(
            ProductCategories.category_id == db.query(Products).filter(
                Products.product_id == row.product_id
            ).first().category_id
        ).first()
        p = db.query(Products).filter(Products.product_id == row.product_id).first()
        results.append(ProductSimpleResponse(
            product_id=p.product_id,
            name=p.name,
            price=p.price,
            desc="",
            image_url="",
            category=cat.category_name if cat else "General"
        ))
    return results


@router.get("/{product_id}", response_model=ProductSimpleResponse)
def get_product_by_id(product_id: int, db: Session = Depends(get_db)):
    product = get_product(db, product_id)
    if not product:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Product not found.")
    cat = db.query(ProductCategories).filter(
        ProductCategories.category_id == product.category_id
    ).first()
    return ProductSimpleResponse(
        product_id=product.product_id,
        name=product.name,
        price=product.price,
        desc="",
        image_url="",
        category=cat.category_name if cat else "General"
    )


@router.post("", response_model=ProductSimpleResponse, status_code=status.HTTP_201_CREATED)
def create_product(
    payload: ProductCreateSimple,
    db: Session = Depends(get_db),
    current_user: Users = Depends(get_current_user)
):
    # Auto-create brand if doesn't exist
    brand_name = f"{current_user.name}'s Brand" if current_user.name else "AyurvedaConnect"
    brand = db.query(Brands).filter(Brands.brand_name == brand_name).first()
    if not brand:
        brand = Brands(brand_name=brand_name)
        db.add(brand)
        db.commit()
        db.refresh(brand)

    # Auto-create category if doesn't exist
    cat_name = payload.category or "General"
    cat = db.query(ProductCategories).filter(ProductCategories.category_name == cat_name).first()
    if not cat:
        cat = ProductCategories(category_name=cat_name)
        db.add(cat)
        db.commit()
        db.refresh(cat)

    product = Products(
        name=payload.name,
        brand_id=brand.brand_id,
        category_id=cat.category_id,
        price=payload.price,
    )
    db.add(product)
    db.commit()
    db.refresh(product)

    return ProductSimpleResponse(
        product_id=product.product_id,
        name=product.name,
        price=product.price,
        desc=payload.desc,
        image_url=payload.image_url,
        category=cat_name
    )

