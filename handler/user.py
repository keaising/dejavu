from handler.base import BaseHandler
import datetime


class UserHandler(BaseHandler):
    """用户管理相关接口"""

    def get(self):

        # self.execute(
        #     "INSERT INTO users \
        # (user_id, pswd_hash, salt, create_time, valid) \
        # VALUE (%s, %s, %s, %s, %s)",
        #     (user_id, user_pswd, "", datetime.datetime.now(), True),
        # )
        try:
            # 获取入参
            user_id = self.get_argument("user_id")
            user_pswd = self.get_argument("user_pswd")
            self.write(user_id + ": " + user_pswd)
        except Exception as ex:
            # 获取入参失败时，抛出错误码及错误信息
            self.write(ex.__repr__())
