from service.dao.BaseDAO import BaseDAO
from service.models import Department
from service.utility.DataValidator import DataValidator


class DepartmentDAO(BaseDAO):
    def get_model(self):
        return Department

    def get_Unique(self):
        return ["department_code", "department_name"]

    def populate(self, obj):
        return obj

    def get_where_conditions(self, query, params):
        value = params.get("department_id", 0)
        if DataValidator.isNotNull(value) and value != 0:
            query = query.filter(department_id=int(value))
        
        return query