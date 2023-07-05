from tinkoff.invest import Client, InstrumentStatus
from tinkoff.invest.services import InstrumentsService, MarketDataService
from datetime import timedelta, datetime

from tinkoff.invest import CandleInterval, Client
from tinkoff.invest.utils import now
import pandas as pd
from config import TOKEN


def candel_last(figi: str, days=7, save=False):

    candel_list = []

    with Client(TOKEN) as client:
        for candle in client.get_all_candles(
                figi=figi,
                from_=now() - timedelta(days=days),
                interval=CandleInterval.CANDLE_INTERVAL_1_MIN,
            ):
                candel_dict = {
                    "date": candle.time.isoformat(),
                    "open": float(f"{candle.open.units}.{candle.open.nano}"),
                    "high": float(f"{candle.high.units}.{candle.high.nano}"),
                    "low": float(f"{candle.low.units}.{candle.low.nano}"),
                    "close": float(f"{candle.close.units}.{candle.close.nano}"),
                    "volume": candle.volume,
                }
                candel_list.append(candel_dict)
    if len(candel_list) == 0:
        raise Exception("Empty data")
    datetime_string = datetime.now().strftime("%m-%d-%Y")
    df = pd.DataFrame(candel_list)

    if save:
        df.to_csv(f"data/data_{figi}_days_{days}_{datetime_string}.csv")

    return df