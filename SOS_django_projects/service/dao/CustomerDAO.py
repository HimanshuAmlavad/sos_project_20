from service.dao.BaseDAO import BaseDAO
from service.models import Customer
from service.utility.DataValidator import DataValidator


class CustomerDAO(BaseDAO):
    def get_model(self):
        return Customer

    def get_Unique(self):
        return ["customer_id","email","phone_number"]

    def populate(self, obj):
        return obj

    def get_where_conditions(self, query, params):
        value = params.get("customer_id", 0)
        if DataValidator.isNotNull(value) and value != 0:
            query = query.filter(customer_id=int(value))

        return query