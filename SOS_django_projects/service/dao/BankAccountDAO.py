from service.dao.BaseDAO import BaseDAO
from service.models import BankAccount
from service.utility.DataValidator import DataValidator


class BankAccountDAO(BaseDAO):
    def get_model(self):
        return BankAccount

    def get_Unique(self):
        return ["account_number"]

    def populate(self, obj):
        return obj

    def get_where_conditions(self, query, params):
        value = params.get("account_number", 0)
        if DataValidator.isNotNull(value) and value != 0:
            query = query.filter(account_number=value)

        return query