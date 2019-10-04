import logging

from src.dal.base import Session
from src.handler.base import BaseHandler
from src.model.result import Result


class QuerySurplusHandler(BaseHandler):
    """查询用户账户余额"""

    def post(self):
        try:
            s = Session()

            self.response(Result.success("success"))
        except Exception as ex:
            logging.exception("signup error!", exc_info=True)
            self.response(Result.error("SignUp error."))
