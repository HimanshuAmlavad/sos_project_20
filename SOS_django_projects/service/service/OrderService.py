from service.dao.OrderDAO import OrderDAO
from service.service.BaseService import BaseService


class OrderService(BaseService):
    def get_dao(self):
        return OrderDAO()