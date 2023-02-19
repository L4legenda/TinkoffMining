from .core import Base
from sqlalchemy import Column, Integer, String, Date, Float


class Statistics(Base):
    __tablename__ = 'statistics'
    id = Column(Integer, primary_key=True)
    ticker = Column(String)
    figi = Column(String)
    date_start = Column(Date)
    date_end = Column(Date)

    profit_sma = Column(Integer)
    percent_profit_sma = Column(Float)

    profit_rsi = Column(Integer)
    percent_profit_rsi = Column(Float)

    profit_macd = Column(Integer)
    percent_profit_macd = Column(Float)

    profit_bb = Column(Integer)
    percent_profit_bb = Column(Float)

    profit_fibo = Column(Integer)
    percent_profit_fibo = Column(Float)
