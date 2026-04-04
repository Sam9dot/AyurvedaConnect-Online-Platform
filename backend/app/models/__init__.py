"""
SQLAlchemy model package.

Importing this module registers all models with `Base.metadata`.
"""

from .ayurveda_models import (  # noqa: F401
    Appointments,
    Brands,
    Doctors,
    Facilities,
    OrderItems,
    Orders,
    ProductCategories,
    Products,
    Reviews,
    Users,
    WellnessCenters,
)

__all__ = [
    "Users",
    "Doctors",
    "WellnessCenters",
    "Facilities",
    "Appointments",
    "ProductCategories",
    "Brands",
    "Products",
    "Orders",
    "OrderItems",
    "Reviews",
]

