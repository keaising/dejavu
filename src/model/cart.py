from sqlalchemy import Column, Integer, String, DateTime, ForeignKey

from src.dal.base import Base


class CartModel(Base):
    """购物车信息"""

    __tablename__ = "cart"

    cart_id = Column(Integer, primary_key=True)
    mobile = Column(String, ForeignKey("profile.mobile"))
    book_id = Column(Integer, ForeignKey("book.book_id"))
    count = Column(Integer)
    add_date = Column(DateTime)  # 添加到购物车的时间

    def __init__(self, mobile, book_id, count, add_date):
        self.mobile = (mobile,)
        self.book_id = book_id
        self.count = (count,)
        self.add_date = add_date
