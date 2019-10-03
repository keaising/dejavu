import logging
import json
from tornado.web import RequestHandler


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
        status_code = 200
        if result is not None:
            data["code"] = result.code
            data["msg"] = result.msg
            data["data"] = result.data
            status_code = result.code

        content = json.dumps(data)
        self.set_status(status_code)
        self.set_header("Content-Type", "application/json; charset=utf-8")
        self.finish(content)


class MainHandler(BaseHandler):
    def get(self):
        self.write("Hello, world")
