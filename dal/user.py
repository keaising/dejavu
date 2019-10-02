from model.account import AccountModel
from dal.base import create, get_one, get_all


def create_account(s, account_model):
    return create(s, account_model)


def get_account(**kw):
    print(**kw)
    return get_one(AccountModel, **kw)


def get_accounts(**kw):
    return get_all(AccountModel, **kw)
