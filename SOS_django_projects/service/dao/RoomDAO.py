from service.dao.BaseDAO import BaseDAO
from service.models import Room
from service.utility.DataValidator import DataValidator


class RoomDAO(BaseDAO):
    def get_model(self):
        return Room

    def get_Unique(self):
        return ["room_no"]

    def populate(self, obj):
        return obj

    def get_where_conditions(self, query, params):
        value = params.get("room_no", 0)
        if DataValidator.isNotNull(value) and value != 0:
            query = query.filter(room_no = int(value))

        return query