from service.dao.BaseDAO import BaseDAO
from service.models import Result
from service.utility.DataValidator import DataValidator


class ResultDAO(BaseDAO):
    def get_model(self):
        return Result

    def get_Unique(self):
        return ["result_id"]

    def populate(self, obj):
        return obj

    def get_where_conditions(self, query, params):
        value = params.get("result_id", 0)
        if DataValidator.isNotNull(value) and value != 0:
            query = query.filter(result_id=int(value))
        
        return query