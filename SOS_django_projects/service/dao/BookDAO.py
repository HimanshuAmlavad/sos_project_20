from service.dao.BaseDAO import BaseDAO
from service.models import Book
from service.utility.DataValidator import DataValidator


class BookDAO(BaseDAO):
    def get_model(self):
        return Book

    def get_Unique(self):
        return ["book_code"]

    def populate(self, obj):
        return obj

    def get_where_conditions(self, query, params):
        value = params.get("book_id", 0)
        if DataValidator.isNotNull(value) and value != 0:
            query = query.filter(book_id=int(value))
        
        return query
