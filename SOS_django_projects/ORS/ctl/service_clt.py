from django.shortcuts import render

from ORS.ctl.BaseCtl import BaseCtl
from ORS.utility.HtmlUtility import HtmlUtility
from service.models import Service
from service.service.ServiceService import ServiceService
from service.utility.DataValidator import DataValidator

class ServiceCtl(BaseCtl):

    def preload(self, request):
        service_category_list = [
            "Cleaning",
            "Electrical",
            "Plumbing",
            "Catering",
            "Photography",
            "Transportation",
            "Maintenance",
            "IT Services"
        ]
        # print("Preload status:", repr(self.form.get("status")))
        self.preload_data["service_select"] = HtmlUtility.get_list_from_list(
            "serviceCategory",
            self.form.get("service_category"),
            service_category_list,
        )
        # Also make preload available under form for templates using `form.preload_data`
        self.form["preload_data"] = self.preload_data
        return self.preload_data

    # Populate Form from HTTP Request
    def request_to_form(self, request):
        self.form["id"] = int(request.get("id", 0) or 0)
        # print('R2F =====================>', self.form["id"])
        self.form["service_id"] = request.get("serviceId", 0)
        self.form["description "] = request.get("description", "")
        self.form["service_name"] = request.get("serviceName", "")
        # print('R2F =====================>', self.form["service_name"])
        self.form["price"] = request.get("price", 0)
        self.form["service_category"] = request.get("serviceType", "")

    # Populate Form from Model
    def model_to_form(self, obj):
        if obj == None:
            return
        self.form["id"] = obj.id
        # print('M2F======================>', self.form["id"])
        self.form["service_id"] = obj.service_id
        self.form["description "] = obj.description
        self.form["service_name"] = obj.service_Name
        print('M2F======================>', self.form["service_name"])
        self.form[" price "] = obj. price
        self.form["service_category"] = obj.service_category
        # print('M2F======================>', self.form["service_category"])

    # Convert form into module
    def form_to_model(self, obj):
        pk = int(self.form.get("id", 0))
        if pk > 0:
            obj.id = pk
        print('F2M======================>', obj.id)
        obj.service_id = int(self.form.get("service_id", 0))
        obj.description  = self.form.get("description ", "")
        obj.service_Name = self.form.get("service_name", "")
        print('F2M======================>', obj.service_Name)
        obj. price  = self.form.get(" price ", 0)
        obj.service_category = self.form.get("service_category", "")
        return obj

    # Validate form
    def input_validation(self):
        super().input_validation()
        inputError = self.form["inputError"]
        if DataValidator.isNull(self.form["service_id"]):
            inputError["service_id"] = "Service Id is required"
            self.form["error"] = True
        if DataValidator.isNull(self.form["description "]):
            inputError["description "] = "Description is required"
            self.form["error"] = True
        if DataValidator.isNull(self.form["service_name"]):
            inputError["service_name"] = "Service Name is required"
            self.form["error"] = True
        if DataValidator.isNull(self.form[" price "]):
            inputError[" price "] = " Price is required"
            self.form["error"] = True
        if DataValidator.isNull(self.form["service_category"]):
            inputError["service_category"] = "Service Category is required"
            self.form["error"] = True
        return self.form["error"]

    # Display Role page
    def display(self, request, params={}):
        if params["id"] > 0:
            service = self.get_service().get(params["id"])
            self.model_to_form(service)
        return render(
            request,
            self.get_template(),
            {"form": self.form, "preload_data": self.preload(request)},
        )

    # Submit Role page
    def submit(self, request, _params={}):
        service = self.form_to_model(Service())
        self.get_service().save(service)
        if int(self.form["id"]) > 0:
            self.form["id"] = service.id
        self.form["error"] = False
        self.form["message"] = "Data is saved"
        return render(
            request,
            self.get_template(),
            {"form": self.form, "preload_data": self.preload(request)},
        )

    # Template html of Role page
    def get_template(self):
        return "ors/service.html"

    # Service of Role
    def get_service(self):
        return ServiceService()
