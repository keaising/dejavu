import datetime
import uuid
from sqlalchemy import Column, Integer, String, DateTime, DECIMAL, ForeignKey
from src.dal.base import Base


class OrderModel(Base):
    """订单信息"""

    __tablename__ = "order"

    order_id = Column(String, primary_key=True)
    mobile = Column(String, ForeignKey("profile.mobile"))
    address_id = Column(String, ForeignKey("address.address_id"))
    fee = Column(DECIMAL)  # 总金额
    status = Column(Integer)  # 订单状态：0：待支付，1：已支付，2：已取消
    creat_date = Column(DateTime)  # 创建时间
    finish_date = Column(DateTime)  # 支付时间

    def __init__(self, mobile, address_id, fee):
        self.order_id = uuid.uuid4()
        self.mobile = mobile
        self.address_id = address_id
        self.fee = fee
        self.status = 0
        self.creat_date = datetime.datetime.now()
        self.finish_date = None
