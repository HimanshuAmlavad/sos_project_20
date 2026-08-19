from service.dao.BaseDAO import BaseDAO
from service.models import Fee
from service.utility.DataValidator import DataValidator


class FeeDAO(BaseDAO):
    def get_model(self):
        return Fee

    def get_Unique(self):
        return ["student_id"]

    def populate(self, obj):
        return obj

    def get_where_conditions(self, query, params):
        value = params.get("fee_id", 0)
        if DataValidator.isNotNull(value) and value != 0:
            query = query.filter(fee_id=int(value))
        
        return query