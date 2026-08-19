from service.dao.BaseDAO import BaseDAO
from service.models import Movie
from service.utility.DataValidator import DataValidator


class MovieDAO(BaseDAO):
    def get_model(self):
        return Movie

    def get_Unique(self):
        return ["movie_name"]

    def populate(self, obj):
        return obj

    def get_where_conditions(self, query, params):
        value = params.get("movie_id", 0)
        if DataValidator.isNotNull(value) and value != 0:
            query = query.filter(movie_id=int(value))
        
        return query