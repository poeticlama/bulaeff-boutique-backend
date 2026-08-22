from fastapi import APIRouter

router = APIRouter(prefix="products")


@router.get("")
async def get_products():
    pass


@router.get("/{id}")
async def get_product():
    pass
