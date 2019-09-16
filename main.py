from typing import Optional, Awaitable

import tornado.ioloop
import tornado.web


class MainHandler(tornado.web.RequestHandler):
    """
    MainHandler make default response to user's request.
    """
    def data_received(self, chunk: bytes) -> Optional[Awaitable[None]]:
        pass

    def get(self):
        self.write("Hello, world")


def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
    ])


if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()
