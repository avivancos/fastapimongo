from fastapi import APIRouter, HTTPException
from typing import List
from .schemas import %_name_%Create, %_name_%Update, %_name_%
from .services import %_name_%Service

router = APIRouter()

@router.post("/", response_model=%_name_%)
async def create_%_name_%(%_name_%: %_name_%Create, service: %_name_%Service):
    return await service.create_%_name_%(%_name_%)

@router.get("/", response_model=List[%_name_%])
async def read_%_name_%s(service: %_name_%Service):
    return await service.get_%_name_%s()

@router.get("/{%_name_%_id}", response_model=%_name_%)
async def read_%_name_%(%_name_%_id: int, service: %_name_%Service):
    %_name_% = await service.get_%_name_%_by_id(%_name_%_id)
    if not %_name_%:
        raise HTTPException(status_code=404, detail="%_name_% not found")
    return %_name_%

@router.put("/{%_name_%_id}", response_model=%_name_%)
async def update_%_name_%(%_name_%_id: int, %_name_%: %_name_%Update, service: %_name_%Service):
    return await service.update_%_name_%(%_name_%_id, %_name_%)

@router.delete("/{%_name_%_id}", response_model=%_name_%)
async def delete_%_name_%(%_name_%_id: int, service: %_name_%Service):
    return await service.delete_%_name_%(%_name_%_id)