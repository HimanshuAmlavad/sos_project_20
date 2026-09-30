from service.dao.BaseDAO import BaseDAO
from service.models import VendorRest
from service.utility.DataValidator import DataValidator


class VendorRestDAO(BaseDAO):
    def get_model(self):
        return VendorRest

    def get_Unique(self):
        return ["id"]

    def populate(self, obj):
        return obj

    def get_where_conditions(self, query, params):
        value = params.get("vendorName", "")
        if DataValidator.isNotNull(value) and value != "":
            query = query.filter(vendorName__istartswith = value.strip())

        value = params.get("serviceType", "")
        if DataValidator.isNotNull(value) and value != "":
            query = query.filter(serviceType__istartswith=value.strip())

        return query