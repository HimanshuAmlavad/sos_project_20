from django.shortcuts import render
from service.models import CreditCard
from ORS.ctl.BaseCtl import BaseCtl
from ORS.utility.HtmlUtility import HtmlUtility
from service.service.CreditCardService import CreditCardService
from service.utility.DataValidator import DataValidator


class CreditCardCtl(BaseCtl):

    def preload(self, request):
        card_type_list = ["Visa",
                          "Mastercard",
                          "RuPay",
                          "American Express"]

        # print("Preload status:", repr(self.form.get("status")))
        self.preload_data["card_select"] = HtmlUtility.get_list_from_list(
            "cardType",
            self.form.get("card_type"),
            card_type_list,
        )
        # Also make preload available under form for templates using `form.preload_data`
        self.form["preload_data"] = self.preload_data
        return self.preload_data

    # Populate Form from HTTP Request
    def request_to_form(self, request):
        self.form["id"] = int(request.get("id", 0) or 0)
        # print('R2F =====================>', self.form["id"])
        self.form["card_id"] = request.get("cardId", 0)
        self.form["card_number"] = request.get("cardNumber", 0)
        self.form["card_holder"] = request.get("cardHolder", "")
        # print('R2F =====================>', self.form["student_name"])
        self.form["expiry_date"] = request.get("expiryDate", "")
        self.form["card_type"] = request.get("cardType", "")
        print('R2F =====================>', self.form["card_type"])

    # Populate Form from Model
    def model_to_form(self, obj):
        if obj == None:
            return
        self.form["id"] = obj.id
        # print('M2F======================>', self.form["id"])
        self.form["card_id"] = obj.card_id
        self.form["card_number"] = obj.card_number
        self.form["card_holder"] = obj.card_holder
        # print('M2F======================>', self.form["student_name"])
        self.form["expiry_date"] = obj.expiry_date.strftime("%Y-%m-%d")
        self.form["card_type"] = obj.card_type
        # print('M2F======================>', self.form["payment_status"])

    # Convert form into module
    def form_to_model(self, obj):
        pk = int(self.form.get("id", 0))
        if pk > 0:
            obj.id = pk
        # print('F2M======================>', obj.id)
        obj.card_id = int(self.form.get("card_id", 0))
        obj.card_number = self.form.get("card_number", "")
        obj.card_holder = self.form.get("card_holder", "")
        # print('F2M======================>', obj.student_name)
        obj.expiry_date = self.form.get("expiry_date", "")
        obj.card_type = self.form.get("card_type", "")
        return obj

    # Validate form
    def input_validation(self):
        super().input_validation()
        inputError = self.form["inputError"]
        if DataValidator.isNull(self.form["card_id"]):
            inputError["card_id"] = "Card Id is required"
            self.form["error"] = True
        if DataValidator.isNull(self.form["card_number"]):
            inputError["card_number"] = "Card Number is required"
            self.form["error"] = True
        if DataValidator.isNull(self.form["card_holder"]):
            inputError["card_holder"] = "Card Holder is required"
            self.form["error"] = True
        if DataValidator.isNull(self.form["expiry_date"]):
            inputError["expiry_date"] = "Expiry Date is required"
            self.form["error"] = True
        if DataValidator.isNull(self.form["card_type"]):
            inputError["card_type"] = "Card Type is required"
            self.form["error"] = True
        return self.form["error"]

    # Display Role page
    def display(self, request, params={}):
        if params["id"] > 0:
            card = self.get_service().get(params["id"])
            self.model_to_form(card)
        return render(
            request,
            self.get_template(),
            {"form": self.form, "preload_data": self.preload(request)},
        )

    # Submit Role page
    def submit(self, request, _params={}):
        card = self.form_to_model(CreditCard())
        self.get_service().save(card)
        if int(self.form["id"]) > 0:
            self.form["id"] = card.id
        self.form["error"] = False
        self.form["message"] = "Data is saved"
        return render(
            request,
            self.get_template(),
            {"form": self.form, "preload_data": self.preload(request)},
        )

    # Template html of Role page
    def get_template(self):
        return "ors/creditcard.html"

    # Service of Role
    def get_service(self):
        return CreditCardService()
