from django.shortcuts import render

from ORS.ctl.BaseCtl import BaseCtl
from service.models import Branch
from service.service.BranchService import BranchService
from service.utility.DataValidator import DataValidator

class BranchCtl(BaseCtl):


    # Populate Form from HTTP Request
    def request_to_form(self, request):
        self.form["id"] = request.get("id", 0)
        # print('R2F =====================>', self.form["id"])
        self.form["branch_id"] = request.get("branchId", 0)
        self.form["branch_name"] = request.get("branchName", "")
        self.form["city"] = request.get("city", "")
        print('R2F =====================>', self.form["city"])
        self.form["manager_name"] = request.get("managerName", "")
        self.form["contact_no"] = request.get("contactNo", "")

    # Populate Form from Model
    def model_to_form(self, obj):
        if obj == None:
            return
        self.form["id"] = obj.id
        # print('M2F======================>', self.form["id"])
        self.form["branch_id"] = obj.branch_id
        self.form["branch_name"] = obj.branch_name
        self.form["city"] = obj.city
        print('M2F======================>', self.form["city"])
        self.form["manager_name"] = obj.manager_name
        self.form["contact_no"] = obj.contact_no
        # print('M2F======================>', self.form["contact_no"])

    # Convert form into module
    def form_to_model(self, obj):
        pk = int(self.form.get("id", 0))
        if pk > 0:
            obj.id = pk
        print('F2M======================>', obj.id)
        obj.branch_id = int(self.form.get("branch_id", 0))
        obj.branch_name = self.form.get("branch_name", "")
        obj.city = self.form.get("city", "")
        print('F2M======================>', obj.city)
        obj.manager_name = self.form.get("manager_name", "")
        obj.contact_no = self.form.get("contact_no", "")
        return obj

    # Validate form
    def input_validation(self):
        super().input_validation()
        inputError = self.form["inputError"]
        if DataValidator.isNull(self.form["branch_id"]):
            inputError["branch_id"] = "Branch Id is required"
            self.form["error"] = True
        if DataValidator.isNull(self.form["branch_name"]):
            inputError["branch_name"] = "Branch Name is required"
            self.form["error"] = True
        if DataValidator.isNull(self.form["city"]):
            inputError["city"] = "City is required"
            self.form["error"] = True
        if DataValidator.isNull(self.form["manager_name"]):
            inputError["manager_name"] = "Manager Name is required"
            self.form["error"] = True
        if DataValidator.isNull(self.form["contact_no"]):
            inputError["contact_no"] = "Contact No. is required"
            self.form["error"] = True
        return self.form["error"]

    # Display branch page
    def display(self, request, params={}):
        if params["id"] > 0:
            branch = self.get_service().get(params["id"])
            self.model_to_form(branch)
        return render(
            request,
            self.get_template(),
            {"form": self.form, "preload_data": self.preload(request)},
        )

    # Submit branch page
    def submit(self, request, _params={}):
        branch = self.form_to_model(Branch())
        self.get_service().save(branch)
        if int(self.form["id"]) > 0:
            self.form["id"] = branch.id
        self.form["error"] = False
        self.form["message"] = "Data is saved"
        return render(
            request,
            self.get_template(),
            {"form": self.form, "preload_data": self.preload(request)},
        )

    # Template html of branch page
    def get_template(self):
        return "ors/branch.html"

    # Service of branch
    def get_service(self):
        return BranchService()
