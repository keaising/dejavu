from src.dal.base import Session
from src.model.address import AddressModel


def create_address(session: Session, address: AddressModel):
    """新增收货地址

    :param session: db session
    :param address: 收货地址
    :return:None
    """
    session.add(address)
