import tornado.ioloop
import tornado.web
from handler.base import MainHandler
from handler.user import SignupHandler, LoginHandler
from dal.base import init_db


class Application(tornado.web.Application):
    def __init__(self):
        init_db()
        handlers = [
            (r"/", MainHandler),
            (r"/user/signup", SignupHandler),
            (r'/user/login', LoginHandler)
        ]
        settings = dict(debug=True)
        tornado.web.Application.__init__(self, handlers, **settings)


if __name__ == "__main__":
    Application().listen(8888)
    tornado.ioloop.IOLoop.current().start()
