from typing import List
from fastapi import APIRouter
from app.base_schemas.base_shemas import SBaseSchemaMenu, SBaseSchemaAddMenu, SBaseSchemaSuccess
from app.city.service import CityService
from app.employment_rate.service import EmploymentRateService

router = APIRouter(prefix="/employment_rate", tags=["Уровень занятости"])


@router.get("/", response_model=List[SBaseSchemaMenu])
async def item():
    record = await EmploymentRateService().find_all(**{})
    return record


@router.post("/", response_model=SBaseSchemaSuccess)
async def add_item(body: SBaseSchemaAddMenu):
    data = body.model_dump()
    record = await EmploymentRateService().add_one_return_id(**data)
    return record


@router.put("/", response_model=SBaseSchemaSuccess)
async def update_item(body: SBaseSchemaMenu):
    data = body.model_dump()
    record = await EmploymentRateService().update_one(**data)
    return record


@router.delete("/", response_model=SBaseSchemaSuccess)
async def delete_item(id: int):
    record = await EmploymentRateService().delete_one(model_id=id)
    return record
