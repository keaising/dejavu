from src.model.account import AccountModel
from src.model.profile import ProfileModel
from src.dal.base import Session


def create_account(session: Session, account: AccountModel):
    """新增用户账户

    :param session:db session
    :param account:账户信息
    :return:None
    """
    session.add(account)


def recharge(session: Session, account: AccountModel):
    """充值账户

    :param session: db session
    :param account: 要充值的账户以及充值金额
    :return: None
    """
    old = (
        session.query(AccountModel)
        .filter(AccountModel.mobile == account.mobile)
        .first()
    )
    old.surplus = old.surplus + account.surplus
    session.commit()


def get_account_by_mobile(session: Session, mobile: str) -> AccountModel:
    """查询账户

    :param session: db session
    :param mobile: 账户手机号
    :return: AccountModel
    """
    return (
        session.query(AccountModel)
        .filter(AccountModel.mobile == mobile)
        .first()
    )
