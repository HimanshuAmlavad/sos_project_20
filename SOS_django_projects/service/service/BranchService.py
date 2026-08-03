from service.dao.BranchDAO import BranchDAO
from service.service.BaseService import BaseService


class BranchService(BaseService):
    def get_dao(self):
        return BranchDAO()