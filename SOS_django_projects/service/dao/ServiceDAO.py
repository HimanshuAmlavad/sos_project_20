from service.dao.BaseDAO import BaseDAO
from service.models import Service
from service.utility.DataValidator import DataValidator


class ServiceDAO(BaseDAO):
    def get_model(self):
        return Service

    def get_Unique(self):
        return ["service_name"]

    def populate(self, obj):
        return obj

    def get_where_conditions(self, query, params):
        value = params.get("service_name", "")

        if DataValidator.isNotNull(value) and value != "":
            query = query.filter(service_name__istartswith = value.strip())

        return query