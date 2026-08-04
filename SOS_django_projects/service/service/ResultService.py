from service.dao.ResultDAO import ResultDAO
from service.service.BaseService import BaseService


class ResultService(BaseService):
    def get_dao(self):
        return ResultDAO()