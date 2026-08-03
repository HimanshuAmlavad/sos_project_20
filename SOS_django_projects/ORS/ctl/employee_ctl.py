from django.shortcuts import render

from ORS.ctl.BaseCtl import BaseCtl
from ORS.utility.HtmlUtility import HtmlUtility
from service.models import Employee
from service.service.EmployeeService import EmployeeService
from service.utility.DataValidator import DataValidator

class EmployeeCtl(BaseCtl):

    def preload(self, request):
        status_list = ["Active",
                       "Inactive",
                       "On Leave",
                       "Resigned",
                       "Retired",
                       "Suspended"]
        # print("Preload status:", repr(self.form.get("status")))
        self.preload_data["status_select"] = HtmlUtility.get_list_from_list(
            "status",
            self.form.get("status"),
            status_list,
        )
        # Also make preload available under form for templates using `form.preload_data`
        self.form["preload_data"] = self.preload_data
        return self.preload_data

    # Populate Form from HTTP Request
    def request_to_form(self, request):
        self.form["id"] = int(request.get("id", 0) or 0)
        # print('R2F =====================>', self.form["id"])
        self.form["employee_id"] = request.get("employeeId", 0)
        self.form["employee_code"] = request.get("employeeCode", "")
        self.form["employee_name"] = request.get("employeeName", "")
        print('R2F =====================>', self.form["employee_name"])
        self.form["department"] = request.get("department", "")
        self.form["salary"] = request.get("salary", 0)
        self.form["status"] = request.get("status", "")

    # Populate Form from Model
    def model_to_form(self, obj):
        if obj == None:
            return
        self.form["id"] = obj.id
        # print('M2F======================>', self.form["id"])
        self.form["employee_id"] = obj.employee_id
        self.form["employee_code"] = obj.employee_code
        self.form["employee_name"] = obj.employee_Name
        print('M2F======================>', self.form["employee_name"])
        self.form["department"] = obj.department
        self.form["salary"] = obj.salary
        self.form["status"] = obj.status
        # print('M2F======================>', self.form["status"])

    # Convert form into module
    def form_to_model(self, obj):
        pk = int(self.form.get("id", 0))
        if pk > 0:
            obj.id = pk
        print('F2M======================>', obj.id)
        obj.employee_id = int(self.form.get("employee_id", 0))
        obj.employee_code = self.form.get("employee_code", "")
        obj.employee_Name = self.form.get("employee_name", "")
        print('F2M======================>', obj.employee_Name)
        obj.department = self.form.get("department", "")
        obj.salary = self.form.get("salary", "")
        obj.status = self.form.get("status", "")
        return obj

    # Validate form
    def input_validation(self):
        super().input_validation()
        inputError = self.form["inputError"]
        if DataValidator.isNull(self.form["employee_id"]):
            inputError["employee_id"] = "Employee Id is required"
            self.form["error"] = True
        if DataValidator.isNull(self.form["employee_code"]):
            inputError["employee_code"] = "Employee Code is required"
            self.form["error"] = True
        if DataValidator.isNull(self.form["employee_name"]):
            inputError["employee_name"] = "Employee Name is required"
            self.form["error"] = True
        if DataValidator.isNull(self.form["department"]):
            inputError["department"] = "Department is required"
            self.form["error"] = True
        if DataValidator.isNull(self.form["salary"]):
            inputError["salary"] = "Salary is required"
            self.form["error"] = True
        if DataValidator.isNull(self.form["status"]):
            inputError["status"] = "Status is required"
            self.form["error"] = True
        return self.form["error"]

    # Display Role page
    def display(self, request, params={}):
        if params["id"] > 0:
            employee = self.get_service().get(params["id"])
            self.model_to_form(employee)
        return render(
            request,
            self.get_template(),
            {"form": self.form, "preload_data": self.preload(request)},
        )

    # Submit Role page
    def submit(self, request, _params={}):
        employee = self.form_to_model(Employee())
        self.get_service().save(employee)
        if int(self.form["id"]) > 0:
            self.form["id"] = employee.id
        self.form["error"] = False
        self.form["message"] = "Data is saved"
        return render(
            request,
            self.get_template(),
            {"form": self.form, "preload_data": self.preload(request)},
        )

    # Template html of Role page
    def get_template(self):
        return "ors/employee.html"

    # Service of Role
    def get_service(self):
        return EmployeeService()
