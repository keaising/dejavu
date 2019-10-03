import json
import unittest
from tornado.testing import AsyncHTTPTestCase
from tornado.web import Application
from src.main import make_app


class AccountHandlerTest(AsyncHTTPTestCase):
    def setUp(self) -> None:
        super().setUp()
        self.headers = {"Content-Type": "application/json; charset=UTF-8"}

    def get_app(self) -> Application:
        # get_app is the hook that Tornado Test uses to get app under test
        return make_app()

    def test_signup_handler(self):
        r = self.fetch(
            r"/user/signup",
            method="POST",
            headers=None,
            body="mobile=15810635978&password=123456",
        )
        data = json.loads(r.body)
        self.assertEqual(data["msg"], "")
        self.assertEqual(r.code, 200)


if __name__ == "__main__":
    unittest.main()
