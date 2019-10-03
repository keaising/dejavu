from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session

engine = create_engine("sqlite:///:memory:", echo=True)
Session = scoped_session(sessionmaker(bind=engine))

Base = declarative_base()


def init_db():
    Base.metadata.create_all(engine)
