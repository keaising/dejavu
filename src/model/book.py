from sqlalchemy import Column, String, DECIMAL
from src.dal.base import Base


class BookModel(Base):
    """图书信息"""

    __tablename__ = "book"

    id = Column(String, primary_key=True)
    name = Column(String)
    author = Column(String)
    price = Column(DECIMAL)  # 价格
    surface_url = Column(String)  # 封面图
    press = Column(String)  # 出版社
    introduction = Column(String)  # 简介
    toc = Column(String)  # 目录
    category = Column(String)  # 类型

    def __init__(
        self,
        id,
        name,
        price,
        author,
        surface_url="",
        press="",
        introduction="",
        toc="",
        category="",
    ):
        self.id = id
        self.name = name
        self.price = price
        self.author = author
        self.surface_url = surface_url
        self.press = press
        self.introduction = introduction
        self.toc = toc
        self.category = category

    def __repr__(self):
        return (
            "<Profile(id='{}', name='{}', price='{}', "
            "author='{}', surface_url='{}', press='{}', "
            "introduction='{}, toc='{}', category='{}')>".format(
                self.id,
                self.name,
                self.price,
                self.author,
                self.surface_url,
                self.press,
                self.introduction,
                self.toc,
                self.category,
            )
        )
