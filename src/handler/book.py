import logging

from src.dal.base import Session
from src.dal.book import get_book_by_category, get_book_by_id
from src.handler.base import BaseHandler
from src.model.result import Result


class QueryBookListHandler(BaseHandler):
    """ 获取图书列表 """

    def post(self):
        try:
            s = Session()
            category = self.get_body_argument("category")
            books = get_book_by_category(category)
            self.response(Result.success(books))
        except Exception as ex:
            logging.exception("query books error!", exc_info=True)
            self.response(Result.error("query books error."))


class QueryBookHandler(BaseHandler):
    """ 获取单本图书 """

    def post(self):
        try:
            s = Session()
            book_id = self.get_body_argument("book_id")
            book = get_book_by_id(book_id)
            self.response(Result.success(book))
        except Exception as ex:
            logging.exception("query book error!", exc_info=True)
            self.response(Result.error("query book error."))
