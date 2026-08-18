from django.shortcuts import render
from service.models import  Order
from ORS.ctl.BaseCtl import BaseCtl
from ORS.utility.HtmlUtility import HtmlUtility
from service.service.OrderService import OrderService
from service.utility.DataValidator import DataValidator


class OrderCtl(BaseCtl):

    def preload(self, request):
        status_list = [
            "Pending",
            "Confirmed",
            "Processing",
            "Shipped",
            "Delivered",
            "Cancelled"
        ]

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
        self.form["order_id"] = request.get("orderId", 0)
        self.form["amount"] = request.get("amount", 0)
        self.form["customer_id"] = request.get("customerId", 0)
        # print('R2F =====================>', self.form["student_name"])
        self.form["order_date"] = request.get("orderDate", "")
        self.form["status"] = request.get("status", "")
        print('R2F =====================>', self.form["status"])

    # Populate Form from Model
    def model_to_form(self, obj):
        if obj == None:
            return
        self.form["id"] = obj.id
        # print('M2F======================>', self.form["id"])
        self.form["order_id"] = obj.order_id
        self.form["amount"] = obj.amount
        self.form["customer_id"] = obj.customer_id
        # print('M2F======================>', self.form["student_name"])
        self.form["order_date"] = obj.order_date.strftime("%Y-%m-%d")
        self.form["status"] = obj.status
        # print('M2F======================>', self.form["payment_status"])

    # Convert form into module
    def form_to_model(self, obj):
        pk = int(self.form.get("id", 0))
        if pk > 0:
            obj.id = pk
        # print('F2M======================>', obj.id)
        obj.order_id = int(self.form.get("order_id", 0))
        obj.amount = self.form.get("amount", "")
        obj.customer_id = self.form.get("customer_id", 0)
        # print('F2M======================>', obj.student_name)
        obj.order_date = self.form.get("order_date", "")
        obj.status = self.form.get("status", "")
        return obj

    # Validate form
    def input_validation(self):
        super().input_validation()
        inputError = self.form["inputError"]
        if DataValidator.isNull(self.form["order_id"]):
            inputError["order_id"] = "Order Id is required"
            self.form["error"] = True
        if DataValidator.isNull(self.form["amount"]):
            inputError["amount"] = "Amount is required"
            self.form["error"] = True
        if DataValidator.isNull(self.form["customer_id"]):
            inputError["customer_id"] = "Customer Id is required"
            self.form["error"] = True
        if DataValidator.isNull(self.form["order_date"]):
            inputError["order_date"] = "Order Date is required"
            self.form["error"] = True
        if DataValidator.isNull(self.form["status"]):
            inputError["status"] = "status is required"
            self.form["error"] = True
        return self.form["error"]

    # Display Role page
    def display(self, request, params={}):
        if params["id"] > 0:
            order = self.get_service().get(params["id"])
            self.model_to_form(order)
        return render(
            request,
            self.get_template(),
            {"form": self.form, "preload_data": self.preload(request)},
        )

    # Submit Role page
    def submit(self, request, _params={}):
        order = self.form_to_model(Order())
        self.get_service().save(order)
        if int(self.form["id"]) > 0:
            self.form["id"] = order.id
        self.form["error"] = False
        self.form["message"] = "Data is saved"
        return render(
            request,
            self.get_template(),
            {"form": self.form, "preload_data": self.preload(request)},
        )

    # Template html of Role page
    def get_template(self):
        return "ors/order.html"

    # Service of Role
    def get_service(self):
        return OrderService()
