from service.models import Faculty, College, Course, Subject
from .BaseDAO import BaseDAO
from service.utility.DataValidator import DataValidator


class FacultyDAO(BaseDAO):

    def get_model(self):
        return Faculty

    def get_Unique(self):
        return None

    def populate(self, obj):
        try:
            college = College.objects.get(id=obj.college_ID)
            obj.collegeName = college.name
        except College.DoesNotExist:
            obj.collegeName = ""
        try:
            course = Course.objects.get(id=obj.course_ID)
            obj.courseName = course.name
        except Course.DoesNotExist:
            obj.courseName = ""
        try:
            subject = Subject.objects.get(id=obj.subject_ID)
            obj.subjectName = subject.name
        except Subject.DoesNotExist:
            obj.subjectName = ""
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
        if DataValidator.isNotNull(value) and value != "":
            query = query.filter(collegeName__istartswith=value.strip())

        value = params.get("courseName", "")
        if DataValidator.isNotNull(value) and value != "":
            query = query.filter(courseName__istartswith=value.strip())

        return query
