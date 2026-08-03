from service.dao.BaseDAO import BaseDAO
from service.models import Department


class DepartmentDAO(BaseDAO):
    def get_model(self):
        return Department

    def get_Unique(self):
        return ["department_code", "department_name"]

    def populate(self, obj):
        return obj