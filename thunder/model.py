from utils.sqlite import Model, Base
from sqlalchemy import *

class ThunderTask(Model, Base):
    __tablename__ = 'thunder_tasks'
    __table_args__ = {"sqlite_autoincrement" : True}
    id = Column("id", Integer, primary_key = True, autoincrement = True)
    name = Column("name", String(255))
    addr = Column("addr", String(1023))
    type = Column("type", Integer)
    status = Column("status", Integer)

    def __init__(self, id=None, name=None, addr=None, type=None, status=None):
        self.id = id
        self.name = name
        self.addr = addr
        self.type = type
        self.status = status

