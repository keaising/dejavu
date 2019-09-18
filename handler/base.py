from tornado.util import ObjectDict
from tornado.web import RequestHandler


class NoResultError(Exception):
    pass


class BaseHandler(RequestHandler):
    @property
    def db(self):
        return self.application.db


class MainHandler(BaseHandler):
    def get(self):
        self.write("Hello, world")
