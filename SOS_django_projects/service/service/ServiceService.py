from service.dao.ServiceDAO import ServiceDAO
from service.service.BaseService import BaseService


class ServiceService(BaseService):
    def get_dao(self):
        return ServiceDAO()