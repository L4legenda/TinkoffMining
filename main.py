import ticker
import candel
# import algor.simple_moving_average as simple_moving_average
import algor.moving_average_crossover as moving_average_crossover
import algor.relative_strength_index as relative_strength_index
import algor.bollinger_bands as bollinger_bands
import algor.MACD_alg as MACD_alg
from datetime import datetime, timedelta
from models import database

delta_days = 30

tickers = ticker.tickerAll()
for index in range(100, len(tickers)):
    _ticker = tickers['ticker'][index]
    figi = tickers['figi'][index]
    try:
        candel_last = candel.candel_last(figi, days=delta_days)
    except Exception:
        continue
    SMA = moving_average_crossover.run(candel_last)
    RSI = relative_strength_index.run(candel_last)
    BB = bollinger_bands.run(candel_last)
    MACD = MACD_alg.run(candel_last)

    date_start = datetime.now()
    date_end = date_start - timedelta(days=delta_days)

    profit_SMA = SMA['profit']
    profit_RSI = RSI['profit']
    profit_MACD = MACD['profit']
    profit_BB = BB['profit']

    statistics = database.Statistics(
        ticker=_ticker,
        figi=figi,
        date_start=date_start,
        date_end=date_end,
        sma=profit_SMA,
        rsi=profit_RSI,
        macd=profit_MACD,
        bb=profit_BB,
    )
    database.session.add(statistics)
    database.session.commit()
    print(f"ticker: {_ticker}, figi: {figi}, SMA: {profit_SMA}, RSI: {profit_RSI}, MACD: {profit_MACD}, BB: {profit_BB}")



