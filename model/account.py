from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from common.hash import generate_random_string, encrypt_password

from dal.base import Base


class AccountModel(Base):
    __tablename__ = "account"

    mobile = Column(Integer, primary_key=True)
    username = Column(String)
    salt = Column(String)
    password = Column(String)

    def __init__(self, mobile, username, password):
        self.mobile = mobile
        self.username = username
        self.salt = generate_random_string()
        self.password = encrypt_password(password, self.salt)

    def __repr__(self):
        return "<User(mobile='%s', username='%s')>" % (
            self.mobile,
            self.username,
        )
