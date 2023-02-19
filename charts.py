import ticker
import candel
# import algor.simple_moving_average as simple_moving_average
import algor.moving_average_crossover as moving_average_crossover
import algor.relative_strength_index as relative_strength_index
import algor.bollinger_bands as bollinger_bands
import algor.MACD_alg as MACD_alg
import algor.fibonacci as fibonacci
import test_code as test_code



delta_days = 60
is_short = True


# RNFT
# NLMK
# MAGN
_ticker = "AFKS"

figi = ticker.findFigiForTicker(_ticker)
print(figi)
candel_last = candel.candel_last(figi, days=delta_days)

# SMA = moving_average_crossover.run(candel_last)
# moving_average_crossover.view(candel_last, SMA["buy_times"], SMA["sell_times"])
# profit_SMA = SMA['profit']
# print(f"SMA: {profit_SMA}")

# RSI = relative_strength_index.run(candel_last)
# relative_strength_index.view(candel_last, RSI["buy_times"], RSI["sell_times"])
# profit_RSI = RSI['profit']
# print(f"RSI: {profit_RSI}")

# fiba = fibonacci.test_algorithm(candel_last)
fiba = fibonacci.test_strategy(candel_last, window_size=16, is_short=is_short)
# print(fiba)
# fibonacci.plot_data(candel_last, fiba['buy_signals'], fiba['sell_signals'])



