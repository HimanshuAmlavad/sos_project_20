from service.dao.CreditCardDAO import CreditCardDAO
from service.service.BaseService import BaseService


class CreditCardService(BaseService):
    def get_dao(self):
        return CreditCardDAO()