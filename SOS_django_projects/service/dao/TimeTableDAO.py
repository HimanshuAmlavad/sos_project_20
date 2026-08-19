from service.models import TimeTable, Course, Subject
from .BaseDAO import BaseDAO
from service.utility.DataValidator import DataValidator


class TimeTableDAO(BaseDAO):

    def get_model(self):
        return TimeTable

    def get_Unique(self):
        return None

    def populate(self, obj):
        try:
            course = Course.objects.get(id=obj.course_id)
            obj.course_name = course.name
        except Course.DoesNotExist:
            obj.course_name = ""
        try:
            subject = Subject.objects.get(id=obj.subject_id)
            obj.subject_name = subject.name
        except Subject.DoesNotExist:
            obj.subject_name = ""
        return obj

    def get_where_conditions(self, query, params):
        value = params.get("id", 0)
        if DataValidator.isNotNull(value) and value != 0:
            query = query.filter(id=int(value))
        
        return query
