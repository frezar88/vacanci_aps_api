from typing import List, Optional

from fastapi import APIRouter

from app.base_schemas.base_shemas import SBaseSchemaSuccess
from app.vacancy.schemas import SVacancy, SAddVacancy, SUpdateVacancy, SSetActive, SGetVacancy
from app.vacancy.service import VacancyService

router = APIRouter(prefix="/vacancy", tags=["Вакансии"])


@router.post("/", response_model=List[SVacancy])
async def item(body: Optional[SGetVacancy]):
    data = body.model_dump()
    filters = {k: v for k, v in data.items() if v}
    record = await VacancyService().find_all(**filters)
    return record


@router.post("/add",  response_model=SBaseSchemaSuccess)
async def add_item(body: SAddVacancy):
    data = body.model_dump()
    record = await VacancyService().add_vacancy(**data)
    return record


@router.put("/update", response_model=SBaseSchemaSuccess)
async def update_item(body: SUpdateVacancy):
    data = body.model_dump()
    record = await VacancyService().update_vacancy(**data)
    return record


@router.delete("/delete", response_model=SBaseSchemaSuccess)
async def delete_item(id: int):
    record = await VacancyService().delete_one(model_id=id)
    return record


@router.put("/set_active_status", response_model=SBaseSchemaSuccess)
async def active_item(body: SSetActive):
    data = body.model_dump()
    status = await VacancyService().update_one(**data)
    return status



