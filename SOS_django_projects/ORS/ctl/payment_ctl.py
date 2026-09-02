from django.shortcuts import render
from service.models import Payment
from ORS.ctl.BaseCtl import BaseCtl
from ORS.utility.HtmlUtility import HtmlUtility
from service.service.PaymentService import PaymentService
from service.utility.DataValidator import DataValidator


class PaymentCtl(BaseCtl):

    def preload(self, request):
        payment_method_list = [
            "Cash",
            "UPI",
            "Credit Card",
            "Debit Card",
            "Net Banking"
        ]

        # print("Preload status:", repr(self.form.get("status")))
        self.preload_data["method_select"] = HtmlUtility.get_list_from_list(
            "paymentMethod",
            self.form.get("payment_method"),
            payment_method_list,
        )
        # Also make preload available under form for templates using `form.preload_data`
        self.form["preload_data"] = self.preload_data
        return self.preload_data

    # Populate Form from HTTP Request
    def request_to_form(self, request):
        self.form["id"] = int(request.get("id", 0) or 0)
        # print('R2F =====================>', self.form["id"])
        self.form["payment_id"] = request.get("paymentId", "")
        self.form["payment_method"] = request.get("paymentMethod", "")
        self.form["amount"] = request.get("amount", 0)
        # print('R2F =====================>', self.form["student_method"])
        self.form["payment_date"] = request.get("paymentDate", "")
        self.form["transaction_id"] = request.get("transactionId", "")
        print('R2F =====================>', self.form["transaction_id"])

    # Populate Form from Model
    def model_to_form(self, obj):
        if obj == None:
            return
        self.form["id"] = obj.id
        # print('M2F======================>', self.form["id"])
        self.form["payment_id"] = obj.payment_id
        self.form["payment_method"] = obj.payment_method
        self.form["amount"] = obj.amount
        # print('M2F======================>', self.form["student_method"])
        self.form["payment_date"] = obj.payment_date.strftime("%Y-%m-%d")
        self.form["transaction_id"] = obj.transaction_id
        # print('M2F======================>', self.form["payment_transaction_id"])

    # Convert form into module
    def form_to_model(self, obj):
        pk = int(self.form.get("id", 0))
        if pk > 0:
            obj.id = pk
        # print('F2M======================>', obj.id)
        obj.payment_id = int(self.form.get("payment_id", ""))
        obj.payment_method = self.form.get("payment_method", "")
        obj.amount = self.form.get("amount", 0)
        # print('F2M======================>', obj.student_method)
        obj.payment_date = self.form.get("payment_date", "")
        obj.transaction_id = self.form.get("transaction_id", "")
        return obj

    # Validate form
    def input_validation(self):
        super().input_validation()
        inputError = self.form["inputError"]
        if DataValidator.isNull(self.form["payment_id"]):
            inputError["payment_id"] = "Payment Id is required"
            self.form["error"] = True
        if DataValidator.isNull(self.form["payment_method"]):
            inputError["payment_method"] = "Payment Method is required"
            self.form["error"] = True
        if DataValidator.isNull(self.form["amount"]):
            inputError["amount"] = "Amount is required"
            self.form["error"] = True
        if DataValidator.isNull(self.form["payment_date"]):
            inputError["payment_date"] = "Payment Date is required"
            self.form["error"] = True
        if DataValidator.isNull(self.form["transaction_id"]):
            inputError["transaction_id"] = "Transaction Id is required"
            self.form["error"] = True
        return self.form["error"]

    # Display Role page
    def display(self, request, params={}):
        if params["id"] > 0:
            payment = self.get_service().get(params["id"])
            self.model_to_form(payment)
        return render(
            request,
            self.get_template(),
            {"form": self.form, "preload_data": self.preload(request)},
        )

    # Submit Role page
    def submit(self, request, _params={}):
        payment = self.form_to_model(Payment())
        self.get_service().save(payment)
        if int(self.form["id"]) > 0:
            self.form["id"] = payment.id
        self.form["error"] = False
        self.form["message"] = "Data is saved"
        return render(
            request,
            self.get_template(),
            {"form": self.form, "preload_data": self.preload(request)},
        )

    # Template html of Role page
    def get_template(self):
        return "ors/payment.html"

    # Service of Role
    def get_service(self):
        return PaymentService()
