from ORSAPI.rest.BaseRestCtl import BaseRestCtl
from service.Serializers import  ServiceSerializers
from service.models import ServiceRest
from service.service.ServiceRestService import ServiceRestService
from service.utility.DataValidator import DataValidator


class ServiceRestCtl(BaseRestCtl):
    def get_model(self):
        return ServiceRest

    def get_serializer_class(self):
        return ServiceSerializers

    def get_service(self):
        return ServiceRestService()

    def input_validation(self, _data):
        errors = {}

        service_name = _data.get("serviceName", "")
        price = int(_data.get("price", 0))
        description = _data.get("description", "")
        service_category = _data.get("serviceCategory", "")

        if DataValidator.isNull(service_name):
            errors["serviceName"] = "Service Name cannot be null"
        elif not DataValidator.isMaxLength(service_name, 100):
            errors["serviceName"] = "Service Name cannot exceed 100 characters"

        if DataValidator.isNull(price):
            errors["price"] = "Price cannot be null"
        elif not DataValidator.isInteger(price):
            errors["price"] = "Integer Value is required"

        if DataValidator.isNull(description):
            errors["description"] = "Description cannot be null"
        elif not DataValidator.isMaxLength(description, 500):
            errors["description"] = "Description cannot exceed 100 characters"

        if DataValidator.isNull(service_category):
            errors["serviceCategory"] = "Service Category cannot be null"
        elif not DataValidator.isMaxLength(service_category, 100):
            errors["serviceCategory"] = "Service Category cannot exceed 100 characters"

        return errors
