from sqlalchemy import Enum, String
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.db.models.__mixin__ import IdMixin
from src.db.models.association import products_brands
from src.db.models.base import Base
from src.db.models.brand import Brand
from src.schemas.shared import Currency, Gender


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
    price_currency: Mapped["Currency"] = mapped_column(
        Enum(Currency),
        default=Currency.RUB,
        nullable=False,
    )

    color: Mapped[str | None]
    gender: Mapped["Gender"] = mapped_column(
        Enum(Gender),
        default=Gender.UNISEX,
        nullable=False,
    )
    size: Mapped[str | None]
    measurements: Mapped[dict[str, int | float] | None] = mapped_column(JSONB)
