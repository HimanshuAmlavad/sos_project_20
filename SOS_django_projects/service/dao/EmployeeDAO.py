from service.dao.BaseDAO import BaseDAO
from service.models import Employee


class EmployeeDAO(BaseDAO):
    def get_model(self):
        return Employee

    def get_Unique(self):
        return ["employee_id"]

    def populate(self, obj):
        return obj