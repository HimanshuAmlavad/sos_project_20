from service.dao.BaseDAO import BaseDAO
from service.models import Doctor
from service.utility.DataValidator import DataValidator


class DoctorDAO(BaseDAO):
    def get_model(self):
        return Doctor

    def get_Unique(self):
        return ["doctor_id"]

    def populate(self, obj):
        return obj

    def get_where_conditions(self, query, params):
        value = params.get("doctor_name","")
        if DataValidator.isNotNull(value) and value != "":
            query = query.filter(doctor_name__istartswith=value.strip())

        return query