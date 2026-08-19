from django.shortcuts import render
from service.models import Customer
from ORS.ctl.BaseCtl import BaseCtl
from ORS.utility.HtmlUtility import HtmlUtility
from service.service.CustomerService import CustomerService
from service.utility.DataValidator import DataValidator


class CustomerCtl(BaseCtl):

    # Populate Form from HTTP Request
    def request_to_form(self, request):
        self.form["id"] = int(request.get("id", 0) or 0)
        # print('R2F =====================>', self.form["id"])
        self.form["customer_id"] = request.get("customerId", 0)
        self.form["customer_name"] = request.get("customerName", "")
        self.form["email"] = request.get("email", "")
        # print('R2F =====================>', self.form["email"])
        self.form["phone_number"] = request.get("phoneNumber", "")
        self.form["address"] = request.get("address", "")
        # print('R2F =====================>', self.form["address"])

    # Populate Form from Model
    def model_to_form(self, obj):
        if obj == None:
            return
        self.form["id"] = obj.id
        # print('M2F======================>', self.form["id"])
        self.form["customer_id"] = obj.customer_id
        self.form["customer_name"] = obj.customer_name
        self.form["email"] = obj.email
        # print('M2F======================>', self.form["student_name"])
        self.form["phone_number"] = obj.phone_number
        self.form["address"] = obj.address
        # print('M2F======================>', self.form["address"])

    # Convert form into module
    def form_to_model(self, obj):
        pk = int(self.form.get("id", 0))
        if pk > 0:
            obj.id = pk
        # print('F2M======================>', obj.id)
        obj.customer_id = int(self.form.get("customer_id", 0))
        obj.customer_name = self.form.get("customer_name", "")
        obj.email = self.form.get("email", "")
        # print('F2M======================>', obj.student_name)
        obj.phone_number = self.form.get("phone_number", "")
        obj.address = self.form.get("address", "")
        return obj

    # Validate form
    def input_validation(self):
        super().input_validation()
        inputError = self.form["inputError"]
        if DataValidator.isNull(self.form["customer_id"]):
            inputError["customer_id"] = "Customer Id is required"
            self.form["error"] = True
        if DataValidator.isNull(self.form["customer_name"]):
            inputError["customer_name"] = "Customer Name is required"
            self.form["error"] = True
        if DataValidator.isNull(self.form["email"]):
            inputError["email"] = "Email is required"
            self.form["error"] = True
        if DataValidator.isNull(self.form["phone_number"]):
            inputError["phone_number"] = "Phone Number is required"
            self.form["error"] = True
        if DataValidator.isNull(self.form["address"]):
            inputError["address"] = "Address is required"
            self.form["error"] = True
        return self.form["error"]

    # Display Role page
    def display(self, request, params={}):
        if params["id"] > 0:
            customer = self.get_service().get(params["id"])
            self.model_to_form(customer)
        return render(
            request,
            self.get_template(),
            {"form": self.form, "preload_data": self.preload(request)},
        )

    # Submit Role page
    def submit(self, request, _params={}):
        customer = self.form_to_model(Customer())
        self.get_service().save(customer)
        if int(self.form["id"]) > 0:
            self.form["id"] = customer.id
        self.form["error"] = False
        self.form["message"] = "Data is saved"
        return render(
            request,
            self.get_template(),
            {"form": self.form, "preload_data": self.preload(request)},
        )

    # Template html of Role page
    def get_template(self):
        return "ors/customer.html"

    # Service of Role
    def get_service(self):
        return CustomerService()
