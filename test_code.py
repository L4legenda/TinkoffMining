import pandas as pd
import talib
import matplotlib.pyplot as plt


def algorithm(data, levels=[0.236, 0.382, 0.5, 0.618, 0.786], window_size=20, stop_loss=0.05):
    # Calculate the highest and lowest price
    highest_price = data['high'].max()
    lowest_price = data['low'].min()

    # Calculate the price range
    price_range = highest_price - lowest_price

    # Calculate the Fibonacci levels
    fib_levels = []
    for level in levels:
        fib_levels.append(highest_price - level * price_range)

    # Initialize the position and profit variables
    position = 0
    profit = 0
    investment = 0

    buy_signals = []
    sell_signals = []

    # Calculate the SMA
    close_prices = data['close']
    sma = talib.SMA(close_prices, window_size)

    # Add improvement 2: Use EMA instead of SMA
    ema = talib.EMA(close_prices, window_size)

    # Add improvement 3: Use RSI to filter signals
    rsi = talib.RSI(close_prices, timeperiod=14)


    # Iterate through the data
    for i in range(len(data)):
        # Add improvement 4: Check if the price crosses above the EMA
        if data['high'][i] > ema[i] and rsi[i] > 50 and position <= 0:
            # Buy
            position += 1
            investment += data['close'][i]
            profit -= data['close'][i]
            buy_signals.append((i, data['close'][i]))
        # Add improvement 4: Check if the price crosses below the EMA
        elif data['low'][i] < ema[i] and rsi[i] < 50 and position >= 0:
            # Sell
            position -= 1
            profit += data['close'][i]
            sell_signals.append((i, data['close'][i]))
        # Add improvement 5: Use trailing stop-loss
        elif position > 0 and data['close'][i] < data['close'][i-1] * 0.98:
            # Sell
            position = 0
            profit += data['close'][i]
            sell_signals.append((i, data['close'][i]))

        # Check for end of data
        if i == len(data) - 1 and position > 0:
            # Sell
            position = 0
            profit += data['close'][i]
            sell_signals.append((i, data['close'][i]))

    if investment != 0:
        percent_profit = round(profit / investment * 100, 2)
    else:
        percent_profit = 0
    profit = int(profit)

    return {
        "profit": profit,
        "percent_profit": percent_profit,
        "buy_signals": buy_signals,
        "sell_signals": sell_signals,
    }


def test_algorithm(data, levels=[0.236, 0.382, 0.5, 0.618, 0.786], window_size=20, stop_loss=0.05):
    result = algorithm(data, levels=levels, window_size=window_size, stop_loss=stop_loss)
    print("Profit: ", result['profit'])
    print("Percent Profit: ", result['percent_profit'])

    return result


def plot_data(data, buy_signals, sell_signals):
    plt.plot(data['close'])
    for buy_signal in buy_signals:
        plt.plot(buy_signal[0], buy_signal[1], marker='^', markersize=10, color='green')
    for sell_signal in sell_signals:
        plt.plot(sell_signal[0], sell_signal[1], marker='v', markersize=10, color='red')
    plt.show()
