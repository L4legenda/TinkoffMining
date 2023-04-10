import ticker
import candel
# import algor.simple_moving_average as simple_moving_average
import algor.moving_average_crossover as moving_average_crossover
import algor.relative_strength_index as relative_strength_index
import algor.bollinger_bands as bollinger_bands
import algor.MACD_alg as MACD_alg
import algor.fibonacci as fibonacci
import test_code as test_code
import algor.ema_crossover as EMA_Crossover
import matplotlib.pyplot as plt
import tikets


delta_days = 30
is_short = True


# RNFT - 0.86% шт 120 days
# NLMK = -
# MAGN = 2.46% in 120 days
# AFKS = 9.68% in 120 days, 20% in 30 days
# AFKS = 9.96% in 120 days, 20% in 30 days
for __ticker in tikets.RUSSIAN_TICKER:
    _ticker = __ticker

    figi = ticker.findFigiForTicker(_ticker)
    print(figi)
    try:
        candel_last = candel.candel_last(figi, days=delta_days)
    except:
        print("Empty data")
    # print(candel_last)

    fiba = fibonacci.test_algorithm(candel_last)
    print(_ticker, fiba['profit'], fiba['percent_profit'], len(candel_last))
    # fiba = fibonacci.run(candel_last)
    # print(fiba)
    # fibonacci.plot_data(candel_last, fiba['buy_signals'], fiba['sell_signals'])
    # fibonacci.plot_trading_signals(candel_last, fiba['buy_signals'], fiba['sell_signals'])
    print("=======")

