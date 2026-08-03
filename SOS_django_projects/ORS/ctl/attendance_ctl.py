from django.shortcuts import render
from service.models import Attendance
from ORS.ctl.BaseCtl import BaseCtl
from ORS.utility.HtmlUtility import HtmlUtility
from service.service.AttendanceService import AttendanceService
from service.utility.DataValidator import DataValidator


class AttendanceCtl(BaseCtl):

    def preload(self, request):
        status_list = ["Present",
                       "Absent",
                       "Leave",]
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
        self.form["attendance_id"] = request.get("attendanceId", 0)
        self.form["student_id"] = request.get("studentId", 0)
        self.form["student_name"] = request.get("studentName", "")
        # print('R2F =====================>', self.form["student_name"])
        self.form["attendance_date"] = request.get("attendanceDate", "")
        self.form["student_class"] = request.get("studentClass", "")
        self.form["status"] = request.get("status", "")
        print('R2F =====================>', self.form["status"])


    # Populate Form from Model
    def model_to_form(self, obj):
        if obj == None:
            return
        self.form["id"] = obj.id
        # print('M2F======================>', self.form["id"])
        self.form["attendance_id"] = obj.attendance_id
        self.form["student_id"] = obj.student_id
        self.form["student_name"] = obj.student_name
        print('M2F======================>', self.form["student_name"])
        self.form["attendance_date"] = obj.attendance_date.strftime("%Y-%m-%d")
        self.form["student_class"] = obj.student_class
        self.form["status"] = obj.status
        # print('M2F======================>', self.form["payment_status"])

    # Convert form into module
    def form_to_model(self, obj):
        pk = int(self.form.get("id", 0))
        if pk > 0:
            obj.id = pk
        print('F2M======================>', obj.id)
        obj.attendance_id = int(self.form.get("attendance_id", 0))
        obj.student_id = self.form.get("student_id", "")
        obj.student_name = self.form.get("student_name", "")
        print('F2M======================>', obj.student_name)
        obj.attendance_date = self.form.get("attendance_date", "")
        obj.student_class = self.form.get("student_class", "")
        obj.status = self.form.get("status", "")
        return obj

    # Validate form
    def input_validation(self):
        super().input_validation()
        inputError = self.form["inputError"]
        if DataValidator.isNull(self.form["attendance_id"]):
            inputError["attendance_id"] = "Attendance Id is required"
            self.form["error"] = True
        if DataValidator.isNull(self.form["student_id"]):
            inputError["student_id"] = "Student Id is required"
            self.form["error"] = True
        if DataValidator.isNull(self.form["student_name"]):
            inputError["student_name"] = "Student Name is required"
            self.form["error"] = True
        if DataValidator.isNull(self.form["attendance_date"]):
            inputError["attendance_date"] = "Attendance Date is required"
            self.form["error"] = True
        if DataValidator.isNull(self.form["student_class"]):
            inputError["student_class"] = "Student Class is required"
            self.form["error"] = True
        if DataValidator.isNull(self.form["status"]):
            inputError["status"] = "Status is required"
            self.form["error"] = True
        return self.form["error"]

    # Display Role page
    def display(self, request, params={}):
        if params["id"] > 0:
            attendance = self.get_service().get(params["id"])
            self.model_to_form(attendance)
        return render(
            request,
            self.get_template(),
            {"form": self.form, "preload_data": self.preload(request)},
        )

    # Submit Role page
    def submit(self, request, _params={}):
        attendance = self.form_to_model(Attendance())
        self.get_service().save(attendance)
        if int(self.form["id"]) > 0:
            self.form["id"] = attendance.id
        self.form["error"] = False
        self.form["message"] = "Data is saved"
        return render(
            request,
            self.get_template(),
            {"form": self.form, "preload_data": self.preload(request)},
        )

    # Template html of Role page
    def get_template(self):
        return "ors/attendance.html"

    # Service of Role
    def get_service(self):
        return AttendanceService()
