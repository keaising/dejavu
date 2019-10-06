import datetime
import logging

from src.dal.base import Session
from src.handler.base import BaseHandler
from src.model.result import Result
from src.model.cart import CartModel
from src.dal.cart import add, delete, get_by_mobile


class QueryCartHandler(BaseHandler):
    """ 查询用户购物车 """

    def post(self):
        try:
            mobile = self.get_current_user()
            s = Session()
            carts = get_by_mobile(s, mobile)
            self.response(Result.success(carts))
        except Exception as ex:
            logging.exception("query cart error!", exc_info=True)
            self.response(Result.error("query cart error."))


class AddCartHandler(BaseHandler):
    """ 添加到购物车 """

    def post(self):
        try:
            mobile = self.get_current_user()
            s = Session()
            book_id = self.get_body_argument("book_id")
            count = self.get_body_argument("count", 1)
            cart = CartModel(mobile, book_id, count, datetime.datetime.now())
            add(cart)
            self.response(Result.success("success"))
        except Exception as ex:
            logging.exception("add cart error!", exc_info=True)
            self.response(Result.error("add cart error."))


class DeleteCartHandler(BaseHandler):
    """ 从购物车删除 """

    def post(self):
        try:
            mobile = self.get_current_user()
            s = Session()
            book_id = self.get_body_argument("book_id")
            cart = CartModel(mobile, book_id, 1, datetime.datetime.now())
            delete(cart)
            self.response(Result.success("success"))
        except Exception as ex:
            logging.exception("remove cart error!", exc_info=True)
            self.response(Result.error("remove cart error."))
