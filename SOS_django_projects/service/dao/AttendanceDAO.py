from service.dao.BaseDAO import BaseDAO
from service.models import Attendance
from service.utility.DataValidator import DataValidator


class AttendenceDAO(BaseDAO):
    def get_Unique(self):
        return ["student_name"]

    def get_model(self):
        return Attendance

    def populate(self, obj):
        return obj

    def get_where_conditions(self, query, params):
        value = params.get("attendance_id", 0)
        if DataValidator.isNotNull(value) and value != 0:
            query = query.filter(attendance_id=int(value))
        
        return query