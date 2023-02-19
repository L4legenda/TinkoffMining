import ticker
import candel
# import algor.simple_moving_average as simple_moving_average
import algor.moving_average_crossover as moving_average_crossover
import algor.relative_strength_index as relative_strength_index
import algor.bollinger_bands as bollinger_bands
import algor.MACD_alg as MACD_alg
import algor.fibonacci as fibonacci
from datetime import datetime, timedelta
from models import database
import time

delta_days = 30

tickers = ticker.tickerAll()
for index in range(0, len(tickers)):
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
    FIBO = fibonacci.test_strategy(candel_last)

    date_start = datetime.now()
    date_end = date_start - timedelta(days=delta_days)

    profit_SMA = SMA['profit']
    percent_profit_SMA = SMA['percent_profit']

    profit_RSI = RSI['profit']
    percent_profit_RSI = RSI['percent_profit']

    profit_MACD = MACD['profit']
    percent_profit_MACD = MACD['percent_profit']

    profit_BB = BB['profit']
    percent_profit_BB = BB['percent_profit']

    profit_FIBO = FIBO['profit']
    percent_profit_FIBO = FIBO['percent_profit']

    statistics = database.Statistics(
        ticker=_ticker,
        figi=figi,
        date_start=date_start,
        date_end=date_end,

        profit_sma=profit_SMA,
        percent_profit_sma=percent_profit_SMA,

        profit_rsi=profit_RSI,
        percent_profit_rsi=percent_profit_RSI,

        profit_macd=profit_MACD,
        percent_profit_macd=percent_profit_MACD,

        profit_bb=profit_BB,
        percent_profit_bb=percent_profit_BB,

        profit_fibo=profit_FIBO,
        percent_profit_fibo=percent_profit_FIBO,
    )
    database.session.add(statistics)
    database.session.commit()
    print(f"""
ticker: {_ticker},
figi: {figi},
SMA: {profit_SMA}, Percent SMA: {percent_profit_SMA},
RSI: {profit_RSI}, Percent RSI: {percent_profit_RSI},
MACD: {profit_MACD}, Percent MACD: {percent_profit_MACD},
BB: {profit_BB}, Percent BB: {percent_profit_BB},
FIBO: {profit_FIBO}, Percent FIBO: {percent_profit_FIBO},
""")
