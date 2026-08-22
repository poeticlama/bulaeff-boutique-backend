from enum import StrEnum
from typing import Annotated
from uuid import UUID

from pydantic import BaseModel, StringConstraints

from src.schemas.brand import Brand
from src.schemas.shared import Gender, Price

Article = Annotated[str, StringConstraints(min_length=6, max_length=6, to_upper=True)]


class ProductType(StrEnum):
    BAG = "bag"
    CLOTH = "cloth"
    SHOES = "shoes"
    ACCESSORY = "accessory"


class BaseProduct(BaseModel):
    """
    Represents a product instance.
    """

    id: UUID
    name: str
    article: Article
    type: ProductType
    brands: list[Brand]
    price: Price
    color: str | None = None
    gender: Gender
    size: str
    measurements: dict[str, int | float] | None = None
