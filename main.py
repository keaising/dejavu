from typing import Optional, Awaitable

import tornado.ioloop
import tornado.web
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from handler.base import MainHandler

Base = declarative_base()
# engine = create_engine()


class Application(tornado.web.Application):
    def __init__(self):
        handlers = [(r"/", MainHandler)]
        settings = dict(debug=True)
        tornado.web.Application.__init__(self, handlers, **settings)


if __name__ == "__main__":
    Application().listen(8888)
    tornado.ioloop.IOLoop.current().start()
