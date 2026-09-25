import logging

from service.models import User, Role
from .BaseDAO import BaseDAO, logger
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
        print("inside where condition")
        value = params.get("firstName", "")
        if DataValidator.isNotNull(value) and value !="":
            query = query.filter(firstName__istartswith=value.strip())
        logger.info(f"value=====>{value}")

        value = params.get("last_name", "")
        if DataValidator.isNotNull(value) and value != "":
            query = query.filter(lastName__istartswith=value.strip())
        logger.info(f"value=====>{value}")

        value = params.get("login", "")
        logger.info(f"value=====>{value}")
        if DataValidator.isNotNull(value) and value != "":
            query = query.filter(login__istartswith=value.strip())

        value = params.get("mobile", "")
        logger.info(f"value=====>{value}")
        if DataValidator.isNotNull(value) and value != "":
            query = query.filter(mobileNumber__istartswith=value.strip())

        return query


