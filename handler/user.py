from handler.base import BaseHandler
import datetime


class UserHandler(BaseHandler):
    """用户管理相关接口"""

    def post(self):
        user_id = self.get_body_argument("user_id")
        user_pswd = self.get_body_argument("user_pswd")
        self.execute(
            "INSERT INTO users (user_id, pswd_hash, salt, create_time, valid) \
        VALUE (%s, %s, %s, %s, %s)",
            (user_id, user_pswd, "", datetime.datetime.now(), True),
        )
