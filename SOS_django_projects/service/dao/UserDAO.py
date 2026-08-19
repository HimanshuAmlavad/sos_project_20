from service.models import User, Role
from .BaseDAO import BaseDAO
from service.utility.DataValidator import DataValidator

#presentation layer
#business layer
#control layer
#service layer
class UserDAO(BaseDAO):

    def get_by_login(self, login):
        try:
            return self.get_model().objects.get(login=login)
        except self.get_model().DoesNotExist:
            return None

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
