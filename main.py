import tornado.ioloop
import tornado.web
from handler.base import MainHandler
from dal.base import init_db, engine
from sqlalchemy.orm import scoped_session, sessionmaker
from handler.user import UserHandler


class Application(tornado.web.Application):
    def __init__(self):
        init_db()
        handlers = [(r"/", MainHandler), (r"/user/regist", UserHandler)]
        settings = dict(debug=True)
        tornado.web.Application.__init__(self, handlers, **settings)
        self.db = scoped_session(
            sessionmaker(
                bind=engine,
                autocommit=False,
                autoflush=True,
                expire_on_commit=False
            )
        )


if __name__ == "__main__":
    Application().listen(8888)
    tornado.ioloop.IOLoop.current().start()
