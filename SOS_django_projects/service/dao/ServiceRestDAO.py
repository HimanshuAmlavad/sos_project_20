from service.dao.BaseDAO import BaseDAO
from service.models import ServiceRest
from service.utility.DataValidator import DataValidator


class ServiceRestDAO(BaseDAO):
    def get_model(self):
        return ServiceRest

    def get_Unique(self):
        return ["serviceName"]

    def populate(self, obj):
        return obj

    def get_where_conditions(self, query, params):
        value = params.get("serviceName", "")
        if DataValidator.isNotNull(value) and value != "":
            query = query.filter(serviceName__istartswith = value.strip())

        value = params.get("description", "")
        if DataValidator.isNotNull(value) and value != "":
            query = query.filter(description__istartswith=value.strip())

        value = params.get("serviceCategory", "")

        if DataValidator.isNotNull(value) and value != "":
            query = query.filter(serviceCategory__istartswith=value.strip())
        return query