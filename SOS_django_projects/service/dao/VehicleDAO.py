from service.dao.BaseDAO import BaseDAO
from service.models import Vehicle


class VehicleDAO(BaseDAO):
    def get_model(self):
        return Vehicle

    def get_Unique(self):
        return ["vehicle_no"]

    def populate(self, obj):
        return obj