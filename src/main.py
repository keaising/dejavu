import tornado.ioloop
import tornado.web
from src.handler.base import MainHandler
from src.handler.user import SignupHandler, LoginHandler
from src.dal.base import init_db


class Application(tornado.web.Application):
    def __init__(self):
        init_db()
        handlers = [
            (r"/", MainHandler),
            (r"/user/signup", SignupHandler),
            (r"/user/login", LoginHandler),
        ]
        settings = dict(debug=True)
        tornado.web.Application.__init__(self, handlers, **settings)


if __name__ == "__main__":
    Application().listen(8888)
    try:
        tornado.ioloop.IOLoop.current().start()
    except KeyboardInterrupt:
        tornado.ioloop.IOLoop.current().stop()
        print("Tonardo Exit.")
