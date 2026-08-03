from service.dao.BaseDAO import BaseDAO
from service.models import Attendance


class AttendenceDAO(BaseDAO):
    def get_Unique(self):
        return ["student_name"]

    def get_model(self):
        return Attendance

    def populate(self, obj):
        return obj