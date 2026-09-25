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
        value = params.get("firstName", "")
        if DataValidator.isNotNull(value) and value != "":
            query = query.filter(firstName__istartswith=value.strip())

        value = params.get("lastName", "")
        if DataValidator.isNotNull(value) and value != "":
            query = query.filter(lastName__istartswith=value.strip())

        value = params.get("email", "")
        if DataValidator.isNotNull(value) and value != "":
            query = query.filter(email__istartswith=value.strip())

        value = params.get("collegeName", "")
        if DataValidator.isNotNull(value) and value != 0:
            query = query.filter(collegeName__istartswith=value.strip())
        
        return query
