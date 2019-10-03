from model.account import AccountModel


def create_account(session, account_model):
    session.add(account_model)


def get_account_by_mobile(session, mobile):
    return session.query(AccountModel).filter_by(mobile=mobile).first()
