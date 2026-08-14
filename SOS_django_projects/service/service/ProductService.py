from service.dao.ProductDAO import ProductDAO
from service.service.BaseService import BaseService


class ProductService(BaseService):
    def get_dao(self):
        return ProductDAO()