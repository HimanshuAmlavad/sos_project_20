from service.dao.BaseDAO import BaseDAO
from service.models import Event
from service.utility.DataValidator import DataValidator


class EventDAO(BaseDAO):
    def get_Unique(self):
        return ["event_id"]

    def get_model(self):
        return Event

    def populate(self, obj):
        return obj

    def get_where_conditions(self, query, params):
        value = params.get('event_id',0)
        if DataValidator.isNotNull(value) or value != 0:
            query = query.filter(event_id=int(value))

            return query