from service.dao.VenderRestDAO import VendorRestDAO
from service.service.BaseService import BaseService


class VendorRestService(BaseService):
    def get_dao(self):
        return VendorRestDAO()