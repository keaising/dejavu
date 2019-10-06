from src.dal.base import Session
from src.model.order import OrderModel
from src.model.account import AccountModel


def create(session: Session, order: OrderModel, order_details: []):
    """ 创建订单

    :param session: db session
    :param order: 订单
    :param order_details: 订单详情
    :return:
    """
    session.add(order)
    session.add_all(order_details)  # 批量插入
    session.commit()


def pay(session: Session, order: OrderModel):
    """ 支付订单

    :param session: db session
    :param order: 订单
    :return:
    """

    # 实际上这里需要大量的校验，校验逻辑应该在外层就完成，
    # 比如余额要大于订单金额、订单状态是否正常之类的，
    # 暂时先省略，以后再补上
    exist_order = (
        session.query(OrderModel)
        .filter(OrderModel.order_id == order.order_id)
        .first()
    )
    exist_order.status = 1  # 已支付
    account = (
        session.query(AccountModel)
        .filter(AccountModel.mobile == exist_order.mobile)
        .first()
    )
    account.surplus -= order.fee
    session.commit()


def cancel(session: Session, order: OrderModel):
    """ 撤销订单

    :param session: db session
    :param order: 订单
    :return:
    """
    exist_order = (
        session.query(OrderModel)
        .filter(OrderModel.order_id == order.order_id)
        .first()
    )
    exist_order.status = 2  # 已取消
    session.commit()
