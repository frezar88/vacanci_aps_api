from app.base_service.base_service import BaseService
from app.city.model import City


class CityService(BaseService):
    model = City
