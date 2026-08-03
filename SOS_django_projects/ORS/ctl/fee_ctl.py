from django.shortcuts import render

from ORS.ctl.BaseCtl import BaseCtl
from ORS.utility.HtmlUtility import HtmlUtility
from service.models import Fee
from service.service.FeeService import FeeService
from service.utility.DataValidator import DataValidator

class FeeCtl(BaseCtl):

    def preload(self, request):
        status_list = ["Pending",
                       "Paid",
                       "Partially Paid",
                       "Failed",
                       "Refunded"]
        # print("Preload status:", repr(self.form.get("status")))
        self.preload_data["status_select"] = HtmlUtility.get_list_from_list(
            "paymentStatus",
            self.form.get("payment_status"),
            status_list,
        )
        # Also make preload available under form for templates using `form.preload_data`
        self.form["preload_data"] = self.preload_data
        return self.preload_data

    # Populate Form from HTTP Request
    def request_to_form(self, request):
        self.form["id"] = int(request.get("id", 0) or 0)
        # print('R2F =====================>', self.form["id"])
        self.form["fee_id"] = request.get("feeId", 0)
        self.form["student_id"] = request.get("studentId", 0)
        self.form["amount"] = request.get("amount", "")
        print('R2F =====================>', self.form["amount"])
        self.form["payment_date"] = request.get("paymentDate", "")
        self.form["payment_status"] = request.get("paymentStatus", "")

    # Populate Form from Model
    def model_to_form(self, obj):
        if obj == None:
            return
        self.form["id"] = obj.id
        # print('M2F======================>', self.form["id"])
        self.form["fee_id"] = obj.fee_id
        self.form["student_id"] = obj.student_id
        self.form["amount"] = obj.amount
        print('M2F======================>', self.form["amount"])
        self.form["payment_date"] = obj.payment_date.strftime("%Y-%m-%d")
        self.form["payment_status"] = obj.payment_status
        # print('M2F======================>', self.form["payment_status"])

    # Convert form into module
    def form_to_model(self, obj):
        pk = int(self.form.get("id", 0))
        if pk > 0:
            obj.id = pk
        print('F2M======================>', obj.id)
        obj.fee_id = int(self.form.get("fee_id", 0))
        obj.student_id = self.form.get("student_id", "")
        obj.amount = self.form.get("amount", "")
        print('F2M======================>', obj.amount)
        obj.payment_date = self.form.get("payment_date", "")
        obj.payment_status = self.form.get("payment_status", "")
        return obj

    # Validate form
    def input_validation(self):
        super().input_validation()
        inputError = self.form["inputError"]
        if DataValidator.isNull(self.form["fee_id"]):
            inputError["fee_id"] = "Fee Id is required"
            self.form["error"] = True
        if DataValidator.isNull(self.form["student_id"]):
            inputError["student_id"] = "Student Id is required"
            self.form["error"] = True
        if DataValidator.isNull(self.form["amount"]):
            inputError["amount"] = "Amount is required"
            self.form["error"] = True
        if DataValidator.isNull(self.form["payment_date"]):
            inputError["payment_date"] = "Payment Date is required"
            self.form["error"] = True
        if DataValidator.isNull(self.form["payment_status"]):
            inputError["payment_status"] = "Payment Status is required"
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
        fee = self.form_to_model(Fee())
        self.get_service().save(fee)
        if int(self.form["id"]) > 0:
            self.form["id"] = fee.id
        self.form["error"] = False
        self.form["message"] = "Data is saved"
        return render(
            request,
            self.get_template(),
            {"form": self.form, "preload_data": self.preload(request)},
        )

    # Template html of Role page
    def get_template(self):
        return "ors/fee.html"

    # Service of Role
    def get_service(self):
        return FeeService()
