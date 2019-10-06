import tornado.ioloop
from tornado.web import Application
from src.handler.base import MainHandler
from src.handler.profile import (
    SignupHandler,
    LoginHandler,
    QueryUserInfoHandler,
)
from src.handler.account import QuerySurplusHandler, RechargeHandler
from src.handler.book import QueryBookHandler, QueryBookListHandler
from src.dal.base import init_db


def make_app(debug=True, cookie_secret="233") -> Application:
    init_db()
    settings = {"debug": debug, "cookie_secret": cookie_secret}
    return Application(
        handlers=[
            (r"/", MainHandler),
            (r"/user/signup", SignupHandler),
            (r"/user/login", LoginHandler),
            (r"/user/query", QueryUserInfoHandler),
            (r"/account/surplus", QuerySurplusHandler),
            (r"/account/recharge", RechargeHandler),
            (r"/book/get_by_category", QueryBookListHandler),
            (r"/book/get_by_id", QueryBookHandler),
        ],
        **settings
    )


if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    try:
        tornado.ioloop.IOLoop.current().start()
    except KeyboardInterrupt:
        tornado.ioloop.IOLoop.current().stop()
        print("Tonardo Exit.")
