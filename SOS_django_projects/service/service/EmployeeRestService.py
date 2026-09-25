from service.dao.EmployeeRestDAO import EmployeeRestDAO
from service.service.BaseService import BaseService


class EmployeeRestService(BaseService):
    def get_dao(self):
        return EmployeeRestDAO()