from datetime import datetime

from sqlalchemy import select, insert, delete
from sqlalchemy.exc import IntegrityError

from app.base_service.base_service import BaseService
from app.city.model import City
from app.database import async_session_maker
from app.employment_rate.model import EmploymentRate
from app.vacancy.model import Vacancy
from app.vacancy_title.model import VacancyTitle
from app.work_experience.model import WorkExperience
from fastapi.responses import JSONResponse


class VacancyService(BaseService):
    model = Vacancy

    @classmethod
    async def check_exist_record(cls, name, record_id, model):
        async with async_session_maker() as session:
            query = select(model).filter_by(id=record_id)
            result = await session.execute(query)
            result = result.scalar_one_or_none()
            if result is None:
                return JSONResponse(status_code=404,
                                    content={"status": False, "detail": f"{name} with id {record_id} was not found"})

    @classmethod
    async def add_vacancy(cls, **data):
        data_for_check = [
            {"name": "city_id", "id": data.get('city_id'), "model": City},
            {"name": "vacancy_title_id", "id": data.get('vacancy_title_id'), "model": VacancyTitle},
            {"name": "work_experience_id", "id": data.get('work_experience_id'), "model": WorkExperience},
            {"name": "employment_rate_id", "id": data.get('employment_rate_id'), "model": EmploymentRate},
        ]
        for row in data_for_check:
            error = await cls.check_exist_record(name=row['name'], record_id=row['id'], model=row['model'])
            if error:
                return error

        status = await cls.add_one_return_id(**data)
        return status

    @classmethod
    async def update_vacancy(cls, **data):
        data_for_check = [
            {"name": "city_id", "id": data.get('city_id'), "model": City},
            {"name": "vacancy_title_id", "id": data.get('vacancy_title_id'), "model": VacancyTitle},
            {"name": "work_experience_id", "id": data.get('work_experience_id'), "model": WorkExperience},
            {"name": "employment_rate_id", "id": data.get('employment_rate_id'), "model": EmploymentRate},
        ]
        for row in data_for_check:
            error = await cls.check_exist_record(name=row['name'], record_id=row['id'], model=row['model'])
            if error:
                return error

        data_to_save = data
        data_to_save['updated_at'] = datetime.utcnow()

        status = await cls.update_one(**data)
        return status
