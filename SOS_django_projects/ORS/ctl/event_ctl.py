from django.shortcuts import render
from service.models import  Event
from ORS.ctl.BaseCtl import BaseCtl
from service.service.EventService import EventService
from service.utility.DataValidator import DataValidator


class EventCtl(BaseCtl):

    # Populate Form from HTTP Request
    def request_to_form(self, request):
        self.form["id"] = int(request.get("id", 0) or 0)
        # print('R2F =====================>', self.form["id"])
        self.form["event_id"] = request.get("eventId", 0)
        self.form["event_name"] = request.get("eventName", "")
        self.form["venue"] = request.get("venue", "")
        # print('R2F =====================>', self.form["student_name"])
        self.form["event_date"] = request.get("eventDate", "")
        self.form["organizer"] = request.get("organizer", "")
        print('R2F =====================>', self.form["organizer"])

    # Populate Form from Model
    def model_to_form(self, obj):
        if obj == None:
            return
        self.form["id"] = obj.id
        # print('M2F======================>', self.form["id"])
        self.form["event_id"] = obj.event_id
        self.form["event_name"] = obj.event_name
        self.form["venue"] = obj.venue
        # print('M2F======================>', self.form["student_name"])
        self.form["event_date"] = obj.event_date.strftime("%Y-%m-%d")
        self.form["organizer"] = obj.organizer
        # print('M2F======================>', self.form["payment_organizer"])

    # Convert form into module
    def form_to_model(self, obj):
        pk = int(self.form.get("id", 0))
        if pk > 0:
            obj.id = pk
        # print('F2M======================>', obj.id)
        obj.event_id = int(self.form.get("event_id", 0))
        obj.event_name = self.form.get("event_name", "")
        obj.venue = self.form.get("venue", "")
        # print('F2M======================>', obj.student_name)
        obj.event_date = self.form.get("event_date", "")
        obj.organizer = self.form.get("organizer", "")
        return obj

    # Validate form
    def input_validation(self):
        super().input_validation()
        inputError = self.form["inputError"]
        if DataValidator.isNull(self.form["event_id"]):
            inputError["event_id"] = "Event Id is required"
            self.form["error"] = True
        if DataValidator.isNull(self.form["event_name"]):
            inputError["event_name"] = "Event Name is required"
            self.form["error"] = True
        if DataValidator.isNull(self.form["venue"]):
            inputError["venue"] = "Venue is required"
            self.form["error"] = True
        if DataValidator.isNull(self.form["event_date"]):
            inputError["event_date"] = "Event Date is required"
            self.form["error"] = True
        if DataValidator.isNull(self.form["organizer"]):
            inputError["organizer"] = "Organizer is required"
            self.form["error"] = True
        return self.form["error"]

    # Display Role page
    def display(self, request, params={}):
        if params["id"] > 0:
            event = self.get_service().get(params["id"])
            self.model_to_form(event)
        return render(
            request,
            self.get_template(),
            {"form": self.form, "preload_data": self.preload(request)},
        )

    # Submit Role page
    def submit(self, request, _params={}):
        event = self.form_to_model(Event())
        self.get_service().save(event)
        if int(self.form["id"]) > 0:
            self.form["id"] = event.id
        self.form["error"] = False
        self.form["message"] = "Data is saved"
        return render(
            request,
            self.get_template(),
            {"form": self.form, "preload_data": self.preload(request)},
        )

    # Template html of Role page
    def get_template(self):
        return "ors/event.html"

    # Service of Role
    def get_service(self):
        return EventService()
