from sqlalchemy import String
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.db.models.__mixin__ import IdMixin
from src.db.models.association import products_brands
from src.db.models.base import Base
from src.db.models.brand import Brand
from src.schemas.shared import CurrencyEnum, GenderEnum


class Product(Base, IdMixin):
    __tablename__ = "products"

    type: Mapped[str]

    name: Mapped[str]
    article: Mapped[str | None] = mapped_column(String(6))

    brands: Mapped[list[Brand]] = relationship(
        secondary=products_brands,
        back_populates="products",
    )

    price_amount: Mapped[int]
    price_currency: Mapped["CurrencyEnum"] = mapped_column(
        default=CurrencyEnum.RUB,
        nullable=False,
    )

    color: Mapped[str | None]
    gender: Mapped["GenderEnum"] = mapped_column(
        default=GenderEnum.UNISEX,
        nullable=False,
    )
    size: Mapped[str | None]
    measurements: Mapped[dict[str, int | float] | None] = mapped_column(JSONB)
