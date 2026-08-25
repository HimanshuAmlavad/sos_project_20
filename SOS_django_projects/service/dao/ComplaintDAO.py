from service.dao.BaseDAO import BaseDAO
from service.models import Complaint
from service.utility.DataValidator import DataValidator


class ComplaintDAO(BaseDAO):
    def get_model(self):
        return Complaint

    def get_Unique(self):
        return ["complaint_id"]

    def populate(self, obj):
        return obj

    def get_where_conditions(self, query, params):
        value = params.get("complaint_id", 0)
        if DataValidator.isNotNull(value) and value != 0:
            query = query.filter(complaint_id=int(value))

        return query