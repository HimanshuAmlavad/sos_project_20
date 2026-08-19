from service.models import College
from .BaseDAO import BaseDAO
from service.utility.DataValidator import DataValidator


class CollegeDAO(BaseDAO):

    def get_model(self):
        return College

    def get_Unique(self):
        return ["name"]

    def populate(self, obj):
        return obj

    def get_where_conditions(self, query, params):
        value = params.get("id", 0)
        if DataValidator.isNotNull(value) and value != 0:
            query = query.filter(id=int(value))
        
        return query
