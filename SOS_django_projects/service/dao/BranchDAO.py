from service.dao.BaseDAO import BaseDAO
from service.models import Branch


class BranchDAO(BaseDAO):
    def get_model(self):
        return Branch

    def get_Unique(self):
        return ["branch_name"]

    def populate(self, obj):
        return obj
