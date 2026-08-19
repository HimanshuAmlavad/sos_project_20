from service.dao.BaseDAO import BaseDAO
from service.models import Order
from service.utility.DataValidator import DataValidator


class OrderDAO(BaseDAO):
    def get_model(self):
        return Order

    def get_Unique(self):
        return ["order_id"]

    def populate(self, obj):
        return obj

    def get_where_conditions(self, query, params):
        # Filter by order_id if provided
        value = params.get("order_id", 0)
        if DataValidator.isNotNull(value) and value != 0:
            query = query.filter(order_id=int(value))
        
        # # Filter by status if provided
        # status = params.get("status", "")
        # if DataValidator.isNotNull(status):
        #     query = query.filter(status__istartswith=status.strip())
        
        # # Filter by customer_id if provided
        # customer_id = params.get("customer_id", 0)
        # if DataValidator.isNotNull(customer_id) and customer_id != 0:
        #     query = query.filter(customer_id=int(customer_id))
        
        return query