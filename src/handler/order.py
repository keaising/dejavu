import datetime
import logging
from src.handler.base import BaseHandler
from src.dal.base import Session
from src.dal.order import create, pay, cancel
from src.model.result import Result
from src.model.order import OrderModel
from src.model.order_detail import OrderDetailModel


class CreateOrderHandler(BaseHandler):
    """生成订单"""

    def post(self):
        try:
            s = Session()
            order = get_order_from_params(self)
            order_details = get_order_detail_from_params(self, order)
            order.fee = sum([detail.price for detail in order_details])
            create(s, order, order_details)
            self.response(Result.success("success"))
        except Exception as ex:
            logging.exception("create order error!", exc_info=True)
            self.response(Result.error("create order error."))


def get_order_from_params(self) -> OrderModel:
    """ 生成订单model

    :param self:
    :return:
    """
    mobile = self.get_current_user()
    address_id = self.get_body_argument("address_id")
    fee = self.get_body_argument("fee")
    return OrderModel(mobile, address_id, fee)


def get_order_detail_from_params(self, order: OrderModel) -> []:
    """ 拼接订单详情列表

    :param self:
    :param order:
    :return: 订单详情列表

    id_prices： 图书id和价格的格式为 'id1:price1,id2:price2,id3:price3'
    所以此处用逗号分割
    """
    id_prices = self.get_body_argument("book_id_price")
    return [create_detail(id_price, order) for id_price in id_prices.split(",")]


def create_detail(id_price_count: str, order: OrderModel):
    """ 拼接订单详情

    :param id_price_count:
    :param order: 订单
    :return: 订单详情
    id_price_count： 图书id和价格的格式为 id:price
    """
    result = id_price_count.split(":")
    book_id = result[0]
    price = result[1]
    return OrderDetailModel(order.mobile, book_id, order.order_id, price)


class PayHandler(BaseHandler):
    """支付订单"""

    def post(self):
        try:
            s = Session()
            # 只是需要一个 Order model，所以用虚假的数据生成一个
            mobile = self.get_current_user()
            order = OrderModel(mobile, 1, 0)
            order.order_id = self.get_body_argument("order_id")
            pay(s, order)
            self.response(Result.success("success"))
        except Exception as ex:
            logging.exception("pay order error!", exc_info=True)
            self.response(Result.error("pay order error."))


class CancelHandler(BaseHandler):
    """取消订单"""

    def post(self):
        try:
            s = Session()
            # 只是需要一个 Order model，所以用虚假的数据生成一个
            mobile = self.get_current_user()
            order = OrderModel(mobile, 1, 0)
            order.order_id = self.get_body_argument("order_id")
            cancel(s, order)
            self.response(Result.success("success"))
        except Exception as ex:
            logging.exception("cancel order error!", exc_info=True)
            self.response(Result.error("cancel order error."))
