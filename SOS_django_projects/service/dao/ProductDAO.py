from service.dao.BaseDAO import BaseDAO
from service.models import Product


class ProductDAO(BaseDAO):
    def get_model(self):
        return Product

    def get_Unique(self):
        return ["product_id"]

    def populate(self, obj):
        return obj