from django.shortcuts import render

from ORS.ctl.BaseCtl import BaseCtl
from ORS.utility.HtmlUtility import HtmlUtility
from service.models import Vehicle
from service.service.VehicleService import VehicleService
from service.utility.DataValidator import DataValidator

class VehicleCtl(BaseCtl):

    def preload(self, request):
        vehicle_type = ["Car", "Bike", "Electric Car", "Electric Bike"]
        status_list = [ "Pending", "Under Maintenance", "Ready"]
        # print("Preload status:", repr(self.form.get("status")))

        self.preload_data["vehicle_select"] = HtmlUtility.get_list_from_list(
            "vehicleType",
            self.form.get("vehicle_type"),
            vehicle_type,
        )

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
        self.form["id"] = request.get("id", 0)
        # print('R2F =====================>', self.form["id"])
        self.form["vehicle_id"] = request.get("vehicleId", 0)
        self.form["vehicle_no"] = request.get("vehicleNo", "")
        self.form["model_name"] = request.get("modelName", "")
        self.form["owner_name"] = request.get("ownerName", "")
        print("R2F ====================>",self.form['owner_name'])
        self.form["vehicle_type"] = request.get("vehicleType", "")
        self.form["status"] = request.get("status", "")

    # Populate Form from Model
    def model_to_form(self, obj):
        if obj == None:
            return
        self.form["id"] = obj.id
        # print('M2F======================>', self.form["id"])
        self.form["vehicle_id"] = obj.vehicle_id
        self.form["vehicle_no"] = obj.vehicle_no
        self.form["model_name"] = obj.model_name
        self.form["owner_name"] = obj.owner_name
        self.form["vehicle_type"] = obj.vehicle_type
        self.form["status"] = obj.status
        print('M2F======================>', self.form["status"])


    # Convert form into module
    def form_to_model(self, obj):
        pk = int(self.form.get("id", 0))
        if pk > 0:
            obj.id = pk
        print('F2M======================>', obj.id)
        obj.vehicle_id = int(self.form.get("vehicle_id", 0))
        obj.vehicle_no = self.form.get("vehicle_no", "")
        obj.model_name = self.form.get("model_name", "")
        obj.owner_name = self.form.get("owner_name", "")
        obj.vehicle_type = self.form.get("vehicle_type", "")
        obj.status = self.form.get("status", "")
        return obj

    # Validate form
    def input_validation(self):
        super().input_validation()
        inputError = self.form["inputError"]
        if DataValidator.isNull(self.form["vehicle_id"]):
            inputError["vehicle_id"] = "Vehicle Id is required"
            self.form["error"] = True
        if DataValidator.isNull(self.form["vehicle_no"]):
            inputError["vehicle_no"] = "Vehicle No is required"
            self.form["error"] = True
        if DataValidator.isNull(self.form["model_name"]):
            inputError["model_name"] = "Model Name is required"
            self.form["error"] = True
        if DataValidator.isNull(self.form["owner_name"]):
            inputError["owner_name"] = "Owner Name is required"
            self.form["error"] = True
        if DataValidator.isNull(self.form["vehicle_type"]):
            inputError["vehicle_type"] = "Vehicle Type is required"
            self.form["error"] = True 
        if DataValidator.isNull(self.form["status"]):
            inputError["status"] = "Status is required"
            self.form["error"] = True
        return self.form["error"]

    # Display Vehicle page
    def display(self, request, params={}):
        if params["id"] > 0:
            vehicle = self.get_service().get(params["id"])
            self.model_to_form(vehicle)
        return render(
            request,
            self.get_template(),
            {"form": self.form, "preload_data": self.preload(request)},
        )

    # Submit Vehicle page
    def submit(self, request, _params={}):
        vehicle = self.form_to_model(Vehicle())
        self.get_service().save(vehicle)
        if int(self.form["id"]) > 0:
            self.form["id"] = vehicle.id
        self.form["error"] = False
        self.form["message"] = "Data is saved"
        return render(
            request,
            self.get_template(),
            {"form": self.form, "preload_data": self.preload(request)},
        )

    # Template html of Vehicle page
    def get_template(self):
        return "ors/vehicle.html"

    # Service of Vehicle
    def get_service(self):
        return VehicleService()
