from service.dao.PatientDAO import PatientDAO
from service.service.BaseService import BaseService


class PatientService(BaseService):
    def get_dao(self):
        return PatientDAO()