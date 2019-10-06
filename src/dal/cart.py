from src.model.cart import CartModel
from src.model.book import BookModel
from src.dal.base import Session


def get_by_mobile(session: Session, mobile: str) -> CartModel:
    """ 根据查询手机号查询用户购物车

    :param session: db session
    :param mobile: 手机号
    :return: CartModel
    """
    return (
        session.query(CartModel, BookModel)
        .filter(CartModel.mobile == mobile)
        .all()
    )


def add(session: Session, cart: CartModel):
    """ 添加到购物车，如果有了的话只需要增加数量

    :param session: db session
    :param cart: 要增加的用户和图书
    :return:
    """
    exist = (
        session.query(CartModel)
        .filter(CartModel.mobile == cart.mobile)
        .filter(CartModel.book_id == cart.book_id)
        .first()
    )
    if exist is not None:
        exist.count += cart.count
    else:
        exist = cart
    session.commit()


def delete(session: Session, cart: CartModel):
    """ 从购物车删除图书

    :param session: db session
    :param cart: 要删除的用户和图书
    :return:
    """
    exist = (
        session.query(CartModel)
        .filter(CartModel.mobile == cart.mobile)
        .filter(CartModel.book_id == cart.book_id)
        .first()
    )
    if exist is not None:
        session.delete(exist)
