from sqlalchemy import Column, String
from src.dal.base import Base


class ProfileModel(Base):
    """用户基本信息"""

    __tablename__ = "profile"

    mobile = Column(String, primary_key=True)
    username = Column(String)
    salt = Column(String)
    password = Column(String)
    # 昵称
    nick_name = Column(String)
    # 头像地址
    avatar_url = Column(String)
    # 签名
    whats_up = Column(String)

    def __init__(
        self,
        mobile,
        username,
        password,
        nick_name="",
        avatar_url="",
        whats_up="",
    ):
        self.mobile = mobile
        self.username = username
        self.password = password
        self.nick_name = nick_name
        self.avatar_url = avatar_url
        self.whats_up = whats_up

    def __repr__(self):
        return (
            "<Profile(mobile='{}', username='{}', nick_name='{}',"
            "avatar_url='{}', whats_up='{}')>".format(
                self.mobile,
                self.username,
                self.nick_name,
                self.avatar_url,
                self.whats_up,
            )
        )
