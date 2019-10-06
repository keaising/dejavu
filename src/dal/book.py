from src.model.book import BookModel
from src.dal.base import Session


def get_book_by_category(session: Session, category: str) -> []:
    """ 根据图书类型查询

    :param session: db session
    :param category: 图书类型
    :return: BookModel List
    """
    return session.query(BookModel).filter(BookModel.category == category)


def get_book_by_id(session: Session, book_id: str) -> BookModel:
    """ 根据图书id查询

    :param session: db session
    :param book_id: 图书类型
    :return: BookModel
    """
    return session.query(BookModel).filter(BookModel.id == id).first()
