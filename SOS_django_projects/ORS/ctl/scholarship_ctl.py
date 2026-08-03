from django.shortcuts import render

from ORS.ctl.BaseCtl import BaseCtl
from ORS.utility.HtmlUtility import HtmlUtility
from service.models import  Scholarship
from service.service.ScholarshipService import ScholarshipService
from service.utility.DataValidator import DataValidator

class ScholarshipCtl(BaseCtl):

    def preload(self, request):
        scholarship_name_list = ["Financial Assistance Scholarship",
                       "Girls Higher Education Scholarship",
                       "Economically Weaker Section Scholarship",
                       "Merit Excellence Scholarship",
                       "Academic Achievement Scholarship"]

        eligibility_list = ["Minimum 90% marks and annual family income below ₹2,50,000",
                            "State level player and minimum 60%",
                            "Is a female and minimum marks 75%",
                            "Minimum marks 60% annual family income below ₹1,50,000 "]
        # print("Preload status:", repr(self.form.get("status")))

        self.preload_data["scholarship_name_select"] = HtmlUtility.get_list_from_list(
            "scholarshipName",
            self.form.get("scholarship_name"),
            scholarship_name_list,
        )
        self.preload_data["eligibility_select"] = HtmlUtility.get_list_from_list(
            "eligibility",
            self.form.get("eligibility"),
            eligibility_list,
        )
        # Also make preload available under form for templates using `form.preload_data`
        self.form["preload_data"] = self.preload_data
        return self.preload_data

    # Populate Form from HTTP Request
    def request_to_form(self, request):
        self.form["id"] = int(request.get("id", 0) or 0)
        # print('R2F =====================>', self.form["id"])
        self.form["scholarship_id"] = request.get("scholarshipId", 0)
        self.form["scholarship_name"] = request.get("scholarshipName", "")
        self.form["amount"] = request.get("amount", "")
        print('R2F =====================>', self.form["amount"])
        self.form["last_date"] = request.get("lastDate", "")
        self.form["eligibility"] = request.get("eligibility", "")

    # Populate Form from Model
    def model_to_form(self, obj):
        if obj == None:
            return
        self.form["id"] = obj.id
        # print('M2F======================>', self.form["id"])
        self.form["scholarship_id"] = obj.scholarship_id
        self.form["scholarship_name"] = obj.scholarship_name
        self.form["amount"] = obj.amount
        print('M2F======================>', self.form["amount"])
        self.form["last_date"] = obj.last_date.strftime("%Y-%m-%d")
        self.form["eligibility"] = obj.eligibility
        # print('M2F======================>', self.form["eligibility"])

    # Convert form into module
    def form_to_model(self, obj):
        pk = int(self.form.get("id", 0))
        if pk > 0:
            obj.id = pk
        print('F2M======================>', obj.id)
        obj.scholarship_id = int(self.form.get("scholarship_id", 0))
        obj.scholarship_name = self.form.get("scholarship_name", "")
        obj.amount = self.form.get("amount", "")
        print('F2M======================>', obj.amount)
        obj.last_date = self.form.get("last_date", "")
        obj.eligibility = self.form.get("eligibility", "")
        return obj

    # Validate form
    def input_validation(self):
        super().input_validation()
        inputError = self.form["inputError"]
        if DataValidator.isNull(self.form["scholarship_id"]):
            inputError["scholarship_id"] = "Scholarship Id is required"
            self.form["error"] = True
        if DataValidator.isNull(self.form["scholarship_name"]):
            inputError["scholarship_name"] = "Scholarship Name is required"
            self.form["error"] = True
        if DataValidator.isNull(self.form["amount"]):
            inputError["amount"] = "Amount is required"
            self.form["error"] = True
        if DataValidator.isNull(self.form["last_date"]):
            inputError["last_date"] = "Last Date is required"
            self.form["error"] = True
        if DataValidator.isNull(self.form["eligibility"]):
            inputError["eligibility"] = "Eligibility is required"
            self.form["error"] = True
        return self.form["error"]

    # Display Role page
    def display(self, request, params={}):
        if params["id"] > 0:
            fee = self.get_service().get(params["id"])
            self.model_to_form(fee)
        return render(
            request,
            self.get_template(),
            {"form": self.form, "preload_data": self.preload(request)},
        )

    # Submit Role page
    def submit(self, request, _params={}):
        scholarship = self.form_to_model(Scholarship())
        self.get_service().save(scholarship)
        if int(self.form["id"]) > 0:
            self.form["id"] = scholarship.id
        self.form["error"] = False
        self.form["message"] = "Data is saved"
        return render(
            request,
            self.get_template(),
            {"form": self.form, "preload_data": self.preload(request)},
        )

    # Template html of Role page
    def get_template(self):
        return "ors/scholarship.html"

    # Service of Role
    def get_service(self):
        return ScholarshipService()
