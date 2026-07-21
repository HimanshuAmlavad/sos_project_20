from service.dao.BaseDAO import BaseDAO
from service.models import VoiceCommand


class VoiceCommandDAO(BaseDAO):
    def get_model(self):
        return VoiceCommand

    def get_Unique(self):
        return ["command_id"]

    def populate(self, obj):
        return obj