from service.dao.BaseDAO import BaseDAO
from service.models import Vendor
from service.utility.DataValidator import DataValidator


class VendorDAO(BaseDAO):
    def get_Unique(self):
        return ["vendor_name"]

    def get_model(self):
        return Vendor

    def populate(self, obj):
        return obj

    def get_where_conditions(self, query, params):
        value = params.get("vendor_name","")

        if DataValidator.isNotNull(value) and value != "":
            query = query.filter(vander_name__istartswith=value.strip())

        return query