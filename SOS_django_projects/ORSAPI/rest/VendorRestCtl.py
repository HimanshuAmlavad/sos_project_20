from ORSAPI.rest.BaseRestCtl import BaseRestCtl
from service.Serializers import  VendorSerializers
from service.models import VendorRest
from service.service.VendorRestService import VendorRestService
from service.utility.DataValidator import DataValidator


class VendorRestCtl(BaseRestCtl):
    def get_model(self):
        return VendorRest

    def get_serializer_class(self):
        return VendorSerializers

    def get_service(self):
        return VendorRestService()

    def input_validation(self, _data):
        errors = {}

        vendor_name = _data.get("vendorName", "")
        mobile_no = _data.get("mobileNo", "")
        address = _data.get("address", "")
        service_type = _data.get("serviceType", "")

        if DataValidator.isNull(vendor_name):
            errors["vendorName"] = "Service Name cannot be null"
        elif not DataValidator.isMaxLength(vendor_name, 100):
            errors["vendorName"] = "Service Name cannot exceed 100 characters"

        if DataValidator.isNull(mobile_no):
            errors["mobileNo"] = "Description cannot be null"
        elif not DataValidator.isMaxLength(mobile_no, 10):
            errors["mobileNo"] = "Mobile No cannot exceed 10 number"

        if DataValidator.isNull(address):
            errors["address"] = "Address cannot be null"
        elif not DataValidator.isMaxLength(address, 255):
            errors["address"] = "Address cannot exceed 100 characters"

        if DataValidator.isNull(service_type):
            errors["serviceType"] = "Service Type cannot be null"
        elif not DataValidator.isMaxLength(service_type, 100):
            errors["serviceType"] = "Service Type cannot exceed 100 characters"

        return errors
