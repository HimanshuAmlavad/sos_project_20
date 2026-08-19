from service.dao.BaseDAO import BaseDAO
from service.models import ATM
from service.utility.DataValidator import DataValidator


class AtmDAO(BaseDAO):
    def get_model(self):
        return ATM

    def get_Unique(self):
        return ["atm_id"]

    def populate(self, obj):
        return obj

    def get_where_conditions(self, query, params):
        value = params.get("atm_id", 0)
        if DataValidator.isNotNull(value) and value != 0:
            query = query.filter(atm_id=int(value))
        
        return query