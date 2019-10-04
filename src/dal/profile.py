from src.model.profile import ProfileModel
from src.model.account import AccountModel
from src.dal.base import Session


def create_profile(session, profile_model):
    """新增用户信息"""
    session.add(profile_model)


def get_profile_by_mobile(session, mobile):
    """查询用户信息，只包含Profile"""
    return session.query(ProfileModel).filter_by(mobile=mobile).first()


def get_info_by_mobile(session: Session, mobile: str):
    """查询用户基础信息和用户账户余额

    用于个人信息页面展示
    """
    return (
        session.query(
            AccountModel.mobile,
            AccountModel.surplus,
            ProfileModel.nick_name,
            ProfileModel.whats_up,
        )
        .join(ProfileModel)
        .filter(AccountModel.mobile == mobile)
        .first()
    )
