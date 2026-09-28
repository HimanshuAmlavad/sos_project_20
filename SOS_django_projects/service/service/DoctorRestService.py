from service.dao.DoctorRestDAO import DoctorRestDAO
from service.service.BaseService import BaseService


class DoctorRestService(BaseService):
    def get_dao(self):
        return DoctorRestDAO()