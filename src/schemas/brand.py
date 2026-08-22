from uuid import UUID

from pydantic import BaseModel


class Brand(BaseModel):
    """
    Represents a certain brand of a product.
    """

    id: UUID
    name: str
