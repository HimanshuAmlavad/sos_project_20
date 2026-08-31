from service.dao.EventDAO import EventDAO
from service.service.BaseService import BaseService


class EventService(BaseService):
    def get_dao(self):
        return EventDAO()