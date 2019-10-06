from sqlalchemy import Column, Integer, String, DateTime, DECIMAL, ForeignKey

from src.dal.base import Base


class AddressModel(Base):
    """收货地址信息"""

    __tablename__ = "address"

    address_id = Column(Integer, primary_key=True)
    mobile = Column(String, ForeignKey("profile.mobile"))
    province = Column(String)  # 省
    city = Column(String)  # 市
    town = Column(String)  # 区
    detail = Column(String)  # 详细地址

    def __init__(self, mobile, province, city, town, detail):
        self.mobile = mobile
        self.province = province
        self.city = city
        self.town = town
        self.detail = detail
