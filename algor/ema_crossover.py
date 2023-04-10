import pandas as pd
import talib

def ema_crossover_strategy(data, short_period=12, long_period=26):
    # Calculate the short and long EMAs
    short_ema = talib.EMA(data['close'], timeperiod=short_period)
    long_ema = talib.EMA(data['close'], timeperiod=long_period)
    
    # Generate buy and sell signals based on EMA crossover
    buy_signals = []
    sell_signals = []
    position = False
    profit = 0
    investment = 0
    total_investment = 0  # Keep track of the total investment
    
    for i in range(1, len(data)):
        # Buy signal: short EMA crosses below long EMA
        if short_ema[i] < long_ema[i] and short_ema[i - 1] >= long_ema[i - 1] and not position:
            buy_signals.append((i, data['close'][i]))
            investment = data['close'][i]
            total_investment += investment  # Add to the total investment
            position = True
        # Sell signal: short EMA crosses above long EMA
        elif short_ema[i] > long_ema[i] and short_ema[i - 1] <= long_ema[i - 1] and position:
            sell_signals.append((i, data['close'][i]))
            profit += data['close'][i] - investment
            investment = 0
            position = False
    
    # Calculate profit percentage
    percent_profit = 0
    if total_investment != 0:
        percent_profit = (profit / total_investment) * 100
    
    return {
        "buy_signals": buy_signals,
        "sell_signals": sell_signals,
        "profit": profit,
        "percent_profit": percent_profit
    }


# Example usage (assuming 'data' is a DataFrame with columns 'high', 'low', and 'close'):
# result = ema_crossover_strategy(data)
# print(result)

