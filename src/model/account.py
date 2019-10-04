from sqlalchemy import Column, DECIMAL, String
from src.common.hash import generate_random_string, encrypt_password

from src.dal.base import Base


class AccountModel(Base):
    """
    用户账户，跟用户的一般信息分开，方便后期扩展账户领域
    """

    __tablename__ = "account"

    # 跟Profile一样用手机号作主键
    mobile = Column(String, primary_key=True)
    # 余额
    surplus = Column(DECIMAL)

    def __init__(self, mobile, surplus=0):
        self.mobile = mobile
        self.surplus = surplus

    def __repr__(self):
        return "<Account(mobile='{}', surplus='{}')>".format(
            self.mobile, self.surplus
        )
