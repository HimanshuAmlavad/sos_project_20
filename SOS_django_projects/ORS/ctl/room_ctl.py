from django.shortcuts import render

from ORS.ctl.BaseCtl import BaseCtl
from ORS.utility.HtmlUtility import HtmlUtility
from service.models import  Room
from service.service.RoomService import RoomService
from service.utility.DataValidator import DataValidator

class RoomCtl(BaseCtl):

    def preload(self, request):
        room_type_list = [
            "Single",
            "Double",
            "Deluxe",
            "Suite",
        ]

        availability_list = [
            "Available",
            "Occupied",
        ]
        self.preload_data["room_type_select"] = HtmlUtility.get_list_from_list(
            "roomType",
            self.form.get("room_type"),
            room_type_list,
        )
        self.preload_data["availability_select"] = HtmlUtility.get_list_from_list(
            "availability",
            self.form.get("availability"),
            availability_list,
        )
        # Also make preload available under form for templates using `form.preload_data`
        self.form["preload_data"] = self.preload_data
        return self.preload_data

    # Populate Form from HTTP Request
    def request_to_form(self, request):
        self.form["id"] = int(request.get("id", 0) or 0)
        # print('R2F =====================>', self.form["id"])
        self.form["room_id"] = request.get("roomId", 0)
        self.form["room_no"] = request.get("roomNo", 0)
        self.form["room_type"] = request.get("roomType", "")
        print('R2F =====================>', self.form["room_type"])
        self.form["price_per_day"] = request.get("pricePerDay", 0)
        self.form["availability"] = request.get("availability", "")

    # Populate Form from Model
    def model_to_form(self, obj):
        if obj == None:
            return
        self.form["id"] = obj.id
        # print('M2F======================>', self.form["id"])
        self.form["room_id"] = obj.room_id
        self.form["room_no"] = obj.room_no
        self.form["room_type"] = obj.room_type
        print('M2F======================>', self.form["room_type"])
        self.form["price_per_day"] = obj.price_per_day
        self.form["availability"] = obj.availability
        # print('M2F======================>', self.form["availability"])

    # Convert form into module
    def form_to_model(self, obj):
        pk = int(self.form.get("id", 0))
        if pk > 0:
            obj.id = pk
        print('F2M======================>', obj.id)
        obj.room_id = int(self.form.get("room_id", 0))
        obj.room_no = self.form.get("room_no", 0)
        obj.room_type = self.form.get("room_type", "")
        print('F2M======================>', obj.room_type)
        obj.price_per_day = self.form.get("price_per_day", 0)
        obj.availability = self.form.get("availability", "")
        return obj

    # Validate form
    def input_validation(self):
        super().input_validation()
        inputError = self.form["inputError"]
        if DataValidator.isNull(self.form["room_id"]):
            inputError["room_id"] = "Room Id is required"
            self.form["error"] = True
        if DataValidator.isNull(self.form["room_no"]):
            inputError["room_no"] = "room No is required"
            self.form["error"] = True
        if DataValidator.isNull(self.form["room_type"]):
            inputError["room_type"] = "Room Type is required"
            self.form["error"] = True
        if DataValidator.isNull(self.form["price_per_day"]):
            inputError["price_per_day"] = "Price is required"
            self.form["error"] = True
        if DataValidator.isNull(self.form["availability"]):
            inputError["availability"] = "Availability is required"
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
        room = self.form_to_model(Room())
        self.get_service().save(room)
        if int(self.form["id"]) > 0:
            self.form["id"] = room.id
        self.form["error"] = False
        self.form["message"] = "Data is saved"
        return render(
            request,
            self.get_template(),
            {"form": self.form, "preload_data": self.preload(request)},
        )

    # Template html of Role page
    def get_template(self):
        return "ors/room.html"

    # Service of Role
    def get_service(self):
        return RoomService()
