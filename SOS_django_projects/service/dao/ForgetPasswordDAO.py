from service.models import User, Role
from .BaseDAO import BaseDAO
from service.utility.DataValidator import DataValidator


class ForgetPasswordDAO(BaseDAO):

    def get_model(self):
        return User

    def get_Unique(self):
        return ["login"]

    def populate(self, obj):
        try:
            role = Role.objects.get(id=obj.role_id)
            obj.role_Name = role.name
        except Role.DoesNotExist:
            obj.role_Name = ""
        return obj

    def get_where_conditions(self, query, params):
        value = params.get("id", 0)
        if DataValidator.isNotNull(value) and value != 0:
            query = query.filter(id=int(value))
        
        return query
