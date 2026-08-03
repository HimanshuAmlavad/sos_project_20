from service.dao.FeeDAO import FeeDAO
from service.service.BaseService import BaseService


class FeeService(BaseService):
    def get_dao(self):
        return FeeDAO()