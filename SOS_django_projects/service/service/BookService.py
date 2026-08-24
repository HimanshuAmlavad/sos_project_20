from service.dao.BookDAO import BookDAO
from service.service.BaseService import BaseService


class BookService(BaseService):

    
    def get_dao(self):
        return BookDAO()