from service.dao.AtmDAO import AtmDAO
from service.service.BaseService import BaseService


class AtmService(BaseService):
    def get_dao(self):
        return AtmDAO()