from enum import StrEnum

from pydantic import BaseModel


class Currency(StrEnum):
    RUB = "rub"
    USD = "usd"
    EUR = "eur"


class Price(BaseModel):
    amount: int
    currency: Currency


class Gender(StrEnum):
    MAN = "man"
    WOMAN = "woman"
    UNISEX = "unisex"
