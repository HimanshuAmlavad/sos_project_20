from service.dao.BaseDAO import BaseDAO
from service.models import Payment
from service.utility.DataValidator import DataValidator


class PaymentDAO(BaseDAO):
    def get_model(self):
        return Payment

    def get_Unique(self):
        return ["payment_id"]

    def populate(self, obj):
        return obj

    def get_where_conditions(self, query, params):
        value = params.get("payment_id", 0)
        if DataValidator.isNotNull(value) and value != 0:
            query = query.filter(payment_id=int(value))
        return query

