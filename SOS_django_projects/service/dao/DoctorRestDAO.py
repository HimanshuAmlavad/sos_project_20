from service.dao.BaseDAO import BaseDAO
from service.models import DoctorRest
from service.utility.DataValidator import DataValidator


class DoctorRestDAO(BaseDAO):
    def get_model(self):
        return DoctorRest

    def get_Unique(self):
        return ["id"]

    def populate(self, obj):
        return obj

    def get_where_conditions(self, query, params):
        value = params.get("doctorName","")
        if DataValidator.isNotNull(value):
            query = query.filter(doctorName__istartswith=value.strip())

        value = params.get("specialization","")
        if DataValidator.isNotNull(""):
            query = query.filter(specialization__istartwith=value.strip())

        return query