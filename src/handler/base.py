import logging
import json
from tornado.web import RequestHandler
from src.model.result import Result


class BaseHandler(RequestHandler):
    def get_current_user(self):
        return self.get_secure_cookie("dejavu_user")

    def prepare(self):
        super().prepare()

        logger = logging.getLogger("dejavu_app")
        logger.debug(
            "{} {} {} {}".format(
                self.request.method,
                self.request.path,
                self.request.arguments,
                self.request.headers,
            )
        )

    def response(self, result=None):
        data = {"code": 200, "msg": ""}
        # 测试框架限制，所有http_status_code=200，具体业务的值只在data.code中体现
        status_code = 200
        if result is not None:
            data["code"] = result.code
            data["msg"] = result.msg
            data["data"] = result.data

        content = json.dumps(data)
        self.set_status(status_code)
        self.set_header("Content-Type", "application/json; charset=utf-8")
        self.finish(content)


class MainHandler(BaseHandler):
    """实现一个测试Handler"""

    def get(self):
        self.response(Result.success(s="Hello, world"))
