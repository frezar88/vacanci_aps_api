from app.base_service.base_service import BaseService
from app.employment_rate.model import EmploymentRate


class EmploymentRateService(BaseService):
    model = EmploymentRate
