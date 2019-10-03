import tornado.ioloop
from tornado.web import Application
from src.handler.base import MainHandler
from src.handler.user import SignupHandler, LoginHandler
from src.dal.base import init_db


def make_app() -> Application:
    init_db()
    return Application(
        handlers=[
            (r"/", MainHandler),
            (r"/user/signup", SignupHandler),
            (r"/user/login", LoginHandler),
        ],
        settings=dict(debug=True),
    )


if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    try:
        tornado.ioloop.IOLoop.current().start()
    except KeyboardInterrupt:
        tornado.ioloop.IOLoop.current().stop()
        print("Tonardo Exit.")
