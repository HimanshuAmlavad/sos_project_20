from service.dao.BaseDAO import BaseDAO
from service.models import Hotel
from service.utility.DataValidator import DataValidator


class HotelDAO(BaseDAO):
    def get_model(self):
        return Hotel

    def get_Unique(self):
        return ["hotel_id"]

    def populate(self, obj):
        return obj

    def get_where_conditions(self, query, params):

        value = params.get("hotel_id", 0)
        if DataValidator.isNotNull(value) and value != 0:
            query = query.filter(hotel_id=int(value))

        return query