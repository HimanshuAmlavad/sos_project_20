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
        value = params.get("name", "")
        if DataValidator.isNotNull(value) and value != "":
            query = query.filter(name__istartswith=value.strip())

        value = params.get("city", "")
        if DataValidator.isNotNull(value) and value != "":
            query = query.filter(city__istartswith=value.strip())

        value = params.get("state", "")
        if DataValidator.isNotNull(value) and value != "":
            query = query.filter(state__istartswith=value.strip())
        
        return query
