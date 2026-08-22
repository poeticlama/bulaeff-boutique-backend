from fastapi import APIRouter, Response

router = APIRouter()


@router.get("/health")
async def health_check():
    return {"status": "ok"}
