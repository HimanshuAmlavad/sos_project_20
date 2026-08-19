from service.models import Student, College
from .BaseDAO import BaseDAO
from service.utility.DataValidator import DataValidator


class StudentDAO(BaseDAO):

    def get_model(self):
        return Student

    def get_Unique(self):
        return None

    def populate(self, obj):
        try:
            college = College.objects.get(id=obj.college_ID)
            obj.collegeName = college.name
        except College.DoesNotExist:
            obj.collegeName = ""
        return obj

    def get_where_conditions(self, query, params):
        value = params.get("id", 0)
        if DataValidator.isNotNull(value) and value != 0:
            query = query.filter(id=int(value))
        
        return query
