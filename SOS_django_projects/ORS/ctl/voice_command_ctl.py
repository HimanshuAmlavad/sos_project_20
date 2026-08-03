from django.shortcuts import render

from ORS.ctl.BaseCtl import BaseCtl
from ORS.utility.HtmlUtility import HtmlUtility
from service.models import VoiceCommand
from service.service.VoiceCommandService import VoiceCommandService
from service.utility.DataValidator import DataValidator


class VoiceCommandCtl(BaseCtl):

    def preload(self, request):
        status_list = [ "Pending", "Processing", "Executed", "Failed"]
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
        self.form["command_id"] = request.get("commandId", 0)
        self.form["command_code"] = request.get("commandCode", "")
        self.form["user_name"] = request.get("userName", "")
        self.form["command_text"] = request.get("commandText", "")
        print("R2F ====================>",self.form['command_text'])
        self.form["status"] = request.get("status", "")

    # Populate Form from Model
    def model_to_form(self, obj):
        if obj == None:
            return
        self.form["id"] = obj.id
        # print('M2F======================>', self.form["id"])
        self.form["command_id"] = obj.command_id
        self.form["command_code"] = obj.command_code
        self.form["user_name"] = obj.user_name
        self.form["command_text"] = obj.command_text
        self.form["status"] = obj.status
        print('M2F======================>', self.form["status"])


    # Convert form into module
    def form_to_model(self, obj):
        pk = int(self.form.get("id", 0))
        if pk > 0:
            obj.id = pk
        print('F2M======================>', obj.id)
        obj.command_id = int(self.form.get("command_id", 0))
        obj.command_code = self.form.get("command_code", "")
        obj.user_name = self.form.get("user_name", "")
        obj.command_text = self.form.get("command_text", "")
        obj.status = self.form.get("status", "")
        return obj

    # Validate form
    def input_validation(self):
        super().input_validation()
        inputError = self.form["inputError"]
        if DataValidator.isNull(self.form["command_id"]):
            inputError["command_id"] = "Command Id is required"
            self.form["error"] = True
        if DataValidator.isNull(self.form["command_code"]):
            inputError["command_code"] = "Command Code is required"
            self.form["error"] = True
        if DataValidator.isNull(self.form["user_name"]):
            inputError["user_name"] = "User Name is required"
            self.form["error"] = True
        if DataValidator.isNull(self.form["command_text"]):
            inputError["command_text"] = "Command Text is required"
            self.form["error"] = True
        if DataValidator.isNull(self.form["status"]):
            inputError["status"] = "Status is required"
            self.form["error"] = True
        return self.form["error"]

    # Display Role page
    def display(self, request, params={}):
        if params["id"] > 0:
            command = self.get_service().get(params["id"])
            self.model_to_form(command)
        return render(
            request,
            self.get_template(),
            {"form": self.form, "preload_data": self.preload(request)},
        )

    # Submit Role page
    def submit(self, request, _params={}):
        command = self.form_to_model(VoiceCommand())
        self.get_service().save(command)
        if int(self.form["id"]) > 0:
            self.form["id"] = command.id
        self.form["error"] = False
        self.form["message"] = "Data is saved"
        return render(
            request,
            self.get_template(),
            {"form": self.form, "preload_data": self.preload(request)},
        )

    # Template html of Role page
    def get_template(self):
        return "ors/voicecommand.html"

    # Service of Role
    def get_service(self):
        return VoiceCommandService()
