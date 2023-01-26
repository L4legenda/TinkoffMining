from .core import Base
from sqlalchemy import Column, Integer, String, Date

class Statistics(Base):
    __tablename__ = 'statistics'
    id = Column(Integer, primary_key=True)
    ticker = Column(String)
    figi = Column(String)
    date_start = Column(Date)
    date_end = Column(Date)
    sma = Column(Integer)
    rsi = Column(Integer)
    macd = Column(Integer)
    bb = Column(Integer)
