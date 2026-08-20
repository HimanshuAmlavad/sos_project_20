from django.shortcuts import render
from service.models import Patient
from ORS.ctl.BaseCtl import BaseCtl
from ORS.utility.HtmlUtility import HtmlUtility
from service.service.PatientService import PatientService
from service.utility.DataValidator import DataValidator


class PatientCtl(BaseCtl):

    def preload(self, request):
        doctor_list = [
            "Duty Dr.",
            "Dr. Amit Sharma",
            "Dr. Suraj Rathi",
             ]

        # print("Preload status:", repr(self.form.get("status")))
        self.preload_data["doctor_select"] = HtmlUtility.get_list_from_list(
            "doctorName",
            self.form.get("doctor_name"),
            doctor_list,
        )
        # Also make preload available under form for templates using `form.preload_data`
        self.form["preload_data"] = self.preload_data
        return self.preload_data

    # Populate Form from HTTP Request
    def request_to_form(self, request):
        self.form["id"] = int(request.get("id", 0) or 0)
        # print('R2F =====================>', self.form["id"])
        self.form["patient_id"] = request.get("patientId", 0)
        self.form["patient_name"] = request.get("patientName", "")
        self.form["disease"] = request.get("disease", "")
        # print('R2F =====================>', self.form["student_name"])
        self.form["admission_date"] = request.get("admissionDate", "")
        self.form["doctor_name"] = request.get("doctorName", "")
        print('R2F =====================>', self.form["doctor_name"])

    # Populate Form from Model
    def model_to_form(self, obj):
        if obj == None:
            return
        self.form["id"] = obj.id
        # print('M2F======================>', self.form["id"])
        self.form["patient_id"] = obj.patient_id
        self.form["patient_name"] = obj.patient_name
        self.form["disease"] = obj.disease
        # print('M2F======================>', self.form["student_name"])
        self.form["admission_date"] = obj.admission_date.strftime("%Y-%m-%d")
        self.form["doctor_name"] = obj.doctor_name
        # print('M2F======================>', self.form["payment_doctor_name"])

    # Convert form into module
    def form_to_model(self, obj):
        pk = int(self.form.get("id", 0))
        if pk > 0:
            obj.id = pk
        # print('F2M======================>', obj.id)
        obj.patient_id = int(self.form.get("patient_id", 0))
        obj.patient_name = self.form.get("patient_name", "")
        obj.disease = self.form.get("disease", 0)
        # print('F2M======================>', obj.student_name)
        obj.admission_date = self.form.get("admission_date", "")
        obj.doctor_name = self.form.get("doctor_name", "")
        return obj

    # Validate form
    def input_validation(self):
        super().input_validation()
        inputError = self.form["inputError"]
        if DataValidator.isNull(self.form["patient_id"]):
            inputError["patient_id"] = "Patient Id is required"
            self.form["error"] = True
        if DataValidator.isNull(self.form["patient_name"]):
            inputError["patient_name"] = "Patient Name is required"
            self.form["error"] = True
        if DataValidator.isNull(self.form["disease"]):
            inputError["disease"] = "Disease is required"
            self.form["error"] = True
        if DataValidator.isNull(self.form["admission_date"]):
            inputError["admission_date"] = "Admission Date is required"
            self.form["error"] = True
        if DataValidator.isNull(self.form["doctor_name"]):
            inputError["doctor_name"] = "Doctor Name is required"
            self.form["error"] = True
        return self.form["error"]

    # Display Role page
    def display(self, request, params={}):
        if params["id"] > 0:
            patient = self.get_service().get(params["id"])
            self.model_to_form(patient)
        return render(
            request,
            self.get_template(),
            {"form": self.form, "preload_data": self.preload(request)},
        )

    # Submit Role page
    def submit(self, request, _params={}):
        patient = self.form_to_model(Patient())
        self.get_service().save(patient)
        if int(self.form["id"]) > 0:
            self.form["id"] = patient.id
        self.form["error"] = False
        self.form["message"] = "Data is saved"
        return render(
            request,
            self.get_template(),
            {"form": self.form, "preload_data": self.preload(request)},
        )

    # Template html of Role page
    def get_template(self):
        return "ors/patient.html"

    # Service of Role
    def get_service(self):
        return PatientService()
