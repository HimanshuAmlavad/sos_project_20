from service.models import Course
from .BaseDAO import BaseDAO
from service.utility.DataValidator import DataValidator


class CourseDAO(BaseDAO):

    def get_model(self):
        return Course

    def get_Unique(self):
        return ["name"]

    def populate(self, obj):
        return obj

    def get_where_conditions(self, query, params):
        value = params.get("name", "")
        if DataValidator.isNotNull(value) and value != "":
            query = query.filter(name__istartswith=value.strip())

        value = params.get("description", "")
        if DataValidator.isNotNull(value) and value != "":
            query = query.filter(description__istartswith=value.strip())

        value = params.get("duration", "")
        if DataValidator.isNotNull(value) and value != "":
            query = query.filter(duration__istartswith=value.strip())
        
        return query
