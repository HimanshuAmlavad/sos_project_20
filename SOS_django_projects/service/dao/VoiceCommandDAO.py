from service.dao.BaseDAO import BaseDAO
from service.models import VoiceCommand
from service.utility.DataValidator import DataValidator


class VoiceCommandDAO(BaseDAO):
    def get_model(self):
        return VoiceCommand

    def get_Unique(self):
        return ["command_id"]

    def populate(self, obj):
        return obj

    def get_where_conditions(self, query, params):
        value = params.get("command_id", 0)
        if DataValidator.isNotNull(value) and value != 0:
            query = query.filter(command_id=int(value))
        
        return query