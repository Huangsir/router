from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base, declared_attr
from sqlalchemy.orm import scoped_session, sessionmaker
import config

engine = create_engine(
    'sqlite:///%s' % config.DB_PATH,
    echo = False,
)
metadata = MetaData(bind = engine)
Base = declarative_base(metadata = metadata)
session = scoped_session(
    sessionmaker(
        autocommit = False,
        autoflush = False,
        bind = engine,
    )
)

class Model():
    @declared_attr
    def session(cls):
        return session

    @classmethod
    def Query(cls):
        return session.query(cls)

    @classmethod
    def Add(cls, obj):
        session.add(obj)
        session.commit()

