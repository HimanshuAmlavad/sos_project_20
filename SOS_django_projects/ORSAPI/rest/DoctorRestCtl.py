from ORSAPI.rest.BaseRestCtl import BaseRestCtl
from service.Serializers import DoctorSerializers
from service.models import DoctorRest
from service.service.DoctorRestService import DoctorRestService
from service.utility.DataValidator import DataValidator


class DoctorRestCtl(BaseRestCtl):
    def get_model(self):
        return DoctorRest

    def get_serializer_class(self):
        return DoctorSerializers

    def get_service(self):
        return DoctorRestService()

    def input_validation(self, _data):
        errors = {}

        doctor_name = _data.get("doctorName", "")
        specialization = _data.get("specialization", "")
        contact_no = _data.get("contactNo", "")

        if DataValidator.isNull(doctor_name):
            errors["doctorName"] = "Doctor Name cannot be null"
        elif not DataValidator.isMaxLength(doctor_name, 100):
            errors["doctorName"] = "Doctor Name cannot exceed 100 characters"

        if DataValidator.isNull(specialization):
            errors["specialization"] = "Specialization cannot be null"
        elif not DataValidator.isMaxLength(specialization, 100):
            errors["specialization"] = "Specialization cannot exceed 100 characters"

        if DataValidator.isNull(contact_no):
            errors["contactNo"] = "Contact No. cannot be null"
        elif not DataValidator.isMaxLength(contact_no, 10):
            errors["contactNo"] = "Contact No. cannot exceed 10 characters"

        return errors
