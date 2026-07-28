from service.dao.BaseDAO import BaseDAO
from service.models import Movie


class MovieDAO(BaseDAO):
    def get_model(self):
        return Movie

    def get_Unique(self):
        return ["movie_name"]

    def populate(self, obj):
        return obj