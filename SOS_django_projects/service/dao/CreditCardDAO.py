from service.dao.BaseDAO import BaseDAO
from service.models import CreditCard
from service.utility.DataValidator import DataValidator


class CreditCardDAO(BaseDAO):
    def get_model(self):
        return CreditCard

    def get_Unique(self):
        return ["card_number","card_id"]

    def populate(self, obj):
        return obj

    def get_where_conditions(self, query, params):
        value = params.get("card_id", 0)
        if DataValidator.isNotNull(value) and value != 0:
            query = query.filter(card_id=int(value))
        
        return query
