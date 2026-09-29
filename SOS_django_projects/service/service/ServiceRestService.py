from service.dao.ServiceRestDAO import ServiceRestDAO
from service.service.BaseService import BaseService


class ServiceRestService(BaseService):
    def get_dao(self):
        return ServiceRestDAO()