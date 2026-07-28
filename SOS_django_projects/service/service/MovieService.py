from service.dao.MovieDAO import MovieDAO
from service.service.BaseService import BaseService


class MovieService(BaseService):
    def get_dao(self):
        return MovieDAO()