from enum import StrEnum

from pydantic import BaseModel


class CurrencyEnum(StrEnum):
    RUB = "rub"
    USD = "usd"
    EUR = "eur"


class Price(BaseModel):
    amount: int
    currency: CurrencyEnum


class GenderEnum(StrEnum):
    MAN = "man"
    WOMAN = "woman"
    UNISEX = "unisex"
