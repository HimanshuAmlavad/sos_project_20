from service.dao.BaseDAO import BaseDAO
from service.models import CreditCard


class CreditCardDAO(BaseDAO):
    def get_model(self):
        return CreditCard

    def get_Unique(self):
        return ["card_number","card_id"]

    def populate(self, obj):
        return obj
