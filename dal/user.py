from model import user
from dal.base import create, get_one, get_all


class UserManager:
    @classmethod
    def create_user(cls, s, **kw):
        return create(s, user.UserModel, **kw)

    @classmethod
    def get_user(cls, **kw):
        return get_one(**kw)

    @classmethod
    def get_users(cls, **kw):
        return get_all(**kw)
