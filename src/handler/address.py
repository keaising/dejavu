import logging
from src.model.address import AddressModel
from src.dal.base import Session
from src.dal.address import create_address
from src.handler.base import BaseHandler
from src.model.result import Result


class AddAddressHandler(BaseHandler):
    """ 添加收货地址"""

    def post(self):
        try:
            s = Session()
            address = get_params(self)
            create_address(s, address)
            self.response(Result.success("success"))
        except Exception as ex:
            logging.exception("add address error!", exc_info=True)
            self.response(Result.error("add address error."))


def get_params(self) -> AddressModel:
    """从请求中获取用户参数"""
    mobile = self.get_current_user()
    province = self.get_body_argument("province")
    city = self.get_body_argument("city")
    town = self.get_body_argument("town")
    detail = self.get_body_argument("detail")
    return AddressModel(mobile, province, city, town, detail)
