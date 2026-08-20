from service.dao.BaseDAO import BaseDAO
from service.models import Patient
from service.utility.DataValidator import DataValidator


class PatientDAO(BaseDAO):
    def get_model(self):
        return Patient

    def get_Unique(self):
        return ["patient_id"]

    def populate(self, obj):
        return obj

    def get_where_conditions(self, query, params):
        # Filter by order_id if provided
        value = params.get("patient_id", 0)
        if DataValidator.isNotNull(value) and value != 0:
            query = query.filter(patient_id=int(value))

        return query