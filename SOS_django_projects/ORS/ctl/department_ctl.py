from django.shortcuts import render

from ORS.ctl.BaseCtl import BaseCtl
from ORS.utility.HtmlUtility import HtmlUtility
from service.models import Department
from service.service.DepartmentService import DepartmentService
from service.utility.DataValidator import DataValidator


class DepartmentCtl(BaseCtl):

    def preload(self, request):
        status_list = [ "Active", "Inactive", "Closed", "Under Review"]
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
        print('R2F =====================>', self.form["id"])
        self.form["department_id"] = request.get("departmentId", 0)
        self.form["department_code"] = request.get("departmentCode", "")
        self.form["department_name"] = request.get("departmentName", "")
        self.form["manager_name"] = request.get("managerName", "")
        print("Manager Name =================>", repr(self.form["manager_name"]))
        self.form["status"] = request.get("status", "")

    # Populate Form from Model
    def model_to_form(self, obj):
        if obj == None:
            return
        self.form["id"] = obj.id
        # print('M2F======================>', self.form["id"])
        self.form["department_id"] = obj.department_id
        self.form["department_code"] = obj.department_code
        self.form["department_name"] = obj.department_name
        self.form["manager_name"] = obj.manager_name
        self.form["status"] = obj.status
        print('M2F======================>', self.form["status"])


    # Convert form into module
    def form_to_model(self, obj):
        pk = int(self.form.get("id", 0))
        if pk > 0:
            obj.id = pk
        print('F2M======================>', obj.id)
        obj.department_id = int(self.form.get("department_id", 0))
        obj.department_code = self.form.get("department_code", "")
        obj.department_name = self.form.get("department_name", "")
        obj.manager_name = self.form.get("manager_name", "")
        obj.status = self.form.get("status", "")
        return obj

    # Validate form
    def input_validation(self):
        super().input_validation()
        inputError = self.form["inputError"]
        if DataValidator.isNull(self.form["department_id"]):
            inputError["department_id"] = "Department Id is required"
            self.form["error"] = True
        if DataValidator.isNull(self.form["department_code"]):
            inputError["department_code"] = "Department Code is required"
            self.form["error"] = True
        if DataValidator.isNull(self.form["department_name"]):
            inputError["department_name"] = "Department Name is required"
            self.form["error"] = True
        if DataValidator.isNull(self.form["manager_name"]):
            inputError["manager_name"] = "Manager Name is required"
            self.form["error"] = True
        if DataValidator.isNull(self.form["status"]):
            inputError["status"] = "Status is required"
            self.form["error"] = True
        return self.form["error"]

    # Display Role page
    def display(self, request, params={}):
        if params["id"] > 0:
            department = self.get_service().get(params["id"])
            self.model_to_form(department)
        return render(
            request,
            self.get_template(),
            {"form": self.form, "preload_data": self.preload(request)},
        )

    # Submit Role page
    def submit(self, request, _params={}):
        department = self.form_to_model(Department())
        self    .get_service().save(department)
        if int(self.form["id"]) > 0:
            self.form["id"] = department.id
        self.form["error"] = False
        self.form["message"] = "Data is saved"
        return render(
            request,
            self.get_template(),
            {"form": self.form, "preload_data": self.preload(request)},
        )

    # Template html of Role page
    def get_template(self):
        return "ors/department.html"

    # Service of Role
    def get_service(self):
        return DepartmentService()
