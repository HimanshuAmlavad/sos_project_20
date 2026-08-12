from service.dao.BaseDAO import BaseDAO
from service.models import ATM


class AtmDAO(BaseDAO):
    def get_model(self):
        return ATM

    def get_Unique(self):
        return ["atm_id"]

    def populate(self, obj):
        return obj