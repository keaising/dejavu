import json
import pytest
from tornado.testing import AsyncHTTPTestCase
from tornado.web import Application
from src.main import make_app
from src.dal.base import Session
from src.model.account import AccountModel


@pytest.fixture(scope="session")
def add_account_data() -> None:
    super().setUp()
    s = Session()
    s.add(AccountModel(mobile="15810635978", username="", password="123456"))
    s.commit()


@pytest.fixture(scope="session")
def app() -> Application:
    # app is the hook that Tornado Test uses to get app under test
    app = make_app()
    return app


async def test_login_handler(http_server_client):
    r = await http_server_client.fetch(
        "/user/login",
        method="POST",
        headers=None,
        body="mobile=13312344321&password=123456",
    )
    data = json.loads(r.body)
    assert r.code == 200
    assert data["msg"] == "Mobile not find"
    assert data["code"] == 400


async def test_signup_handler(http_server_client):
    r = await http_server_client.fetch(
        "/user/signup",
        method="POST",
        headers=None,
        body="mobile=13312344321&password=123456",
    )
    assert r.code == 200
    data = json.loads(r.body)
    assert data["msg"] == "success"
    assert data["code"] == 200
