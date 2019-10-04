from src.model.account import AccountModel


def get_profile_by_mobile(session, mobile):
    return session.query(AccountModel).filter_by(mobile=mobile).first()
