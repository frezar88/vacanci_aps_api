from app.base_service.base_service import BaseService
from app.users.model import Users


class UserService(BaseService):
    model = Users
