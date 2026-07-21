from service.dao.EmployeeDAO import EmployeeDAO
from service.service.BaseService import BaseService


class EmployeeService(BaseService):
    def get_dao(self):
        return EmployeeDAO()