import logging

from src.dal.base import Session
from src.handler.base import BaseHandler
from src.model.result import Result
from src.model.account import AccountModel
from src.dal.account import get_account_by_mobile, recharge


class QuerySurplusHandler(BaseHandler):
    """ 查询用户账户余额 """

    def post(self):
        try:
            user = self.get_current_user()
            s = Session()
            account = get_account_by_mobile(s, user)
            self.response(Result.success(account))
        except Exception as ex:
            logging.exception("query surplus error!", exc_info=True)
            self.response(Result.error("query surplus error."))


class RechargeHandler(BaseHandler):
    """ 充值 """

    def post(self):
        try:
            user = self.get_current_user()
            mobile = self.get_body_argument("mobile")
            fee = self.get_body_argument("fee")
            if mobile != user:
                self.response(
                    Result.error("Not same user, please logout and re-login.")
                )
            s = Session()
            recharge(s, AccountModel(mobile, fee))
            self.response(Result.success("success"))
        except Exception as ex:
            logging.exception("signup error!", exc_info=True)
            self.response(Result.error("SignUp error."))
