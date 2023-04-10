from tinkoff.invest import Client, InstrumentStatus
from tinkoff.invest.services import InstrumentsService, MarketDataService
from pandas import DataFrame
from config import TOKEN

def tickerAll():
    with Client(TOKEN) as client:
        instruments: InstrumentsService = client.instruments

        date_frame = DataFrame(
            instruments.shares(instrument_status=InstrumentStatus.INSTRUMENT_STATUS_ALL).instruments,
            columns=['name', 'figi', 'ticker', 'class_code']
        )
        return date_frame

def findOneTicker(ticker):
    ticker_all = tickerAll()
    return ticker_all[ticker_all['ticker'] == ticker]

def findFigiForTicker(ticker):
    ticker_all = tickerAll()
    finded_ticker = ticker_all[ticker_all['ticker'] == ticker]
    if len(finded_ticker['figi'].values) > 0:
        return finded_ticker['figi'].values[0]
    return None
