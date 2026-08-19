from service.dao.BaseDAO import BaseDAO
from service.models import Employee
from service.utility.DataValidator import DataValidator


class EmployeeDAO(BaseDAO):
    def get_model(self):
        return Employee

    def get_Unique(self):
        return ["employee_id"]

    def populate(self, obj):
        return obj

    def get_where_conditions(self, query, params):
        value = params.get("employee_id", 0)
        if DataValidator.isNotNull(value) and value != 0:
            query = query.filter(employee_id=int(value))
        
        return query