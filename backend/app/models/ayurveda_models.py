from __future__ import annotations

from sqlalchemy import (
    CheckConstraint,
    Column,
    DateTime,
    ForeignKey,
    Integer,
    Numeric,
    String,
    Text,
    func,
)
from sqlalchemy.orm import relationship

from ..database import Base


class Users(Base):
    __tablename__ = "users"

    user_id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String(255), nullable=False)
    email = Column(String(255), unique=True, nullable=False, index=True)
    phone = Column(String(30))
    password_hash = Column(String(255), nullable=False)
    user_type = Column(String(20), nullable=False, default="patient")

    doctor = relationship(
        "Doctors",
        back_populates="user",
        uselist=False,
        cascade="all, delete-orphan",
        passive_deletes=True,
    )
    appointments = relationship(
        "Appointments",
        back_populates="user",
        cascade="all, delete-orphan",
        passive_deletes=True,
    )
    orders = relationship(
        "Orders",
        back_populates="user",
        cascade="all, delete-orphan",
        passive_deletes=True,
    )
    reviews = relationship(
        "Reviews",
        back_populates="user",
        cascade="all, delete-orphan",
        passive_deletes=True,
    )

    def __repr__(self) -> str:
        return f"Users(user_id={self.user_id!r}, email={self.email!r})"


class Doctors(Base):
    __tablename__ = "doctors"

    doctor_id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    user_id = Column(
        Integer,
        ForeignKey("users.user_id", ondelete="CASCADE"),
        unique=True,
        nullable=True,
        index=True,
    )
    name = Column(String(255), nullable=False, default="")
    specialization = Column(String(255), nullable=False)
    qualification = Column(Text)
    experience = Column(String(50))
    phone = Column(String(30))
    location = Column(String(255))
    image_url = Column(Text)
    daily_footfall = Column(String(20))
    bio = Column(Text)
    rating = Column(Numeric(3, 1), default=4.5)

    user = relationship("Users", back_populates="doctor")
    appointments = relationship(
        "Appointments",
        back_populates="doctor",
        cascade="all, delete-orphan",
        passive_deletes=True,
    )

    def __repr__(self) -> str:
        return (
            f"Doctors(doctor_id={self.doctor_id!r}, "
            f"name={self.name!r}, specialization={self.specialization!r})"
        )


class WellnessCenters(Base):
    __tablename__ = "wellness_centers"

    center_id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String(255), nullable=False)
    location = Column(String(255), nullable=False)
    amenities = Column(Text)
    center_type = Column(String(30), nullable=False, default="wellness")
    experience = Column(String(50))
    daily_footfall = Column(String(20))
    image_url = Column(Text)
    phone = Column(String(30))
    services = Column(Text)
    rating = Column(Numeric(3, 1), default=4.5)

    facilities = relationship(
        "Facilities",
        back_populates="center",
        cascade="all, delete-orphan",
        passive_deletes=True,
    )
    appointments = relationship(
        "Appointments",
        back_populates="center",
        cascade="all, delete-orphan",
        passive_deletes=True,
    )

    def __repr__(self) -> str:
        return f"WellnessCenters(center_id={self.center_id!r}, name={self.name!r})"


class Facilities(Base):
    __tablename__ = "facilities"

    facility_id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    center_id = Column(
        Integer,
        ForeignKey("wellness_centers.center_id", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )
    name = Column(String(255), nullable=False)
    description = Column(Text)

    center = relationship("WellnessCenters", back_populates="facilities")

    def __repr__(self) -> str:
        return (
            f"Facilities(facility_id={self.facility_id!r}, center_id={self.center_id!r}, "
            f"name={self.name!r})"
        )


class Appointments(Base):
    __tablename__ = "appointments"

    appointment_id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    user_id = Column(
        Integer,
        ForeignKey("users.user_id", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )
    doctor_id = Column(
        Integer,
        ForeignKey("doctors.doctor_id", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )
    center_id = Column(
        Integer,
        ForeignKey("wellness_centers.center_id", ondelete="CASCADE"),
        nullable=True,
        index=True,
    )
    appointment_date = Column(DateTime(timezone=True), nullable=False)

    user = relationship("Users", back_populates="appointments")
    doctor = relationship("Doctors", back_populates="appointments")
    center = relationship("WellnessCenters", back_populates="appointments")

    def __repr__(self) -> str:
        return (
            "Appointments("
            f"appointment_id={self.appointment_id!r}, user_id={self.user_id!r}, "
            f"doctor_id={self.doctor_id!r}, center_id={self.center_id!r}, "
            f"appointment_date={self.appointment_date!r})"
        )


class ProductCategories(Base):
    __tablename__ = "product_categories"

    category_id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    category_name = Column(String(255), unique=True, nullable=False, index=True)

    products = relationship(
        "Products",
        back_populates="category",
        cascade="all, delete-orphan",
        passive_deletes=True,
    )

    def __repr__(self) -> str:
        return f"ProductCategories(category_id={self.category_id!r}, name={self.category_name!r})"


class Brands(Base):
    __tablename__ = "brands"

    brand_id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    brand_name = Column(String(255), unique=True, nullable=False, index=True)

    products = relationship(
        "Products",
        back_populates="brand",
        cascade="all, delete-orphan",
        passive_deletes=True,
    )

    def __repr__(self) -> str:
        return f"Brands(brand_id={self.brand_id!r}, brand_name={self.brand_name!r})"


class Products(Base):
    __tablename__ = "products"

    product_id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String(255), nullable=False)
    brand_id = Column(
        Integer,
        ForeignKey("brands.brand_id", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )
    category_id = Column(
        Integer,
        ForeignKey("product_categories.category_id", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )
    price = Column(Numeric(10, 2), nullable=False)

    brand = relationship("Brands", back_populates="products")
    category = relationship("ProductCategories", back_populates="products")
    order_items = relationship(
        "OrderItems",
        back_populates="product",
        cascade="all, delete-orphan",
        passive_deletes=True,
    )

    def __repr__(self) -> str:
        return (
            f"Products(product_id={self.product_id!r}, name={self.name!r}, "
            f"price={self.price!r})"
        )


class Orders(Base):
    __tablename__ = "orders"

    order_id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    user_id = Column(
        Integer,
        ForeignKey("users.user_id", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )
    total_amount = Column(Numeric(10, 2), nullable=False)
    status = Column(String(50), nullable=False, default="pending")
    tracking_status = Column(String(50), nullable=False, default="placed")
    estimated_delivery = Column(String(100))
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    user = relationship("Users", back_populates="orders")
    items = relationship(
        "OrderItems",
        back_populates="order",
        cascade="all, delete-orphan",
        passive_deletes=True,
    )

    def __repr__(self) -> str:
        return (
            f"Orders(order_id={self.order_id!r}, user_id={self.user_id!r}, "
            f"status={self.status!r}, total_amount={self.total_amount!r})"
        )


class OrderItems(Base):
    __tablename__ = "order_items"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    order_id = Column(
        Integer,
        ForeignKey("orders.order_id", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )
    product_id = Column(
        Integer,
        ForeignKey("products.product_id", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )
    quantity = Column(Integer, nullable=False)

    order = relationship("Orders", back_populates="items")
    product = relationship("Products", back_populates="order_items")

    def __repr__(self) -> str:
        return (
            f"OrderItems(id={self.id!r}, order_id={self.order_id!r}, "
            f"product_id={self.product_id!r}, quantity={self.quantity!r})"
        )


class Reviews(Base):
    __tablename__ = "reviews"

    review_id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    user_id = Column(
        Integer,
        ForeignKey("users.user_id", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )
    target_id = Column(Integer, nullable=False, index=True)
    rating = Column(Integer, nullable=False)
    comments = Column(Text)

    user = relationship("Users", back_populates="reviews")

    __table_args__ = (
        CheckConstraint("rating >= 1 AND rating <= 5", name="ck_reviews_rating_1_to_5"),
    )

    def __repr__(self) -> str:
        return (
            f"Reviews(review_id={self.review_id!r}, user_id={self.user_id!r}, "
            f"target_id={self.target_id!r}, rating={self.rating!r})"
        )
