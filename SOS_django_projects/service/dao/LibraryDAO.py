from service.dao.BaseDAO import BaseDAO
from service.models import Library
from service.utility.DataValidator import DataValidator


class LibraryDAO(BaseDAO):
    def get_model(self):
        return Library

    def get_Unique(self):
        return ["libraryId"]

    def populate(self, obj):
        return obj

    def get_where_conditions(self, query, params):
        value = params.get("library_name","")
        if DataValidator.isNotNull(value) and value != "":
            query = query.filter(library_name__istartswith=value.split())
        return query