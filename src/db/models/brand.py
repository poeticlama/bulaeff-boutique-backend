from typing import TYPE_CHECKING

from sqlalchemy.orm import Mapped, relationship

from src.db.models.__mixin__ import IdMixin
from src.db.models.association import products_brands
from src.db.models.base import Base

if TYPE_CHECKING:
    from src.db.models.product import Product


class Brand(Base, IdMixin):
    __tablename__ = "brands"

    name: Mapped[str]

    products: Mapped[list["Product"]] = relationship(
        secondary=products_brands,
        back_populates="brands",
    )
