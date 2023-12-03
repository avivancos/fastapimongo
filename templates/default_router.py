from fastapi import APIRouter
from .models import %_name_%

router = APIRouter()

@router.get("/")
async def read_items():
    return [{"name": "item1"}, {"name": "item2"}]