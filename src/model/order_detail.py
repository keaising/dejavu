from sqlalchemy import Column, Integer, String, DECIMAL, ForeignKey

from src.dal.base import Base


class OrderDetailModel(Base):
    """订单详情，每本书一条记录"""

    __tablename__ = "order_detail"

    order_detail_id = Column(Integer, primary_key=True)
    mobile = Column(String, ForeignKey("profile.mobile"))
    book_id = Column(Integer, ForeignKey("book.book_id"))
    order_id = Column(String, ForeignKey("order.order_id"))
    price = Column(DECIMAL)  # 图书价格

    def __init__(self, mobile, book_id, order_id, price):
        self.mobile = mobile
        self.book_id = book_id
        self.order_id = order_id
        self.price = price
