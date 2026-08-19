from service.models import Role
from .BaseDAO import BaseDAO
from service.utility.DataValidator import DataValidator


class RoleDAO(BaseDAO):

    def get_model(self):
        return Role

    def get_Unique(self):
        return ["name"]

    def populate(self, obj):
        return obj

    def get_where_conditions(self, query, params):
        value = params.get("id", 0)
        if DataValidator.isNotNull(value) and value != 0:
            query = query.filter(id=int(value))
        
        return query