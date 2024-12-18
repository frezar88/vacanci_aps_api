from app.base_service.base_service import BaseService
from app.vacancy_title.model import VacancyTitle


class VacancyTitleService(BaseService):
    model = VacancyTitle
