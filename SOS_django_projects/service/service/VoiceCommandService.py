from service.dao.VoiceCommandDAO import VoiceCommandDAO
from service.service.BaseService import BaseService


class VoiceCommandService(BaseService):
    def get_dao(self):
        return VoiceCommandDAO()