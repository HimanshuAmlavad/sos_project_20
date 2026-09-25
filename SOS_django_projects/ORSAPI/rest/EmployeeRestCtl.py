from ORSAPI.rest.BaseRestCtl import BaseRestCtl
from service.Serializers import EmployeeSerializers
from service.models import EmployeeRest
from service.service.EmployeeRestService import EmployeeRestService
from service.utility.DataValidator import DataValidator


class EmployeeRestCtl(BaseRestCtl):
    def get_model(self):
        return EmployeeRest

    def get_service(self):
        return EmployeeRestService()

    def get_serializer_class(self):
        return EmployeeSerializers

    def input_validation(self, data):
        errors = {}

        employee_id = data.get("employeeId", "")
        employee_name = data.get("employeeName", "")
        department = data.get("department", "")
        salary = data.get("salary", "")
        status = data.get("status", "")

        if DataValidator.isNull(employee_id):
            errors["employeeId"] = "employee Id cannot be null"
        elif not DataValidator.isMaxLength(employee_id, 20):
            errors["employeeId"] = "Employee Id cannot exceed 20 characters"

        if DataValidator.isNull(employee_name):
            errors["employeeName"] = "Employee Name cannot be null"
        elif not DataValidator.isMaxLength(employee_name, 100):
            errors["employeeName"] = "Employee Name cannot exceed 100 characters"

        if DataValidator.isNull(department):
            errors["department"] = "Department cannot be null"
        elif not DataValidator.isMaxLength(department, 50):
            errors["department"] = "Department cannot exceed 50 characters"

        if DataValidator.isNull(salary):
            errors["salary"] = "Salary cannot be null"
        elif not DataValidator.isMaxLength(salary, 10):
            errors["salary"] = "Salary cannot exceed 10 characters"

        if DataValidator.isNull(status):
            errors["status"] = "status cannot be null"
        elif not DataValidator.isMaxLength(status, 20):
            errors["status"] = "status cannot exceed 20 characters"

        return errors

