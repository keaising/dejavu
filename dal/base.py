from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session

engine = create_engine("sqlite:///:memory:", echo=True)
Session = scoped_session(sessionmaker(bind=engine))

Base = declarative_base()


def init_db():
    Base.metadata.create_all(engine)


def create(s, model):
    s.add(model)
    s.commit()
    return model


def get_one(s, Model, **kw):
    return s.query(Model).filter_by(**kw).first()


def get_all(model_cls, **kw):
    return model_cls.query.fitler_by(**kw)


def delete(s, model):
    model.delete()
    s.commit()
    return True
