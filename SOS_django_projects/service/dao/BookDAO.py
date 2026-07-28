from service.dao.BaseDAO import BaseDAO
from service.models import Book


class BookDAO(BaseDAO):
    def get_model(self):
        return Book

    def get_Unique(self):
        return ["book_code"]

    def populate(self, obj):
        return obj
