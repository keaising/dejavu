from abc import ABC

from model.account import AccountModel
from handler.base import BaseHandler
from common.hash import is_right_password
from dal.user import create_account, get_account
from dal.base import Session


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
    mobile = self.get_body_argument("mobile")
    password = self.get_body_argument("password")
    return mobile, password


def exist(session, mobile):
    account = session.query(AccountModel).filter_by(mobile=mobile).first()
    # get_account(["mobile", mobile])
    return False if account is None else True


class LoginHandler(BaseHandler, ABC):
    def post(self):
        try:
            s = Session()
            mobile, password = get_params(self)
            account = s.query(AccountModel).filter_by(mobile=mobile).first()
            if account is None:
                self.write("mobile not exist.")

            is_right = is_right_password(
                password, account.salt, account.password
            )
            if not is_right:
                self.write("password not correct!")

            self.write("login success!")
        except Exception as ex:
            self.write(ex.__repr__())
