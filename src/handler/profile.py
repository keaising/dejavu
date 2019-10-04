from src.model.profile import ProfileModel
from src.handler.base import BaseHandler
from src.common.hash import is_right_password
from src.dal.profile import create_profile, get_profile_by_mobile
from src.dal.base import Session
from src.model.result import Result
from src.common.hash import generate_random_string, encrypt_password
import logging


class SignupHandler(BaseHandler):
    def post(self):
        try:
            s = Session()
            profile = get_params(self)
            if exist(s, profile.mobile):
                self.response(Result.error("mobile has been used."))
                return

            new_profile = ProfileModel(profile.mobile, "", profile.password)
            new_profile.salt = generate_random_string()
            new_profile.password = encrypt_password(
                new_profile.password, new_profile.salt
            )
            create_profile(s, new_profile)
            self.response(Result.success("success"))
        except Exception as ex:
            logging.exception("signup error!", exc_info=True)
            self.response(Result.error("SignUp error."))


class LoginHandler(BaseHandler):
    def post(self):
        try:
            s = Session()
            profile = get_params(self)
            account = get_profile_by_mobile(s, profile.mobile)
            if account is None:
                # 手机号没注册，需要先注册，跳转到注册页面
                self.response(Result.error("Mobile not find"))
                return

            is_right = is_right_password(
                profile.password, account.salt, account.password
            )
            if not is_right:
                self.response(Result.error("password not correct!"))
                return

            # 可以再做一个全局dict维护登陆状态并用guid代替mobile，提高速度和安全性
            self.set_secure_cookie("dejavu_user", profile.mobile)
            self.response(Result.success("success"))
        except Exception as ex:
            logging.exception("login error!", exc_info=True)
            self.response(Result.error("Some error, please try later."))


def get_params(self) -> ProfileModel:
    mobile = self.get_body_argument("mobile")
    password = self.get_body_argument("password")
    username = self.get_body_argument("username", "")
    nick_name = self.get_body_argument("nick_name", "")
    avatar_url = self.get_body_argument("avatar_url", "")
    whats_up = self.get_body_argument("whats_up", "")
    return ProfileModel(
        mobile, username, password, nick_name, avatar_url, whats_up
    )


def exist(s, mobile):
    account = get_profile_by_mobile(s, mobile)
    return False if account is None else True
