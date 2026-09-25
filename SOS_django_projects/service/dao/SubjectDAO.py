from service.models import Subject, Course
from service.utility.DataValidator import DataValidator
from .BaseDAO import BaseDAO, logger


class SubjectDAO(BaseDAO):

    def get_model(self):
        return Subject

    def get_Unique(self):
        return ["name"]

    def populate(self, obj):
        try:
            course = Course.objects.get(id=obj.course_ID)
            obj.courseName = course.name
        except Course.DoesNotExist:
            obj.courseName = ""
        return obj

    def get_where_conditions(self, query, params):
        value = params.get("subject", "")
        if DataValidator.isNotNull(value) and value != "":
            query = query.filter(subject__istartswith=value.strip())

        value = params.get("description", "")
        if DataValidator.isNotNull(value) and value != "":
            query = query.filter(description__istartswith=value.strip())

        value = params.get("dob", "")
        logger.info(f"course======>{value}")
        if DataValidator.isNotNull(value) and value != "":
            query = query.filter(dob__istartswith=value.strip())

        value = params.get("course_ID", "")
        logger.info(f"course======>{value}")
        if DataValidator.isNotNull(value) and value != "":
            query = query.filter(course_ID=int(value))
        return query
