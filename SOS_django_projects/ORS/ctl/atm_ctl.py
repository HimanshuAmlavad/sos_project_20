from django.shortcuts import render

from ORS.ctl.BaseCtl import BaseCtl
from ORS.utility.HtmlUtility import HtmlUtility
from service.models import Drone, ATM
from service.service.AtmService import AtmService
from service.utility.DataValidator import DataValidator



class AtmCtl(BaseCtl):

    def preload(self, request):
        status_list = ["Active", "Inactive", "Out of Cash", "Under Maintenance"]
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
        self.form["atm_id"] = request.get("atmId", 0)
        self.form["location"] = request.get("location", "")
        self.form["bank_name"] = request.get("bankName", "")
        self.form["cash_available"] = request.get("cashAvailable", "")
        self.form["status"] = request.get("status", "")

    # Populate Form from Model
    def model_to_form(self, obj):
        if obj == None:
            return
        self.form["id"] = obj.id
        # print('M2F======================>', self.form["id"])
        self.form["atm_id"] = obj.atm_id
        self.form["location"] = obj.location
        self.form["bank_name"] = obj.bank_name
        self.form["cash_available"] = obj.cash_available
        self.form["status"] = obj.status
        print('M2F======================>', self.form["status"])


    # Convert form into module
    def form_to_model(self, obj):
        pk = int(self.form.get("id", 0))
        if pk > 0:
            obj.id = pk
        print('F2M======================>', obj.id)
        obj.atm_id = int(self.form.get("atm_id", 0))
        obj.location = self.form.get("location", "")
        obj.bank_name = self.form.get("bank_name", "")
        obj.cash_available = self.form.get("cash_available", "")
        obj.status = self.form.get("status", "")
        return obj

    # Validate form
    def input_validation(self):
        super().input_validation()
        inputError = self.form["inputError"]
        if DataValidator.isNull(self.form["atm_id"]):
            inputError["atm_id"] = "ATM Id is required"
            self.form["error"] = True
        if DataValidator.isNull(self.form["location"]):
            inputError["location"] = "Location is required"
            self.form["error"] = True
        if DataValidator.isNull(self.form["bank_name"]):
            inputError["bank_name"] = "Bank Name is required"
            self.form["error"] = True
        if DataValidator.isNull(self.form["cash_available"]):
            inputError["cash_available"] = "Cash Available is required"
            self.form["error"] = True
        if DataValidator.isNull(self.form["status"]):
            inputError["status"] = "Status is required"
            self.form["error"] = True
        return self.form["error"]

    # Display Role page
    def display(self, request, params={}):
        if params["id"] > 0:
            atm = self.get_service().get(params["id"])
            self.model_to_form(atm)
        return render(
            request,
            self.get_template(),
            {"form": self.form, "preload_data": self.preload(request)},
        )

    # Submit Role page
    def submit(self, request, _params={}):
        atm = self.form_to_model(ATM())
        self    .get_service().save(atm)
        if int(self.form["id"]) > 0:
            self.form["id"] = atm.id
        self.form["error"] = False
        self.form["message"] = "Data is saved"
        return render(
            request,
            self.get_template(),
            {"form": self.form, "preload_data": self.preload(request)},
        )

    # Template html of Role page
    def get_template(self):
        return "ors/atm.html"

    # Service of Role
    def get_service(self):
        return AtmService()
