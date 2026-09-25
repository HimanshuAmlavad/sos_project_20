from service.models import Marksheet, Student, Subject
from .BaseDAO import BaseDAO
from service.utility.DataValidator import DataValidator


class MarksheetDAO(BaseDAO):

    def get_model(self):
        return Marksheet

    def get_Unique(self):
        return ["rollNumber"]

    def populate(self, obj):
        if obj.student_id:
            try:
                student = Student.objects.get(id=obj.student_id)
                obj.student_Name = student.firstName + " " + student.lastName
            except Student.DoesNotExist:
                obj.student_Name = ""
        else:
            obj.student_Name = ""
        return obj

    def get_where_conditions(self, query, params):
        value = params.get("rollNumber", "")
        if DataValidator.isNotNull(value) and value != "":
            query = query.filter(rollNumber__istartswith=value.strip())

        value = params.get("name", "")
        if DataValidator.isNotNull(value) and value != "":
            query = query.filter(name__istartswith=value.strip())

        value = params.get("year", 0)
        if DataValidator.isNotNull(value) and value != 0:
            query = query.filter(year__istartswith=int(value))

        return query
