from service.dao.BaseDAO import BaseDAO
from service.models import Vehicle
from service.utility.DataValidator import DataValidator


class VehicleDAO(BaseDAO):
    def get_model(self):
        return Vehicle

    def get_Unique(self):
        return ["vehicle_no"]

    def populate(self, obj):
        return obj

    def get_where_conditions(self, query, params):
        value = params.get("vehicle_id", 0)
        if DataValidator.isNotNull(value) and value != 0:
            query = query.filter(vehicle_id=int(value))
        
        return query