from dataclasses import Field
from datetime import datetime
from typing import Optional

from pydantic import BaseModel, conint


class SItem(BaseModel):
    id: int
    name: str


class SSetActive(BaseModel):
    id: int
    active: bool


class SGetVacancy(BaseModel):
    id: Optional[conint(ge=1)] = None
    city_id: Optional[conint(ge=1)] = None
    vacancy_title_id: Optional[conint(ge=1)] = None
    work_experience_id: Optional[conint(ge=1)] = None
    employment_rate_id: Optional[conint(ge=1)] = None
    active: Optional[bool] = False


class SVacancy(BaseModel):
    id: int
    city_id: Optional[int] = None
    vacancy_title_id: Optional[int] = None
    salary: Optional[str] = None
    work_experience_id: Optional[int] = None
    employment_rate_id: Optional[int] = None
    active: Optional[bool] = None
    description: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    work_experience: Optional[SItem] = None
    employment_rate: Optional[SItem] = None
    city: Optional[SItem] = None
    vacancy_title: Optional[SItem] = None


class SUpdateVacancy(BaseModel):
    id: int
    city_id: Optional[int] = None
    vacancy_title_id: Optional[int] = None
    salary: Optional[str] = None
    work_experience_id: Optional[int] = None
    employment_rate_id: Optional[int] = None
    active: Optional[bool] = None
    description: Optional[str] = None


class SAddVacancy(BaseModel):
    city_id: conint(ge=1)
    vacancy_title_id: conint(ge=1)
    salary: str
    work_experience_id: conint(ge=1)
    employment_rate_id: conint(ge=1)
    active: bool
    description: Optional[str] = None
