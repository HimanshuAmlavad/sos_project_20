from service.dao.BaseDAO import BaseDAO
from service.models import EmployeeRest
from service.utility.DataValidator import DataValidator


class EmployeeRestDAO(BaseDAO):
    def get_model(self):
        return EmployeeRest

    def get_Unique(self):
        return ["employeeId"]

    def populate(self, obj):
        return obj

    def get_where_conditions(self, query, params):
        value = params.get("employeeId","")
        print("value=======>",value)

        if DataValidator.isNotNull(value) and value != "":
            query = query.filter(employeeId__istartswith=value.strip())

        value = params.get("employeeName","")
        print("value=======>",value)

        if DataValidator.isNotNull(value) and value != "":
            query = query.filter(employeeName__istartswith=value.strip())

        value = params.get("department", "")
        print("value=======>",value)

        if DataValidator.isNotNull(value) and value != "":
            query = query.filter(department__istartswith=value.strip())

        value = params.get("salary", 0)
        print("value=======>",value)
        if DataValidator.isNotNull(value) and value != 0:
            query = query.filter(salary=value)

        value = params.get("status", "")
        if DataValidator.isNotNull(value) and value != "":
            query = query.filter(status__istartswith=value.strip())
        return query