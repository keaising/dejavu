import json
import logging
import pytest
from tornado.httpclient import HTTPClientError
from tornado.web import Application
from src.main import make_app
from src.dal.base import Session
from src.model.profile import ProfileModel


@pytest.fixture(scope="session")
def add_account_data() -> None:
    super().setUp()
    # s = Session()
    # s.add(ProfileModel(mobile="15810635978", username="", password="123456"))
    # s.commit()


@pytest.fixture(scope="session")
def app() -> Application:
    # app is the hook that Tornado Test uses to get app under test
    app = make_app()
    return app


async def test_signup_handler(http_server_client):
    test_cases = [
        {
            "body": "mobile=15810635978&password=123456",
            "msg": "success",
            "code": 200,
        },
        {
            "body": "mobile=15810635978&password=123456",
            "msg": "mobile has been used.",
            "code": 400,
        },
    ]

    for case in test_cases:
        r = None
        try:
            r = await http_server_client.fetch(
                "/user/signup",
                method="POST",
                headers=None,
                body="mobile=15810635978&password=123456",
            )
            assert r.code == 200
            data = json.loads(r.body)
            assert data["msg"] == case["msg"]
            assert data["code"] == case["code"]
        except Exception:
            assert 1 == 0


async def test_login_handler(http_server_client):
    test_cases = [
        {
            "body": "mobile=13312344321&password=123456",
            "msg": "Mobile not find",
            "code": 400,
        },
        {
            "body": "mobile=15810635978&password=000000",
            "msg": "password not correct!",
            "code": 400,
        },
        {
            "body": "mobile=15810635978&password=123456",
            "msg": "success",
            "code": 200,
        },
    ]
    for case in test_cases:
        r = None
        try:
            r = await http_server_client.fetch(
                "/user/login",
                method="POST",
                headers=None,
                body=case["body"],
                follow_redirects=False,
            )
            data = json.loads(r.body)
            assert r.code == 200
            assert data["msg"] == case["msg"]
            assert data["code"] == case["code"]
        except HTTPClientError:
            logging.error(r, exc_info=True)
            assert r.code == case["code"]
        except Exception as ex:
            logging.error(ex, exc_info=True)
            assert 1 == 0
