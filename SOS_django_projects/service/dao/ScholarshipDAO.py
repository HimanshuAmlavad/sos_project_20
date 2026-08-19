from service.dao.BaseDAO import BaseDAO
from service.models import Scholarship
from service.utility.DataValidator import DataValidator


class ScholarshipDAO(BaseDAO):
    def get_model(self):
        return Scholarship

    def get_Unique(self):
        return ["scholarship_id"]

    def populate(self, obj):
        return obj

    def get_where_conditions(self, query, params):
        value = params.get("scholarship_id", 0)
        if DataValidator.isNotNull(value) and value != 0:
            query = query.filter(scholarship_id=int(value))
        
        return query