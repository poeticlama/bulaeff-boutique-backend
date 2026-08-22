from sqlalchemy import Column, ForeignKey, Table

from src.db.models.base import Base

products_brands = Table(
    "products_brands",
    Base.metadata,
    Column(
        "product_id",
        ForeignKey("products.id", ondelete="CASCADE"),
        primary_key=True,
    ),
    Column(
        "brand_id",
        ForeignKey("brands.id", ondelete="CASCADE"),
        primary_key=True,
    ),
)
