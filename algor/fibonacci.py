import pandas as pd
import talib
import matplotlib.pyplot as plt
from datetime import datetime
import matplotlib.dates as mdates
import matplotlib.animation as animation


def run(data, levels=[0.236, 0.382, 0.5, 0.618, 0.786], window_size=20, stop_loss=0.05):
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
        # Look for a buy signal when the price is near a support level
        if data['low'][i] < fib_levels[0] and rsi[i] < 30 and position <= 0:
            # Buy
            position += 1
            investment += data['close'][i] * 1.0004  # Include commission
            profit -= data['close'][i] * 1.0004
            buy_signals.append((i, data['close'][i]))
        # Look for a sell signal when the price is near a resistance level
        elif data['high'][i] > fib_levels[-1] and rsi[i] > 70 and position >= 0:
            # Sell
            position -= 1
            profit += data['close'][i]
            sell_signals.append((i, data['close'][i]))
        # Use trailing stop-loss
        elif position > 0 and data['close'][i] < data['close'][i-1] * (1 - stop_loss):
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
    result = run(data, levels=levels,
                 window_size=window_size, stop_loss=stop_loss)
    print("Profit: ", result['profit'])
    print("Percent Profit: ", result['percent_profit'])

    return result


def plot_data(data, buy_signals, sell_signals):
    # Convert date string to datetime objects
    dates = [datetime.strptime(d, '%Y-%m-%dT%H:%M:%S+00:00')
             for d in data['date']]

    # Plot the data
    fig, ax = plt.subplots(figsize=(16, 8))
    ax.plot(dates, data['close'])

    # Plot the buy signals
    for signal in buy_signals:
        ax.plot(dates[signal[0]], signal[1], marker='^',
                markersize=10, color='green')

    # Plot the sell signals
    for signal in sell_signals:
        ax.plot(dates[signal[0]], signal[1], marker='v',
                markersize=10, color='red')

    # Format the date axis
    date_fmt = mdates.DateFormatter('%d-%b')
    ax.xaxis.set_major_formatter(date_fmt)
    plt.xticks(rotation=45)

    # Add labels and legend
    plt.title('Trading signals')
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.legend(['Close', 'Buy', 'Sell'])
    plt.show()


def get_signal(data, position, levels=[0.236, 0.382, 0.5, 0.618, 0.786], window_size=20, is_short=False, stop_loss=0.05):
    # Calculate the highest and lowest price
    highest_price = data['high'].max()
    lowest_price = data['low'].min()

    # Calculate the price range
    price_range = highest_price - lowest_price

    # Calculate the Fibonacci levels
    fib_levels = []
    for level in levels:
        fib_levels.append(highest_price - level * price_range)

    # Calculate the SMA
    close_prices = data['close']

    # Add improvement 3: Use RSI to filter signals
    rsi = talib.RSI(close_prices, timeperiod=14)

    # Get the latest price and the EMA
    latest_price = close_prices.iloc[-1]
    prelatest_price = close_prices.iloc[-2]
    latest_low_price = data['low'].iloc[-1]
    latest_high_price = data['high'].iloc[-1]
    latest_rsi = rsi.iloc[-1]

    position_sell = 0 if is_short else 1

    # Check if the price crosses above the EMA
    if latest_low_price < fib_levels[0] and latest_rsi < 50 and position <= 0:
        # Buy signal
        return "buy"
    # Look for a sell signal when the price is near a resistance level
    elif latest_high_price > fib_levels[-1] and latest_rsi > 50 and position >= position_sell:
        # Sell signal
        return "sell"
    # Use trailing stop-loss
    elif position > 0 and latest_price < prelatest_price * (1 - stop_loss):
        # Sell signal
        return "sell"
    else:
        return None


def test_strategy(data, levels=[0.236, 0.382, 0.5, 0.618, 0.786], window_size=20, is_short=False, stop_loss=0.02):
    # Check if data is empty
    if data.empty:
        print("Error: Data is empty")
        return

    # Calculate the signals
    signals = []
    position = 0
    investment = 0.0
    profit = 0.0
    buy_signals = []
    sell_signals = []
    for i in range(window_size, len(data)):
        signal = get_signal(
            data.iloc[i-window_size:i+1], position=position, levels=levels, is_short=is_short)
        signals.append(signal)
        if signal == 'buy':
            print('buy', data.iloc[i-window_size:i+1])
            position += 1
            investment += data['close'][i] * 1.0004  # Include commission
            profit -= data['close'][i] * 1.0004
            buy_signals.append((i, data['close'][i]))

        elif signal == 'sell':
            print('sell', data.iloc[i-window_size:i+1])
            position -= 1
            profit += data['close'][i]
            sell_signals.append((i, data['close'][i]))

    # Calculate percent profit
    if investment != 0:
        percent_profit = round(profit / investment * 100, 2)
    else:
        percent_profit = 0

    # Print results
    print("Total profit:", profit)
    print("Percent profit:", percent_profit)

    # Plot the graph
    plt.plot(data['close'], label='Price')
    plt.plot([x[0] for x in buy_signals], [x[1]
             for x in buy_signals], 'o', color='g', label='Buy')
    plt.plot([x[0] for x in sell_signals], [x[1]
             for x in sell_signals], 'o', color='r', label='Sell')
    plt.legend()
    plt.show()

    return {
        "profit": profit,
        "percent_profit": percent_profit,
    }


def plot_trading_signals(data, buy_signals, sell_signals):
    plt.figure(figsize=(14, 7))
    plt.plot(data['close'], label='Close Price', alpha=0.5)

    # Plot buy signals
    for signal in buy_signals:
        plt.scatter(signal[0], signal[1], marker='^',
                    color='g', label='Buy', alpha=1)

    # Plot sell signals
    for signal in sell_signals:
        plt.scatter(signal[0], signal[1], marker='v',
                    color='r', label='Sell', alpha=1)

    plt.title('Buy and Sell signals')
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.legend(loc='best')
    plt.show()
