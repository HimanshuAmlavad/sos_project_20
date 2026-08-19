from service.dao.BaseDAO import BaseDAO
from service.models import Parking
from service.utility.DataValidator import DataValidator


class ParkingDAO(BaseDAO):
    def get_model(self):
        return Parking

    def get_Unique(self):
        return ["parking_id"]

    def populate(self, obj):
        return obj

    def get_where_conditions(self, query, params):
        value = params.get("parking_id", 0)
        if DataValidator.isNotNull(value) and value != 0:
            query = query.filter(parking_id=int(value))
        
        return query