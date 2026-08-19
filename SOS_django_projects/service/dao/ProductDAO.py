from service.dao.BaseDAO import BaseDAO
from service.models import Product
from service.utility.DataValidator import DataValidator


class ProductDAO(BaseDAO):
    def get_model(self):
        return Product

    def get_Unique(self):
        return ["product_id"]

    def populate(self, obj):
        return obj

    def get_where_conditions(self, query, params):
        value = params.get("product_id", 0)
        if DataValidator.isNotNull(value) and value != 0:
            query = query.filter(product_id=int(value))
        
        return query