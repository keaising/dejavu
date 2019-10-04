import logging

from src.dal.base import Session
from src.handler.base import BaseHandler
from src.model.result import Result


class QueryBookListHandler(BaseHandler):
    """ 获取图书列表 """

    def post(self):
        try:
            s = Session()

            self.response(Result.success())
        except Exception as ex:
            logging.exception("query surplus error!", exc_info=True)
            self.response(Result.error("query surplus error."))
