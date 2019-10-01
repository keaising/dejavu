from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine("sqlite:///:memory:", echo=True)
base_db = declarative_base()


def create(s, model_cls, **kw):
    model = model_cls(**kw)
    s.add(model)
    s.commit()
    return model


def get_one(cls, model_cls, **kw):
    return model_cls.query.filter_by(**kw).first()


def get_all(cls, model_cls, **kw):
    return model_cls.query.fitler_by(**kw)


def delete(cls, s, model):
    model.delete()
    s.commit()
    return True


def init_db():
    base_db.metadata.create_all(engine)
    print("init db!")
