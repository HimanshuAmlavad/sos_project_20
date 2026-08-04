from service.dao.BaseDAO import BaseDAO
from service.models import Result


class ResultDAO(BaseDAO):
    def get_model(self):
        return Result

    def get_Unique(self):
        return ["result_id"]

    def populate(self, obj):
        return obj