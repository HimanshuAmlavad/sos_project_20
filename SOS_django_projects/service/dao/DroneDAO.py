from service.dao.BaseDAO import BaseDAO
from service.models import Drone
from service.utility.DataValidator import DataValidator


class DroneDAO(BaseDAO):
    def get_model(self):
        return Drone

    def get_Unique(self):
        return ['drone_id']

    def populate(self, obj):
        return obj

    def get_where_conditions(self, query, params):
        value = params.get("drone_id", 0)
        if DataValidator.isNotNull(value) and value != 0:
            query = query.filter(drone_id=int(value))
        
        return query