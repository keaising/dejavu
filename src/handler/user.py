from abc import ABC

from src.model.account import AccountModel
from src.handler.base import BaseHandler
from src.common.hash import is_right_password
from src.dal.user import create_account, get_account_by_mobile
from src.dal.base import Session
from src.model.result import Result
import logging


class SignupHandler(BaseHandler, ABC):
    def post(self):
        try:
            s = Session()
            mobile, password = get_params(self)
            if exist(s, mobile):
                self.write("mobile has been used.")
                return

            account = AccountModel(mobile, "", password)
            create_account(s, account)
            self.write("success")
        except Exception as ex:
            self.write(ex.__repr__())


def get_params(self):
    mobile = self.get_body_argument("mobile").strip()
    password = self.get_body_argument("password").strip()
    return mobile, password


def exist(s, mobile):
    account = get_account_by_mobile(s, mobile)
    return False if account is None else True


class LoginHandler(BaseHandler, ABC):
    def post(self):
        try:
            s = Session()
            mobile, password = get_params(self)
            account = get_account_by_mobile(s, mobile)
            if account is None:
                # 手机号没注册，需要先注册，跳转到注册页面
                self.write(Result.error("Mobile not find"))
                return

            is_right = is_right_password(
                password, account.salt, account.password
            )
            if not is_right:
                self.write(Result.error("password not correct!"))
                return

            # 可以再做一个全局dict维护登陆状态并用guid代替mobile，提高速度和安全性
            self.set_secure_cookie("dejavu_user", mobile)
            self.redirect(self.get_argument("next", "/"))

        except Exception as ex:
            logging.exception("login error!", exc_info=True)
            self.write(Result.error("Some error, please try latter."))
