from typing import List

from fastapi import APIRouter

from app.base_schemas.base_shemas import SBaseSchemaMenu, SBaseSchemaAddMenu, SBaseSchemaSuccess
from app.work_experience.service import WorkExperienceService

router = APIRouter(prefix="/word_experience", tags=["Опыт работы"])


@router.get("/", response_model=List[SBaseSchemaMenu])
async def item():
    city = await WorkExperienceService().find_all(**{})
    return city


@router.post("/", response_model=SBaseSchemaSuccess)
async def add_item(body: SBaseSchemaAddMenu):
    data = body.model_dump()
    record = await WorkExperienceService().add_one_return_id(**data)
    return record


@router.put("/", response_model=SBaseSchemaSuccess)
async def update_item(body: SBaseSchemaMenu):
    data = body.model_dump()
    record = await WorkExperienceService().update_one(**data)
    return record


@router.delete("/", response_model=SBaseSchemaSuccess)
async def delete_item(id: int):
    record = await WorkExperienceService().delete_one(model_id=id)
    return record
