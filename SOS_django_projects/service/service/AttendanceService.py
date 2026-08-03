from service.dao.AttendanceDAO import AttendenceDAO
from service.service.BaseService import BaseService


class AttendanceService(BaseService):
    def get_dao(self):
        return AttendenceDAO()