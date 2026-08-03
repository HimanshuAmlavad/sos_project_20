from service.dao.BaseDAO import BaseDAO
from service.models import Fee


class FeeDAO(BaseDAO):
    def get_model(self):
        return Fee

    def get_Unique(self):
        return ["student_id"]

    def populate(self, obj):
        return obj